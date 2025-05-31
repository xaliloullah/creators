def controller(name:str, model, resource:bool=False):
        code = f"""from main import Creator
""" 
        
        if model:
            code += f"""from app.models.{str(model).lower()} import {str(model).capitalize()}
"""
         
        code += f"""
class {name}:
    from utils.creator.src.requests.request import Request
"""
         
        if resource:
            code += f"""
    @staticmethod
    def index():
        #
        return

    @staticmethod
    def create():
        #
        return

    @staticmethod
    def store(request: Request):
        #
        return

    @staticmethod
    def edit(id):
        #
        return

    @staticmethod
    def update(request: Request, id):
        #
        return

    @staticmethod
    def show(id):
        #
        return

    @staticmethod
    def destroy(id):
        #
        return
    """ 
        else:
            code += f"""    pass
"""

        return code 