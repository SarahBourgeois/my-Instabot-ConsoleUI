from configparser import ConfigParser
from configparser import SafeConfigParser
import os
import seleniumManager.instagram_manager as instagram_manager

def read_config():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config.ini')
    config = SafeConfigParser()
    config.read(initfile)
    return config

def get_login():
    return config.get('ACCOUNT', 'login')

def get_password():
    return config.get('ACCOUNT', 'password')

def get_automatic_like_authorization(): 
    option = config.get('LIKE_SECTION', 'automatic_like')
    if(option == "yes"):
        return True
    else:
        return False

def get_bot_is_activate():
    option = config.get('BOT_STATUS', 'is_activate')
    if(option == "yes"):
        return True
    else:
        return False

def set_bot_status(status):
    config.set('BOT_STATUS', 'is_activate', status)    
    # save the file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config.ini')
    with open(initfile, 'w') as configfile:
        config.write(configfile)


config = read_config()

