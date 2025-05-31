from utils.creator.src.core.file import File 

class Lang:
    def __init__(self, lang):
        self.lang = lang
        self.path = f"lang/{self.lang}/"
        self.translations = self.load()
        self.languages = self.translations["languages"]

    def check(self, lang):
        if lang in self.languages:
            return True 
        return False
        
    def load(self, **kwargs):  
        retry = kwargs.get("retry", True)
        try:
            self.files = File.list_dir(self.path)
            content = {}
            for file in self.files:
                content.update(File.load(f"{self.path}{file}", format="json")) 
            return content
        except Exception as e:
            
            if retry: 
                self.path = f"lang/en/" 
                return self.load(retry=False)
            else:
                raise FileNotFoundError from e 
        
    def save(self, content):
        backup = self.load()
        try:
            File.save(self.path, content, format="json", indent=2)
        except Exception as e:
            File.save(self.path, backup, format="json", indent=2) 
            raise e

    def get_placeholders(self, text: str):
        import re 
        return re.findall(r'\{(.*?)\}', text)
    
    def resolve(self, arg:str, **kwargs):  
        placeholders = self.get_placeholders(arg)
        for placeholder in placeholders:
            if placeholder in kwargs:
                arg = arg.replace(f"{{{placeholder}}}", str(kwargs[placeholder]))
        return arg  
    
    def collect(self, *keys, **kwargs):
        default = kwargs.get("default", "")
        text = self.translations.copy()
        for key in keys:
            if key in text:
                text = text[key]
            else:
                return default
        return self.resolve(text, **kwargs)
    
    def get(self, key:str, **kwargs):
        key = key.split(".")
        
        result = self.collect(*key, **kwargs)
        return result
    
    def set(self, **kwargs):
        for key, value in kwargs.items():
            self.translations[key] = value
        self.save(self.translations)
    
    def translate(self, text:str, target=None, source="auto"):      
        from utils.creator.src.core import Translator
        if target:
            self.target = target
        else:
            self.target = self.lang
        self.source = source 
        translate:str = Translator.translate(text, self.target, source=self.source) 
        params = self.get_placeholders(text)
        if params:
            placeholders = self.get_placeholders(translate)
            for placeholder in placeholders:
                translate = translate.replace(f"{{{placeholder}}}", f"{{{params[placeholders.index(placeholder)]}}}")
        return translate
    
    def generate(self, lang): 
        targetination = self.path.replace(self.lang, lang) 
        for file in self.files:
            src_path = f"{self.path}{file}" 
            target_path = f"{targetination}{file}" 
            content = File.load(src_path, format="json")
            
            def translate_content(content, lang):
                for text in content: 
                    if isinstance(content[text], dict):
                        content[text] = translate_content(content[text], lang)
                    elif isinstance(content[text], str):
                        content[text] = self.translate(content[text], target=lang) 
                return content
            
            content = translate_content(content, lang)
            File.save(target_path, content, format="json", indent=2) 
    
    def __setitem__(self, key, value):
        self.translations[key] = value
    
    def __getitem__(self, key):
        return self.translations[key]
    
    def __str__(self):
        return f"{self.lang}"
    
    def __repr__(self):
        return f"Lang({self.lang})"
    
    def __del__(self):
        del self.lang
        del self.path
        del self.translations
        
        
