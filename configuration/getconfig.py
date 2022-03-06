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

###########################
# ACCOUNT CONFIG
##########################
def get_login():
    return config.get('ACCOUNT', 'login')

def get_password():
    return config.get('ACCOUNT', 'password')


###########################
# LIKE_SECTION CONFIG
##########################
def get_automatic_like_authorization(): 
    option = config.get('LIKE_SECTION', 'automatic_like')
    if(option == "yes"):
        return True
    else:
        return False


###########################
# BOT_STATUS CONFIG
##########################
def write_config():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config.ini')
    with open(initfile, 'w') as configfile:
        config.write(configfile)

def get_bot_is_activate():
    option = config.get('BOT_STATUS', 'is_activate')
    if(option == "yes"):
        return True
    else:
        return False

def set_bot_status(status):
    config.set('BOT_STATUS', 'is_activate', status)    
    # save the file
    write_config()

def set_bot_session_id(session_id):
    config.set('BOT_STATUS', 'session_id', session_id)
    write_config()

def set_bot_executor_url(executor_url):
    config.set('BOT_STATUS', 'executor_url', executor_url)
    write_config()



def get_bot_session_id():
    return config.get('BOT_STATUS', 'session_id')

def get_bot_url_executor():
    return config.get('BOT_STATUS', 'executor_url')




config = read_config()


