from utils.creator.src.core.router import Router 

class Route:
    router = Router()
        
    @staticmethod
    def get(uri, action, name=None):
        Route.router.get(uri, action, name)
        

    @staticmethod
    def post(uri, action, name=None):
        Route.router.post(uri, action, name)

    @staticmethod
    def put(uri, action, name=None):
        Route.router.put(uri, action, name)

    @staticmethod
    def delete(uri, action, name=None):
        Route.router.delete(uri, action, name)

    @staticmethod
    def patch(uri, action, name=None):
        Route.router.patch(uri, action, name)

    @staticmethod
    def any(uri, action, name=None):
        Route.router.any(uri, action, name)
        
    @staticmethod
    def resource(name, controller): 
        Route.get(f'/{name}', controller.index, f'{name}.index')      
        Route.get(f'/{name}/create', controller.create, f'{name}.create')  
        Route.post(f'/{name}/store', controller.store, f'{name}.store')       
        Route.get(f'/{name}/{{id}}', controller.show, f'{name}.show')
        Route.get(f'/{name}/{{id}}/edit', controller.edit, f'{name}.edit')
        Route.put(f'/{name}/{{id}}/update', controller.update, f'{name}.update')
        Route.delete(f'/{name}/{{id}}/destroy', controller.destroy, f'{name}.destroy')

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
    def route(name, **params): 
        method = params.get("method", "GET")
        return Route.router.route(method, name, **params)
    
    @staticmethod
    def dispatch(uri, **params):
        method = params.get("method", "GET")
        return Route.router.dispatch(method, uri)


