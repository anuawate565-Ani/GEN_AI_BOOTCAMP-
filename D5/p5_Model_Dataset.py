import csv

class ModelDataset:

    def __init__(self):
        self.model_dataset = "models.csv"
    
        self.models = [
            ["Model", "temperature", "Max token"],
            ["Llama3", 0.9, 888],
            ["gemini", 0.5, 1022],
            ["GPT", 0.6, 1002]
        ]
    
    def save_dataset(self):
        with open(self.model_dataset, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.models)
   
        print("Dataset saved successfully.")


dataset = ModelDataset()
dataset.save_dataset()
