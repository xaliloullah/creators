import sys
import subprocess
from utils.creator.src.core import File

class Task:
    
    @staticmethod
    def replace(data:str, old, new="", count=-1): 
        if not isinstance(old, str): 
            for item in old:
                data = data.replace(item, new, count)
        else:
            data = data.replace(old, new, count)
        return data 

    @staticmethod
    def explode(separator, data:str): 
        return data.split(separator)

    @staticmethod
    def implode(separator:str, data:list): 
        return separator.join(data)
    
    @staticmethod    
    def install(package, **kwargs): 
        try:
            version = kwargs.get('version', "")  
            extra_args = kwargs.get('extra_args', []) 
            user = kwargs.get('user', False) 
            quiet = kwargs.get('quiet', False)  
            force_reinstall = kwargs.get('force_reinstall', False)  
            
            command = [sys.executable, '-m', 'pip', 'install']
            
            if version:
                command.append(f"{package}=={version}")
            else:
                command.append(package)
            
            if quiet:
                command.append('--quiet')
            
            if user:
                command.append('--user')
            
            if force_reinstall:
                command.append('--force-reinstall')
            
            if extra_args:
                command.extend(extra_args)
                
            subprocess.check_call(command) 
            
            if not version:
                result = subprocess.run([sys.executable, "-m", "pip", "show", package], capture_output=True, text=True)
                version_line = next(line for line in result.stdout.splitlines() if line.startswith("Version:"))
                version = version_line.split(":")[1].strip()
            
            source = 'requirements.json'   
            requirements = File.load(source, format="json")
            
            # requirements[package] = {
            #     "package": package, 
            #     "version": version
            # }
            requirements[package] = version
            
            File.save(source,requirements, format="json", indent=2) 
        except Exception as e:
            raise Exception(e)   
            
    @staticmethod
    def uninstall(package):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', package, '-y'])
            source = 'requirements.json'   
            
            requirements = File.load(source, format="json")
            del requirements[package]  
            File.save(source,requirements, format="json", indent=2) 
        except Exception as e:
            raise Exception(e) 
            
    @staticmethod        
    def execute(*command, **kwargs):
        script = kwargs.get("script", False)
        try:
            if script:
                subprocess.run(list(command), shell=True, check=True)
            else: 
                subprocess.run([sys.executable, '-m'] + list(command), shell=True, check=True)
        except Exception as e:
            raise Exception(e) 
    
    @staticmethod
    def run(source:str, namespace=None):
        try: 
            with open(source, 'r') as file:
                code = compile(file.read(), source, 'exec') 
                if namespace: 
                    exec(code, namespace)  
                else:
                    exec(code)  
        except Exception as e:
            raise Exception(e)  
     
    @staticmethod   
    def build_import(source:str, *modules) -> str:
        try: 
            source = Task.replace(source,['/','\\'], '.') 
            if modules:
                return f"from {source} import {', '.join(File.strip_extension(m) for m in modules)}"
            
            if '.' in source:
                path, module = source.rsplit('.', 1)
                return f"from {path} import {module}"
            
            return f"import {source}"
            
        except Exception as e:
            raise Exception(e)








