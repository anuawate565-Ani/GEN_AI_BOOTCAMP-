import json

class ChatBotConfig:

    def __init__(self):
        self.chat_bot = "chat_bot.json"

        self.config = {
            "Model": "Llama 3",
            "Temperature": 0.6,
            "Max Token": 1022,
            "System Prompt assistant": "You are a helpful ai assistant"
        }

    def save_chat(self):

        with open(self.chat_bot, "w") as f:
            json.dump(self.config, f, indent=2)
        print("Configuration Saved successfully")

    def load_chat(self):
        with open(self.chat_bot, "r") as f:
            self.config = json.load(f)
        print("\nConfiguration loaded successfully")

    def show_chat(self):
        print("\n Current Chatbot Configuration: \n")
        print(self.config)
        print(type(self.config))
        print(type(str(self.config)))


chat = ChatBotConfig()
chat.save_chat()
chat.load_chat()
chat.show_chat()
