from main import Creator  
from app.models.user import User

class Auth:
    def __init__(self): 
        self._user_:User

    def authenticate(self, user): 
        if user:
            if Creator.hash.check(Creator.request['password'], user["password"]):
                Creator.request.session.set("user_id", user["id"])
                Creator.request.session.update()
                self._user_ = user
        return self.check()


    def check(self):
        return bool(self._user_)
    

    def user(self):
        return self._user_
    


