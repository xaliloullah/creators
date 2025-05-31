from utils.creator.src.models.model import Model

class Produit(Model):
    def __init__(self):
        self.table = 'produits'
        super().__init__(self.table)
        # 
