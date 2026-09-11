import re

class PromptSanitizer:
    """Production-grade prompt sanitizer for GenAI"""
    
    def __init__(self, max_tokens: int = 4000):
        self.max_tokens = max_tokens
    
    def sanitize(self, prompt: str) -> dict:
        """Complete sanitization pipeline"""
        try:
            # Step 1: Validate not empty
            if not prompt or not prompt.strip():
                return {
                    "status": "error",
                    "message": "Prompt cannot be empty"
                }
            
            # Step 2: Remove extra whitespace
            cleaned = re.sub(r'\s+', ' ', prompt).strip()
            
            # Step 3: Remove unwanted special chars (keep basic punctuation)
            cleaned = re.sub(r'[^\w\s\.\,\?\!\-\'\"]', '', cleaned)
            
            # Step 4: Validate length
            word_count = len(cleaned.split())
            if word_count > self.max_tokens:
                return {
                    "status": "error",
                    "message": f"Prompt too long: {word_count} words (max: {self.max_tokens})"
                }
            
            # Step 5: Extract entities
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cleaned)
            urls = re.findall(r'https?://[^\s]+', cleaned)
            
            return {
                "status": "success",
                "original": prompt,
                "cleaned": cleaned,
                "word_count": word_count,
                "entities": {
                    "emails": emails,
                    "urls": urls
                }
            }
        
        except Exception as e:
            return {
                "status": "error",
                "message": f"Sanitization failed: {str(e)}"
            }


print("=== PROJECT 4: PromptSanitizer for LLM ===\n")

sanitizer = PromptSanitizer(max_tokens=100)

# Test 1: Normal prompt
print("--- Test 1: Normal Prompt ---")
result = sanitizer.sanitize("Explain Python programming")
print(f"Status: {result['status']}")
print(f"Cleaned: {result['cleaned']}")
print(f"Word count: {result['word_count']}\n")

# Test 2: Messy prompt
print("--- Test 2: Messy Prompt ---")
result = sanitizer.sanitize("   Explain     Python!!!   @#$   ")
print(f"Status: {result['status']}")
print(f"Cleaned: {result['cleaned']}\n")

# Test 3: Prompt with email
print("--- Test 3: Prompt with Email ---")
result = sanitizer.sanitize("Contact me at anu@gmail.com for Python help")
print(f"Status: {result['status']}")
print(f"Cleaned: {result['cleaned']}")
print(f"Emails found: {result['entities']['emails']}\n")

# Test 4: Empty prompt
print("--- Test 4: Empty Prompt ---")
result = sanitizer.sanitize("   ")
print(f"Status: {result['status']}")
print(f"Message: {result['message']}\n")

# Test 5: Too long prompt
print("--- Test 5: Too Long Prompt ---")
long_prompt = "word " * 150  # 150 words
result = sanitizer.sanitize(long_prompt)
print(f"Status: {result['status']}")
print(f"Message: {result['message']}")