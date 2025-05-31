# from creators.src.console.terminal import Terminal
# from creators.src.core.request import *
# from creators.src.core.error import *
# from creators.src.core.setup import *


class Handler:

    @classmethod
    def exception(cls, e): 
        raise Exception(cls.terminal.error(f"{str(e)}"))
#     def __init__(self, app_mode):
#         self.Terminal = Terminal() 
#         self.mode = app_mode
#         self.events = {}
#         self.ERROR = "error"
#         self.SUCCESS = "success"
#         self.INFO = "info"
#         self.WARNING = "warning"
#         self.COMMENT = "comment"
#         self.DEBUG = "debug"
#         self.DD = "dump and die"
        
#     def get_mode(self):
#         return self.mode
    
#     def set_mode(self, mode):
#         self.mode = mode
        
#     def get_terminal(self):
#         return self.Terminal
    
#     def response(self, status, *message, **data): 
#         if isinstance(data, set):   
#             data = list(data)
        
#         response = {
#             'status': status, 
#             'message': message
#         } 
        
#         if data is not None:   
#             response['data'] = data  
        
#         # 
#         if self.mode == 'console':
#             return self.response_console(response)
        
#         if self.mode == 'app':
#             return self.response_app(response)
        
#         if self.mode == 'web': 
#             return self.response_web(response)
        
#         raise ValueError('Mode not recognized')
    
        
#     def response_console(self, response):
        
#         if response["status"] == self.ERROR:
#             self.Terminal.error(response["message"]) 
#             exit()
#             # raise
            
#         if response["status"] == self.SUCCESS: 
#             self.Terminal.success(response["message"]) 
            
#         if response["status"] == self.WARNING: 
#             self.Terminal.warning(response["message"]) 
            
#         if response["status"] == self.INFO: 
#             self.Terminal.info(response["message"]) 
            
#         if response["status"] == self.COMMENT: 
#             self.Terminal.comment(response["message"]) 
            
#         if response["status"] == self.DD: 
#             self.Terminal.echo(response["message"]) 
#             exit()
            
#         if response["status"] == self.DEBUG: 
#             self.Terminal.echo(response["message"])  
    
#     def response_web(self,response): 
#         import json
#         return json.dumps(response)
        
#     def response_app(self,response):
#         return response 
    
#     # event
#     def set_event(self, event, callback): 
#         if event not in self.events:
#             self.events[event] = []
#         self.events[event].append(callback)
#         # print(f"Événement '{event}' enregistré avec succès.")

#     def remove_event(self, event, callback): 
#         if event in self.events and callback in self.events[event]:
#             self.events[event].remove(callback)
#             # print(f"Événement '{event}' désenregistré avec succès.")
#         # else:
#             # print(f"Événement '{event}' ou callback introuvable.")

#     def event(self, event, *args, **kwargs): 
#         if event in self.events:
#             # print(f"Gestion de l'événement '{event}'...")
#             for callback in self.events[event]:
#                 callback(*args, **kwargs)
#         # else:
#         #     print(f"Aucun gestionnaire trouvé pour l'événement '{event}'.")
    
#     def error(self, arg, data=None):
#         return self.response(self.ERROR, arg, data)
    
#     def success(self, arg, data=None):
#         return self.response(self.SUCCESS, arg, data)
    
#     def info(self, arg, data=None):
#         return self.response(self.INFO, arg, data)
    
#     def warning(self, arg, data=None):
#         return self.response(self.WARNING, arg, data)
    
#     def debug(self, *args, **kwargs):
#         return self.response("debug", args, kwargs)
    
#     def dd(self, *args, **kwargs):
#         return self.response("dump and die", args, kwargs)
    
    
# def handler():
#     return Handler(app["mode"])


# def dd(*args, **kwargs): 
#     return handler().debug(args, kwargs) 

# def debug(*args, **kwargs): 
#     return handler().debug(args, kwargs) 

# def setup(): 
#     handler().Terminal.info(f"load settings file...")
#     try:
#         path = 'creators/src/core/settings.json'
#         setting(path)
#         handler().Terminal.info(f"creating settings file to : {path}")
#     except Exception:
#         handler().Terminal.error(f"{traceback.format_exc()}") 
        
#     handler().Terminal.info(f"load settings file...")
#     try:
#         path = '.vscode/settings.json'
#         vscode_setting(path)
#         handler().Terminal.info(f"creating settings vscode file to : {path}")
#     except Exception:
#         handler().Terminal.error(f"{traceback.format_exc()}") 
        
    
        
#     # requirements 
#     handler().Terminal.info(f"installing requirements packages ...")
#     install_requirements(path = 'requirements.json')
#     handler().Terminal.info(f"installing packages fininsh ...")
    
    
#     handler().Terminal.info(f"creating resources ...")
#     creating_resources()
    
#     handler().Terminal.info(f"creating config ...")
#     source = "config"
#     destination="creators/src/core/config.py"
#     creating_config(source, destination)
    
    
#     path = 'docs/ARCHITECTURE.md' 
#     make_architecture(path)
#     handler().Terminal.info(f"creating ARCHITECTURE file to : {path}")
    
    
    
    
    