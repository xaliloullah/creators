def middleware(name: str, table: str):
    code = f"""from utils.creator.src.middlewares import Middleware

class {name}(Middleware):
    def __init__(self):
        self.table = '{table}'
        super().__init__(self.table)
        # 
"""
    return code