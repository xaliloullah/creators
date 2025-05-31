class Rules: 
    
    # REQUIRED = "required"
    # STRING = "string"
    # MIN = "min"
    # MAX = "max"
    # MINLENGTH = "minlength"
    # MAXLENGTH = "maxlength"
    # INTEGER = "integer"
    # PASSWORD = "password"
    # EMAIL = "email"
    # REGEX = "regex"
    # URL = "url"
    # DATE = "date"
    # BOOLEAN = "boolean"
    # ARRAY = "array"
    # OBJECT = "object"
    # BETWEEN = "between"
    # ALPHA = "alpha"
    # ALPHA_NUM = "alpha_num"
    # ALPHA_DASH = "alpha_dash"
    # IP_ADDRESS = "ip"
    # UUID = "uuid"

    def __init__(self):
        self.rules = []
        
    def required(self):
        self.rules.append("required") 
        return self
    
    def string(self):
        self.rules.append("string") 
        return self

    def min(self, value):
        self.rules.append(f"min:{value}")
        return self
    
    def max(self, value):
        self.rules.append(f"max:{value}")
        return self
    
    def minlength(self, value):
        self.rules.append(f"minlength:{value}")
        return self
    
    def maxlength(self, value):
        self.rules.append(f"maxlength:{value}")
        return self
    
    def integer(self):
        self.rules.append("integer")
        return self
    
    def password(self):
        self.rules.append("password")
        return self
    
    def unique(self, table):
        self.rules.append(f"unique:{table}")
        return self

    def email(self):
        self.rules.append("email")
        return self

    def regex(self, pattern):
        self.rules.append(f"regex:{pattern}")
        return self
    
    def url(self):
        self.rules.append("url")
        return self

    def date(self):
        self.rules.append("date")
        return self
    
    def boolean(self):
        self.rules.append("boolean")
        return self
    
    def array(self):
        self.rules.append("array")
        return self
    
    def object(self):
        self.rules.append("object")
        return self

    def between(self, min, max):
        self.rules.append(f"between:{min},{max}")
        return self
    
    def alpha(self):
        self.rules.append("alpha")
        return self
    
    def number(self):
        self.rules.append("number")
        return self
    
    def alpha_num(self):
        self.rules.append("alpha_num")
        return self

    def alpha_dash(self):
        self.rules.append("alpha_dash")
        return self

    def ip_address(self):
        self.rules.append("ip")
        return self

    def uuid(self):
        self.rules.append("uuid")
        return self 
    
    def get(self):  
        return self.rules
    
    def __str__(self):
        return str(self.rules)
    
    def __iter__(self):
        return iter(self.rules)
    
    def __repr__(self):
        return f"Rules({self.rules})"