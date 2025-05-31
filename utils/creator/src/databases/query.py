from utils.creator.src.databases.database import Database 
# from utils.creator.src.models.collection import Collection

class DB:
    def __init__(self): 
        self.DB = Database() 
        self.sql = ""
        self.values = ()
        self.conditions = ""
        self.attributes = "" 
        self.placeholder = self.DB.Connection.get_placeholder()
        # self.collection = Collection
        
        
    def execute(self):
        self.DB.execute(self.sql, self.values)
        
    def get(self):
        return self.DB.fetchall(self.sql, self.values)
    
    def fetchall(self):
        return self.DB.fetchall(self.sql, self.values)
    
    def fetchone(self):
        return self.DB.fetchone(self.sql, self.values)
    
    def create(self, table, columns):  
        self.values = ()
        self.sql = f'''CREATE TABLE IF NOT EXISTS {table} ({columns})''' 
        return self
        
    def drop(self, table):
        self.values = ()
        self.sql = f'''DROP TABLE IF EXISTS {table}'''
        return self
    
    def insert(self, table, **kwargs):
        columns = ', '.join(kwargs.keys())
        self.values = tuple(kwargs.values())
        placeholders = ', '.join([f'{self.placeholder}' for _ in kwargs.keys()])
        self.sql = f'''INSERT INTO {table} ({columns}) VALUES ({placeholders})'''  
        return self
    
    def update(self, table, **kwargs): 
        columns = ', '.join([f'{key}={self.placeholder}' for key in kwargs.keys()])
        self.values = tuple(kwargs.values())
        columns += ', updated_at=CURRENT_TIMESTAMP'
        self.sql = f'''UPDATE {table} SET {columns}'''
        return self
    
    def delete(self, table): 
        self.values = ()
        self.sql = f'''DELETE FROM {table}''' 
        return self
    
    def select(self, table, *columns):
        self.values = ()
        if not columns:
            columns = ['*'] 
        columns = ', '.join(columns)
        self.sql = f'''SELECT {columns} FROM {table}'''  
        return self
    
    def where(self, **kwargs):
        self.conditions = ' AND '.join([f'{key}={self.placeholder}' for key in kwargs.keys()])
        self.values += tuple(kwargs.values())
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} AND {self.conditions}'''
        else:
            self.sql = f'''{self.sql} WHERE {self.conditions}'''
        return self
    
    def where_not(self, **kwargs):
        self.conditions = ' AND '.join([f'{key}!={self.placeholder}' for key in kwargs.keys()])
        self.values += tuple(kwargs.values())
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} AND {self.conditions}'''
        else:
            self.sql = f'''{self.sql} WHERE {self.conditions}''' 
        return self
    
    def like(self, **kwargs):
        self.conditions = ' AND '.join([f'{key} LIKE {self.placeholder}' for key in kwargs.keys()])
        self.values += tuple(f"%{value}%" for value in kwargs.values())
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} AND {self.conditions}'''
        else:
            self.sql = f'''{self.sql} WHERE {self.conditions}''' 
        return self
    
    def or_where(self, **kwargs):
        self.conditions = ' OR '.join([f'{key}={self.placeholder}' for key in kwargs.keys()])
        self.values += tuple(kwargs.values())
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} OR {self.conditions}'''
        else:
            self.sql = f'''{self.sql} WHERE {self.conditions}''' 
        return self
    
    def where_null(self, column):
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} AND {column} IS NULL'''
        else:
            self.sql = f'''{self.sql} WHERE {column} IS NULL'''
        return self

    def where_not_null(self, column):
        if 'WHERE' in self.sql:
            self.sql = f'''{self.sql} AND {column} IS NOT NULL'''
        else:
            self.sql = f'''{self.sql} WHERE {column} IS NOT NULL'''
        return self

    def in_clause(self, column, values):
        placeholders = ', '.join([self.placeholder for _ in values])
        self.sql = f'''{self.sql} WHERE {column} IN ({placeholders})'''
        self.values += tuple(values)
        return self
    
    def having(self, **kwargs):
        conditions = ' AND '.join([f'{key}={self.placeholder}' for key in kwargs.keys()])
        self.sql = f'''{self.sql} HAVING {conditions}'''
        self.values += tuple(kwargs.values())
        return self
    
    def raw(self, sql, *values):
        self.sql = sql
        self.values = values
        return self
    
    def subquery(self, subquery_sql, alias):
        self.sql = f'''({subquery_sql}) AS {alias}'''
        return self
    
    def paginate(self, page, per_page):
        offset = (page - 1) * per_page
        self.sql = f"{self.sql} LIMIT {per_page} OFFSET {offset}" 
        return self
    
    def order_by(self, column='id', option='ASC'):
        self.sql = f'''{self.sql} ORDER BY {column} {option}''' 
        return self
    
    def limit(self, value):
        self.sql = f'''{self.sql} LIMIT {value}''' 
        return self
    
    def alias(self, alias):
        self.sql = f'''{self.sql} AS {alias}'''  
        return self
    
    def join(self, table, option=""):
        self.sql = f'''{self.sql} {option} JOIN {table}'''  
        return self
    
    def on(self, **kwargs): 
        self.conditions = [f"{key} = {value}" for key, value in kwargs.items()] 
        conditions_str = ' AND '.join(self.conditions) 
        self.sql = f"{self.sql} ON {conditions_str}" 
        return self
    
    def count(self, column='*'):
        self.sql = f'''SELECT COUNT({column}) FROM ({self.sql}) AS alias''' 
        return self
    
    def first(self):  
        self.order_by().limit(1) 
        return self
    
    def last(self):  
        self.order_by(option="DESC").limit(1) 
        return self
    
    def generate_script(self):
        return self.sql, self.values
    
    def debug(self):
        sql_with_values = self.sql
        for value in self.values:
            sql_with_values = sql_with_values.replace(self.placeholder, repr(value), 1)
        return f"SQL Query: {sql_with_values}"

    def begin_transaction(self):
        self.sql = 'BEGIN TRANSACTION' 
        return self

    def commit(self):
        self.sql = 'COMMIT' 
        return self

    def rollback(self):
        self.sql = 'ROLLBACK' 
        return self
    
    def generate_script(self):
        return self.sql, self.values
    
    def reset_script(self):
        self.sql=""
        self.values=() 
        
    def __str__(self):
        return f"{self.sql}, {self.values}"
    
    def __repr__(self):
        return self.sql
    
    def __call__(self):
        return self.DB.fetchall(self.sql, self.values)

#   
# table = Query()
# table.select('migrations').order_by(option='DESC').limit(1).like(na='sa').like(asd='dsa').first()
 
# print(table.generate_script()) 


#     # def has_one(self, related_table, foreign_key, foreign_id,pk='id'):
#     #     conditions = {f"{foreign_key}":f"{foreign_id}"}
#     #     self.Query.select(related_table).where(conditions) 
#     #     self.attributes = self.DB.fetchone(self.Query.sql,self.Query.values)
#     #     return self

#     # def has_many(self,related_table, foreign_key, foreign_id, pk='id'): 
#     #     conditions = {f"{foreign_key}":f"{foreign_id}"}
#     #     self.Query.select(related_table).where(conditions) 
#     #     self.attributes = self.DB.fetchall(self.Query.sql, self.Query.values)
#     #     return self


#     # def belongs_to(self, related_table,table, foreign_key=None, foreign_id=None):
#     #     query = f"""SELECT * FROM {related_table} WHERE id = (SELECT {foreign_key} FROM {table} WHERE id = ?)"""
#     #     self.attributes = self.DB.fetchall(query, (foreign_id,))    
#     #     return self
 