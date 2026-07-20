#other state
class EpochCounter:
    def __init__(self):
        self.epoch_count = 0
    def increase_epoch(self):
        self.epoch_count +=1
        print("Epoch Completed")

    def show_epoch(self):
        print(f"Current Epoch: {self.epoch_count}")

epochh = EpochCounter()
epochh.show_epoch()
epochh.increase_epoch()
epochh.increase_epoch()
epochh.increase_epoch()
epochh.show_epoch()
