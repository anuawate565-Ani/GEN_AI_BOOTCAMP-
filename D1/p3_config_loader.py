class ConfigLoader:
    def __init__(self, config_path):
        self.config_path =config_path

    def load(self):
        print(f"Showing configuration: {self.config_path}")
loader = ConfigLoader("config.ymal")
loader.load()