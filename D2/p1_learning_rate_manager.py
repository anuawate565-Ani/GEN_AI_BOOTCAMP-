class LearningRateManager:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
   
    def get_learning_rate(self):
        return self.learning_rate


lr = LearningRateManager(0.002)
rate = lr.get_learning_rate()

print(rate)