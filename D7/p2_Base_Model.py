class BaseModel:
    def __init__(self,model_name, model_type):     #constructor
        self.model_name = model_name
        self.model_type = model_type
        self.is_loaded = False

    def load(self):               #normal method
        self.is_loaded = True
        print(f"{self.model_name} Loaded successfully")

    def unload(self):
        self.is_loaded = False
        print(f"{self.model_name} unloaded successfully")

    def get_info(self):
        return{
            "Model Name": self.model_name,
            "Model_Type": self.model_type,
            "Loaded": self.is_loaded
        }
    