import time
from functools import wraps
from typing import Callable
 
def rate_limit(requests_per_second: int):
    """Rate limit decorator: max N requests per second"""
    def decorator(func: Callable):
        last_called = [0.0]
        min_interval = 1.0 / requests_per_second
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            
            if elapsed < min_interval:
                wait_time = min_interval - elapsed
                print(f"Rate limit: waiting {wait_time:.2f}s...")
                time.sleep(wait_time)
            
            last_called[0] = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
 
 
@rate_limit(requests_per_second=2)
def api_call(endpoint: str) -> str:
    print(f"Calling {endpoint}")
    return f"Response from {endpoint}"
 
if __name__ == "__main__":
    print("=== PROJECT 2: Rate Limiter ===\n")
    
    start = time.time()
    for i in range(5):
        api_call(f"/api/endpoint{i}")
    
    elapsed = time.time() - start
    print(f"\nTotal time: {elapsed:.2f}s (should be ~2s for 2 req/sec)")