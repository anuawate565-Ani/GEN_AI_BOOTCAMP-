import csv
class DatasetDictReader:

    def __init__(self):
        self.file_name = "training_dataset.csv"

    def read_dataset(self):
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(row)
dataset = DatasetDictReader()
dataset.read_dataset() 