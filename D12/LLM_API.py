import logging
import time
from functools import wraps
from typing import Callable, Any, Dict

logger = logging.getlogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
         @wraps(func)
         def wrapper(*args, **kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    logger.info(f"Attempt {attempt + 1}/{max_attempts}: {func.__name}")
                    result = func(*args, **kwargs)
                    logger.error(f"All {max_attempts} attempts failed: {e}")
                    raise

                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                time.sleep(delay)

        return wrapper
    return decorator

def log_execution_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        logger.info(f"Completed {func.__name__} after {elapsed:.3f}s")
        return result

    except Exception as e:
        elapsed