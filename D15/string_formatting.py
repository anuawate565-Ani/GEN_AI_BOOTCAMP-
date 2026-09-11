print("=== PROJECT 5: String Formatting ===\n")

# Test 1: Basic f-strings
print("--- Test 1: Basic f-strings ---")
name = "Anu"
age = 21
message = f"My name is {name} and I am {age} years old"
print(message)

# Test 2: Expression in f-string
print("\n--- Test 2: Expression in f-string ---")
x, y = 10, 20
result = f"Sum of {x} and {y} is {x + y}"
print(result)

# Test 3: Format specifiers
print("\n--- Test 3: Format Specifiers ---")
price = 99.9876
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Integer: {42:05d}")    # Pad to 5 digits

# Test 4: LLM Prompt construction
print("\n--- Test 4: LLM Prompt Construction ---")
user_input = "What is AI?"
context = "assistant"

prompt = f"""You are a helpful {context}.
User asks: {user_input}
Please provide a detailed answer."""

print(prompt)

# Test 5: Dynamic API message
print("\n--- Test 5: Dynamic API Message ---")
endpoint = "https://api.openai.com"
api_key = "sk-xxx"
model = "gpt-4"

request = f"""
URL: {endpoint}/v1/completions
Model: {model}
Key: {api_key[:5]}...
"""
print(request)

print("\n=== PROJECT 5 COMPLETE ===")