class ConfigValidationError(Exception):
    """Custom exception for configuration validation errors."""
    pass


class AIConfigValidator:
    """
    Validates AI model configuration.

    Args:
        model_name (str): Name of the AI model.
        learning_rate (float): Learning rate for training.
        batch_size (int): Batch size used during training.
    """

    def __init__(
        self,
        model_name: str,
        learning_rate: float,
        batch_size: int
    ) -> None:
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size

    def validate(self) -> None:
        """
        Validates the AI model configuration.

        Raises:
            TypeError: If datatype is incorrect.
            ValueError: If value is invalid.
            ConfigValidationError: For unexpected validation failures.
        """

        try:
            # Validate model_name
            if not isinstance(self.model_name, str):
                raise TypeError("Model name must be a string.")

            if not self.model_name.strip():
                raise ValueError("Model name cannot be empty.")

            # Validate learning_rate
            if not isinstance(self.learning_rate, (int, float)):
                raise TypeError("Learning rate must be a number.")

            if not (0 < self.learning_rate <= 1):
                raise ValueError("Learning rate must be between 0 and 1.")

            # Validate batch_size
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
            print("✅ Configuration Valid")

        finally:
            print("Validation Finished")


if __name__ == "__main__":

    validator = AIConfigValidator(
        model_name="Llama-3",
        learning_rate=0.001,
        batch_size=32
    )

    validator.validate()