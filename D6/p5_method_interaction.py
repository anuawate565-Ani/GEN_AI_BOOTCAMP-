class MethodInteraction:
    def first(self):
        print("first method executed")
        self.second()
        print("third method executed")
    def second(self):
        print("second method executed")
demo = MethodInteraction()
demo.first()
#method interaction\

