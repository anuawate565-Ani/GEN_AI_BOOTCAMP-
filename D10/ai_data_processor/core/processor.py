from typing import Dict, Optional
from ..handlers.error_handler import ConfigValidationError
class BaseProcessor:
    def __init__(
        self,
        model_name: str,
        learning_rate: float,
        batch_size: int
    ) -> None:
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size

    def process(self, data: Dict) -> Dict:
        return {
            "processed": True,
            "data": data
        }

    def validate(self) -> None:
        try:
            if not isinstance(self.model_name, str):
                raise TypeError("Model name must be a string.")

            if not self.model_name.strip():
                raise ValueError("Model name cannot be empty.")

            if not isinstance(self.learning_rate, (int, float)):
                raise TypeError("Learning rate must be a number.")

            if not (0 < self.learning_rate <= 1):
                raise ValueError("Learning rate must be between 0 and 1.")

            if not isinstance(self.batch_size, int):
                raise TypeError("Batch size must be an integer.")

            if self.batch_size <= 0:
                raise ValueError("Batch size must be greater than zero.")

        except (TypeError, ValueError) as error:
            print(f"Validation Error: {error}")

        except Exception as error:
            raise ConfigValidationError(
                f"Unexpected validation error: {error}"
            )

        else:
            print("Configuration Valid")

        finally:
            print("Validation Finished")