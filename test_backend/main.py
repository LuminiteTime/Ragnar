import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from unittest import mock, TestCase
from backend.config import UPLOAD_DIR
from backend.apps.ollama.main import save_llm_response_as_note
import asyncio

class TestSaveLLMResponseAsNote(TestCase):
    @mock.patch("backend.apps.ollama.main.save_llm_response_as_note")
    def test_save_llm_response_as_note_saves_in_upload_dir(self, mock_save_llm_response_as_note):
        # Setup
        llm_response_text = "Text of LLM response for unit testing"
        
        # Act
        path = asyncio.run(save_llm_response_as_note(llm_response_text))

        # Assert
        self.assertTrue(os.path.exists(path))
