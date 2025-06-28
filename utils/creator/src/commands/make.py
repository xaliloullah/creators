# coding python
from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator
from utils.creator.src.core import Builder  
import traceback  

class MakeCommand(Command):
    
    @classmethod
    def config(cls, subparsers):
        # ex :
        # parser = subparsers.add_parser('make', help="Create something")
        # parser.add_argument('--name', help="Name of the thing to create")
        # parser.set_defaults(func=cls.handle)


        # 'make' command
        parser:Command = subparsers.add_parser('make', help="Create a model, controller, migration, view, cache, or a backup")
        
        parser.add_argument('--model', help="Create a new model")
        parser.add_argument('--controller', help="Create a new controller")
        parser.add_argument('--migration', help="Create a new migration file")
        parser.add_argument('--middleware', help="Create a new middleware")
        parser.add_argument('--view', help="Create a new view")
        parser.add_argument('--command', help="Create a new CREATOR command")
        parser.add_argument('-m', '--migrate', action='store_true', help="Create a migration for the model")
        parser.add_argument('-r', '--resource', action='store_true', help="Create a resource for the controller")

        make_cache_parser = parser.add_argument_group("cache")
        make_cache_parser.add_argument('--cache', type=str, nargs='?', help="cache app") 
        
        make_backup_parser = parser.add_argument_group("backup")
        make_backup_parser.add_argument('--backup', action='store_true', help="Create a new Backup")
        make_backup_parser.add_argument('-s','--source', help="Specify the source location for the backup")
        make_backup_parser.add_argument('-d','--destination', help="Specify the destination location for the backup")
        make_backup_parser.add_argument('-a','--all', action='store_true', help="Perform the backup action on all available sources and destinations")
        
        make_subparsers = parser.add_subparsers(dest='new command', help="Available commands of new", title="Sous-commandes pour 'new'")
        make_new_parser = make_subparsers.add_parser('new', help="Available commands")
        make_new_parser.add_argument("--project", type=str, nargs='?', help="Name of the new project to create")
        make_version_parser = make_new_parser.add_argument_group("version")
        make_version_parser.add_argument("-v", "--version", nargs='?',choices=['major', 'minor', 'patch'], const='patch')
        make_version_parser.add_argument('-s','--suffix', choices=['alpha', 'beta', 'rc','stable'],   help="suffix of the version")

        # new_parser = parser.add_subparsers('new', action='store_true', help="Perform the backup action on all available sources and destinations")
        make_new_parser.set_defaults(func=cls.new)
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
        """Create a new model, controller, migration or a backup."""
        if args.controller:
            name = str(args.controller).replace(" ", "_") 
            try:
                path = "app/controllers/"
                filename = path + name + ".py"
                if Creator.file.path_exists(filename):
                    return Creator.terminal.error(Creator.lang.get("error.exist", resource=f"Controller '{args.controller}'"))
                Creator.file.ensure_path_exists(filename)
                
                with open(filename, 'w') as file:
                    file.write(Builder.controller(Creator.file.get_last_part(name), args.model, args.resource))
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"Controller '{args.controller}'"))
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}")  

        elif args.model:
            name = str(args.model).replace(" ", "_")
            table = name.lower()
            if not table.endswith('s'):
                table += 's'
            try:
                path = "app/models/"
                filename = path + name.lower() + ".py"
                if Creator.file.path_exists(filename):
                    return Creator.terminal.error(Creator.lang.get("error.exist", resource=f"Model '{args.model}'"))
                Creator.file.ensure_path_exists(filename)
                with open(filename, 'w') as file:
                    file.write(Builder.model(Creator.file.get_last_part(name), table))
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"Model '{args.model}'")) 
                
                if args.migrate: 
                    from utils.creator.src.databases.migration import Migration
                    Migration().create(table)
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}") 
                
        elif args.migration:
            from utils.creator.src.databases.migration import Migration
            name = str(args.migration).lower().replace(" ", "_")
            Migration().create(name)

        elif args.middleware:
            name = str(args.middleware).replace(" ", "_") 
            try:
                path = "app/middlewares/"
                filename = path + name + ".py"
                if Creator.file.path_exists(filename):
                    return Creator.terminal.error(Creator.lang.get("error.exist", resource=f"middleware '{args.middleware}'"))
                Creator.file.ensure_path_exists(filename)
                
                with open(filename, 'w') as file:
                    file.write(Builder.middleware(Creator.file.get_last_part(name), args.model))
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"middleware '{args.middleware}'"))
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}") 

        elif args.command:
            name = str(args.command).replace(" ", "_") 
            try:
                path = "app/commands/"
                filename = path + name + ".py"
                if Creator.file.path_exists(filename):
                    return Creator.terminal.error(Creator.lang.get("error.exist", resource=f"command '{args.command}'"))
                Creator.file.ensure_path_exists(filename)
                
                with open(filename, 'w') as file:
                    file.write(Builder.command(Creator.file.get_last_part(name)))
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"command '{args.command}'"))
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}") 

        elif args.cache: 
            pass
            # name = str(args.cache).lower().replace(" ", "_")
            # if name == 'config': 
            #     Creator.settings.cache(source = Creator.path.config, destination=Creator.file.set_extension(Creator.path.config,'py'), mode="import") 
            # elif name == 'routes':
            #     Creator.settings.cache(source = Creator.path.routes, destination=Creator.file.set_extension(Creator.path.routes,'py'), mode="import") 
            # Creator.terminal.success(Creator.lang.get("success.create", resource=f"Cache '{args.cache}'"))

            
        elif args.backup:
            try: 
                source = args.source
                if not source:
                    source = "/"
                else:
                    source = Creator.file.join_path("/", source)
                source = Creator.file.get_path(source) 
                
                destination = args.destination
                if not destination:
                    timestamp = Creator.date.now().strftime('%Y%m%d_%H%M%S') 
                    destination = f"backup_{timestamp}" 
                destination = Creator.file.storage_path(f"backups/{destination}.zip")
                Creator.file.ensure_path_exists(destination)
                all = args.all
                ignore = ["backups", "__pycache__"]
                if not all: 
                    ignore.append("utils") 
                     
                Creator.file.save(source, destination, format="zip", ignore=ignore) 
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"Backup '{destination}'"))  
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}") 

        elif args.view:
            if args.resource: 
                view = f"{Creator.file.resources_path(args.view)}"
                resources = ['index', 'create', 'edit', 'view']
                for resource in resources:
                    Creator.file.save(f"{view}/{resource}.cre", Builder.view())
            else:
                view = f"{Creator.file.resources_path(args.view)}.cre"
                Creator.file.save(view, Builder.view())
            Creator.terminal.success(Creator.lang.get("success.create", resource=f"View '{view}'")) 
        else:
            Creator.terminal.warning(Creator.lang.get("warning.options", resource=f"model, controller, migration, backup, or view"))
        
            

    @staticmethod
    def new(args):
        try:   
            if args.version:
                if args.version == 'major':
                    Creator.version.major()
                elif args.version == 'minor':
                    Creator.version.minor()
                elif args.version == 'patch':
                    Creator.version.patch()
                    
                if args.suffix:
                    Creator.version.suffix(args.suffix)
                Creator.upgrade()
                source = Creator.file.get_path("./") 
                     
                destination = f"{Creator.name}_{Creator.version}" 
                destination = Creator.file.storage_path(f"versions/{destination}.zip")
                Creator.file.ensure_path_exists(destination) 
                ignore = ["__pycache__"]  
                
                only = ['app', 'utils', 'config', 'resources', 'routes', 'lang', 'creator', 'main.py']
                        
                Creator.file.save(source, destination, format="zip", only=only, ignore=ignore)   
                Creator.terminal.success(f"New version : {Creator.version} saved at {destination}") 

            elif args.project:
                Creator.terminal.info(Creator.lang.get("info.create", resource=f"project {args.project}"))  
                Creator.create(args.project) 

            else: 
                Creator.terminal.warning("Please specify either a version or ... .")
        except Exception:
            Creator.terminal.error(f"{traceback.format_exc()}")
 
