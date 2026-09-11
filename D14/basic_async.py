import asyncio
import time
 
async def fetch_data(api_endpoint: str, delay: float = 2.0) -> str:
    """Async function to fetch data from API"""
    print(f"Fetching from {api_endpoint}...")
    await asyncio.sleep(delay)  # Simulate API delay
    return f"Data from {api_endpoint}"
 
async def main_project1():
    """Run async functions sequentially"""
    print("=== PROJECT 1: Basic Async ===\n")
    
    print("--- Sequential (one after another) ---")
    start = time.time()
    result1 = await fetch_data("/api/users", 2.0)
    result2 = await fetch_data("/api/posts", 2.0)
    result3 = await fetch_data("/api/comments", 2.0)
    elapsed = time.time() - start
    
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Result 3: {result3}")
    print(f"Sequential time: {elapsed:.2f}s (6 seconds)\n")
 
if __name__ == "__main__":
    asyncio.run(main_project1())