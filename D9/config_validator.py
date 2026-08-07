class ConfigValidator:

    def validate_learning_rate(self, lr: float) -> str:

        try:

            if not isinstance(lr, (int, float)):
                raise TypeError("Learning rate must be a number.")
            
            if lr <= 0:
                raise ValueError("Learning rate cannot be zero or negative.")

            if lr > 1:
                raise ValueError("Learning rate cannot be greater than 1.")

            return "Learning rate is valid."

        except TypeError as e:
            print(f"Type Error : {e}")
        except ValueError as e:
            print(f"Value Error : {e}")