class ModelVersion:
    def __init__(self, version):
        self.version = version
    def update_version(self, new_version):
        self.version = new_version
        print("version is updated")

    def show_version(self):
        print(f"Current Version: {self.version}")
version = ModelVersion("v1.0")
version.show_version()
version.update_version("v2.0")
version.show_version()