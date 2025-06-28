from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
import traceback

class LangCommand(Command):
    @classmethod
    def config(cls, subparsers): 
        parser:Command = subparsers.add_parser("lang", help="Configurer la langue")
        parser.add_argument("--set", help="Définir la langue (ex: fr, en)", type=str)
        parser.add_argument("--list", help="Lister les langues disponibles", action="store_true")
        parser.add_argument("--check", help="Lister les langues disponibles", type=str)
        parser.add_argument("--generate", help="Lister les langues disponibles", type=str)

        parser.set_defaults(func=cls.handle)

    @staticmethod
    def handle(args):
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
            return Creator.terminal.error(Creator.lang.get("error.invalid", data=f"{args.set}"))