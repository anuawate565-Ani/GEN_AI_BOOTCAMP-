class APIKeyManager:
    def __init__(self, api_key):
        self.api_key = api_key
    def show_key(self):
        print(f"API Key: {self.api_key}")
manager = APIKeyManager("xyz-1234")
manager.show_key()