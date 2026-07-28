import csv 

class ModelMetrics:

    def __init__(self):
        self.model = "model_metrics.csv"

        self.metrics = [
            {
                "Model" : "Llama3",
                "Accuracy" : 99,
                "Loss" : 0.22
            },
            {
                "Model" : "GPT-4",
                "Accuracy" : 88,
                "Loss" : 0.55
            },
            {
                "Model" : "Gemini",
                "Accuracy": 85,
                "Loss" : 0.66
            }
        ]
    def save_metrics(self):
        with open(self.model, "w", newline="") as file:
            field_names = ["Model", "Accuracy", "Loss"]
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()

            writer.writerows(self.metrics)
            print("Model metrics saved successfully")
metrics = ModelMetrics()
metrics.save_metrics()                                                                                                                                                                                                                                                                                                          
