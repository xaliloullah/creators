from utils.creator.src.environment import env


name = env('APP_NAME', 'creator')
url = env("APP_URL",'http://localhost')
lang = env("APP_LANG",'en')
key = env("APP_KEY", None)
debug = env("APP_DEBUG", False) 