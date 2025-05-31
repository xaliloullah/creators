from utils.creator.src.core.router import Router 

class Route:
    router = Router()

    @staticmethod
    def add(uri, action, name=None):
        Route.router.any(uri, action, name)
        
    @staticmethod
    def resource(name, controller): 
        Route.add(f'/{name}', controller.index, f'{name}.index')      
        Route.add(f'/{name}/create', controller.create, f'{name}.create')  
        Route.add(f'/{name}/store', controller.store, f'{name}.store')       
        Route.add(f'/{name}/{{id}}', controller.show, f'{name}.show')
        Route.add(f'/{name}/{{id}}/edit', controller.edit, f'{name}.edit')
        Route.add(f'/{name}/{{id}}/update', controller.update, f'{name}.update')
        Route.add(f'/{name}/{{id}}/destroy', controller.destroy, f'{name}.destroy')

    @staticmethod
    def group(attributes, action):
        Route.router.group(attributes, action)
        return Route

    @staticmethod
    def controller(self, controller, action: callable):
        pass
    
    @staticmethod
    def show():
        return Route.router.show()
        
    @staticmethod
    def list():
        return Route.router.list()
     
    @staticmethod
    def route(name, **kwargs): 
        method = kwargs.get("method", "ANY")  
        uri =  Route.router.route(method, name, **kwargs) 
        handler = Route.router.dispatch(method, uri, **kwargs)   
        return handler
    
    # @staticmethod
    # def dispatch(uri, **params):
    #     method = params.get("method", "ANY")
    #     return Route.router.dispatch(method, uri)


