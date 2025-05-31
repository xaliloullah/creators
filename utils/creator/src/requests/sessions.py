import uuid
from config import session 
from utils.creator.src.core import File, Date, Collection

class Session:  
    
    def __init__(self, **kwargs) -> None:
        self.id = str(uuid.uuid4().hex) 
        
        if session.driver == 'file':  
            self.path = File.storage_path(f"{session.path}")
            self.format = kwargs.get("format", "json") 
            self.path = File.set_extension(self.path, self.format)
            
        self.autoload()
            
    
    def autoload(self, **kwargs):
        self.data = self.load()
        if self.data: 
            if self.is_active():
                self.update() 
        else:
            self.create()
            self.autoload()
            
    
    def load(self, **kwargs):
        try:    
            if session.driver == 'file': 
                return Collection(File.load(self.path, format=self.format, **kwargs))
        except Exception as e:
            raise Exception(e)
          
    def save(self, **kwargs):  
        if session.driver == 'file':
            backup = self.load()
            try:    
                File.save(self.path, self.data.get(), format=self.format, **kwargs)   
            except Exception as e:
                File.save(self.path, backup, format=self.format)   
                raise Exception(e)
           
            
    def create(self):    
        self.set(f"id", self.id)
        self.set(f"user_id", None) 
        self.set(f"expires_at", f"{Date.add_minutes(Date.now(), int(session.lifetime))}") 
        self.set(f"last_activity", f"{Date.now()}") 
        self.save() 
        
    def update(self):  
        self.set(f"last_activity", f"{Date.now()}") 
        self.save()
        
    def get(self, key:str, default=None):
        # key = f"{self.id}.{key}"
        return self.data.get(key, default)  
    
    def set(self, key:str, value):
        # key = f"{self.id}.{key}"
        
        self.data.set(key, value)  

    def is_active(self):
        if Date.now() < Date.strtotime(self.get(f"expires_at")):
            return True
        else:
            return False
             
    def all(self):
        return self.data
    
    def flash(self, status, message):  
        messages = self.get(f"flash.{status}", default=[])  
        if isinstance(message, (tuple, list)):
            messages.extend(message)
        else:
            messages.append(message)
        
        self.set(f"flash.{status}", messages) 
        self.update()

    def get_flash(self, status=None):
        if status:
            flash = self.get(f"flash.{status}", [])
            self.set(f"flash.{status}", [])
        else: 
            flash = self.get("flash", {})
            self.set("flash", {})
        self.update()
        return flash
     
    def error(self, *message):
        self.flash("error", message) 
          
     
    def success(self, *message):
        self.flash("success", message)
         
        
    def has(self, key: str):
        return bool(self.get(key)) 
    
    def has_errors(self):
        return self.has("flash.error")
    
    def has_success(self):
        return self.has("flash.success")
    
    def get_errors(self):
        return self.get_flash("error")
    
    def get_success(self):
        return self.get_flash("success") 