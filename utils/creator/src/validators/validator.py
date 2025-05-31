from utils.creator.src.app import Creator

class Validator:
    def __init__(self) -> None:  
        self.lang = Creator.lang
        self.errors = []
        
    def validate(self, validate: dict, data: dict): 
        for field, rules in validate.items():
            value = data.get(field)
            for rule in rules:
                rule = str(rule)
                if rule == "required":
                    if value is None or value == "": 
                        self.errors.append(self.lang.get("validation.required", attribute=field))
                
                if rule == "nullable":
                    if value is None:
                        continue
                    
                if rule == "numeric":
                    if value and not isinstance(value, (int, float)):
                        self.errors.append(self.lang.get("validation.numeric", attribute=field)) 
                
                if rule == "boolean":
                    if value and not isinstance(value, bool):
                        self.errors.append(self.lang.get("validation.boolean", attribute=field))
                        
                if rule == "string":
                    if value and not isinstance(value, str):
                        self.errors.append(self.lang.get("validation.string", attribute=field))
               
                if rule == "email":
                    if value and (not isinstance(value, str) or "@" not in value or "." not in value):
                        self.errors.append(self.lang.get("validation.email", attribute=field))
                                                           
                if rule == "password": 
                    from utils.creator.src.validators import Password
                    password = Password(value, field).default()
                    if password.errors:
                        for error in password.errors:
                            self.errors.append(error) 
                        
                if rule.startswith("min"):
                    if value:
                        min = int(rule.split(":")[1])
                        if len(str(value)) < min:
                            
                            self.errors.append(self.lang.get("validation.min", attribute=field, min=min))  
                 
                if rule.startswith("max"):
                    if value:
                        max = int(rule.split(":")[1])
                        if len(str(value)) > max:
                            self.errors.append(self.lang.get("validation.max", attribute=field, max=max)) 

                if rule == "integer":
                    if value:
                        try:
                            int(value)
                        except ValueError:
                            self.errors.append(self.lang.get("validation.integer", attribute=field))  
                 
                if rule == "decimal":
                    if value:
                        try:
                            float(value)
                        except ValueError:
                            self.errors.append(f"The '{field}' field must be a valid real.")
                            # break
                if rule == "array":
                    if value:
                        if not isinstance(value, list):
                            self.errors.append(f"The '{field}' field must be a valid array.")
                            
                if rule == "object":
                    if value:
                        if not isinstance(value, object):
                            self.errors.append(f"The '{field}' field must be a valid object.")
                            
                if rule == "phone":
                    if value and (not isinstance(value, str) or len(value) < 10):
                        self.errors.append(self.lang.get("validation.phone", attribute=field)) 
                        
                if rule == "date":
                    if value:
                        try:
                            # Date(value)
                            pass
                        except ValueError:
                            self.errors.append(f"The '{field}' field must be a valid date.") 
                            
                if rule == "file":
                    if value:
                        if not isinstance(value, dict):
                            self.errors.append(f"The '{field}' field must be a valid file.")
                            
                if rule == "image":
                    if value:
                        if not isinstance(value, dict):
                            self.errors.append(f"The '{field}' field must be a valid image.")
                            
                if rule == "video":
                    if value:
                        if not isinstance(value, dict):
                            self.errors.append(f"The '{field}' field must be a valid video.")
                if rule == "audio":
                    if value:
                        if not isinstance(value, dict):
                            self.errors.append(f"The '{field}' field must be a valid audio.")
                            
                if rule == "document":
                    if value:
                        if not isinstance(value, dict):
                            self.errors.append(f"The '{field}' field must be a valid document.")

                if rule == "url":
                    if value:
                        if not isinstance(value, str) or not value.startswith("http"):
                            self.errors.append(f"The '{field}' field must be a valid URL.")
                            
                if rule == "ip":
                    if value:
                        if not isinstance(value, str) or not value.count(".") == 3:
                            self.errors.append(f"The '{field}' field must be a valid IP address.")
                            
                if rule == "ipv4":
                    if value:
                        if not isinstance(value, str) or not value.count(".") == 3:
                            self.errors.append(f"The '{field}' field must be a valid IPv4 address.")
                            
                if rule == "ipv6":
                    if value:
                        if not isinstance(value, str) or not value.count(":") == 7:
                            self.errors.append(f"The '{field}' field must be a valid IPv6 address.")
                            
                            
                if rule == "mac":
                    if value:
                        if not isinstance(value, str) or not value.count(":") == 5:
                            self.errors.append(f"The '{field}' field must be a valid MAC address.")
                            
                            
                if rule == "uuid":
                    if value:
                        try:
                            # uuid.UUID(value)
                            pass
                        except ValueError:
                            self.errors.append(f"The '{field}' field must be a valid UUID.")
                            
                if rule == "json":
                    if value:
                        try:
                            # json.loads(value)
                            pass
                        except ValueError:
                            self.errors.append(f"The '{field}' field must be a valid JSON.")
                             
                if rule == "alpha":
                    if value and not value.isalpha():
                        self.errors.append(f"The '{field}' field must be alphabetic characters.")
                
                if rule == "alphanumeric":
                    if value and not value.isalnum():
                        self.errors.append(f"The '{field}' field must be alphanumeric characters.")
                
                if rule == "alpha_dash":
                    if value and not value.replace("-", "").replace("_", "").isalnum():
                        self.errors.append(f"The '{field}' field must be alphanumeric characters with dashes and underscores.")
                        
                if rule == "alpha_space":
                    if value and not value.replace(" ", "").isalpha():
                        self.errors.append(f"The '{field}' field must be alphabetic characters with spaces.")
                        
                if rule == "alpha_num":
                    if value and not value.isalnum():
                        self.errors.append(f"The '{field}' field must be alphanumeric characters.")
                        
                if rule == "alpha_num_dash":
                    if value and not value.replace("-", "").replace("_", "").isalnum():
                        self.errors.append(f"The '{field}' field must be alphanumeric characters with dashes and underscores.")
                        
                        
                if rule == "alpha_num_space":
                    if value and not value.replace(" ", "").isalnum():
                        self.errors.append(f"The '{field}' field must be alphanumeric characters with spaces.")
                       
                if rule.startswith("unique"):
                    from utils.creator.src.models.model import Model
                    if value:
                        params = rule.split(":")[1].split(",")
                        table = str(params[0])
                        ignore = params[1] if len(params) > 1 else None 
                        if table:
                           row = Model(table).where(**{field: value}).first()
                           if row:
                            self.errors.append(self.lang.get("validation.unique", attribute=field)) 
                                
                # if rule.startswith("exists"):
                #     from utils.creator.src.models.model import Model
                #     if value:
                #         params = rule.split(":")[1].split(",")
                #         table = params[0]
                #         if table:
                #             rows = Model(table).where(**{field: value})
                #             if not rows.exists():
                #                 self.errors.append(f"The value of the '{field}' field does not exist.")
    

        return not self.has_errors()

    def has_errors(self):
        return bool(self.errors)
            
