from utils.creator.src.command.terminal import Terminal  
from utils.creator.src.core import Path, File, Task, Date, View, Lang, Hash, Crypt, Builder, Injector, Storage, Collection, Translator, Http
#
# , Interface
 
from utils.creator.src.app.configs import Settings,Version 

from utils.creator.src.requests.sessions import Session

from utils.creator.src.routes.app import Route

# from utils.creator.src.core.handler import Handler 
from utils.creator.src.app.cache import config

class Creator:  
    
    settings = Settings
    name = settings.get("name", 'creator')  
    author = settings.get("author", None)
    description = settings.get("description", None)
    version = Version(settings.get("version", None))   
    python = settings.get("python", None)
    packages = settings.get("packages", {})

    key = config.app.key 
    lang = Lang(config.app.lang) 
    debug = config.app.debug

    settings.lang = lang

    injector = Injector()
    session = Session
    terminal = Terminal
    path = Path
    file = File
    task = Task
    date = Date
    crypt = Crypt
    hash = Hash()
    build = Builder  
    storage = Storage 
    collection = Collection 
    translator = Translator 
    http = Http 
    
    supported_database = {
        "sqlite": "SQLite",
        "mysql": "MySQL",
        # "postgresql": "PostgreSQL",
        # "mongodb": "MongoDB",
        # "oracle": "Oracle",
        # "mssql": "Microsoft SQL Server",
        # "redis": "Redis",
        # "cassandra": "Cassandra",
        # "dynamodb": "DynamoDB",
        # "neo4j": "Neo4j"
    } 
    # http = Http
    # interface =Interface


    class route(Route):
        def __init__(self, name, **kwargs): 
            Creator.handle_request(self.route(name, **kwargs))  
            
    class view(View):
        def __init__(self, path:str='', *args): 
            super().__init__(path, *args)


    @classmethod 
    def start(cls): 
        try:  
            from utils.creator.src.app.cache import routes
            cls.route(cls.main)  
             
        except Exception as e:
            cls.handle_exception(e)

    @classmethod 
    def auth(cls):
        from utils.creator.src.auth import Auth
        return Auth()

        
    @classmethod
    def configure(cls, **kwargs):
        try:    
            retry = kwargs.get("retry", True)
            cls.main = kwargs.get("main", "main")
            cls.debug = kwargs.get("debug", False)

            cls.name = cls.settings.get("name")  
            # cls.key = cls.settings.get("key")
            cls.version = Version(cls.settings.get("version"))   
            if cls.key:
                if cls.key  == "$2b$12$hxdTfdcIPOCP3x3YxhZ3JOEIC4rD38dD1XMbd/mskWHivqzmdiWru":
                    return cls
                else:
                    raise RuntimeError("Invalid key provided in the configuration.")
            else:
                cls.create()
        except KeyError as e:    
            if retry:   
                cls.settings.setup()
                return cls.configure(retry=False)
            else:
                raise RuntimeError("Configuration échouée après une tentative de récupération.") from e

    @classmethod
    def create(cls, project=None):
        cls.terminal.progress_bar(10, 100, 50)
        cls.terminal.highlight(cls.build.creator())  
        if not project:
            project = cls.terminal.input("project", type="text") 
        cls.terminal.progress(10, 100)
        cls.settings.vscode_setting()  
        # cls.settings.publish_views()
        # cls.settings.publish_routes()
        cls.terminal.info(cls.lang.get("info.install", resource="packages"))
        cls.settings.install_packages()
        cls.terminal.progress(1, 100)
        lang = cls.terminal.input(cls.lang.get("info.options", resource=f"lang"), type="select", options=cls.lang.languages, value="en")
        
        
        cls.generate_lang(lang)
        # cls.settings.set("key", cls.hash.generate_key())
        key = "$2b$12$hxdTfdcIPOCP3x3YxhZ3JOEIC4rD38dD1XMbd/mskWHivqzmdiWru" 
        database = cls.terminal.input(cls.lang.get("info.options", resource=f"database"), type="select", options=cls.supported_database, value="sqlite") 
        
        debug = cls.terminal.input("Activate debug app", type="checkbox", value="no")
        env = Builder.env(app_name=project, app_lang=lang, app_key=key, app_debug=debug, db_driver=database) 
        cls.file.save('.env', env, format=".env") 
         
        cls.settings.make_architecture()
           
    @classmethod
    def upgrade(cls): 
        cls.terminal.highlight(cls.build.creator()) 
        # cls.settings.set("key", False) 
        cls.settings.set("version", f"{cls.version}") 
        cls.settings.upgrade()

    @classmethod
    def update(cls):
        cls.terminal.progress_bar(10, 100) 
        cls.terminal.highlight(cls.build.creator())  
        cls.settings.update()

    @classmethod
    def generate_lang(cls, lang):
        if lang in cls.lang.languages:
            langs:list = cls.settings.get("langs")
            if lang not in langs:
                cls.terminal.info(cls.lang.get("info.create", resource=f"lang {lang}"))
                cls.lang.generate(lang)
                langs.append(lang)
                cls.settings.set("langs", langs)
                cls.terminal.success(cls.lang.get("success.create", resource=f"lang {lang}"))
                cls.settings.upgrade()
        else:
            cls.terminal.error(cls.lang.get("error.invalid", data=f"lang '{lang}'"))

        
    
    @classmethod
    def handle_request(cls, handler):
        from utils.creator.src.requests.request import Request  
        from utils.creator.src.validators.validator import Validator
        
        cls.request = Request()
        cls.request.session = cls.session()
        cls.request.validator = Validator() 
        
        cls.injector.register(Request, cls.request.new(handler["data"]))  
        if handler:
            try: 
                if handler["params"]:
                    func, args, kwargs = cls.injector.resolve(handler["action"], **handler["params"]) 
                else:
                    func, args, kwargs = cls.injector.resolve(handler["action"])
                    
                cls.view.set_history({"action": func, "args": args, "kwargs": kwargs})
                # cls.session.set
                return func(*args, **kwargs) 
            
            except Exception as e:
                raise Exception(e)
        else:
            raise ValueError(f"No handler found for URL '{handler["url"]}' and method '{handler["method"]}'.")
    
    @classmethod
    def handle_exception(cls, e): 
        raise Exception(cls.terminal.error(f"{str(e)}")) 
    
    # @classmethod
    # def route(cls, name, **params):
    #     url = cls.Route.route(name, **params) 
    #     handler = cls.Route.dispatch(url, **params) 
    #     request = cls.request
    #     request(handler["query"]) 
    #     cls.injector.register(cls.request, request)
    #     if handler:
    #         try: 
    #             if handler["params"]:
    #                 handle = cls.injector.resolve(handler["action"], **handler["params"])
    #             else:
    #                 handle = cls.injector.resolve(handler["action"])
    #             response = handle["action"](*handle["params"], **handle["data"]) 
    #             return response
            
    #         except Exception as e:
    #             raise Exception(e)
    #     else:
    #         raise ValueError(f"No handler found for URL '{handler["url"]}' and method '{handler["method"]}'.") 
    
    # @classmethod
    # def handle(cls):
    #     if cls.mode == "console": 
    #         from utils.creator.src.routes.app import Route 
    #         cls.Route = Route
    #         cls.route("main")
    #     else:
    #         return None  