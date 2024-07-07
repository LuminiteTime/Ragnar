import os
from unittest import mock, TestCase
from backend.config import UPLOAD_DIR
from backend.apps.ollama.main import save_llm_response_as_note

class TestSaveLLMResponseAsNote(TestCase):
    ...