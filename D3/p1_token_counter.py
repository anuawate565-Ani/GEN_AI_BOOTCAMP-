#MULTIPLE METHOD
class TokenCounter:
    def __init__(self, prompt):
        self.prompt = prompt
    def count_tokens(self):
        words = self.prompt.split()
        print(f"Total Token: {len(words)}")
    def show_prompt(self):
        print(f"Prompt: {self.prompt}")

counter = TokenCounter("Explain Artifical Intelligence and machine learning")
counter.show_prompt()
counter.count_tokens()


#this code count the number of words in the stored prompt 