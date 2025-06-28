# from utils.creator.src.commands import Command
# from utils.creator.src.app.creator import Creator 
# import traceback

# class AppCommand(Command):
#     @classmethod
#     def config(cls, subparsers):  
#         # 'upgrade' command
#         upgrade_parser:Command = subparsers.add_parser('upgrade', help="upgrades projets")
#         # upgrade_parser.add_argument('--action', choices=['run', 'delete'], default='create', help="upgrades action to perform")
#         upgrade_parser.set_defaults(func=cls.upgrade)
#         # 'update' command
#         update_parser:Command = subparsers.add_parser('update', help="updates projets")
#         update_parser.set_defaults(func=cls.update)
#         # parser.set_defaults(func=cls.handle)

#     @staticmethod
#     def handle(args):
#         pass

#     @staticmethod
#     def upgrade(args):  
#         # upgrade
#         Creator.terminal.info(Creator.lang.get("info.update", resource="project"))
#         # try: 
#         #     Creator.upgrade()
#         # except Exception as e:
#         #     Creator.terminal.error(f"{traceback.format_exc()}") 

#     @staticmethod
#     def update(args):  
#         # update
#         Creator.terminal.info(Creator.lang.get("info.update", resource="project"))
#         # try: 
#         #     Creator.update()
#         # except Exception as e:
#         #     Creator.terminal.error(f"{traceback.format_exc()}") 
       