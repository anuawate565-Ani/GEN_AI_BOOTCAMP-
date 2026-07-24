import json

class ConfigLoader:
    def __init__(self):
        self.file_name = "config.json"

    def load_config(self):
        with open(self.file_name, "r") as file:
            config = json.load(file)
        print(config)
        print(type(config))

loader = ConfigLoader()
loader.load_config()
