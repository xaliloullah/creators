from config import database
from utils.creator.src.core import File, Date, Builder
from utils.creator.src.command.terminal import Terminal 


class Migration:
    def __init__(self):
        File.ensure_path_exists(database.migrations['path']) 
        self.table = database.migrations['name']
        self.path = database.migrations['path']  

    def create(self, name):
        try:
            _timestamp = Date.now().strftime("%Y_%m_%d")
            filename = f"{_timestamp}_create_{name}_table.py"
            path = File.join_path(self.path,filename) 
            with open(path, "w") as f:
                f.write(Builder.migration(name))
            Terminal.success(f"Migration {filename} created successfully.")
        except Exception as e:
            Terminal.error(f"{e}") 
            exit()
            
    def run(self, name, action='up'): 
        try:
            path = File.join_path(self.path,name)
            with open(path, 'r') as file:
                code = compile(file.read(), path, 'exec')
                namespace = {}
                exec(code, namespace)
                if action in namespace:
                    namespace[action]()
                else:
                    raise AttributeError(f"{action.capitalize()} function not found in {name}") 
        except Exception as e:
            Terminal.error(f"{e}") 
            exit()

    def get(self):
        try:
            migrations = File.list_dir(self.path, endswith=".py")       
            return sorted(migrations)
        except Exception as e: 
            Terminal.error(f"{e}") 
            exit()
        
    def get_name(self):
        return [File.strip_extension(migration)[0] for migration in self.get()]
        
    def get_last_batch(self): 
        from utils.creator.src.databases.query import DB
        result = DB().select(self.table, 'batch').last().fetchone()
        if result is not None:
            return result['batch']
        else: 
            return 0
    
    def migrate(self, run='up'):
        self.up()  
        from utils.creator.src.databases.query import DB
        alert = {}
        try:
            if run == 'up':
                self.up()  
                applied_migrations = self.check()  
                migrations = self.get()
                if migrations is not None: 
                    migrations
                    batch = self.get_last_batch()+1
                for migration in migrations:
                    if migration not in applied_migrations:  
                        self.run(migration, "up")  
                        Terminal.success(f"Applying migration '{migration}'.") 
                        DB().insert(self.table, migration=migration,batch=batch).execute() 
                        alert = {'info': 'Migrations applied successfully.'}
                    else:
                        alert = {'warning': 'Nothing to migrate...'}
            elif run == 'down':  
                applied_migrations = self.check()  
                migrations = self.get()
                if migrations is not None:
                    migrations.sort(reverse=True)
                    batch = self.get_last_batch()
                for migration in migrations:
                    if migration in applied_migrations: 
                        if DB().select(self.table).where(batch=batch).fetchone(): 
                            self.run(migration, "down")   
                            Terminal.warning(f"Rollback of migration '{migration}'.")
                            DB().delete(self.table).where(migration=migration, batch=batch).execute()  
                            alert = {'info': 'Rollback of migrations executed successfully.'} 
                    else:
                        alert = {'error': 'Migrations was not applied; cannot rollback.'}
            if alert:
                for type, message in alert.items():
                    if type == 'success':
                        Terminal.success(message)
                    elif type == 'warning':
                        Terminal.warning(message)
                    elif type == 'error':
                        Terminal.error(message)
                    elif type == 'info':
                        Terminal.info(message)
                    else:
                        Terminal.error(f"Unknown message type: {type}, Message: {message}")

        except Exception as e:
            Terminal.error(f"{e}") 
            exit()
        

    def check(self): 
        from utils.creator.src.databases.query import DB 
        results = DB().select(self.table, 'migration').get() 
        migrations = self.get()
        applied_migrations = []
        for result in results: 
            if result['migration'] in migrations:
                applied_migrations.append(result['migration'])     
        return applied_migrations


    def up(self):
        from utils.creator.src.databases.schema.table import Table 
        table = Table(self.table) 
        table.id()
        table.string('migration').unique().not_null()
        table.tinyint('batch').default(1) 
        table.create()

    def down(self):
        from utils.creator.src.databases.schema.table import Table 
        table = Table(self.table)
        table.drop()
