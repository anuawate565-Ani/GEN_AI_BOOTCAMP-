from p1_base_model import BaseModel 

import logging

logger = logging.getLogger(__name__)

class EmbeddingModel(BaseModel):
    def __init__(self, model_name: str, dimension: int) -> None:
        """ 
        Initialize an Embedding model.
        Args:
            model_name : name of the embedding model
            dimension : size of the embedding vector 
        """
        super().__init__(model_name, "EMBEDDING")
        self.dimension = dimension

    def embed(self, text: str) -> list[float]:
        """ Generate Embedding for the given text
        Args:
            tetxt: Input text for embedding generation
        """
        logger.info(f"Generating embedding for: {text}")
        return [0.12, 0.44, 0.66]

    def get_info(self) -> dict:
        """ Return complete information for embedding.
        Returns:
            dict: Dictionary containing model information and embedding dimension
        """

        info = super().getinfo()
        info["Dimension"] = self.dimension
        return info
