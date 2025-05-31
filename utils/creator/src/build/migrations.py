def migration(name: str):
        code = f"""from utils.creator.src.databases.schema import Table


# Up function for {name} table
def up():
    table = Table('{name}')
    table.id()
    #
    table.timestamps()
    table.create()


# Down function for {name} table
def down():
    table = Table('{name}')
    table.drop()
"""
        return code