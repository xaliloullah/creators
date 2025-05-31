from main import Creator
from app.controllers.auth.LoginController import LoginController 
from app.controllers.auth.RegisterController import RegisterController


Creator.route.add('/login', LoginController.create,'login')
Creator.route.add('/login/store', LoginController.store,'login.store')
Creator.route.add('/register', RegisterController.create,'register')
Creator.route.add('/register/store', RegisterController.store,'register.store')