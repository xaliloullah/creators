from main import Creator   
from utils.creator.src.validators import Rules
from app.models.user import User

class RegisterController:
    from utils.creator.src.requests.request import Request

    
    @staticmethod
    def index():
        #
        return

    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "REGISTER") 
    @Creator.view.section("content")
    def create():
        #
        return Creator.view("auth.register")

    @staticmethod
    def store(request: Request):
        if request.validate({
            'name': Rules().required().string().min(3).max(50).unique('users'),  
            'email': Rules().required().email().unique('users'),  
            'password': Rules().password()
        }):
            user = User()
            user.create(
                name = request['name'],
                email = request['email'],
                password = Creator.hash.make(request['password'])
            ) 
            Creator.auth().authenticate(user)
            Creator.request.session.success(Creator.lang.get('auth.succeeded'))
            return Creator.route('dashboard')
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
        user = User().find(id) 
        user.delete() 
    
        Creator.request.session.success("Supprimer avec succees")
        return Creator.view.back() 
    