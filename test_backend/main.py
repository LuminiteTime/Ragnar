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
        
        # assert True

    @mock.patch("backend.apps.ollama.main.save_llm_response_as_note")
    def test_save_llm_response_as_note_called_once(self, mock_save_llm_response_as_note):
        # Setup
        llm_response_text = "Example text to test"
        
        # Act
        asyncio.run(mock_save_llm_response_as_note(llm_response_text))
        
        # Assert that save_llm_response_as_note was called exactly once
        mock_save_llm_response_as_note.assert_called_once_with(llm_response_text)
        
        # Verify the returned value
        expected_path = os.path.join(UPLOAD_DIR, f"{'_'.join(llm_response_text.split()[:5])}.md")
        self.assertEqual(expected_path, mock_save_llm_response_as_note.return_value)
        
        # assert True
