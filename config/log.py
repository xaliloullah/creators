# import logging
# from logging.handlers import RotatingFileHandler
# from config.app import app, env


# config = {
#     'log': {
#         'path': 'storage/logs/creators.log',
#         'max_size': 1000000,  # 1 MB
#         'backup_count': 5,     # Keep 5 backup logs
#         'level': logging.DEBUG,
#         'format': '%(asctime)s - %(levelname)s - %(message)s'
#     }
# }
# log = config['log']

# # ensure_path_exists(log['path'])

# # Create a rotating file handler
# file_handler = RotatingFileHandler(
#     filename=log['path'], maxBytes=log['max_size'], backupCount=log['backup_count'])
# file_handler.setLevel(log['level'])
# file_handler.setFormatter(logging.Formatter(log['format']))

# # # Create a console handler
# # console_handler = logging.StreamHandler()
# # console_handler.setLevel(log['level'])
# # console_handler.setFormatter(logging.Formatter(log['format']))

# # Get the root logger and add the handlers
# logger = logging.getLogger()
# logger.setLevel(log['level'])
# logger.addHandler(file_handler)
# # logger.addHandler(console_handler)


# def info(message):
#     logging.info(message)


# def error(message):
#     logging.error(message)


# def warning(message):
#     logging.warning(message)


# def debug(message):
#     logging.debug(message)


# def critical(message):
#     logging.critical(message)


# def exception(message):
#     logging.exception(message)
