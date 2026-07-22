class DatasetFileManager:

    def __init__(self):
        self.file_name = "dataset.txt"
    
    def save_dataset(self):

        with open(self.file_name, "w") as file:
            file.write("Dataset : Iris.\n")
            file.write("Row: 150. \n")
            file.write("Features: 4" )
        
        print("Dataset saved sucessfully")

    def read_dataset(self):

        with open(self.file_name) as file:
            content = file.read()

        print("\nCompleted Dataset:\n")
    
        print(content)
    
    def read_line(self):
    
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            
        print("\n Dataset Line by Line: \n")

        for line in lines:
            print(line.strip())
        
manager = DatasetFileManager()

manager.save_dataset()
manager.read_dataset()
manager.read_line()
