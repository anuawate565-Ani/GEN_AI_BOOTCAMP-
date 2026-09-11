import unittest
from unittest.mock import Mock, patch

class LLMClient:
    """LLM client that calls external API"""
    
    def __init__(self, api_url):
        self.api_url = api_url
    
    def generate_response(self, prompt):
        """Call external API"""
        import requests
        response = requests.post(self.api_url, json={"prompt": prompt})
        return response.json()["text"]

class TestLLMClient(unittest.TestCase):
    """Test LLM client with mocking"""
    
    def setUp(self):
        self.client = LLMClient("https://api.example.com")
    
    # Test 1: Mock entire requests.post
    @patch("requests.post")
    def test_generate_response_with_mock(self, mock_post):
        """Test without calling real API"""
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"text": "AI is great!"}
        mock_post.return_value = mock_response
        
        result = self.client.generate_response("What is AI?")
        
        # Verify
        self.assertEqual(result, "AI is great!")
        mock_post.assert_called_once()
    
    # Test 2: Verify mock was called with correct args
    @patch("requests.post")
    def test_api_called_with_correct_prompt(self, mock_post):
        """Verify correct prompt sent to API"""
        mock_response = Mock()
        mock_response.json.return_value = {"text": "Response"}
        mock_post.return_value = mock_response
        
        self.client.generate_response("Test prompt")
        
        # Verify post was called with correct data
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        self.assertEqual(call_args[1]["json"]["prompt"], "Test prompt")
    
    # Test 3: Test error handling
    @patch("requests.post")
    def test_api_error_handling(self, mock_post):
        """Test handling API errors"""
        mock_post.side_effect = Exception("API Error")
        
        with self.assertRaises(Exception):
            self.client.generate_response("test")

# Additional test class for data validation
class DataValidator:
    """Validate data"""
    
    def validate_input(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        if not isinstance(data, dict):
            raise TypeError("Data must be dict")
        return True

class TestDataValidator(unittest.TestCase):
    """Test data validator"""
    
    def setUp(self):
        self.validator = DataValidator()
    
    def test_valid_data(self):
        result = self.validator.validate_input({"name": "Anu"})
        self.assertTrue(result)
    
    def test_empty_data_raises_error(self):
        with self.assertRaises(ValueError):
            self.validator.validate_input({})
    
    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            self.validator.validate_input("not a dict")

if __name__ == "__main__":
    unittest.main()