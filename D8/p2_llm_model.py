from  p1_base_model import BaseModel

import logging 

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)

class LLMModel(BaseModel):
    def __init__(self, model_name: str, max_token: int ) -> None:
        """
        Initialize an LLM Model
        Args:
            model_name = name of the llm model
            max_token = maximum number of token supported 
        """
        super().__init__(model_name, "LLM")
        self.max_token = max_token

    def generate(self, prompt: str) -> str:
        """ 
        Generate a response for given prompt.
        
        Args:
            prompt: Input text given to the LLM
        Return:

        """
        logger.info(f"Generate a response for: {prompt}")
        return "This is Golden Retriever.."

    def get_info(self) -> dict:
        """ 
        Return Complete information about LLm Model.

        Returns:
            dict : Dictionary conataining model information and max tokens
        """
        info = super().get_info()

        info["Max Token"] = self.max_token
        return info