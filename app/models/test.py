from utils.creator.src.models.model import Model 

class Test(Model):
    def __init__(self):
        self.table = 'tests'
        super().__init__(self.table)
        # 
