from p2_llm_model import LLMModel
from p3_vision_model import VisionModel
from p4_embedding_model import EmbeddingModel

import logging

logger = logging.getLogger(__name__)

class ModelRegistry:
    def __init__(self) -> None:
            """
            Initialize the Model Registry
            """
            self.models : dict = {}

    def register_model(self, model) -> None:
            """ 
            Register a model.
            Args:
                model : Model object to register
            """
            self.models[model.model_name] = model
            logger.info(f" Registered model: {model.model_name}")

    def get_model(self, model_name: str):
                """
                Return model by name.
                Args:
                    model_name : Name of the model
                Returns:
                    Basemodel or none
                """
                return self.models.get(model_name)

    def list_model(self) -> None:
            """
            Display all registered model."""
    
            logger.info("Availabe Model: ")
    
            for name in self.models:
                logger.info(f" - {name}")

    def load_all(Self) -> None:
           """    Load all regisitered models. """
           logger.info("Loading all model....")

           for model in Self.models.values():
                  model.load()

    def unload_all(self) -> None:
           
           """
            Unload all regisitered models.
           """
           logger.info("Unloading all models....")

           for model in self.models.values():
                  model.unload()