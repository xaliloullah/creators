from utils.creator.src.environment import env


driver =  env('DB_CONNECTION', 'sqlite')  #driver

connections =  {
    # SQLite Config 
    'sqlite': {
        'driver': 'sqlite',
        'path': f"{env('DB_PATH', 'database')}/{env('DB_DATABASE', f"{env('APP_NAME', 'creator')}.db")}"
    },

    # MySQL Config 
    'mysql': {
        'driver': 'mysql',
        'host': env('DB_HOST', '127.0.0.1'),
        'port': env('DB_PORT', '3306'),
        'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
        'username': env('DB_USERNAME', 'root'),
        'password': env('DB_PASSWORD', ''),
    },

    # PostgreSQL Config 
    'postgresql': {
        'driver': 'postgresql',
        'host': env('DB_HOST', '127.0.0.1'),
        'port': env('DB_PORT', '5432'),
        'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
        'username': env('DB_USERNAME', 'postgres'),
        'password': env('DB_PASSWORD', ''),
    },

    # SQL Server Config 
    'sqlserver': {
        'driver': 'sqlserver',
        'host': env('DB_HOST', '127.0.0.1'),
        'port': env('DB_PORT', '1433'),
        'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
        'username': env('DB_USERNAME', 'sa'),
        'password': env('DB_PASSWORD', ''),
    },

    # Oracle Config 
    'oracle': {
        'driver': 'oracle',
        'host': env('DB_HOST', '127.0.0.1'),
        'port': env('DB_PORT', '1521'),
        'database': env('DB_DATABASE', 'ORCLCDB'),
        'username': env('DB_USERNAME', 'system'),
        'password': env('DB_PASSWORD', ''),
    }
}

migrations = {
    'name': 'migrations',
    'path': f"{env('DB_PATH', 'database')}/migrations/"
} 

# database = {
#     'db': env('DB_CONNECTION', 'sqlite'),  #default

#     'connections': {
#         # SQLite Config 
#         'sqlite': {
#             'driver': 'sqlite',
#             'path': f"{env('DB_PATH', 'database')}/{env('DB_DATABASE', f"{env('APP_NAME', 'creator')}.db")}"
#         },

#         # MySQL Config 
#         'mysql': {
#             'driver': 'mysql',
#             'host': env('DB_HOST', '127.0.0.1'),
#             'port': env('DB_PORT', '3306'),
#             'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
#             'username': env('DB_USERNAME', 'root'),
#             'password': env('DB_PASSWORD', ''),
#         },

#         # PostgreSQL Config 
#         'postgresql': {
#             'driver': 'postgresql',
#             'host': env('DB_HOST', '127.0.0.1'),
#             'port': env('DB_PORT', '5432'),
#             'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
#             'username': env('DB_USERNAME', 'postgres'),
#             'password': env('DB_PASSWORD', ''),
#         },

#         # SQL Server Config 
#         'sqlserver': {
#             'driver': 'sqlserver',
#             'host': env('DB_HOST', '127.0.0.1'),
#             'port': env('DB_PORT', '1433'),
#             'database': env('DB_DATABASE', env('APP_NAME', 'creator')),
#             'username': env('DB_USERNAME', 'sa'),
#             'password': env('DB_PASSWORD', ''),
#         },

#         # Oracle Config 
#         'oracle': {
#             'driver': 'oracle',
#             'host': env('DB_HOST', '127.0.0.1'),
#             'port': env('DB_PORT', '1521'),
#             'database': env('DB_DATABASE', 'ORCLCDB'),
#             'username': env('DB_USERNAME', 'system'),
#             'password': env('DB_PASSWORD', ''),
#         }
#     },

#     'migrations': {
#         'name': 'migrations',
#         'path': f"{env('DB_PATH', 'database')}/migrations/"
#     }
# }

