"""
Configuration management for llm client.
loads api key from environment variable.
"""

import os
from typing import Dict

def load_config() -> Dict[str, str|float]:
    """ Load config from environment variables. """
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")
    return {
        "api_key": api_key,
        "model" : model,
        "temperature" : float(os.getenv("GEMINI_TEMPERATURE", 0.9))
    }

def validate_config(config: Dict[str, str|float]) -> bool:
    """ validate config has required keys."""

    required = ["api_key", "model", "temperature"]

    for key in required:
        if key not in config:
            raise ValueError(f"Missing config key: {key}")

    return True