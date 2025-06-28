from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class VenvCommand(Command):
    @classmethod
    def config(cls, subparsers):  
        parser:Command = subparsers.add_parser("venv", help="Gérer un environnement virtuel")
        parser.add_argument("--create", help="Créer un environnement virtuel", action="store_true")
        parser.add_argument("--path", help="Spécifier le chemin de l'environnement virtuel")
        parser.add_argument("--activate", help="Spécifier le chemin de l'environnement virtuel", action="store_true")
        parser.add_argument("--deactivate", help="Spécifier le chemin de l'environnement virtuel", action="store_true")
        parser.add_argument("--remove", help="Supprimer l'environnement virtuel", action="store_true")
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
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
                
            
