from config import database
from utils.creator.src.databases.connectors import Sqlite
from utils.creator.src.databases.connectors import MySQL

sqlite = 'sqlite'
mysql = 'mysql'

driver = database.driver
connections = database.connections
config = connections[driver]

class Connector:
    @staticmethod
    def connect(): 
        if driver == sqlite:
            return Sqlite(config)
        elif driver == mysql:
            # require('mysql-connector-python')
            return MySQL(config) 
        else: 
            raise Exception(f"Unsupported database driver: {driver}")
    
    @staticmethod
    def get_database():
        if driver == sqlite:  
            return Sqlite
        elif driver == mysql:
            return MySQL 
        else:
            raise Exception(f"The database driver '{driver}' is not supported.")
        
     
 
        
    
