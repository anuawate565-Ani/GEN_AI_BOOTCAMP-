class PromptProcessor:
    
    def __init__(self):
        self.prompt = ""
        self.word = []

    def load_prompt(self):
        self.prompt = (
            " Explain Machine Learning in simple words,"
            )
        print("Prompt has been loaded") 

    def create_word(self):
        
        if self.prompt == "" :
            self.load_prompt()

        self.word = self.prompt.split()

        print("Word is created")

    def show_word(self):

        if len(self.word) == 0:
            self.create_word()
        
        print("Prompt word : ")

        for word in self.word:
            print(word)

processor = PromptProcessor()

processor.show_word()