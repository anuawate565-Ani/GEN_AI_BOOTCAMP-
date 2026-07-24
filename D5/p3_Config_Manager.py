import json

class ConfigManager:

    def __init__(self):
        self.file_name = "configm.json"

        self.config = {
            "Model" : "Gpt",
            "Temperature": 0.77,
            "Token": 546
        }
    
    def save_config(self):
        
        with open(self.file_name, "w") as f:
            json.dump(self.config, f, indent=2)
        print("Configuration saved successfully")

    def load_config(self):
        with open(self.file_name, "r") as f:
            self.config = json.load(f)
            print("Configuration loaded successfully")

    def show_config(self):
        print("\n Current Configuration: \n")
        print(self.config)
        print(type(self.config))

manager = ConfigManager()
manager.save_config()
manager.load_config()
manager.show_config()