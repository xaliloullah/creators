from utils.creator.src.databases.schema.table import Table


# Up function for tests table
def up():
    table = Table('tests')
    table.id()
    table.string('name')
    table.text('details')
    table.tinyint('etat')
    table.timestamps()
    table.create()


# Down function for tests table
def down():
    table = Table('tests')
    table.drop()
