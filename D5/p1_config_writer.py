import  json

class ConfigWriter:

    def __init__(self):
        self.file_name = "config.json"

        self.config = {
            "model ": "Llama3",
            "temperature": 0.6,
            "max_tokens": 566
        }
    def save_config(self):
        with open(self.file_name, "w") as file:
            json.dump(self.config, file, indent=4)
        print("Configuration Saved Successfully")

writer = ConfigWriter()
writer.save_config()