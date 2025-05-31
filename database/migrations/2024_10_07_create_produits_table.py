from utils.creator.src.databases.schema.table import Table


# Up function for produits table
def up():
    table = Table('produits')
    table.id()
    table.string("name")
    table.decimal("prix")
    table.foreign_id("categorie_id").constrained().on_delete("CASCADE").on_update("CASCADE") 
    table.tinyint("etat").default(0)
    table.text('details')
    table.timestamps()
    table.create()


# Down function for produits table
def down():
    table = Table('produits')
    table.drop()
