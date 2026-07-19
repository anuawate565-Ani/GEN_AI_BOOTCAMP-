class ModelLoader:
    def __init__(self, model_name):
        self.model_name = model_name

    def load(self):
        print(f"loading model: {self.model_name}")
model = ModelLoader("llama 3")
model.load()