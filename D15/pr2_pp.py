import re

print("=== PROJECT 2: Pattern Extraction ===\n")

text = """
My email is anu@gmail.com
Contact: Ani@yahoo.com
Phone: +91-9870000000
Website: https://www.example.com
Another URL: http://test.org
"""
print("--- Emails ---")
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(f"Found emails: {emails}")

# Extract phone numbers
print("\n--- Phone Numbers ---")
phones = re.findall(r"\+?91[\s.-]?\d{10}", text)
print(f"Found phones: {phones}")

# Extract URLs
print("\n--- URLs ---")
urls = re.findall(r"https?://[^\s]+", text)
print(f"Found URLs: {urls}")

# Extract all numbers
print("\n--- All Numbers ---")
numbers = re.findall(r"\d+", text)
print(f"Found numbers: {numbers}")