from utils.creator.src.build import assets, controllers, env, middlewares, migrations, models, routes, views
class Builder:

    @staticmethod
    def creator():
        return assets.creator() 

    @staticmethod
    def model(name: str, table: str):
        return models.model(name, table)
    
    
    @staticmethod
    def controller(name: str, model, resource: bool):
        return controllers.controller(name, model, resource)


    @staticmethod
    def migration(name: str):
        return migrations.migration(name)
    
    @staticmethod
    def middleware(name: str, table: str):
        return middlewares.middleware(name, table)
    
    
    def env(**kwargs):
        app_name = kwargs.get("app_name", "creator")
        app_key = kwargs.get("app_key", False)
        app_lang = kwargs.get("app_lang", "en")
        app_debug = kwargs.get("debug", False)

        db_name = kwargs.get("db_name", app_name)
        db_path = kwargs.get("db_path", "database")
        db_driver = kwargs.get("db_driver", "sqlite")

        session_name = kwargs.get("session_name", f"{app_name}_session")
        session_driver = kwargs.get("session_driver", "file")
        session_lifetime = kwargs.get("session_lifetime", 30)
        
        code= env.app(app_name, app_lang, app_debug, app_key)
        code+= env.session(session_name, session_driver, session_lifetime) 
        code+= env.database(db_name, db_path, db_driver)
        return code
    
    
    @staticmethod
    def view(view=None):
        if view == 'app':
            return views.app()
        elif view == 'main':
            return views.main()
        elif view == 'dashboard':
            return views.dashboard()
        else:
            return views.default()
    
    @staticmethod
    def route(route=None):
        if route == 'main':
            return routes.main()
        else:
            return routes.default()