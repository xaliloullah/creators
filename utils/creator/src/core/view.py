from utils.creator.src.core.file import File
from utils.creator.src.core.task import Task 


class View:
    data = {}
    history = []
    
    
    def __init__(self, path:str=None, *args):
        if path:
            path = path.replace('.', '/')
            if args:
                args
            path = File.resources_path(f"{path}.cre")
            Task.run(path)
            
    @staticmethod
    def include(source:str,*args): 
        try:
            source = source.replace('.', '/')
            Task.run(File.resources_path(source+".cre"), args) 
        except Exception as e:
            raise Exception(e) 
        
    @classmethod   
    def get(cls, key):
        return cls.data.get(key)

    @classmethod
    def set(cls, key, value):
        cls.data[key] = value
        
        
    @classmethod
    def share(cls, key, value):
        cls.data[key] = value
        
    @classmethod   
    def get_history(cls):
        return cls.history

    @classmethod
    def set_history(cls, arg):
        cls.history.append(arg)

    @classmethod
    def compact(cls, **kwargs):
        for key, value in kwargs.items():
            cls.set(key, value)
            
    @classmethod
    def back(cls):
        if len(cls.history) > 1:  
            cls.history.pop()   
            previous = cls.history[-1]
            return previous['action'](*previous['args'], **previous['kwargs'])  
        # else:
        #     return "Aucune page précédente à laquelle retourner." 
            
        
    @classmethod
    def section(cls, key, value=None):  
        def decorator(function):
            def wrapper(*args, **kwargs): 
                if value: 
                    cls.set(key, value)
                    return function(*args, **kwargs)  
                else:
                    cls.set(key,{'action': function, 'args': args, 'kwargs': kwargs}) 
                    return
            return wrapper
        return decorator

    @classmethod
    def extend(cls, path): 
        def decorator(function):
            def wrapper(*args, **kwargs):  
                function(*args, **kwargs)
                cls(path) 
                return 
            return wrapper
        return decorator

    @classmethod
    def generate(cls, arg):  
        result = cls.get(arg)  
        if isinstance(result, dict): 
            return result['action'](*result['args'], **result['kwargs']) 
        elif result:   
            return result
        else:
            return "" 