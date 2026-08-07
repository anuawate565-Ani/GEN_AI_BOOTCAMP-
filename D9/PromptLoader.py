from pathlib import Path
from custom_exceptions import PromptValidationError


class PromptLoader:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load_prompt(self) -> str:
       
        try:

            if not isinstance(self.file_path, str):
                raise TypeError("File path must be a string.")

            path = Path(self.file_path)

            if not path.exists():
                raise FileNotFoundError("Prompt file not found.")

            with open(path, "r", encoding="utf-8") as file:
                prompt = file.read()

            if not prompt.strip():
                raise ValueError("Prompt file is empty.")

            if len(prompt.strip()) < 10:
                raise ValueError(
                    "Prompt must contain at least 10 characters."
                )

        except (TypeError, FileNotFoundError, ValueError) as error:
            print(f"Validation Error: {error}")
            return ""

        except Exception as error:
            raise PromptValidationError(
                f"Unexpected validation error: {error}"
            )

        else:
            print("✅ Prompt Loaded Successfully")
            return prompt

        finally:
            print("Prompt Validation Finished")