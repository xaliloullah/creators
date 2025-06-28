import argparse
from utils.creator.src.app.creator import Creator

class Command(argparse.ArgumentParser):

    commands = []

    @classmethod
    def setup(cls, commands):
        cls.commands = commands

    @classmethod
    def add(cls, *command):
        cls.commands.extend(command)

    @classmethod
    def config(cls, subparsers: argparse._SubParsersAction) -> None:
        raise NotImplementedError("Each command must implement 'config'.")

    @staticmethod
    def handle(args: argparse.Namespace):
        raise NotImplementedError("Each command must implement 'handle'.")
    
    @classmethod
    def run(cls):  
        parser = cls(prog=f"{Creator.terminal.style(f"{Creator.name} v{Creator.version} :", Creator.terminal.cyan, Creator.terminal.bold)}", description=f"{Creator.terminal.style(f"CLI tool for managing creator.", Creator.terminal.cyan, Creator.terminal.bold)}")
        subparsers = parser.add_subparsers(dest='command', help="Available Commands")

        parser.add_argument("-v" ,"--version", action='version', version=f'{Creator.version}') 
        parser.add_argument("--author","--creator","--developer", action="store_true") 
        parser.add_argument("--description", "--desc", action="store_true") 
        parser.add_argument("--python", "--language", action="store_true") 
        parser.add_argument("--packages", action="store_true")
        parser.add_argument("--key", action="store_true") 
        parser.add_argument("--update", action="store_true")  
        parser.add_argument("--upgrade", action="store_true") 

        for command in cls.commands:
            command.config(subparsers)

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
        elif args.update:
            Creator.update()
        elif args.upgrade:
            Creator.upgrade()
        elif args.command:
            args.func(args)
        else:
            parser.print_help()

 
# from .delete import DeleteCommand
# from .make import MakeCommand

# __all__ = ["Command", "DeleteCommand", "MakeCommand"]