import asyncio
import time
async def fetch_from_api(endpoint: str, delay: float = 2.0) -> str:
    """Async API fetch"""
    print(f"Starting fetch from {endpoint}...")
    await asyncio.sleep(delay)
    print(f"Completed fetch from {endpoint}")
    return f"Response from {endpoint}"
 
async def main_project2():
    """Run multiple async functions in parallel"""
    print("\n=== PROJECT 2: Parallel Async (asyncio.gather) ===\n")
    
    start = time.time()
    
    # Create tasks (don't await yet)
    task1 = fetch_from_api("/api/users", 2.0)
    task2 = fetch_from_api("/api/posts", 2.0)
    task3 = fetch_from_api("/api/comments", 2.0)
    
    # Run all in parallel
    results = await asyncio.gather(task1, task2, task3)
    
    elapsed = time.time() - start
    
    print(f"\nResults: {results}")
    print(f"Parallel time: {elapsed:.2f}s (2 seconds, not 6!)\n")
 
if __name__ == "__main__":
    asyncio.run(main_project2())