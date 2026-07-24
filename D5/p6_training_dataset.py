import csv

class TrainingDataset:

    def __init__(self):
        self.training_data = "training_dataset.csv"

        self.dataset = [
            ["Dataset", "image", "Classes"],
            ["Cats_vs_dogs", 250, 2],
            ["CIFAR", 1000, 10]
        ]

    def save_dataset(self):
        with open(self.training_data, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.dataset)
        print("Training Dataset SAved Successfully")
training = TrainingDataset()
training.save_dataset()