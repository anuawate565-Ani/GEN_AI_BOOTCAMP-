
@contextmanager
def timer(task_name: str = "Task"):
    """Timer context manager using @contextmanager decorator"""
    start_time = time.time()
    logger.info(f"Starting: {task_name}")
    
    try:
        yield start_time
    except Exception as e:
        elapsed = time.time() - start_time
        logger.error(f"Error in {task_name} after {elapsed:.4f}s: {e}")
        raise
    finally:
        elapsed = time.time() - start_time
        logger.info(f"Completed: {task_name} in {elapsed:.4f}s")
 
 
# Test Project 3
if __name__ == "__main__":
    print("\n\n=== PROJECT 3: Timer Context Manager ===\n")
    
    print("--- Test 1: Quick Operation ---")
    with timer("Quick task") as start:
        time.sleep(0.1)
    
    print("\n--- Test 2: Slow Operation ---")
    with timer("Slow task") as start:
        time.sleep(0.5)
    
    print("\n--- Test 3: Nested Timers ---")
    with timer("Outer task"):
        time.sleep(0.2)
        with timer("Inner task"):
            time.sleep(0.3)
    
    print("\n--- Test 4: Exception Handling ---")
    try:
        with timer("Task with error"):
            time.sleep(0.1)
            raise ValueError("Something went wrong!")
    except ValueError:
        print("Caught exception but timer still measured!")