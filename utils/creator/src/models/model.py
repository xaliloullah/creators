from utils.creator.src.core import Collection 
from utils.creator.src.databases.query import DB  


class Model:
    def __init__(self, table, id=""):
        self.table = table
        self.id = id
        self.DB = DB()
        self.attributes = self.all().get() 

    def __str__(self):
        return str(self.get())
    
    def __getattr__(self, name):
        return self.get().get(name)
     
    def __getitem__(self, index): 
        return self.get()[index]
    
    def __iter__(self): 
        return iter(self.get())
    
    def __len__(self):
        return len(self.get())
    
    def __repr__(self):
        return str(self.get())

    def new(self,columns):
        self.DB.create(self.table, columns).execute()
        return self
    
    def create(self, **column):
        self.DB.insert(self.table, **column).execute()

    def update(self, **kwargs):
        self.DB.update(self.table, **kwargs).where(id=self.get_id()).execute()

    def delete(self): 
        self.DB.delete(self.table).where(id=self.get_id()).execute()

    def drop(self):
        self.DB.drop(self.table).execute()
        
        
    def all(self):
        self.attributes = self.DB.select(self.table).fetchall()
        return self

    def find(self, id):
        self.id = id
        self.attributes = self.DB.select(self.table).where(id=id).fetchone()
        return self     

    def where(self, **kwargs): 
        self.attributes = self.DB.select(self.table).where(**kwargs).fetchall()
        return self

    def where_not(self, **kwargs):
        self.attributes = self.DB.select(self.table).where_not(**kwargs).fetchall()
        return self

    def or_where(self, **kwargs):
        self.attributes = self.DB.select(self.table).or_where(**kwargs).fetchall()
        return self

    def like(self, **kwargs):
        self.attributes = self.DB.select(self.table).like(**kwargs).fetchall()
        return self

    def take(self, value:int):
        self.attributes = self.DB.select(self.table).limit(value).fetchall()
        return self

    def order_by(self, column='id'):
        self.attributes = self.DB.select(self.table).order_by(column).fetchall()
        return self

    def order_by_desc(self, column='id'):
        self.attributes = self.DB.select(self.table).order_by(column,"DESC").fetchall()
        return self

    def count(self): 
        return self.DB.count(self.table)
    
    def first(self):  
        return self.DB.first().fetchone()   
    
    def last(self):  
        return self.DB.last().fetchone()
    
    def get_id(self):
        return self.id

    def get(self):
        return self.attributes
    
    
    
    

    # def get_schema(self):
    #     return self.DB.get_schema(self.table)

    # def get_methodes(self):
    #     self.methodes = []
    #     for function, membre in self.__class__.__dict__.items():
    #         if callable(membre) and not function.startswith('__'):
    #             self.methodes.append(f" - {function}()")
    #     return self.methodes

    # def get_variables(self):
    #     variables = ""
    #     for key, value in vars(self).items():
    #         if isinstance(value, list):
    #             variables += f"{key}:\n{'\n'.join(map(str, value))}\n\n"
    #         elif isinstance(value, dict):
    #             variables += f"{key}:\n"
    #             variables += '\n'.join([f" {sub_key}: {item}" for sub_key,
    #                                     item in value.items()])
    #         else:
    #             variables += f"{key}: {value}\n\n"
    #     return variables

    # def get_primary_key_value(self):
    #     return self.DB.get_primary_key_value(self.table)
