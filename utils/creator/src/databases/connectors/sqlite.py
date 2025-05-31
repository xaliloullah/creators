import sqlite3 

class Sqlite:
    """SQLite-specific implementation of the database connector."""
    def __init__(self, config):
        try:
            self.connection = sqlite3.connect(config['path'])
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            self.master = 'sqlite_master'    
            self.placeholder ='?'
    
        except sqlite3.Error as e:
            raise Exception(e)
            
    def execute(self, query, params=None):
        try: 
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            self.connection.rollback()
            raise Exception(e)
 
    def get_placeholder(self):
        return self.placeholder
        
    @staticmethod
    def get_syntax():
        # Definitions sqlite
        return { 
            'ID' : 'INTEGER',
            'VARCHAR': 'TEXT',          
            'BIGINT': 'INTEGER',        
            'INT': 'INTEGER',           
            'SMALLINT': 'INTEGER',
            'MEDIUMINT': 'INTEGER',    
            'CHAR': 'TEXT',          
            'FLOAT': 'REAL',       
            'DATE': 'TEXT',            
            'DECIMAL': 'INTEGER',   
            'DOUBLE': 'REAL',      
            'TINYTEXT': 'TEXT',      
            'TINYINT': 'INTEGER',      
            'VARBINARY': 'BLOB',   
            'BINARY': 'BLOB',         
            'BLOB': 'BLOB',   
            'ENUM': 'TEXT',            
            'TEXT': 'TEXT', 
            'JSON': 'TEXT',            
            'BIT': 'INTEGER',           
            'BOOLEAN': 'INTEGER',       
            'DATETIME': 'TEXT',         
            'NUMERIC': 'INTEGER',       
            'STRING': 'TEXT',          
            'TIME': 'TEXT',
            'AUTO_INCREMENT':'AUTOINCREMENT',   
            'FOREIGN_KEY': 'FOREIGN KEY',        
            'PRIMARY_KEY': 'PRIMARY KEY',       
            'REFERENCES': 'REFERENCES',   
            'DEFAULT': 'DEFAULT',  
            'NOT_NULL': 'NOT NULL',                   
            'NULL': 'NULL',                   
            'UNIQUE': 'UNIQUE',                        
            'SET_NULL': 'SET NULL',
            'CHECK': 'CHECK',
            'COMMENT': 'COMMENT',  
            'TIMESTAMP': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP',   
            'UNSIGNED': '', 
            'ON_UPDATE': 'ON UPDATE', 
            'ON_DELETE': 'ON DELETE',      
        }
