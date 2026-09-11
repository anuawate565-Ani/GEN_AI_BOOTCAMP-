import pytest

class StringValidator:
    """Validate strings"""
    
    @staticmethod
    def is_email_valid(email):
        if not email or "@" not in email:
            return False
        return True
    
    @staticmethod
    def is_length_valid(text, min_len=1, max_len=100):
        if len(text) < min_len or len(text) > max_len:
            return False
        return True
    
    @staticmethod
    def remove_whitespace(text):
        return text.strip()

# Test functions (pytest style)
def test_valid_email():
    validator = StringValidator()
    assert validator.is_email_valid("anu@gmail.com") == True

def test_invalid_email_no_at():
    validator = StringValidator()
    assert validator.is_email_valid("anugmail.com") == False

def test_invalid_email_empty():
    validator = StringValidator()
    assert validator.is_email_valid("") == False

def test_length_valid():
    validator = StringValidator()
    assert validator.is_length_valid("Hello", min_len=1, max_len=100) == True

def test_length_too_short():
    validator = StringValidator()
    assert validator.is_length_valid("a", min_len=5, max_len=100) == False

def test_length_too_long():
    validator = StringValidator()
    text = "x" * 150
    assert validator.is_length_valid(text, min_len=1, max_len=100) == False

def test_remove_whitespace():
    validator = StringValidator()
    result = validator.remove_whitespace("   hello   ")
    assert result == "hello"

def test_remove_whitespace_multiple():
    validator = StringValidator()
    result = validator.remove_whitespace("\n\t  world  \n")
    assert result == "world"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])