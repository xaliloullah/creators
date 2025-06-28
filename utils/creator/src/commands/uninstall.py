from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class UninstallCommand(Command):
    @classmethod
    def config(cls, subparsers): 
        parser:Command  = subparsers.add_parser('uninstall', help="Uninstall a package")
        parser.add_argument('package', help="Name of the package to uninstall")
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
        try:
            Creator.terminal.info(Creator.lang.get("info.uninstall", resource=f"package {args.package}"))
            Creator.task.uninstall(args.package)
        except Exception as e:
            Creator.terminal.error(e)
            
