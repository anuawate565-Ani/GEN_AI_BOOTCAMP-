class BaseModell:

    def load(self):
        print("Base")

class LLm(BaseModell):

    def load(self):
        super().load()    #super() is used to call the load method of the parent class (BaseModel) from the child class (LLm)
        print("LLM")
model = LLm()
model.load()
#method overriding
