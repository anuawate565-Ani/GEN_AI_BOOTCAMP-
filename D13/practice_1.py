import logging
import time
from contextlib import contextmanager
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
class ModelSession:
    """Context manager for model lifecycle"""
    
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None
        self.is_loaded = False
    
    def __enter__(self):
        logger.info(f"Loading model: {self.model_name}")
        time.sleep(0.5)
        self.model = {
            "name": self.model_name,
            "weights": f"loaded_{self.model_name}"
        }
        self.is_loaded = True
        logger.info(f"✓ Model loaded: {self.model_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f"Unloading model: {self.model_name}")
        if self.is_loaded:
            time.sleep(0.2)
            self.model = None
            self.is_loaded = False
            logger.info(f"✓ Model unloaded: {self.model_name}")
        
        if exc_type is not None:
            logger.error(f"Exception in model session: {exc_val}")
            return False
        
        return False
    
    def predict(self, prompt: str) -> str:
        if not self.is_loaded:
            raise RuntimeError("Model not loaded")
        logger.info(f"Predicting: {prompt}")
        return f"Response to: {prompt}"
 
 
class DatabaseConnection:
    """Context manager for database connections"""
    
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connection = None
    
    def __enter__(self):
        logger.info(f"Connecting to: {self.db_url}")
        self.connection = {"url": self.db_url, "connected": True}
        logger.info("✓ Connected")
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("Closing database connection")
        self.connection = None
        if exc_type is not None:
            logger.error(f"DB error: {exc_val}")
        return False
 
 
# Test Project 1
if __name__ == "__main__":
    print("\n=== PROJECT 1: ModelSession + DatabaseConnection ===\n")
    
    print("--- Example 1: Model Session ---")
    try:
        with ModelSession("gpt-2") as model:
            result = model.predict("What is AI?")
            print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n--- Example 2: Database Connection ---")
    with DatabaseConnection("postgresql://localhost") as conn:
        print(f"Using connection: {conn}")
    
    print("\n--- Example 3: Multiple Resources ---")
    with ModelSession("bert") as model, DatabaseConnection("sqlite://db") as db:
        result = model.predict("test")
        print(f"Stored: {result}")