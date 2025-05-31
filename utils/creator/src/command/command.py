from utils.creator.src.app.creator import Creator
from utils.creator.src.core import Builder  
from utils.creator.src.servers.server import Server
import argparse
import traceback 


class Command(argparse.ArgumentParser): 
    
    @staticmethod
    def make(args):
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
                    file.write(Builder.command(Creator.file.get_last_part(name), args.model))
                Creator.terminal.success(Creator.lang.get("success.create", resource=f"command '{args.command}'"))
            except Exception:
                Creator.terminal.error(f"{traceback.format_exc()}") 

        elif args.cache: 
            name = str(args.cache).lower().replace(" ", "_")
            if name == 'config': 
                Creator.settings.cache(source = Creator.path.config, destination=Creator.file.set_extension(Creator.path.config,'py'), mode="import") 
            elif name == 'routes':
                Creator.settings.cache(source = Creator.path.routes, destination=Creator.file.set_extension(Creator.path.routes,'py'), mode="import") 
            Creator.terminal.success(Creator.lang.get("success.create", resource=f"Cache '{args.cache}'"))

            
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
    def delete(args):
        """Delete a model, controller, migration, or a backup."""
        if args.model: 
            name = str(args.model).replace(" ", "_").lower()
            filename = f"app/models/{name}.py"
            if Creator.file.path_exists(filename):
                Creator.file.remove(filename) 
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"Model '{args.model}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"Model {args.model}")) 
                
        elif args.controller: 
            name = str(args.controller).replace(" ", "_").lower()
            filename = f"app/controllers/{name}.py"
            if Creator.file.path_exists(filename):
                Creator.file.remove(filename) 
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"Controller '{args.controller}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"Controller '{args.controller}'")) 
                
        elif args.migration: 
            name = str(args.migration).replace(" ", "_").lower()
            filename = f"databases/migrations/{name}"
            if Creator.file.path_exists(filename):
                Creator.file.remove(filename)
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"Migration '{args.migration}'")) 
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"Migration '{args.migration}'")) 

        elif args.backup:
            try:  
                name = str(args.backup)
                folder = Creator.file.storage_path(f"backups/{name}")
                if Creator.file.path_exists(folder):
                    Creator.file.rmdir(folder)
                    Creator.terminal.success(Creator.lang.get("success.delete", resource=f"Backups {args.backup}"))
                else:
                    Creator.terminal.error(Creator.lang.get("error.delete",resource=f"Backups {args.backup}")) 
            except Exception as e:
                Creator.terminal.error(f"{traceback.format_exc()}") 
        elif args.middleware: 
            name = str(args.middleware).replace(" ", "_").lower()
            filename = f"app/middlewares/{name}.py"
            if Creator.file.path_exists(filename):
                Creator.file.remove(filename) 
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"Middleware '{args.middleware}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"Middleware '{args.middleware}'")) 


        elif args.view:
            folder = f"{Creator.file.resources_path(args.view)}.cre" 
            if Creator.file.path_exists(folder):
                Creator.file.remove(folder)
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"View '{args.view}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"View '{args.view}'"))  
        else:
            Creator.terminal.warning(Creator.lang.get("warning.options", resource=f"model, controller, migration, backup, or view"))
            
    # @staticmethod
    # def backup(args): 
    #     if args.action == 'create': 
    #         pass

                
    @staticmethod
    def upgrade(args):  
        # upgrade
        Creator.terminal.info(Creator.lang.get("info.update", resource="project"))
        try: 
            Creator.upgrade()
        except Exception as e:
            Creator.terminal.error(f"{traceback.format_exc()}") 

    @staticmethod
    def update(args):  
        # update
        Creator.terminal.info(Creator.lang.get("info.update", resource="project"))
        try: 
            Creator.update()
        except Exception as e:
            Creator.terminal.error(f"{traceback.format_exc()}") 
            
        
    @staticmethod
    def migrate(args):
        from utils.creator.src.databases.migration import Migration
        """Execute migration actions.""" 
        
        if args.run:
            Creator.terminal.info(Creator.lang.get("info.run", resource="migration")) 
            Migration().migrate()

        elif args.rollback:
            Creator.terminal.info(Creator.lang.get("info.rollback", resource="migration"))
            Migration().migrate('down')

        elif args.check:
            Creator.terminal.info(Creator.lang.get("info.check", resource="migration")) 
            migrations = Migration().check()
            Creator.terminal.list(migrations, icon = Creator.terminal.icon_light_check(), margin=3, display=True) 

        elif args.list:
            Creator.terminal.info(Creator.lang.get("info.list", resource="migration"))
            migrations = Migration().get()
            Creator.terminal.list(migrations, icon = Creator.terminal.icon_arrow_right(), margin=3, color = Creator.terminal.black, display=True) 

        elif args.fresh:
            Creator.terminal.info(Creator.lang.get("info.fresh", resource="migration"))
            Migration().migrate('down')
            Migration().migrate()
            
        elif args.drop:
            Creator.terminal.info(Creator.lang.get("info.drop", resource="migration"))
            Migration().down()  
        else: 
            Creator.terminal.info(Creator.lang.get("info.run", resource="migration"))
            Migration().migrate()
 
            
    @staticmethod
    def serve(args):
        """Start a server."""
        port = args.port
        if port:
            Server.set_port(port)
        # directory = args.directory or public_path('index.html')   
        # change_directory(directory)
        Server.start() 
        Creator.terminal.success(f"Server running on port: {Server.port}. URL: http://{Server.host}:{Server.port}")
        try:
            while not Server.stop_event.is_set():
                pass   
        except KeyboardInterrupt:
            Creator.terminal.warning(f"Stopping the server...")  
            Server.stop() 

     
            

    @staticmethod
    def install(args):
        try:
            Creator.terminal.info(Creator.lang.get("info.install", resource=f"package {args.package}"))
            if args.version:
                version = args.version
            else:
                version = None
            Creator.task.install(args.package, version=version) 
        except Exception as e:
            Creator.terminal.error(e)

    @staticmethod
    def uninstall(args):
        try:
            Creator.terminal.info(Creator.lang.get("info.uninstall", resource=f"package {args.package}"))
            Creator.task.uninstall(args.package)
        except Exception as e:
            Creator.terminal.error(e)
            
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
 

    @staticmethod
    def publish(args):
        if args.package: pass

    @staticmethod
    def lang(args):
        if args.set:
            if args.set in Creator.settings.get("langs"): 
                env = Creator.storage('.env', absolute=False, format="env")
                collect = Creator.collection(env) 
                collect.set("APP_LANG", args.set) 
                env.save(collect.get()) 
                Creator.terminal.success(Creator.lang.get("success.process"))
            else:
                Creator.terminal.error(Creator.lang.get("error.invalid", data=f"{args.set}"))
        elif args.list:
            Creator.terminal.list(Creator.lang.languages, display=True)
        elif args.check: 
            Creator.terminal.info(Creator.lang.check(args.check))
        elif args.generate:
            Creator.generate_lang(args.lang)
        else:
            return
        
    @staticmethod
    def venv(args):
        if args.create:
            Creator.terminal.info(Creator.lang.get("info.create", resource="virtual environment"))
            Creator.settings.create_venv() # args.path
        elif args.activate:
            Creator.terminal.info(Creator.lang.get("info.run", resource="virtual environment"))
            Creator.settings.activate_venv() # args.path
        elif args.deactivate:
            Creator.terminal.info(Creator.lang.get("info.run", resource="virtual environment"))
            Creator.settings.deactivate_venv() # args.path
        else:
            Creator.terminal.warning(Creator.lang.get("warning.options", resource="create, activate, or deactivate"))
                
    @classmethod
    def start(cls):
        # Main parser initialization 
        parser = Command(prog=f"{Creator.terminal.style(f"{Creator.name} v{Creator.version}", Creator.terminal.cyan, Creator.terminal.bold)}", description=f"CLI tool for managing creator.")
        
        subparsers = parser.add_subparsers(dest='command', help="Available commands") 

        # 'make' command
        make_parser = subparsers.add_parser('make', help="Create a model, controller, migration, view, cache, or a backup")
        
        make_parser.add_argument('--model', help="Create a new model")
        make_parser.add_argument('--controller', help="Create a new controller")
        make_parser.add_argument('--migration', help="Create a new migration file")
        make_parser.add_argument('--middleware', help="Create a new middleware")
        make_parser.add_argument('--view', help="Create a new view")
        make_parser.add_argument('--command', help="Create a new CREATOR command")
        make_parser.add_argument('-m', '--migrate', action='store_true', help="Create a migration for the model")
        make_parser.add_argument('-r', '--resource', action='store_true', help="Create a resource for the controller")

        make_cache_parser = make_parser.add_argument_group("cache")
        make_cache_parser.add_argument('--cache', type=str, nargs='?', help="cache app") 
        
        make_backup_parser = make_parser.add_argument_group("backup")
        make_backup_parser.add_argument('--backup', action='store_true', help="Create a new Backup")
        make_backup_parser.add_argument('-s','--source', help="Specify the source location for the backup")
        make_backup_parser.add_argument('-d','--destination', help="Specify the destination location for the backup")
        make_backup_parser.add_argument('-a','--all', action='store_true', help="Perform the backup action on all available sources and destinations")
        
        make_subparsers = make_parser.add_subparsers(dest='new command', help="Available commands of new", title="Sous-commandes pour 'new'")
        make_new_parser = make_subparsers.add_parser('new', help="Available commands")
        make_new_parser.add_argument("--project", type=str, nargs='?', help="Name of the new project to create")
        make_version_parser = make_new_parser.add_argument_group("version")
        make_version_parser.add_argument("-v", "--version", nargs='?',choices=['major', 'minor', 'patch'], const='patch')
        make_version_parser.add_argument('-s','--suffix', choices=['alpha', 'beta', 'rc','stable'],   help="suffix of the version")

        # new_parser = make_parser.add_subparsers('new', action='store_true', help="Perform the backup action on all available sources and destinations")
        make_new_parser.set_defaults(func=Command.new)
        make_parser.set_defaults(func=Command.make)

        # 'delete' command
        delete_parser = subparsers.add_parser('delete', help="Delete a model, controller, migration, or a backup")
        delete_parser.add_argument('--model', help="Delete a model")
        delete_parser.add_argument('--controller', help="Delete a controller")
        delete_parser.add_argument('--migration', help="Delete a migration file")
        delete_parser.add_argument('--middleware', help="Delete a middleware")
        delete_parser.add_argument('--command', help="Delete a command")
        delete_parser.add_argument('--view', help="Delete a view")
        delete_parser.add_argument('--backup', help="Delete a backup") 
        delete_parser.set_defaults(func=Command.delete)

        # 'migrate' command
        migrate_parser = subparsers.add_parser('migrate', help="Migration actions")
        migrate_parser_group = migrate_parser.add_argument_group("migrate")
        migrate_parser_group.add_argument('--run', action='store_true', help="Run the migrations")
        migrate_parser_group.add_argument('--rollback', action='store_true', help="Rollback the last migration")
        migrate_parser_group.add_argument('--check', action='store_true', help="Check the migration status")
        migrate_parser_group.add_argument('--list', action='store_true', help="List all migrations")
        migrate_parser_group.add_argument('--fresh', action='store_true', help="Fresh migration")
        migrate_parser_group.add_argument('--drop', action='store_true', help="Drop all migrations")
        
        migrate_parser.set_defaults(func=Command.migrate) 

        # 'upgrade' command
        upgrade_parser = subparsers.add_parser('upgrade', help="upgrades projets")
        # upgrade_parser.add_argument('--action', choices=['run', 'delete'], default='create', help="upgrades action to perform")
        upgrade_parser.set_defaults(func=Command.upgrade)
        # 'update' command
        update_parser = subparsers.add_parser('update', help="updates projets")
        # update_parser.add_argument('--action', choices=['run', 'delete'], default='create', help="updates action to perform")
        update_parser.set_defaults(func=Command.update)

        # 'serve' command
        serve_parser = subparsers.add_parser('serve', help="Start a simple server")
        serve_parser.add_argument('-p','--port', type=int, help="Port to run the server on")
        serve_parser.add_argument('-d','--directory', help="Directory to serve files from (default: current working directory)")
        serve_parser.set_defaults(func=Command.serve)

        # 'install' command
        install_parser = subparsers.add_parser('install', help="Install a package")
        install_parser.add_argument('package', help="Name of the package to install")
        install_parser.add_argument('-v','--version', help="version of the package to install")
        install_parser.set_defaults(func=Command.install)

        # 'uninstall' command
        uninstall_parser = subparsers.add_parser('uninstall', help="Uninstall a package")
        uninstall_parser.add_argument('package', help="Name of the package to uninstall")
        uninstall_parser.set_defaults(func=Command.uninstall)

        

        # # 'clean' command
        # clean_parser = subparsers.add_parser('clean', help="clean a package")
        # clean_parser.add_argument('package', help="Name of the package to clean")
        # clean_parser.set_defaults(func=Command.uninstall)
        
        # 'publish' command
        publish_parser = subparsers.add_parser('publish', help="Publish a resources")
        publish_parser.add_argument('--package', help="Name of the package to publish")
        publish_parser.add_argument('--lang', help="Name of the lang to publish")
        publish_parser.add_argument('--tag', help="tag of the package to publish") 
        
        publish_parser.set_defaults(func=Command.publish)
        
        # Sub-command 'venv'
        venv_parser = subparsers.add_parser("venv", help="Gérer un environnement virtuel")
        venv_parser.add_argument("--create", help="Créer un environnement virtuel", action="store_true")
        venv_parser.add_argument("--path", help="Spécifier le chemin de l'environnement virtuel")
        venv_parser.add_argument("--activate", help="Spécifier le chemin de l'environnement virtuel", action="store_true")
        venv_parser.add_argument("--deactivate", help="Spécifier le chemin de l'environnement virtuel", action="store_true")
        venv_parser.set_defaults(func=Command.venv)

        # Sub-command 'lang'
        lang_parser = subparsers.add_parser("lang", help="Configurer la langue")
        lang_parser.add_argument("--set", help="Définir la langue (ex: fr, en)", type=str)
        lang_parser.add_argument("--list", help="Lister les langues disponibles", action="store_true")
        lang_parser.add_argument("--check", help="Lister les langues disponibles", type=str)
        lang_parser.add_argument("--generate", help="Lister les langues disponibles", type=str)
        lang_parser.set_defaults(func=Command.lang)

        
        parser.add_argument("-v" ,"--version", action='version', version=f'{Creator.version}') 
        parser.add_argument("--author","--creator","--developer", action="store_true") 
        parser.add_argument("--description", "--desc", action="store_true") 
        parser.add_argument("--python","--language", action="store_true") 
        parser.add_argument("--packages", action="store_true") 
        parser.add_argument("--key", action="store_true")  
        # 'activate' command 
        
        
        args = parser.parse_args()
        if args.author:
            Creator.terminal.highlight(Creator.author)
        elif args.description: 
            Creator.terminal.quote(Creator.description, Creator.author)
        elif args.python:
            Creator.terminal.info(f"Python : {Creator.python}")
        elif args.packages:
            Creator.terminal.info(Creator.packages)
        elif args.key:
            Creator.terminal.info(Creator.key)
        elif args.command:
            args.func(args)
        else:
            parser.print_help()



