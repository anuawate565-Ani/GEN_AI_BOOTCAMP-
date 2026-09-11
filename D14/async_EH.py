import asyncio

async def call_llm_api(prompt: str, might_fail: bool = False) -> str:
    """Async LLM API call with potential error"""
    print(f"Calling LLM with prompt: {prompt}")
    await asyncio.sleep(1.0)
    
    if might_fail:
        raise ConnectionError(f"API failed for: {prompt}")
    
    return f"Response to: {prompt}"
 
async def main_project3():
    """Handle exceptions in async functions"""
    print("\n=== PROJECT 3: Async with Exception Handling ===\n")
    
    print("--- Case 1: Successful calls ---")
    try:
        result1 = await call_llm_api("What is AI?", might_fail=False)
        result2 = await call_llm_api("What is ML?", might_fail=False)
        print(f"Result 1: {result1}")
        print(f"Result 2: {result2}")
    except ConnectionError as e:
        print(f"Error: {e}")
    
    print("\n--- Case 2: One call fails ---")
    try:
        result1 = await call_llm_api("Q1", might_fail=False)
        result2 = await call_llm_api("Q2", might_fail=True)  # This fails
        result3 = await call_llm_api("Q3", might_fail=False)
        print(f"Results: {result1}, {result2}, {result3}")
    except ConnectionError as e:
        print(f"Caught exception: {e}")
    
    print("\n--- Case 3: asyncio.gather with exception handling ---")
    tasks = [
        call_llm_api("Q1", might_fail=False),
        call_llm_api("Q2", might_fail=True),
        call_llm_api("Q3", might_fail=False),
    ]
    
    try:
        results = await asyncio.gather(*tasks)
        print(f"All results: {results}")
    except ConnectionError as e:
        print(f"One or more tasks failed: {e}")
    
    print("\n--- Case 4: Continue despite errors ---")
    tasks = [
        call_llm_api("Q1", might_fail=False),
        call_llm_api("Q2", might_fail=True),
        call_llm_api("Q3", might_fail=False),
    ]
    
    # return_exceptions=True means don't raise, return exceptions as results
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"Task {i}: Error - {result}")
        else:
            print(f"Task {i}: {result}")
 
if __name__ == "__main__":
    asyncio.run(main_project3())