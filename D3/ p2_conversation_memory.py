class ConservationMemory:  #other state
    def __init__(self):
        self.message_count = 0

    def add_message(self):
        self.message_count +=1
        print("Message Added")
    def show_count(self):
        print(f"Total message: {self.message_count}")
message = ConservationMemory()
message.show_count()
message.add_message()
message.add_message()
message.show_count()

#store and update the total number of message in a conversation