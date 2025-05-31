from utils.creator.src.core import Path, File, Task, Date, Builder, Cache
import os
import sys

class Settings:
    path = Path.settings  
    lang = 'en'
    @classmethod
    def setup(cls):
        try:  
            cls.settings = cls.load()
            cls.settings["name"] = "creator"
            cls.settings["version"] = "1.0.0"
            cls.settings["author"] = "Ibrahima Khaliloullah Thiam"
            cls.settings["description"] = "Creator is a versatile Python framework designed to streamline the development process by providing a comprehensive set of tools and libraries. It supports various databases including MySQL, PostgreSQL, and MongoDB, and offers functionalities for encryption, argument parsing, keyboard interactions, markdown processing, YAML parsing, PDF manipulation, and image processing. The framework is built to be compatible with Python 3.12.4 and includes a wide range of packages to facilitate rapid application development." 
            cls.settings["langs"] = ['en']
            cls.settings["python"] = f"{sys.version.split()[0]}"
            cls.settings["packages"] = File.load(Path.requirements, format="json")
            cls.settings["created_at"] = "2024-09-22 00:00:00.000000"
            cls.settings["updated_at"] = f"{Date.now()}"
            cls.save()
        except Exception as e:
            raise Exception(e)
        
    @classmethod 
    def upgrade(cls):
        try: 
            cls.upgrade_requirements()
            cls.settings["python"] = f"{sys.version.split()[0]}"
            cls.settings["packages"] = File.load(Path.requirements, format="json")
            cls.settings["updated_at"] = f"{Date.now()}" 
            cls.make_architecture()
            cls.save()
        except Exception as e:
            raise Exception(e)
         
    @classmethod 
    def update(cls):
        try:     
            cls.update_requirements()
            cls.settings["updated_at"]=f"{Date.now()}"
            cls.cache(source=Path.config, destination=File.set_extension(Path.config,'py'), mode="import")
            cls.cache(source=Path.routes, destination=File.set_extension(Path.routes,'py'), mode="import") 
            cls.make_architecture()
            cls.save()
        except Exception as e:
            raise Exception(e) 
        
    @classmethod
    def get(cls, key, default=None):
        cls.settings = cls.load()
        if key in cls.settings:
            return cls.settings[key]
        else:
            return default
        
    @classmethod
    def set(cls, key, value): 
        cls.settings = cls.load()
        # if key in cls.settings:
        cls.settings[key] = value  
        
    @classmethod
    def load(cls):
        return File.load(cls.path, format="json") 
        
    @classmethod
    def save(cls):
        backup = cls.load()
        try:
            File.save(cls.path, cls.settings, format="json", indent=2)
        except Exception as e:
            File.save(cls.path, backup, format="json", indent=2) 
            raise
        
    @classmethod
    def install_packages(cls): 
        for package, version in cls.settings["packages"].items(): 
            Task.install(package, version=version)
    
    @staticmethod
    def vscode_setting(path = ".vscode/settings.json"):
        try:  
            settings = File.load(path, format="json")
            
            settings["files.associations"] = {
                "*.cre": "python", 
                "creator": "python"
            } 
            File.save(path, settings, format="json", indent=2)   
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def update_requirements(path=Path.requirements):
        requirements = File.load(path, format="json")  
        for package, version in requirements.items(): 
            Task.install(package,  version=version) 

    @staticmethod
    def upgrade_requirements(path=Path.requirements):
        requirements = File.load(path, format="json")  
        for package, version in requirements.items(): 
            Task.install(package) 

    def cache(**kwargs):
        source=kwargs.get('source', None)
        destination=kwargs.get('destination', None)
        mode=kwargs.get('mode', "default")
        Cache.make(source, destination, mode)  
    
    # def backup(source, destination):
    #     pass
    
    @staticmethod
    def make_architecture(path=Path.architecture, **kwargs):
        ignore:list = kwargs.get("ignore", []) 
        all = kwargs.get("all", False) 
        
        if '__pycache__' not in ignore:
            ignore.append('__pycache__')
        if '.vscode' not in ignore:
            ignore.append('.vscode')
        if not all:
            ignore.append('utils') 
            
        File.save(path, File.make_structure(ignore=ignore))

    # def publish_routes(path=Path.routes): 
    #     File.copy_files('utils/creator/src/build/routes/', path) 

    # def publish_views(path=Path.resources): 
    #     File.copy_folders('utils/creator/src/build/resources/', path) 

        
    @staticmethod
    def create_venv(path=Path.venv):
        try:
            if not File.path_exists(path): 
                Task.execute("venv", path)
                print(f"Environnement virtuel creer à {path}")
        except Exception as e:
            raise Exception(e) 
        
    @staticmethod
    def activate_venv(path=Path.venv): 
        if os.name == 'nt':
            activate_script = File.join_path(path, "Scripts", "activate")
        else:
            activate_script= File.join_path(path, "bin", "activate")
            
        if File.path_exists(activate_script):
            activate_script = File.absolute_path(activate_script)
            if os.name == 'nt':
                os.system(f'cmd /k "{activate_script}"')
            else:
                os.system(f'bash -c "{activate_script}"')
            print(f"Environnement virtuel activé à {path}")
        else: 
            Settings.create_venv()
            Settings.activate_venv() 

    @staticmethod
    def deactivate_venv():
        if os.name == 'nt':
            deactivate_script = "deactivate"
        else:
            deactivate_script = "deactivate"
        
        os.system(deactivate_script)
        print("Environnement virtuel désactivé")

        
  