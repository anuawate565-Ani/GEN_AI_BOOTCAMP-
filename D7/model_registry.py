from p3_llm_model import LLMModel
from p4_Vision_Model import VisisonModel
from p5_Embedding_Model import EmbeddingModel

class ModelRegistry:

    def __init__(self):
        self.models = {}
        self.register(LLMModel("Llama3", 2048))
        self.register(EmbeddingModel("BGE", 768))
        self.register(VisisonModel("YOLOv11", 640))

    def register(self, model):
        self.models[model.model_name] = model
        print(f"{model.model_name} registered successfully.")

    def get_model(self, model_name):
        return self.models.get(model_name)

    def load_all(self):
        for model in self.models.values():
            model.load()

    def unload_all(self):
        for model in self.models.values():
            model.unload()

    def list_models(self):
        for model_name in self.models:
            print(model_name)