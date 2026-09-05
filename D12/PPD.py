import time
from functools import wraps
from typing import Callable

def profile_performance(func: Callable):
    """Performance profiler: measures time, args, returns, exceptions"""
    
    stats = {
        "call_count": 0,
        "total_time": 0.0,
        "avg_time": 0.0,
        "errors": 0,
        "last_result": None
    }
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
        
            stats["call_count"] += 1
            stats["total_time"] += elapsed
            stats["avg_time"] = stats["total_time"] / stats["call_count"]
            stats["last_result"] = type(result)
            
            print(f"[{func.__name__}] Executed in {elapsed:.4f}s | Args: {args} | Result type: {type(result).__name__}")
            
            return result
        
        except Exception as e:
            elapsed = time.time() - start_time
            stats["call_count"] += 1
            stats["total_time"] += elapsed
            stats["avg_time"] = stats["total_time"] / stats["call_count"]
            stats["errors"] += 1
            
            print(f"[{func.__name__}] Error after {elapsed:.4f}s: {str(e)}")
            raise
    
    def get_stats():
        return stats.copy()
    
    wrapper.get_stats = get_stats
    
    return wrapper
 
 
@profile_performance
def process_data(data, verbose=False):
    """Process data"""
    if not isinstance(data, list):
        raise TypeError("Data must be list")
    
    time.sleep(0.1)  # Sim
    return len(data)
 
 
@profile_performance
def fetch_from_api(url: str):
    """Fetch from API"""
    time.sleep(0.2)  # Simulate API call
    return {"status": "success", "data": "response"}
 
if __name__ == "__main__":
    print("\n\n=== PROJECT 3: Performance Profiler ===\n")

    result1 = process_data([1, 2, 3])
    print(f"Result 1: {result1}\n")
    
    result2 = process_data([1, 2, 3, 4, 5])
    print(f"Result 2: {result2}\n")
    
    result3 = fetch_from_api("https://api.example.com")
    print(f"Result 3: {result3}\n")
    
    # Get statistics
    stats1 = process_data.get_stats()
    stats2 = fetch_from_api.get_stats()
    
    print("=== PROCESS_DATA STATS ===")
    print(f"Call count: {stats1['call_count']}")
    print(f"Total time: {stats1['total_time']:.4f}s")
    print(f"Avg time: {stats1['avg_time']:.4f}s")
    print(f"Errors: {stats1['errors']}")
    print(f"Last result type: {stats1['last_result']}")
    
    print("\n=== FETCH_FROM_API STATS ===")
    print(f"Call count: {stats2['call_count']}")
    print(f"Total time: {stats2['total_time']:.4f}s")
    print(f"Avg time: {stats2['avg_time']:.4f}s")
    print(f"Errors: {stats2['errors']}")
    print(f"Last result type: {stats2['last_result']}")
    
    # Test exception handling
    print("\n=== TESTING EXCEPTION HANDLING ===")
    try:
        process_data("not a list")  # This will raise TypeError
    except TypeError as e:
        print(f"Caught exception: {e}")
    
    stats_after_error = process_data.get_stats()
    print(f"Call count after error: {stats_after_error['call_count']}")
    print(f"Errors: {stats_after_error['errors']}")