def app(name, lang, debug, key):
    code = f"""APP_NAME={name}  
APP_LANG={lang}  
APP_URL=http://localhost  
APP_DEBUG={debug} 
APP_KEY={key}
"""
    return code

def  session(name, driver="file", lifetime="30"):
    code = f"""SESSION_DRIVER={driver}
SESSION_LIFETIME={lifetime}
SESSION_COOKIE={name} 
"""
    return code


def database(name, path, driver):
    code = f"""DB_PATH={path}
"""
    if driver == 'sqlite':
        code+= f"""DB_CONNECTION=sqlite
DB_DATABASE={name}
"""

    elif driver == 'mysql':
        code += f"""DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE={name}
DB_USERNAME=root
DB_PASSWORD=
"""
    elif driver == 'postgresql':
        code += f"""DB_CONNECTION=pgsql
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE={name}
DB_USERNAME=postgres
DB_PASSWORD=
"""
    elif driver == 'sqlserver':
        code += f"""DB_CONNECTION=sqlsrv
DB_HOST=127.0.0.1
DB_PORT=1433
DB_DATABASE={name}
DB_USERNAME=sa
DB_PASSWORD=
"""
    return code

 

# from utils.creator.src.core import Storage, Collection, Path

# class ENV:  

#     def __init__(self, path= Path.env):
#         self.file = Storage(path, absolute=False, format="env", default={})
#         self.data = Collection(self.file)
    
#     def save(self):
#         self.file.save(self.data.get())

    
#     def app(self, name, lang="en", key=None, debug=False, url="http://localhost"):
#         self.data.set("APP_NAME", name) 
#         self.data.set("APP_LANG", lang) 
#         self.data.set("APP_URL", url) 
#         self.data.set("APP_DEBUG", debug) 
#         self.data.set("APP_KEY", key)  
#         return self
    
    
#     def session(self, name, driver="file", lifetime="30"):
#         self.data.set("SESSION_COOKIE", name) 
#         self.data.set("SESSION_DRIVER", driver) 
#         self.data.set("SESSION_LIFETIME", lifetime)  
#         return self  
    
    
#     def database(self, name, path=Path.database, driver="sqlite"):
#         self.data.set("DB_DATABASE", name)   
#         self.data.set("DB_PATH", path) 

#         if driver == "sqlite":
#             self.data.set("DB_CONNECTION", "sqlite")

#         elif driver == 'mysql':
#             self.data.set("DB_CONNECTION", "mysql") 
#             self.data.set("DB_HOST", "127.0.0.1") 
#             self.data.set("DB_PORT", "3306") 
#             self.data.set("DB_USERNAME", "root")  
#             self.data.set("DB_PASSWORD", "") 

#         elif driver == 'postgresql':
#             self.data.set("DB_CONNECTION", "pgsql") 
#             self.data.set("DB_HOST", "127.0.0.1") 
#             self.data.set("DB_PORT", "5432") 
#             self.data.set("DB_USERNAME", "postgres")  
#             self.data.set("DB_PASSWORD", "") 

#         elif driver == 'sqlserver':
#             self.data.set("DB_CONNECTION", "sqlsrv") 
#             self.data.set("DB_HOST", "127.0.0.1") 
#             self.data.set("DB_PORT", "1433") 
#             self.data.set("DB_USERNAME", "sa")  
#             self.data.set("DB_PASSWORD", "") 

#         return self
 