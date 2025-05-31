# from creators.src.core.process import *
# from creators.src.core.debug import *
# from creators.src.core.date import * 


# from creators.src.core.view import * 

# def vscode_setting(path):
#     try:  
#         settings = load(path, format="json")
        
#         settings["files.associations"] = {
#             "*.cre": "python", 
#             "creator": "python"
#         } 
#         save(path, settings, format="json", indent=2)   
#     except Exception as e:
#         raise Exception(e)
    
# def setting(path):
#     try:   
#         settings = load(path, format="json")
        
#         settings["metadata"] = {
#             "name": "mon_projet",
#             "version": "1.0.0",
#             "author": "John Doe",
#             "author_email": "john.doe@example.com",
#             "description": "Un exemple de projet Python avec JSON",
#             "long_description": "file: README.md",
#             "long_description_content_type": "text/markdown",
#             "url": "https://github.com/johndoe/mon_projet",
#             "license": "MIT",
#             "classifiers": [
#                 "Development Status :: 4 - Beta",
#                 "Intended Audience :: Developers",
#                 "License :: OSI Approved :: MIT License",
#                 "Programming Language :: Python :: 3",
#                 "Programming Language :: Python :: 3.8",
#                 "Programming Language :: Python :: 3.9",
#                 "Programming Language :: Python :: 3.10",
#                 "Operating System :: OS Independent",
#                 "Topic :: Software Development :: Libraries"
#             ]
#         },
#         settings["options"]={
#             "packages": ["find:"],
#             "python_requires": ">=3.8",
#             "install_requires": [
#                 "requests>=2.25.1",
#                 "numpy>=1.21.0"
#             ]
#         },
#         settings["extras_require"]={
#             "dev": ["black", "flake8", "pytest"],
#             "docs": ["sphinx", "sphinx-rtd-theme"]
#         },
#         settings["package_data"]={
#             "*": ["*.txt", "*.md"]
#         },
#         settings["entry_points"]={
#             "console_scripts": [
#                 "mon_projet = mon_projet.main:main"
#             ]
#         },
#         settings["bdist_wheel"]={
#             "universal": True
#         }
#         save(path, settings, format="json", indent=2)  
#     except Exception as e:
#         raise Exception(e)
    
# def install_requirements(path):
    
#     requirements = load(path, format="json")  
#     for key, value in requirements.items():
#         package = value["package"]
#         version = value["version"]
#         install(package, version=version)
        
# def creating_resources():
#     path = resources_path()
#     ensure_path_exists(path)
    
# def creating_config(source, destination):
#     ensure_path_exists(source)
#     configs_file = list_dir(source, endswith='.py')
    
#     content = []
#     for config in configs_file:
#         content.append(build_import(join_path(source, config), "*"))
        
#     save(destination, "\n".join(content)) 
    
# def backup(source, destination):
#     pass
    
# def make_architecture(path):
#     ensure_path_exists(path) 
#     save(path, make_structure(ignore=['__pycache__', '.vscode']))
        
  