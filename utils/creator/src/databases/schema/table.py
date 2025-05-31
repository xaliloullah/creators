from utils.creator.src.databases.query import DB
from utils.creator.src.databases.schema.column import Column 

class Table(Column):
    def __init__(self, name):
        super().__init__()
        self.name = name 
        
    def __str__(self):
        return self.get_definition()

    def get_definition(self):
        return self.generate_script().replace("|", ",")
        
    
    def get_script(self):
        return self.generate_script().replace("|", "\n")
        

    def create(self):  
        DB().create(self.name, self.get_definition()).execute()

    def generate_script(self):
        return "| ".join(self.definition+self.foreign_keys)

    def drop(self): 
        DB().drop(self.name).execute() 