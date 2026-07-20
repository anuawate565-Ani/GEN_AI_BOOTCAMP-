class DatasetTracker:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def update_dataset(self, new_dataset):
        self.dataset_name = new_dataset
        print("dataset updated")

    def show_dataset(self):
        print(f"Current Dataset: {self.dataset_name}")

dataset = DatasetTracker("Titanic Dataset")
dataset.show_dataset()
dataset.update_dataset("Iris Dataset")
dataset.show_dataset()
 
 #stores and update the current dataset being used 