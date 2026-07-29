from p2_Base_Model import BaseModel

class VisisonModel(BaseModel):

    def __init__(self, model_name, image_size):
        super().__init__(model_name, "Vision")
        self.image_size = image_size

    def classify(self, image_path):
        print(f"Classifying image : {image_path}")

        return {
            "Label" : "Cat",
            "Confidence" : 0.88
        }

    def get_info(self):
        info = super().get_info()

        info["Image Size"] = self.image_size

        return info