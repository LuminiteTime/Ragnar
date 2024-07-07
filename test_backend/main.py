import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from unittest import mock, TestCase
from backend.config import UPLOAD_DIR
from backend.apps.ollama.main import save_llm_response_as_note
from backend.apps.webui.routers.memories import save_response_as_note, SaveResponseAsNoteForm
import asyncio

class TestSaveLLMResponseAsNote(TestCase):
    @mock.patch("backend.apps.webui.routers.memories.save_llm_response_as_note")
    @mock.patch("backend.apps.webui.routers.memories.Memories.insert_new_memory", return_value=mock.MagicMock(id="123"))
    def test_save_response_as_note_with_valid_content_and_user(self, mock_insert_new_memory, mock_save_llm_response_as_note):
        request = mock.MagicMock()
        form_data = SaveResponseAsNoteForm(content="Valid content")
        response = asyncio.run(save_response_as_note(request, form_data))
        self.assertEqual(response["message"], "Note saved successfully")
        self.assertEqual(response["note_id"], "123")

    @mock.patch("backend.apps.ollama.main.save_llm_response_as_note")
    def test_save_llm_response_as_note_saves_in_upload_dir(self, mock_save_llm_response_as_note):
        llm_response_text = "Text of LLM response for unit testing"
        path = asyncio.run(save_llm_response_as_note(llm_response_text))
        self.assertTrue(os.path.exists(path))
