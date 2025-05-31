from utils.creator.src.databases.connectors import Connector 

class Database:
    def __init__(self):
        self.Connection = Connector.connect()

    def execute(self, query, params=None):
        if not params: 
            return self.Connection.execute(query)
        else: 
            return self.Connection.execute(query, params) 

    def commit(self):
        self.Connection.connection.commit()

    def rollback(self):
        self.Connection.connection.rollback()

    def fetchall(self, query, params=None):
        self.execute(query, params)
        return self.Connection.cursor.fetchall()

    def fetchone(self, query, params=None):
        self.execute(query, params)
        return self.Connection.cursor.fetchone()

    def close(self):
        self.Connection.cursor.close() 

    
     
     
 
    
