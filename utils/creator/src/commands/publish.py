from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class PublishCommand(Command):
    @classmethod
    def config(cls, subparsers):  
        parser:Command = subparsers.add_parser('publish', help="Publish a resources")
        parser.add_argument('--package', help="Name of the package to publish")
        parser.add_argument('--lang', help="Name of the lang to publish")
        parser.add_argument('--tag', help="tag of the package to publish") 
        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
        pass