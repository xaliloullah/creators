from utils.creator.src.app import Creator

class Password:
    def __init__(self, password: str, field="password") -> None:
        self.password = password
        self.field = field
        self.errors = []
        
    def required(self):
        if not self.password:
            self.errors.append(Creator.lang.get("validation.required", attribute=self.field))
        return self
    
    def min(self, min): 
        if len(self.password) < min:
            self.errors.append(Creator.lang.get("validation.password.min", attribute=self.field, min=min))
        return self 
    
    
    def max(self, max):
        if len(self.password) > max:
            self.errors.append(Creator.lang.get("validation.password.max", attribute=self.field, max=max))
        return self
    
    def uppercase(self):
        if not any(char.isupper() for char in self.password):
            self.errors.append(Creator.lang.get("validation.password.uppercase", attribute=self.field))
        return self

    def lowercase(self):
        if not any(char.islower() for char in self.password):
            self.errors.append(Creator.lang.get("validation.password.lowercase", attribute=self.field))
        return self

    def number(self):
        if not any(char.isdigit() for char in self.password):
            self.errors.append(Creator.lang.get("validation.password.number", attribute=self.field))
        return self

    def special(self):
        if not any(char in "@$!%*?&#" for char in self.password):
            self.errors.append(Creator.lang.get("validation.password.special", attribute=self.field))
        return self
    
    def validate(self):
        return not self.errors
    
    def default(self):
        self.required().min(6).uppercase().lowercase().number().special()
        return self
     