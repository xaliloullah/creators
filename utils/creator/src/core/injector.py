class Injector:
    def __init__(self):
        self._dependencies = {}
        
    def __str__(self):
        return str(self._dependencies)

    def register(self, cls, instance=None): 
        if instance is None:
            self._dependencies[cls] = cls
        else:
            self._dependencies[cls] = instance

    def inject(self, annotation): 
        if annotation in self._dependencies: 
            dependency = self._dependencies[annotation]
            return dependency
        return None

    def update(self, cls, instance):
        self._dependencies[cls] = instance
        

    def resolve(self, func, *args, **kwargs):
        from inspect import signature 
        sig = signature(func)
        for name, param in sig.parameters.items():
            if param.annotation != param.empty and name not in kwargs:
                dependency = self.inject(param.annotation)
                if dependency is not None:
                    kwargs[name] = dependency
                else:
                    raise Exception(f"Impossible de résoudre la dépendance pour le paramètre: {name}")  
        return func, args, kwargs 