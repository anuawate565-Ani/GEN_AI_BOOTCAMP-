import asyncio
import time

class AsyncLLMClient:
    """Async LLM client for batch processing"""
    
    def __init__(self, api_url: str):
        self.api_url = api_url
    
    async def generate(self, prompt: str, temperature: float = 0.7) -> dict:
        """Generate response from LLM (async)"""
        print(f"[{time.time():.2f}] Calling LLM: {prompt[:30]}...")
        
        # Simulate API call
        await asyncio.sleep(2.0)
        
        return {
            "prompt": prompt,
            "response": f"AI response to: {prompt}",
            "temperature": temperature,
            "status": "success"
        }
    
    async def batch_generate(self, prompts: list[str]) -> list[dict]:
        """Generate responses for multiple prompts in parallel"""
        print(f"\n--- Starting batch processing for {len(prompts)} prompts ---")
        
        start_time = time.time()
        
        # Create tasks for all prompts
        tasks = [self.generate(prompt) for prompt in prompts]
        
        # Run all in parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        elapsed = time.time() - start_time
        
        print(f"--- Batch completed in {elapsed:.2f}s ---")
        
        return results
 
async def main_project4():
    """Real-world async batch processing"""
    print("\n=== PROJECT 4: Async LLM Batch Processor ===\n")
    
    client = AsyncLLMClient("https://api.openai.com")
    
    prompts = [
        "What is artificial intelligence?",
        "Explain machine learning",
        "What are neural networks?",
        "What is deep learning?",
        "What is NLP?"
    ]
    
    print("Sequential approach (5 prompts × 2 seconds = 10 seconds):")
    print("Async approach (5 prompts parallel = 2 seconds)\n")
    
    # Process batch
    results = await client.batch_generate(prompts)
    
    print("\n--- Results Summary ---")
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"Prompt {i}: Error - {result}")
        else:
            print(f"Prompt {i}: {result['response'][:40]}... | Status: {result['status']}")
    
    print("\n--- Performance Comparison ---")
    sequential_time = len(prompts) * 2.0  # Each takes 2 seconds
    parallel_time = 2.0  # All run together
    speedup = sequential_time / parallel_time
    
    print(f"Sequential time: {sequential_time:.1f}s")
    print(f"Parallel time: {parallel_time:.1f}s")
    print(f"Speedup: {speedup:.1f}x faster!")
 
if __name__ == "__main__":
    asyncio.run(main_project4())
 