import os
from unittest import mock, TestCase
from backend.config import UPLOAD_DIR
from backend.apps.ollama.main import save_llm_response_as_note


class TestSaveLLMResponseAsNote(TestCase):
    @mock.patch("backend.apps.ollama.main.save_llm_response_as_note")
    async def test_save_llm_response_as_note_saves_in_upload_dir(self, mock_save_llm_response_as_note):
        # Setup
        llm_response_text = "Text of LLM response for unit testing"
        expected_file_path = os.path.join(UPLOAD_DIR, "Text_of_LLM_response_for.md")
        
        # Act
        await save_llm_response_as_note(llm_response_text)

        # Assert
        self.assertEquals(os.path.exists(expected_file_path), True)
