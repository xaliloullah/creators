from main import Creator
from app.models.test import Test 
from utils.creator.src.validators import Rules

class TestController:
    from utils.creator.src.requests.request import Request
     
    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "TEST - INDEX") 
    @Creator.view.section("content")
    def index(): 
        tests = Test().all()
        return Creator.view('pages.test.index', Creator.view.compact(tests=tests))

    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "TEST - CREATE") 
    @Creator.view.section("content")
    def create(): 
        return Creator.view('pages.test.create')

    @staticmethod
    def store(request: Request):  
        if request.validate({
            'name': Rules().required().string().min(3).max(10),  
            'etat': Rules().required().integer(), 
            'details': Rules().string()
        }):
            test = Test()
            test.create(
                name = request['name'],
                etat = request['etat'],
                details = request['details']
            ) 
            
            Creator.request.session.success(Creator.lang.get("success.create", resource="Test"))
            return Creator.route('tests.index') 
        return Creator.view.back()
        
    
    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "TEST - EDIT") 
    @Creator.view.section("content")
    def edit(id):
        test = Test().find(id)
        return Creator.view('pages.test.edit', Creator.view.compact(test=test))

    @staticmethod 
    def update(request: Request, id):
        
        if request.validate({
            'name': Rules().required().string().min(3).max(10),  
            'etat': Rules().required().integer(), 
            'details': Rules().string()
        }): 
            test = Test().find(id)
            if test:
                test.update(
                    name = request['name'],
                    etat = request['etat'],
                    details = request['details']
                ) 
                Creator.request.session.success(Creator.lang.get("success.update", resource="Test"))
                return Creator.route('tests.index')
            Creator.request.session.success(Creator.lang.get("error.update", resource="Test"))
        return Creator.view.back()

    @staticmethod
    @Creator.view.extend("app")
    @Creator.view.section("title", "TEST - SHOW") 
    @Creator.view.section("content")
    def show(id):
        test = Test().find(id) 
        return Creator.view('pages.test.view', Creator.view.compact(test=test))


    @staticmethod
    def destroy(id):
        test = Test().find(id) 
        if test:
            test.delete() 
            Creator.request.session.success(Creator.lang.get("success.delete", resource="Test"))
        else:
            Creator.request.session.error(Creator.lang.get("error.delete", resource="Test"))
        return Creator.view.back() 
    