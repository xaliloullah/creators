from main import Creator
from app.controllers.TestController import TestController  

Creator.route.resource("tests", TestController)

 