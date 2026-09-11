import re

class TextCleaner:
    """Clean and sanitize user input for LLM"""
    
    def remove_extra_whitespace(self, text: str) -> str:
        """Remove extra spaces, tabs, newlines"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def remove_special_chars(self, text: str, keep_punctuation: bool = False) -> str:
        """Remove unwanted special characters"""
        if keep_punctuation:
            text = re.sub(r'[^a-zA-Z0-9\s\.\,\?\!]', '', text)
        else:
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
    
    def extract_emails(self, text: str) -> list:
        """Extract all email addresses"""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)
    
    def validate_length(self, text: str, min_length: int = 1, max_length: int = 10000) -> bool:
        """Validate text length"""
        return min_length <= len(text) <= max_length
    
    def normalize_text(self, text: str) -> str:
        """Complete text normalization"""
        text = self.remove_extra_whitespace(text)
        text = self.remove_special_chars(text, keep_punctuation=True)
        return text


print("=== PROJECT 3: Text Cleaning ===\n")

cleaner = TextCleaner()

# Test 1: Remove extra whitespace
print("--- Test 1: Remove Extra Whitespace ---")
messy = "   Hello    Anu    World   "
clean = cleaner.remove_extra_whitespace(messy)
print(f"Before: '{messy}'")
print(f"After:  '{clean}'")

# Test 2: Remove special characters
print("\n--- Test 2: Remove Special Characters ---")
text = "Hello!!! @@@Anu### $$$World"
clean = cleaner.remove_special_chars(text, keep_punctuation=False)
print(f"Before: '{text}'")
print(f"After:  '{clean}'")

# Test 3: Extract emails
print("\n--- Test 3: Extract Emails ---")
text = "Contact anu@gmail.com or john@yahoo.com for help"
emails = cleaner.extract_emails(text)
print(f"Text: {text}")
print(f"Emails found: {emails}")

# Test 4: Validate length
print("\n--- Test 4: Validate Length ---")
texts = ["Hi", "This is a normal prompt", "x" * 15000]
for t in texts:
    valid = cleaner.validate_length(t, min_length=2, max_length=10000)
    print(f"'{t[:30]}...' Valid: {valid}")

# Test 5: Normalize complete text
print("\n--- Test 5: Complete Normalization ---")
raw = "   Explain   Python!!!  @#$  please   "
normalized = cleaner.normalize_text(raw)
print(f"Before: '{raw}'")
print(f"After:  '{normalized}'")