# Internal Selenium module
import selenium_bot_manager.instabot_unfollow_module as unfollow_module
import selenium_bot_manager.instagram_manager as common_module
# Internal other
import helpers.filehelper as helper
import Ui.console.text_display.simpleprint as simpleprint
import configuration.getconfig as getconfig
# external other
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def unfollow_people(driver):
    print("starting to unfollow")
    content = helper.get_file_content()
    for user_to_unfollow in content:
        if(user_to_unfollow != ''):
            response =  unfollow_module.unfollow_from_list(driver, user_to_unfollow)
            if(response == True):
            helper.delete_user(user_to_unfollow)
            common_module.go_home(driver)


