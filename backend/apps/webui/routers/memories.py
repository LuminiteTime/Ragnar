from fastapi import Response, Request
from fastapi import Depends, FastAPI, HTTPException, status
from datetime import datetime, timedelta
from typing import List, Union, Optional

from fastapi import APIRouter
from pydantic import BaseModel
import logging

from apps.webui.models.memories import Memories, MemoryModel
from apps.ollama.main import save_llm_response_as_note

from utils.utils import get_verified_user
from constants import ERROR_MESSAGES

from config import SRC_LOG_LEVELS, CHROMA_CLIENT


from fastapi import APIRouter

from apps.webui.models.memories import Memories
from utils.utils import get_verified_user

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()


@router.get("/ef")
async def get_embeddings(request: Request):
    return {"result": request.app.state.EMBEDDING_FUNCTION("hello world")}


############################
# GetMemories
############################


@router.get("/", response_model=List[MemoryModel])
async def get_memories(user=Depends(get_verified_user)):
    return Memories.get_memories_by_user_id(user.id)


############################
# AddMemory
############################


class AddMemoryForm(BaseModel):
    content: str


@router.post("/add", response_model=Optional[MemoryModel])
async def add_memory(
    request: Request, form_data: AddMemoryForm, user=Depends(get_verified_user)
):
    memory = Memories.insert_new_memory(user.id, form_data.content)
    memory_embedding = request.app.state.EMBEDDING_FUNCTION(memory.content)

    collection = CHROMA_CLIENT.get_or_create_collection(name=f"user-memory-{user.id}")
    collection.upsert(
        documents=[memory.content],
        ids=[memory.id],
        embeddings=[memory_embedding],
        metadatas=[{"created_at": memory.created_at}],
    )

    return memory


class SaveResponseAsNoteForm(BaseModel):
    content: str


@router.post("/save_response_as_note")
async def save_response_as_note(
        request: Request,
        form_data: SaveResponseAsNoteForm,
):
    if not form_data.content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Content is required to save a note."
        )
    path = await save_llm_response_as_note(form_data.content)
    user_id: str = "57d0beb6-7bf8-434a-babd-24c7a4088dca"
    note = Memories.insert_new_memory(user_id, form_data.content)

    if note:
        return {"message": "Note saved successfully", "note_id": note.id, "note_path": path}
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save the note."
        )



############################
# QueryMemory
############################


class QueryMemoryForm(BaseModel):
    content: str


@router.post("/query")
async def query_memory(
    request: Request, form_data: QueryMemoryForm, user=Depends(get_verified_user)
):
    query_embedding = request.app.state.EMBEDDING_FUNCTION(form_data.content)
    collection = CHROMA_CLIENT.get_or_create_collection(name=f"user-memory-{user.id}")

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1,  # how many results to return
    )

    return results


############################
# ResetMemoryFromVectorDB
############################
@router.get("/reset", response_model=bool)
async def reset_memory_from_vector_db(
    request: Request, user=Depends(get_verified_user)
):
    CHROMA_CLIENT.delete_collection(f"user-memory-{user.id}")
    collection = CHROMA_CLIENT.get_or_create_collection(name=f"user-memory-{user.id}")

    memories = Memories.get_memories_by_user_id(user.id)
    for memory in memories:
        memory_embedding = request.app.state.EMBEDDING_FUNCTION(memory.content)
        collection.upsert(
            documents=[memory.content],
            ids=[memory.id],
            embeddings=[memory_embedding],
        )
    return True


############################
# DeleteMemoriesByUserId
############################


@router.delete("/user", response_model=bool)
async def delete_memory_by_user_id(user=Depends(get_verified_user)):
    result = Memories.delete_memories_by_user_id(user.id)

    if result:
        try:
            CHROMA_CLIENT.delete_collection(f"user-memory-{user.id}")
        except Exception as e:
            log.error(e)
        return True

    return False


############################
# DeleteMemoryById
############################


@router.delete("/{memory_id}", response_model=bool)
async def delete_memory_by_id(memory_id: str, user=Depends(get_verified_user)):
    result = Memories.delete_memory_by_id_and_user_id(memory_id, user.id)

    if result:
        collection = CHROMA_CLIENT.get_or_create_collection(
            name=f"user-memory-{user.id}"
        )
        collection.delete(ids=[memory_id])
        return True

    return False
