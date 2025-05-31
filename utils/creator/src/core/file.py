try: 
    import os 
    import json
    import configparser
    import csv
    import zipfile
    import tarfile
    import xml.etree.ElementTree as ET 
except ImportError:
    pass

try:
    import yaml
except ImportError:
    yaml = None

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

from utils.creator.src.core import Path

class File: 
    
    def __init__(self):
        pass
    
    @staticmethod
    def ensure_path_exists(path):
        try:
            """Check if the specified path exists; if not, create it."""
            directory, file = os.path.split(path)
            if directory and not File.path_exists(directory): 
                try:
                    os.makedirs(directory)
                except PermissionError:
                    return
            try:
                with open(path, 'a') as f:
                    pass
            except PermissionError:
                return 
        except Exception as e:
            raise Exception(e)
       
    @staticmethod 
    def load(path, **kwargs):
        try:
            File.ensure_path_exists(path)
            mode = kwargs.get("mode", "r")
            format = kwargs.get('format', "txt") 
            ignore = kwargs.get('ignore', []) 
            
            with open(path, mode) as file:
                content = file.read() 
                
                if format == 'json':
                    
                    if not content:
                        return {}
                    return json.loads(content)
                
                elif format == 'xml':
                    return ET.fromstring(content)
                
                elif format == 'yaml': 
                    return yaml.safe_load(content)
                
                elif format == 'ini':
                    config = configparser.ConfigParser()
                    config.read_string(content)
                    return config
                
                elif format == 'csv':  
                    file.seek(0)
                    reader = csv.DictReader(file)
                    return [row for row in reader] 
                
                elif format == 'zip': 
                    with zipfile.ZipFile(path, mode) as zip_ref:
                        zip_ref.extractall('_temp')
                        return zip_ref.namelist()
                    
                elif format == 'tar' or format == 'tar.gz' or format == 'tgz': 
                    with tarfile.open(path, 'r:gz') as tar:
                        tar.extractall('_temp')
                        return tar.getnames()
                    
                elif format == 'jpg' or format == 'jpeg' or format == 'png' or format == 'gif':
                    image = Image.open(path)
                    image.show()
                    
                elif format == 'pdf':
                    with open(path, 'rb') as file:
                        reader = PyPDF2.PdfReader(file)
                        text = ""
                        for page in reader.pages:
                            text += page.extract_text()
                        return text 
                    
                elif format == 'env': 
                    env = {}
                    with open(path, mode) as file:
                        for line in file:
                            if line and not line.startswith((';', '#')):
                                if '=' in line:
                                    key, value = line.strip().split('=', 1)
                                    env[key] = value  
                        return env
                    
                else:
                    return str(content)
                
                
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def save(path, content, **kwargs): 
        File.ensure_path_exists(path)
        mode = kwargs.get("mode","w")
        try:
            format = kwargs.get('format', "txt")
            encoding = kwargs.get("encoding", "utf-8")
            
            if format == 'json': 
                indent = kwargs.get('indent', None) 
                with open(path, mode) as file:
                    json.dump(content, file, indent=indent)
                    
            elif format == 'xml': 
                root = ET.Element("root")
                # You can customize this according to your XML structure
                for key, value in content.items():
                    child = ET.SubElement(root, key)
                    child.text = str(value)
                tree = ET.ElementTree(root)
                tree.write(path)
                
            elif format == 'ini': 
                config = configparser.ConfigParser()
                for section, values in content.items():
                    config[section] = values
                with open(path, mode, encoding=encoding) as file:
                    config.write(file)
                    
            elif format == 'csv': 
                with open(path, mode, encoding=encoding, newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=content[0].keys())
                    writer.writeheader()
                    writer.writerows(content)
                    
            elif format == 'zip': 
                endswith = kwargs.get("endswith", None)
                ignore = kwargs.get("ignore", []) 
                only = kwargs.get("only", [])
                with zipfile.ZipFile(content, 'w', zipfile.ZIP_DEFLATED) as zipf: 
                    for root, dirs, files in File.walk_path(path, ignore=ignore, endswith=endswith, only=only):
                        for file in files:
                            file_path = File.join_path(root, file) 
                            zipf.write(file_path, os.path.relpath(file_path, path))
                        
            elif format == 'tar' or format == 'tar.gz' or format == 'tgz': 
                with tarfile.open(path, 'w:gz') as tar:
                    for file_name in content:
                        tar.add(file_name)
                        
            elif format == 'jpg' or format == 'jpeg' or format == 'png' or format == 'gif': 
                image = Image.fromarray(content)
                image.save(path)
                
            elif format == 'yaml': 
                with open(path, mode) as file:
                    yaml.dump(content, file, default_flow_style=False)

            elif format == 'pdf': 
                with open(path, 'wb', encoding=encoding) as file:
                    writer = PyPDF2.PdfWriter()
                    # You can add pages to the PDF
                    # writer.add_page(some_page)
                    file.write(writer)
            
            elif format == 'env': 
                groups = {}
                for key in sorted(content):
                    prefix = key.split('_')[0]
                    if prefix not in groups:
                        groups[prefix] = []
                    groups[prefix].append(f"{key}={str(content[key])}")
                env = "\n\n".join("\n".join(groups[prefix]) for prefix in groups)

                with open(path, mode, encoding=encoding) as file:
                    file.write(f"{env}\n")
                    
            else:
                with open(path, mode, encoding=encoding) as file:
                    file.write(f"{content}")  
                        
        except Exception as e:
            raise Exception(e)
   
    @staticmethod     
    def walk_path(path, **kwargs): 
        endswith = kwargs.get("endswith", None)
        ignore = kwargs.get("ignore", []) 
        only = kwargs.get("only", []) 
        topdown = kwargs.get("topdown", True)  
        for root, dirs, files in os.walk(path, topdown=topdown):  
            if only:
                dirs[:] = [dir for dir in dirs if dir in only] 
                files = [file for file in files if file in only]
                only = False
            dirs[:] = [dir for dir in dirs if dir not in ignore] 
            files = [file for file in files if file not in ignore]
            if endswith:
                files = [file for file in files if file.endswith(endswith)]

            yield root, dirs, files

    @staticmethod
    def copy_files(source, destination, **kwargs):
        import shutil
        try:
            only = kwargs.get("only", [])
            ignore = kwargs.get("ignore", []) 
            def ignore_files(src, names):  
                return [dossier for dossier in names if dossier in ignore]  
            shutil.copytree(source, destination, ignore=ignore_files, dirs_exist_ok=True)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def copy_folders(source, destination, **kwargs):
        import shutil
        try:
            
            ignore = kwargs.get("ignore", []) 
            only = kwargs.get("only", [])
            format = kwargs.get("format", None) 
            def ignore_folders(src, names):  
                return [dossier for dossier in names if dossier in ignore]  
            shutil.copytree(source, destination, ignore=ignore_folders, dirs_exist_ok=True)
        except Exception as e:
            raise Exception(e)
    
    @staticmethod    
    def get_real_path(path: str) -> str:
        try:
            absolute_path = File.absolute_path(path)
            directory_reference = os.getcwd()
            relative_path = os.path.relpath(absolute_path, directory_reference)
            return relative_path
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def absolute_path(path):
        return os.path.abspath(path)
    
    @staticmethod
    def remove(path):
        try:
            return os.remove(path)
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def clean(directory = '.', cleans= '__pycache__'): 
        for root, dirs, files in File.walk_path(directory, topdown=False):
            for name in dirs:
                if name == cleans:
                    path = File.join_path(root, name)
                    print(f"Suppression de : {path}")
                    File.rmdir(path)
        
    @staticmethod
    def rmdir(path):
        import shutil
        try:
            return shutil.rmtree(path)
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def is_dir(path):
        try:
            return os.path.isdir(path)
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def list_dir(path, **kwargs):
        try:
            endswith = kwargs.get("endswith", None)
            ignore = kwargs.get("ignore", []) 
            files = os.listdir(path) 
            if endswith:
                files = [file for file in files if file.endswith(endswith)]
            
            files = [file for file in files if file not in ignore]
            return files
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def get_path(path: str=""):
        try:
            return os.getcwd()+path
        except Exception as e:
            raise Exception(e) 
        
    @staticmethod
    def path_exists(path): 
        try:
            return os.path.exists(path)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def join_path(*args):
        try:
            return os.path.join(*args)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def resources_path(path: str=""): 
        return File.join_path(Path.views, path) 

    @staticmethod
    def public_path(path: str=""):
        return File.join_path(Path.public, path)

    @staticmethod
    def asset_path(path: str=""):
        return File.join_path(Path.assets, path)

    @staticmethod
    def storage_path(path: str=""):
        return File.join_path(Path.storage, path)

    @staticmethod
    def change_directory(path: str):
        try:
            return os.chdir(os.path.dirname(path))
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def make_structure(path= '.', level=0, prefix="", **kwargs):
        try:
            ignore = kwargs.get("ignore", []) 
            elements = File.list_dir(path, ignore = ignore)
            # elements.sort()
            structure = ""
            
            for index, element in enumerate(elements): 
                folder = File.join_path(path, element)
                if index == len(elements) - 1:
                    new_prefix = prefix + "    "
                    structure += f"{prefix}└── {element}\n"
                else:
                    new_prefix = prefix + "│   "
                    structure += f"{prefix}├── {element}\n"
                if File.is_dir(folder):
                    structure += File.make_structure(folder, level + 1, new_prefix, ignore=ignore)
            return structure
        except Exception as e:
            raise Exception(e) 

    @staticmethod
    def strip_extension(path):
        return os.path.splitext(path)[0]
        
    @staticmethod
    def get_extension(path, **kwargs):
        without_dot = kwargs.get("without_dot", False)
        if without_dot:
            return os.path.splitext(path)[1][1:] 
        return os.path.splitext(path)[1]
    
    @staticmethod
    def set_extension(path, extension):
        return File.strip_extension(path) + "." + extension
    
    @staticmethod
    def get_name(path):
        return os.path.basename(path)
    
    @staticmethod
    def get_last_part(path):
        return os.path.basename(path)