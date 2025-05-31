def model(name: str, table: str):
    code = f"""from utils.creator.src.models import Model

class {name.capitalize()}(Model):
    def __init__(self):
        self.table = '{table}'
        super().__init__(self.table)
        # 
"""
    return code


