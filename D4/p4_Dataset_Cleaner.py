class DatasetCleaner:
    
    def __init__(self):
        self.dataset = ""
        self.word = []

    def load_dataset(self):
        self.dataset = (
            "Ai," " Machine learning," " Deep Learning, "
            " Computer vision," 
            )
        print("Dataset loaded")

    def clean_dataset(self):

        if self.dataset == "":
            self.load_dataset()
        
        self.word = self.dataset.split()

        print("Dataset is Cleaned")
   
    def show_dataset(self):

        if len(self.word) == 0:
            self.clean_dataset()
        
        print("Dataset Item: ")

        for word in self.word:
            print(word)

cleaner = DatasetCleaner()
cleaner.show_dataset()