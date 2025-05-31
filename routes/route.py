from main import Creator

Creator.route.add("main", Creator.view.extend('app')(
    Creator.view.section('title','Creator')(
        Creator.view.section('content')(
            lambda: Creator.view('pages.main')
            )
        )
    ), "main")

Creator.route.add("dashboard", Creator.view.extend('app')(
    Creator.view.section('title','Creator - Dashboard')(
        Creator.view.section('content')(
            lambda: Creator.view('dashboard')
            )
        )
    ), "dashboard")
# 

# from routes import app
# from routes import auth