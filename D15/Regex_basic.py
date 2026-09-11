import re

print("=== PROJECT 1: Regex Basics ===\n")

text = "Contact me at anu@gmail.com or john@yahoo.com"

# match() - from beginning only
print("--- re.match() ---")
result = re.match("Contact", text)
print(f"Match 'Contact' at start: {result is not None}")  # True

result = re.match("anu@", text)
print(f"Match 'anu@' at start: {result is not None}")  # False

# search() - anywhere in string
print("\n--- re.search() ---")
result = re.search("anu@gmail.com", text)
print(f"Search 'anu@gmail.com': {result is not None}")  # True
print(f"Found: {result.group()}")

# findall() - all occurrences
print("\n--- re.findall() ---")
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"All emails: {emails}")  # ['anu@gmail.com', 'john@yahoo.com']

# sub() - replace pattern
print("\n--- re.sub() ---")
cleaned = re.sub(r"\s+", " ", "Hello    Anu    World")
print(f"Removed extra spaces: '{cleaned}'")

masked = re.sub(r"\w+@\w+", "[EMAIL]", text)
print(f"Masked emails: {masked}")