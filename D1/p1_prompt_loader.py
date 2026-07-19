class PromptLoader:
    def __init__(self, prompt_name):
        self.prompt_name = prompt_name

    def load(self):
        print(f"Loading prompt: {self.prompt_name}")

loader = PromptLoader("gen.csv")
loader.load()