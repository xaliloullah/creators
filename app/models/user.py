from utils.creator.src.models.model import Model

class User(Model):
    def __init__(self):
        self.table = 'users'
        super().__init__(self.table)
        # 
