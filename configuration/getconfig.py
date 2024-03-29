from configparser import ConfigParser
from configparser import SafeConfigParser
import os
import selenium_bot_manager.instagram_manager as instagram_manager
import Ui.console.constants.module as module_const

def read_config():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config.ini')
    config = SafeConfigParser()
    config.read(initfile)
    return config

###########################
# ACCOUNT CONFIG
##########################

# get the login of the user
def get_login():
    return config.get('BOT_STATUS', 'connected_account')

# password must be renseign
def get_password():
    return config.get('ACCOUNT', 'password')

def set_login(login):
    config.set('BOT_STATUS', 'connected_account', login)    
    # save the file
    write_config()

###########################
# LIKE_SECTION CONFIG
##########################

# check if like_module is authorize
def get_automatic_like_authorization(): 
    option = config.get('LIKE_SECTION', 'automatic_like')
    if(option == "yes"):
        return True
    else:
        return False

###########################
# HYBRID_MODULE
##########################
# check if hybrid module is authorize
def automatic_hybrid_authorization(): 
    option = config.get('HYBRID_SECTION', 'automatic_hybrid')
    if(option == "yes"):
        return True
    else:
        return False


###########################
# COMMON
##########################
def get_hashtag(module):
    if(module == module_const.HYBRID_MODULE):
        return config.get('HYBRID_SECTION', 'hashtags')

def set_module_activation(choice, module):
    if(module == module_const.HYBRID_MODULE):
        choice_activation = str(choice[0])
        config.set('HYBRID_SECTION', 'automatic_hybrid', choice[0])
    if(module == module_const.FOLLOW_MODULE):
        choice_activation = str(choice[0])
        config.set('FOLLOW_SECTION', 'automatic_follow', choice[0])
    write_config()

def set_module_speed(choice, module):
    if(module == module_const.HYBRID_MODULE):
        choice_speed = str(choice[1])
        config.set('HYBRID_SECTION', 'speed', choice[1])
    write_config()

def set_hashtag(choice, module):
    if(module == module_const.HYBRID_MODULE):
        config.set('HYBRID_SECTION', 'hashtags', choice)
    write_config()




###########################
# UNFOLLOW_SECTION CONFIG
##########################

def get_unfollow_module_authorization():
    option = config.get('UNFOLLOW_SECTION', 'automatic_unfollow')
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

# check if the bot is link to the user account or not (retated to its specific sessionId)
def get_bot_is_activate():
    option = config.get('BOT_STATUS', 'is_activate')
    if(option == "yes"):
        return True
    else:
        return False

# set the bot status (activate/desactivate)
def set_bot_status(status):
    config.set('BOT_STATUS', 'is_activate', status)    
    # save the file
    write_config()

# set the sessionId to use the same session and identify the user
def set_bot_session_id(session_id):
    config.set('BOT_STATUS', 'session_id', session_id)
    write_config()

# get the sessionId of the current user bot
def get_bot_session_id():
    return config.get('BOT_STATUS', 'session_id')

# set the localhost url of the bot
def set_bot_executor_url(executor_url):
    config.set('BOT_STATUS', 'executor_url', executor_url)
    write_config()

# get the localhost url of the bot
def get_bot_url_executor():
    return config.get('BOT_STATUS', 'executor_url')


config = read_config()


