from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class InstallCommand(Command):
    @classmethod
    def config(cls, subparsers):
        parser:Command = subparsers.add_parser('install', help="Install a package")
        parser.add_argument('package', help="Name of the package to install")
        parser.add_argument('-v','--version', help="version of the package to install")
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
        try:
            Creator.terminal.info(Creator.lang.get("info.install", resource=f"package {args.package}"))
            if args.version:
                version = args.version
            else:
                version = None
            Creator.task.install(args.package, version=version) 
        except Exception as e:
            Creator.terminal.error(e)
