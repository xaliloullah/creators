from utils.creator.src.environment import env
 

name = 'sessions'
driver = env('SESSION_DRIVER', 'file')
lifetime = env('SESSION_LIFETIME', 30)
expire_on_close = env('SESSION_EXPIRE_ON_CLOSE', True)
encrypt = env('SESSION_ENCRYPT', True)
path = f"sessions/{env('APP_NAME', 'creator')}"