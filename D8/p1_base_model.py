#type hint
import logging

logging.basicConfig(
    level = logging.INFO,
    format= "%(levelname)s:  %(message)s"
)

logger = logging.getLogger(__name__)

class BaseModel:

    def __init__(self, model_name: str, model_type: str) -> None :
        """
           Initialize the base model
        """
        self.model_name = model_name
        self.model_type = model_type
        self.is_loaded = False

    def load(self) -> bool:
        """
        load the model in memory
        Return:
            bool : 
        """
        self.is_loaded = True
        logger.info(f"{self.model_name} loaded.") 
        return True

    def unload(self) -> bool:
        """ Unload the model from memory """
        self.is_loaded = False 
        logger.info(f"{self.model_name} unloaded.")
        return True

    def get_info(self) -> dict:
        """
        Return basic information about the model.

        Return :
                dict: Dictionary containing model details. 
        """
        return {
            "Model Name" : self.model_name,
            "Model Type" : self.model_type
        }