import pytest
from unittest.mock import MagicMock, patch
from response_generator import GeminiResponseGenerator

@pytest.fixture
def response_generator():
    # Mock environment variable for API key to avoid error during init
    with patch('os.getenv', return_value='fake_key'):
        with patch('google.generativeai.configure'):
            generator = GeminiResponseGenerator()
            return generator

def test_generate_fallback_response(response_generator):
    response = response_generator.generate_fallback_response("أنا حزين", "depression")
    assert isinstance(response, str)
    assert len(response) > 0

def test_generate_followup_question(response_generator):
    question = response_generator.generate_followup_question("anxiety")
    assert isinstance(question, str)
    assert "مقلقاك" in question

@patch('google.generativeai.GenerativeModel')
def test_generate_ai_response_success(mock_model_class, response_generator):
    # Mock the model and its generate_content method
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "رد تجريبي من الذكاء الاصطناعي"
    mock_model.generate_content.return_value = mock_response
    mock_model_class.return_value = mock_model

    response = response_generator.generate_ai_response("أنا قلقان", "anxiety", "")
    assert response == "رد تجريبي من الذكاء الاصطناعي"

@patch('google.generativeai.GenerativeModel')
def test_generate_ai_response_failure(mock_model_class, response_generator):
    # Mock the model to raise an exception
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API Error")
    mock_model_class.return_value = mock_model

    # Should fall back to fallback response
    response = response_generator.generate_ai_response("أنا قلقان", "anxiety", "")
    assert isinstance(response, str)
    assert len(response) > 0
