import unittest
import re


class PromptSanitizer:
    """Production-grade prompt sanitizer"""

    def __init__(self, max_tokens=4000):
        self.max_tokens = max_tokens

    def sanitize(self, prompt):
        """Sanitize prompt"""

        # 1. Check input type first
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be string")

        # 2. Check empty or whitespace-only prompt
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        # 3. Remove extra whitespace
        cleaned = re.sub(r'\s+', ' ', prompt).strip()

        # 4. Remove unwanted special characters
        # Keep:
        # \w  -> letters, numbers, underscore
        # \s  -> whitespace
        # . , ? - ' "
        cleaned = re.sub(r'[^\w\s\.,\?\-\'\"]', '', cleaned)

        # 5. Normalize whitespace again
        # Special-character removal may create double spaces
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        # 6. Count words AFTER cleaning
        word_count = len(cleaned.split())

        # 7. Check maximum word limit
        if word_count > self.max_tokens:
            raise ValueError(
                f"Prompt too long: {word_count} words"
            )

        # 8. Return result
        return {
            "cleaned": cleaned,
            "word_count": word_count
        }


class TestPromptSanitizer(unittest.TestCase):
    """Complete test suite for PromptSanitizer"""

    def setUp(self):
        self.sanitizer = PromptSanitizer(max_tokens=100)

    def test_valid_prompt(self):
        result = self.sanitizer.sanitize(
            "Explain Python programming"
        )

        self.assertIsNotNone(result)
        self.assertIn("cleaned", result)
        self.assertEqual(result["word_count"], 3)

    def test_empty_prompt_raises_error(self):
        with self.assertRaises(ValueError):
            self.sanitizer.sanitize("")

    def test_whitespace_only_raises_error(self):
        with self.assertRaises(ValueError):
            self.sanitizer.sanitize("   ")

    def test_non_string_raises_error(self):
        with self.assertRaises(TypeError):
            self.sanitizer.sanitize(123)

    def test_list_raises_error(self):
        with self.assertRaises(TypeError):
            self.sanitizer.sanitize(["test"])

    def test_removes_special_chars(self):
        result = self.sanitizer.sanitize(
            "Explain Python!!! @#$ please"
        )

        self.assertEqual(
            result["cleaned"],
            "Explain Python please"
        )

    def test_removes_extra_whitespace(self):
        result = self.sanitizer.sanitize(
            "Hello    World     Test"
        )

        self.assertEqual(
            result["cleaned"],
            "Hello World Test"
        )

    def test_long_prompt_raises_error(self):
        long_prompt = "word " * 150

        with self.assertRaises(ValueError):
            self.sanitizer.sanitize(long_prompt)

    def test_word_count_accurate(self):
        result = self.sanitizer.sanitize(
            "One Two Three Four Five"
        )

        self.assertEqual(
            result["word_count"],
            5
        )

    def test_preserves_punctuation(self):
        result = self.sanitizer.sanitize(
            "What is Python? It's amazing!"
        )

        self.assertIn("?", result["cleaned"])
        self.assertIn("'", result["cleaned"])

    def test_case_preservation(self):
        result = self.sanitizer.sanitize(
            "Python Java"
        )

        self.assertIn("Python", result["cleaned"])
        self.assertIn("Java", result["cleaned"])

    def test_messy_input(self):
        messy = (
            "   Explain   Python!!!   @#$   please   "
        )

        result = self.sanitizer.sanitize(messy)

        self.assertEqual(
            result["cleaned"],
            "Explain Python please"
        )


class TestPromptSanitizerIntegration(unittest.TestCase):
    """Integration tests for complete workflow"""

    def setUp(self):
        self.sanitizer = PromptSanitizer(max_tokens=50)

    def test_complete_sanitization_flow(self):
        prompts = [
            ("Explain AI", 2),
            ("What is ML?", 3),
            ("   Python   Programming   ", 2)
        ]

        for prompt, expected_words in prompts:
            result = self.sanitizer.sanitize(prompt)

            self.assertEqual(
                result["word_count"],
                expected_words
            )

    def test_error_cases_comprehensive(self):
        error_cases = [
            ("", ValueError),
            ("   ", ValueError),
            (None, TypeError),
            (123, TypeError),
            (["test"], TypeError)
        ]

        for invalid_input, expected_error in error_cases:
            with self.assertRaises(expected_error):
                self.sanitizer.sanitize(invalid_input)


if __name__ == "__main__":
    unittest.main(verbosity=2)