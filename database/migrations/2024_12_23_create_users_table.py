from utils.creator.src.databases.schema.table import Table


# Up function for users table
def up():
    table = Table('users')
    
    table.id()
    table.string("name")
    table.string("email").unique()
    table.string("password")
    table.timestamps()
    
    table.create()


# Down function for users table
def down():
    table = Table('users')
    table.drop()
