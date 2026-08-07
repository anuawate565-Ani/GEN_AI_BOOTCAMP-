class ConfigValidationError(Exception):
    """ Custom Exception for configuration validation errors. """
    pass

class AIAIConfigValidator:
    def __init__(self, model_name: str, learning_rate: float, batch_size: int):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size

    def validate(self):

        try:
            if  not isinstance(self.model_name, str):
                raise TypeError("Model name must be a string.")

            if not self.model_name.strip():
                raise ValueError("Model name cannot be empty.")

            if not isinstance(self.learning_rate,(int, float)):
                raise ValueError("Learning rate must be a number.")
            if not (0 < self.learning_rate <= 1):
                raise ValueError("Learning rate must be between 0 and 1.")
            if not isintance(self.batch_size , int):
                raise TypeError("Batch sizer must be an nuumber.")
            if self.batch_size <= 0:
                raise ValueError("Batch size must be greater than zero.")
        except (TypeError, ValueError) as error:
            print(f"Validation Error: {error}")
        except Exception as error:
            raise ConfigValidationError(f"Unexpected validation error: {error}")

        else:
            print("Configuration is valid.")

        finally:
            print("Validation process completed.")

if __name__ == "__main__":

    validator = AIAIConfigValidator(
        model_name = "Llama-3",
        learning_rate = 0.02,
        batch_size = 33
    )