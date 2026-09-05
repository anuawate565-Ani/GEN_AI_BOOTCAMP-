import time
import logging
from functools import wraps
from typing import Callable, Any, Dict

logger = logging.getLogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Retry decorator: retry failed function calls
    
    Usage:
        @retry(max_attempts=3)
        def call_api():
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    logger.info(f"Attempt {attempt + 1}/{max_attempts}: {func.__name__}")
                    result = func(*args, **kwargs)
                    logger.info(f"Success on attempt {attempt + 1}")
                    return result
                
                except Exception as e:
                    if attempt == max_attempts - 1:
                        logger.error(f"All {max_attempts} attempts failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
        return wrapper
    return decorator

def log_execution_time(func: Callable) -> Callable:
    """
    Log execution time of function
    
    Usage:
        @log_execution_time
        def slow_function():
            time.sleep(2)
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        logger.info(f"Starting {func.__name__}...")
        
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            logger.info(f"Completed {func.__name__} in {elapsed:.3f}s")
            return result
        
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Failed {func.__name__} after {elapsed:.3f}s: {e}")
            raise
    
    return wrapper


def cache_response(func: Callable) -> Callable:
    """
    Cache function responses
    
    Usage:
        @cache_response
        def expensive_api_call(prompt: str):
            ...
    """
    cache: Dict[str, Any] = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = str(args) + str(kwargs)
        
        if cache_key in cache:
            logger.info(f"Cache hit for {func.__name__}")
            return cache[cache_key]
        
        logger.info(f"Cache miss for {func.__name__}. Computing...")
        result = func(*args, **kwargs)
        cache[cache_key] = result
        logger.info(f"Cached result for {func.__name__}")
        
        return result
    wrapper.cache = cache
    wrapper.clear_cache = lambda: cache.clear()
    
    return wrapper

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    @cache_response
    @log_execution_time
    @retry(max_attempts=2, delay=0.5)
    def call_llm_api(prompt: str) -> str:
        """Simulated LLM API call"""
        time.sleep(0.5)  # Simulate API delay
        return f"Response to: {prompt}"
    
   
    print("\n=== First Call ===")
    result1 = call_llm_api("What is AI?")
    print(f"Result: {result1}\n")
    
    print("=== Second Call (Same Prompt) ===")
    result2 = call_llm_api("What is AI?")
    print(f"Result: {result2}\n")
    
    print("=== Third Call (Different Prompt) ===")
    result3 = call_llm_api("What is ML?")
    print(f"Result: {result3}\n")
    
    print(f"Cache contents: {call_llm_api.cache}")
    call_llm_api.clear_cache()
    print("Cache cleared")