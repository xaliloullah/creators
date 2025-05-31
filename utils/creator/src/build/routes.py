def default():
    code = f"""from main import Creator
# 

""" 
    return code


def main():
    code=f"""from main import Creator

Creator.route.add("main", Creator.view.extend('app')(
Creator.view.section('title', 'Creator')(
    Creator.view.section('content')(
        lambda: Creator.view('pages.main')
        )
    )
), "main")
"""
    return code