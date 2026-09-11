class FileWriter:
    """Context manager for safe file writing"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None
    
    def __enter__(self):
        logger.info(f"Opening file: {self.filepath}")
        try:
            self.file = open(self.filepath, "w")
            logger.info("✓ File opened")
            return self
        except IOError as e:
            logger.error(f"Cannot open file: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            logger.info("Closing file")
            self.file.close()
        
        if exc_type is not None:
            logger.error(f"Error during write: {exc_val}")
        
        return False
    
    def write(self, text: str) -> None:
        if not self.file:
            raise RuntimeError("File not open")
        self.file.write(text + "\n")
 
 
# Test Project 2
if __name__ == "__main__":
    print("\n\n=== PROJECT 2: FileWriter Context Manager ===\n")
    
    with FileWriter("output.txt") as writer:
        writer.write("Line 1")
        writer.write("Line 2")
        writer.write("Line 3")
        print("✓ File written successfully")
    
    # Read back
    with open("output.txt", "r") as f:
        print("\n--- File Contents ---")
        print(f.read())