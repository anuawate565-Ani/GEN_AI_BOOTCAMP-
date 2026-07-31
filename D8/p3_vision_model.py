from p1_base_model import BaseModel

import logging

logger = logging.getLogger(__name__)

class VisionModel(BaseModel):

    def __init__(self, model_name: str, image_size: int) -> None:
        """
        Initialize the Vision Model.
        Args:
            model_name : Name of the vision model
            image size : number of image size supported
        """
        super().__init__(model_name, "Vision")
        self.image_size = image_size

    def analysis_image(self, image_path: str) -> str:
        """ Analyse the image.
        Args:
            image_path: Path of the image
        """

        logger.info(f"Analyse image: {image_path}")
        return "Dog detected "

    def get_info(self) -> dict:
        """
        Return the complete information about vision model.
        Returns:
            dict: Dictionary containing model info and image size """

        info = super().get_info()
        info["Image size"] = self.image_size

        return info