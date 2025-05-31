_env = {}
_ini = ".env"
try:
    with open(_ini, 'r') as file:
        for line in file:
            if line and not line.startswith((';', '#')):
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    _env[key] = value
except:
    pass
                
def env(name: str, default=None):
    return _env.get(name.upper(), default) 


# class ENV:
#     def __init__(self, name: str, default=None):
#         self.name = name
#         self.default = default

#     def __get__(self, instance, owner):
#         return env(self.name, self.default)

#     def __set__(self, instance, value):
#         _env[self.name] = value

#     def __delete__(self, instance):
#         if self.name in _env:
#             del _env[self.name]
#         else:
#             raise AttributeError(f"Attribute {self.name} not found in environment variables.")
        
#     def __repr__(self):
#         return f"ENV({self.name}, {self.default})"
    
#     def __str__(self):
#         return f"ENV: {self.name} = {self.default}"
    
#     def __bool__(self):
#         return self.name in _env and bool(_env[self.name])
    
#     def __contains__(self, item):
#         return item in _env
    
#     def __getitem__(self, item):
#         return _env.get(item, self.default)
    
#     def __setitem__(self, key, value):
#         _env[key] = value

#     def __delitem__(self, key):
#         if key in _env:
#             del _env[key]
#         else:
#             raise KeyError(f"Key {key} not found in environment variables.")
        
#     def __iter__(self):
#         return iter(_env.items())
    
#     def __len__(self):
#         return len(_env)
    
#     def __call__(self, name: str, default=None):
#         return env(name, default)
    
