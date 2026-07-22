class  TextChunnker:
   
    def __init__(self):
        self.text = ""            #empty string
        self.chunks = []         #empty list 
    
    def load_text(self):
        self.text = ( 
            "Article Intelligence is transforming healthcare, "
             "education, finance and other industries,"
            )
        print("Text Loaded")
        
    def  create_chunks(self):     #create_chunk depend on the data prepared by load_text()
        
        if self.text == "":      
            self.load_text()

        self.chunks = self.text.split()

        print("Chunk Created")    # this line is for user ...so it will understand what happens (confirmation message )
    
    def show_chunks(self):
        
        if len(self.chunks) == 0:
            self.create_chunks()
            
        print("word chunks: ")

        for word in self.chunks:
            print(word)

chunker = TextChunnker()

chunker.show_chunks() 