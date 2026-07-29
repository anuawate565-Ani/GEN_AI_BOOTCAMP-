from p2_Base_Model import BaseModel

class LLMModel(BaseModel):

    def __init__(self, model_name, max_tokens):

        super().__init__(model_name, "LLM")

        self.max_tokens = max_tokens

    def generate(self, prompt):
        print(f"Generating response for: {prompt}")

    def get_info(self):

        info = super().get_info()

        info["Max Tokens"] = self.max_tokens

        return info 