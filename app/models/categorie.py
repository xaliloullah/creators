from utils.creator.src.models.model import Model

class Categorie(Model):
    def __init__(self):
        self.table = 'categories'
        super().__init__(self.table)
        # 
