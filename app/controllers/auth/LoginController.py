from main import Creator  

from app.models.user import User
from utils.creator.src.validators import Rules

class LoginController:
    from utils.creator.src.requests.request import Request

    @staticmethod
    def index():
        #
        return

    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "LOGIN") 
    @Creator.view.section("content")
    def create():
        #
        return Creator.view("auth.login")

    @staticmethod
    def store(request: Request):
        validate = request.validate({
            # 'email': ["required","email"], #"unique:users"
            'name': Rules().required().string(),  
            'password': Rules().required().string()
        })    
        user = User().where(name=request['name']).first()
        if validate:
            if Creator.auth().authenticate(user):
                request.session.success(Creator.lang.get('auth.succeeded'))
                return Creator.route('dashboard')
            else:
                request.session.error(Creator.lang.get('auth.failed'))  
        
        return Creator.view.back()
    
    @staticmethod
    def edit(id):
        #
        return

    @staticmethod
    def update(request: Request, id):
        #
        return

    @staticmethod
    def show(id):
        #
        return

    @staticmethod
    def destroy(id):
        #
        return
    