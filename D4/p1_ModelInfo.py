class ModelInfo:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def show_name(self):
        print(f"Model Name: {self.name}")
    def show_version(self):
        print(f"Version: {self.version}")

    def Welcome(self):
        self.show_name()
        self.show_version()
        print(f"Welcome to {self.name} ({self.version})")

model = ModelInfo("Llama3","v1.0")
model.Welcome()