# Usage:
#   command [options] [arguments]

# Options:
#   -h, --help            Display help for the given command. When no command is given display help for the list command  
#   -q, --quiet           Do not output any message
#   -V, --version         Display this application version
#       --ansi|--no-ansi  Force (or disable --no-ansi) ANSI output
#   -n, --no-interaction  Do not ask any interactivate question
#       --env[=ENV]       The environment the command should run under
#   -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

# Available commands for the "make" namespace:
#   make:cache-table          [cache:table] Create a migration for the cache database table
#   make:cast                 Create a new custom Eloquent cast class
#   make:channel              Create a new channel class
#   make:class                Create a new class
#   make:command              Create a new Artisan command
#   make:component            Create a new view component class
#   make:controller           Create a new controller class
#   make:enum                 Create a new enum
#   make:event                Create a new event class
#   make:exception            Create a new custom exception class
#   make:factory              Create a new model factory
#   make:interface            Create a new interface
#   make:job                  Create a new job class
#   make:job-middleware       Create a new job middleware class
#   make:listener             Create a new event listener class
#   make:mail                 Create a new email class
#   make:middleware           Create a new HTTP middleware class
#   make:migration            Create a new migration file
#   make:model                Create a new Eloquent model class
#   make:notification         Create a new notification class
#   make:notifications-table  [notifications:table] Create a migration for the notifications table
#   make:observer             Create a new observer class
#   make:policy               Create a new policy class
#   make:provider             Create a new service provider class
#   make:queue-batches-table  [queue:batches-table] Create a migration for the batches database table
#   make:queue-failed-table   [queue:failed-table] Create a migration for the failed queue jobs database table
#   make:queue-table          [queue:table] Create a migration for the queue jobs database table
#   make:request              Create a new form request class
#   make:resource             Create a new resource
#   make:rule                 Create a new validation rule
#   make:scope                Create a new scope class
#   make:seeder               Create a new seeder class
#   make:session-table        [session:table] Create a migration for the session database table
#   make:test                 Create a new test class
#   make:trait                Create a new trait
#   make:view                 Create a new view