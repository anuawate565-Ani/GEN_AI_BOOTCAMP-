"""
Gemini API client 
Handles api call with error handling."""

import logging
from typing import Optional

from google import genai
from ..config.settings import load_config, validate_config

logger = logging.getLogger(__name__)
class GeminiClient:
    def __init__(self):
        """Initialize client with config from environment."""

        try:
            self.config = load_config()
            validate_config(self.config)

            self.client = genai.Client(
            api_key=self.config["api_key"]
            )

            logger.info(
            f"GeminiClient initialized with model: {self.config['model']}"
            )

        except ValueError as e:
            logger.error(f"Config error: {e}")
            raise
    def generate(self, prompt: str) -> Optional[str]:

        try:
            response = self.client.models.generate_content(
                model=self.config["model"],
                contents=prompt
            )

            return response.text

        except Exception as e:
            logger.error(f"Generation error: {e}")
            raise          