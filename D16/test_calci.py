import unittest

class Calculator:
    """Simple calculator for testing"""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator"""
    
    def setUp(self):
        """Run before each test"""
        self.calc = Calculator()
    
    def tearDown(self):
        """Run after each test"""
        self.calc = None
    
    # Test add
    def test_add_positive_numbers(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
    
    # Test subtract
    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)
    
    # Test divide
    def test_divide_valid(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()