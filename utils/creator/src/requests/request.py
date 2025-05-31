from utils.creator.src.requests.requests import Requests
from utils.creator.src.requests.sessions import Session
from utils.creator.src.validators import Validator  

class Request:
    data = {}  

    def __init__(self, qwery=None, **kwargs):
        self.session :Session = kwargs.get("session", None)
        self.validator :Validator = kwargs.get("validator", None) 
        self.method = kwargs.get("method", None)
        self.url = kwargs.get("url", None)
        self.headers = kwargs.get("headers", {})
        self.files = kwargs.get("files", None)
        self.params = kwargs.get("params", None)
        self.auth = kwargs.get("auth", None)
        self.cookies = kwargs.get("cookies", None)
        self.hooks = kwargs.get("hooks", None)
        self.json = kwargs.get("json", None)
        
        
        if qwery:
            self.qwery = qwery 
            self.data.update(**self.qwery) 
            
    def __getattr__(self, name):
        return self.data.get(name)

    def __getitem__(self, key):
        return self.data[key]

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        
    def new(self, request):  
        self.request = request 
        self.data.update(**self.request) 
        return self
    
    def all(self):
        return self.data
    
    
    @classmethod
    def capture(cls):
        requests = Requests()
        _SERVER = requests.get_server() 
        
        if _SERVER:
            return _SERVER
            # return  {
            #     "method": _SERVER["REQUEST_METHOD"],
            #     "url": _SERVER["PATH_INFO"],
            #     "headers": _SERVER,
            #     "data": _SERVER,
            #     "files": _SERVER,
            #     "params": _SERVER,
            #     "auth": _SERVER,
            #     "cookies": _SERVER,
            #     "json": _SERVER, 
            # }
        
        # return SERVER
    
    def ip(self):
        return

    def validate(self, validation: dict) -> bool:
        if self.validator.validate(validation, self.request):
            return True
        self.session.error(*self.validator.errors)   
        return False 
        