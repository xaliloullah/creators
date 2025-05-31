def default():
    code = f"""from main import Creator
"""
    return code


def app():
    code=f"""from main import Creator
    
Creator.terminal.clear()  

Creator.view.include('includes.header') 

Creator.view.include('components.alert') 
 
Creator.view.generate("content") 

Creator.view.include('includes.footer') 
""" 
    return code

def main(auth=False):
    code=f"""from main import Creator

Creator.terminal.subtitle(Creator.lang.get("messages.welcome", app="Creator"))
"""
    if auth:
        code+="""
option = Creator.terminal.input("option", options={"1":"Connection", "2":"Inscription", "0":" Quitter"})
if option == "1":
    Creator.route("login") 
elif option == "2":
    Creator.route("register") 
elif option == "0":
    Creator.terminal.clear()
    Creator.terminal.comment(Creator.lang.get("messages.goodbye"))
    exit() 
"""
    else:
        code+="""
option = Creator.terminal.input("option", options={"0":" Quitter"})
if option == "0":
    Creator.terminal.clear()
    Creator.terminal.comment(Creator.lang.get("messages.goodbye"))
    exit() 
"""
    return code 

def dashboard():
    code=f"""from main import Creator

"""
    return code