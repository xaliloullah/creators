try:
    import mysql.connector
except:
    pass
    # ImportError("MySQL connector is not installed. Please install it using 'pip install mysql-connector-python'") from e

class MySQL:
    """MySQL-specific implementation of the database connector."""
    def __init__(self, config):
        try:
            self.connection = mysql.connector.connect(
                host=config['host'],
                user=config['username'],
                password=config['password'],
                database=config['database']
            )
            self.cursor = self.connection.cursor(dictionary=True, buffered=True)  

            self.master = 'mysql_master'
            self.placeholder ='%s'
            
        except mysql.connector.Error as e: 
            raise Exception(e)
            
    def execute(self, query, params=None):
        try:
            self.connection.start_transaction() 
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as e:
            self.connection.rollback()
            raise Exception(e)
            
    def get_placeholder(self):
        return self.placeholder
    
    @staticmethod
    def get_syntax():
        # Definitions MySQL 
        return {
            'ID' : 'BIGINT(20)',
            'VARCHAR': 'VARCHAR',
            'BIGINT': 'BIGINT',
            'INT': 'INT',
            'SMALLINT': 'SMALLINT',
            'MEDIUMINT': 'MEDIUMINT',
            'CHAR': 'CHAR',
            'FLOAT': 'FLOAT',
            'DATE': 'DATE',
            'DECIMAL': 'DECIMAL',
            'DOUBLE': 'DOUBLE',
            'TINYTEXT': 'TINYTEXT',
            'TINYINT': 'TINYINT',
            'VARBINARY': 'VARBINARY',
            'BINARY': 'BINARY',
            'BLOB': 'BLOB',
            'ENUM': 'ENUM',
            'TEXT': 'TEXT',
            'JSON': 'JSON',
            'BIT': 'BIT',
            'BOOLEAN': 'BOOLEAN',
            'DATETIME': 'DATETIME', 
            'NUMERIC': 'NUMERIC', 
            'STRING': 'STRING',  
            'TIME': 'TIME',
            'AUTO_INCREMENT': 'AUTO_INCREMENT',
            'PRIMARY_KEY': 'PRIMARY KEY',   
            'FOREIGN_KEY': 'FOREIGN KEY',   
            'REFERENCES': 'REFERENCES',   
            'DEFAULT': 'DEFAULT',  
            'NOT_NULL': 'NOT NULL',                   
            'NULL': 'NULL',                   
            'UNIQUE': 'UNIQUE',                        
            'SET_NULL': 'SET NULL',
            'CHECK': 'CHECK',
            'COMMENT': 'COMMENT', 
            'TIMESTAMP': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP',  
            'UNSIGNED': 'UNSIGNED', 
            'ON_UPDATE': 'ON UPDATE', 
            'ON_DELETE': 'ON DELETE', 
        }


 