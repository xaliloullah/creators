from utils.creator.src.core import File

class Storage:

    def __init__(self, path: str=None, **kwargs): 
        self.path = path  
        self.format = kwargs.get("format", None)
        self.default = kwargs.get("default", None)
        self.absolute = kwargs.get("absolute", True)

        if self.absolute:
            self.path = File.storage_path(self.path)

        if self.format:
            if self.format == 'auto':
                self.format = File.get_extension(self.path, without_dot=True)
                # self.path = File.set_extension(self.path, self.format)

        self.data = self.load() or self.default
 
    def load(self, **kwargs):
        try:    
            return File.load(self.path, format=self.format, **kwargs)
        except Exception as e:
            raise Exception(e)
    
    def save(self, data=None, **kwargs):  
        backup = self.load()
        format = kwargs.get("format", self.format)
        default = kwargs.get("default", self.default)
        try:     
            File.save(self.path, data or self.data, format=format, **kwargs)   
        except Exception as e:
            File.save(self.path, backup, format=self.format)   
            raise Exception(e) 
    
    def all(self):
        return self.data 
    
    def create(self, data):
        try:
            if isinstance(self.data, list):
                self.data.append(data)
            elif isinstance(self.data, dict):
                self.data.update(data)  
            elif isinstance(self.data, str):
                self.data += f"\n{data}"
            elif isinstance(self.data, set):
                self.data.add(data)
            else:
                self.data = data
            self.save()
        except: 
            raise TypeError("Invalid !")
        
    def update(self, key, value=None):
        try:
            if isinstance(self.data, list):
                index = self.data.index(key)
                self.data[index] = value
            elif isinstance(self.data, dict):
                self.data.update(key)
            elif isinstance(self.data, str):
                self.data = self.data.replace(key, value, 1)
                print(self.data)
            elif isinstance(self.data, set):
                self.data.update(key)
            else:
                self.data = key
            self.save()
        except: 
            raise TypeError("Invalid !")
        
    def delete(self, data):
        try:
            if isinstance(self.data, list):
                self.data.remove(data)
            elif isinstance(self.data, dict):
                self.data.pop(data, None) 
            elif isinstance(self.data, str):
                self.data = self.data.replace(str(data), "", 1)
            elif isinstance(self.data, set):
                self.data.discard(data)
            else:
                raise TypeError("Invalid !")
            self.save()
        except ValueError:
            raise ValueError("Not found !")
        
    def reset(self): 
        if isinstance(self.data, list):
            self.data = []
        elif isinstance(self.data, dict):
            self.data = {}
        elif isinstance(self.data, str):
            self.data = ""
        elif isinstance(self.data, set):
            self.data = set()
        else:
            raise TypeError("Invalid !")
        return self.data
    
    def remove(self):
        try:
            File.remove(self.path)
        except Exception as e:
            raise Exception(e)

    def exists(self):
        return File.path_exists(self.path)
        
    
    def __str__(self):
        return str(self.data)
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.path}, format={self.format}), data={self.data}"