# (c) Code-x-Mania
import os
from os import getenv, environ
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')


class Var(object):
    API_ID = int(getenv('API_ID' '11482890'))
    API_HASH = str(getenv('API_HASH' 'c034759952399cc34bd31e87bea8cb8b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'filetolinkprobot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL' '-1001976413677'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "878334582").split())  
    #OWNER_ID=int(getenv('OWNER_ID'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME' 'dryland21'))
    A_G = str(getenv('A_G'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL' 'mongodb+srv://techiboyllcapp:user2@cluster0.jht0xkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
