from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class DeleteCommand(Command):
    @classmethod
    def config(cls, subparsers):
        # parser:Command = subparsers.add_parser('delete', help="Delete something")
        # parser.add_argument('--name', help="Name of the thing to delete")
        # parser.set_defaults(func=cls.handle)

        # 'delete' command
        parser:Command  = subparsers.add_parser('delete', help="Delete a model, controller, migration, or a backup")
        parser.add_argument('--model', help="Delete a model")
        parser.add_argument('--controller', help="Delete a controller")
        parser.add_argument('--migration', help="Delete a migration file")
        parser.add_argument('--middleware', help="Delete a middleware")
        parser.add_argument('--command', help="Delete a command")
        parser.add_argument('--view', help="Delete a view")
        parser.add_argument('--backup', help="Delete a backup")
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
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
        elif args.command: 
            name = str(args.command).replace(" ", "_").lower()
            filename = f"app/commands/{name}.py"
            if Creator.file.path_exists(filename):
                Creator.file.remove(filename) 
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"command '{args.command}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"command '{args.command}'")) 


        elif args.view:
            folder = f"{Creator.file.resources_path(args.view)}.cre" 
            if Creator.file.path_exists(folder):
                Creator.file.remove(folder)
                Creator.terminal.success(Creator.lang.get("success.delete", resource=f"View '{args.view}'"))
            else:
                Creator.terminal.error(Creator.lang.get("error.delete", resource=f"View '{args.view}'"))  
        else:
            Creator.terminal.warning(Creator.lang.get("warning.options", resource=f"model, controller, migration, backup, or view"))
            