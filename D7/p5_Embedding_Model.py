from p2_Base_Model import BaseModel

class EmbeddingModel(BaseModel):

    def __init__(self, model_name, embedding_dim):
        super().__init__(model_name, "Embedding")
        self.embedding_dim = embedding_dim

    def embed(self, text):
        print(f"Creating Embedding for  : {text}")
        return[0.33, 0.44, 0.99]

    def get_info(self):
        info = super().get_info()

        info["Embedding Dimension : "] = self.embedding_dim

        return info