import pytest
import tempfile
import os

class FileProcessor:
    """Process files"""
    
    @staticmethod
    def read_file(filepath):
        with open(filepath, 'r') as f:
            return f.read()
    
    @staticmethod
    def write_file(filepath, content):
        with open(filepath, 'w') as f:
            f.write(content)
    
    @staticmethod
    def count_lines(filepath):
        with open(filepath, 'r') as f:
            return len(f.readlines())

# Fixture: Create temporary file for testing
@pytest.fixture
def temp_file():
    """Create temp file for testing"""
    # Setup
    temp_dir = tempfile.gettempdir()
    filepath = os.path.join(temp_dir, "test_file.txt")
    
    # Write test data
    with open(filepath, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    yield filepath  # Tests run here
    
    # Teardown
    if os.path.exists(filepath):
        os.remove(filepath)

# Fixture: Create empty file
@pytest.fixture
def empty_file():
    """Create empty file for testing"""
    temp_dir = tempfile.gettempdir()
    filepath = os.path.join(temp_dir, "empty_file.txt")
    
    with open(filepath, 'w') as f:
        f.write("")
    
    yield filepath
    
    if os.path.exists(filepath):
        os.remove(filepath)

# Tests using fixtures
def test_read_file(temp_file):
    processor = FileProcessor()
    content = processor.read_file(temp_file)
    assert "Line 1" in content
    assert "Line 2" in content

def test_write_file(temp_file):
    processor = FileProcessor()
    processor.write_file(temp_file, "New content")
    content = processor.read_file(temp_file)
    assert content == "New content"

def test_count_lines(temp_file):
    processor = FileProcessor()
    count = processor.count_lines(temp_file)
    assert count == 3

def test_empty_file(empty_file):
    processor = FileProcessor()
    content = processor.read_file(empty_file)
    assert content == ""

def test_count_lines_empty(empty_file):
    processor = FileProcessor()
    count = processor.count_lines(empty_file)
    assert count == 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])