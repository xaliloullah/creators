import re
from urllib.parse import urlparse, parse_qs

class Router:
    
    routes = {} 
    
    def __init__(self): 
        self.absolute = "http://localhost:8000"

    def create(self, method, uri, action, name=None): 
        self._route_ = {
            'method': method,
            'uri': uri,
            'action': action,
            'name': name
        } 
        return self
    
         
    def add(self):
        if hasattr(self, '_route_'):
            route = self._route_
            method = route["method"]
            if method not in self.routes:
                self.routes[method] = []
                
            self.routes[route["method"]].append({'uri': route['uri'], 'action': route['action'], 'name': route['name']})
            
            del self._route_   
        return self 
        
    def get(self, uri, action, name=None): 
        self.create("GET", uri, action, name).add()

    def post(self, uri, action, name=None):
        self.create("POST", uri, action, name).add()

    def put(self, uri, action, name=None):
        self.create("PUT", uri, action, name).add()

    def delete(self, uri, action, name=None):
        self.create("DELETE", uri, action, name).add()

    def patch(self, uri, action, name=None):
        self.create("PATCH", uri, action,name).add()

    def any(self, uri, action, name=None):
        self.create("ANY", uri, action, name).add()

    def group(self, attributes, action: callable):
        prefix = attributes.get('prefix', '')
        for route in self.routes.get('ANY', []):
            route['uri'] = prefix + route['uri']
        action(self)
        
    def controller(self, controller, action: callable):
        action(controller)
        
    def prefix(self, prefix):
        self._prefix_ = prefix
        return self
    
    def name(self, name):
        self._name_ = name
        return self
    
    def middleware(self, middleware):
        self._middleware_ = middleware
        return self
    
    def domain(self, domain):
        self._domain_ = domain
        return self
    
    def namespace(self, namespace):
        self._namespace_ = namespace
        return self
     
        
    def list(self):
        return self.routes

    def show(self): 
        return self.routes
     
    def route_name(self, name, method):
        try:
            if method in self.routes: 
                for route in self.routes[method]:
                    if route['name'] == name:
                        return route
        except Exception as e: 
            raise Exception(e) 
        
    def route_uri(self, url, method):
        try:
            if method in self.routes: 
                for route in self.routes[method]:
                    if self.resolve(url, f"{self.absolute}{route['uri']}") == url:
                        return route
        except Exception as e: 
            raise Exception(e)
        
    def dispatch(self, method: str, uri: str, **kwargs): 
        return self.resolve(method.upper(), uri, **kwargs) 
   
    def resolve(self, method, uri: str, **kwargs):
        try:  
            url = urlparse(uri)
            if method in self.routes: 
                for route in self.routes[method]: 
                    pattern = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', f"{route['uri']}")
                    pattern = f'^{pattern}$'
                     
                    match = re.match(pattern, url.path)
                    if match:   
                        params = match.groupdict() 
                        return {
                            'method': method,
                            'params': params,
                            'query': {key: value[0] for key, value in parse_qs(url.query).items()},   
                            'data': kwargs.get("data", {}),
                            'action': route['action'],
                            'scheme': url.scheme,
                            'netloc': url.netloc,
                            'path': url.path,
                            'fragment': url.fragment,
                            'port': url.port,
                            'hostname': url.hostname, 
                        } 
            return None
        except Exception as e: 
            raise Exception(e) 

    def route(self, method: str, arg, **params):  
        try: 
            absolute = params.get("absolute", False)
            route = self.route_name(arg, method.upper())
            if route:
                uri: str = route['uri']
                if params:
                    for param, value in params.items():
                        try:
                            uri = uri.replace(f"{{{param}}}", str(value))
                        except Exception as e:
                            raise Exception(e)  
                if absolute:
                    uri = f"{self.absolute}{uri}" 
                return uri
            else:
                raise Exception(f"Route '{arg}' not found.")
        except Exception as e:
            raise Exception(e) 
    
    def url(self, url):
        pass