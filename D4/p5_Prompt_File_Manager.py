class PromptFileManager:
    
    def __init__(self):
        self.file_name = "prompt.txt"

    def save_prompt(self):

        with open(self.file_name, "w") as file:
            file.write("System: You are an AI Assistant.\n")
            file.write("User: Explain Machine Learning.\n")
            file.write("Assistant: Machine Learning is... ")

        print("Prompt Saved Sucessfully ")

    def read_prompt(self):

        with open(self.file_name, "r") as file:
            content = file.read()
        
        print("\nCompleted Prompt:\n")
        print(content)

    def read_line(self):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        
        print("\nPrompt Line by Line :\n")

        for line in lines:
            print(line.strip())

manager = PromptFileManager()

manager.save_prompt()
manager.read_prompt()
manager.read_line()
