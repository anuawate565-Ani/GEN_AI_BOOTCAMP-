import csv

class DatasetReader:

    def __init__(self):
        self.file_name = "training_dataset.csv"

    def read_dataset(self):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

dataset = DatasetReader()
dataset.read_dataset()