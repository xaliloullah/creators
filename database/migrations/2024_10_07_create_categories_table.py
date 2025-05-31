from utils.creator.src.databases.schema.table import Table


# Up function for categories table
def up():
    table = Table('categories')
    table.id()
    table.string('name')
    table.tinyint("etat").default(0)
    table.text('details')
    table.timestamps()
    table.create()


# Down function for categories table
def down():
    table = Table('categories')
    table.drop()
