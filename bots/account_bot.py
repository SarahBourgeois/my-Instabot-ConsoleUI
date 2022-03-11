# internal 
import selenium_bot_manager.instagram_manager as instagram_manager
import selenium_bot_manager.instabot_driver_service as instabot_driver_service
import selenium_bot_manager.instabot_account_module as account_module
import configuration.getconfig as getconfig
import Ui.console.text_display.pyInquirer as pyInquirer
import Ui.console.text_display.simpleprint as simpleprint
import Ui.console.animations.progress_bar as progress_bar
import Ui.console.constants.launcher_arg as launcher_arg
import helpers.filehelper as helper
import commands.process as process
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# others
from apscheduler.schedulers.blocking import BlockingScheduler
import time 

TIME_SLEEP = 2

def connect_account_to_instabot(driver):
    response = ''
    try:
        response =  account_module.connect_user_to_instabot(driver)
        if (response == True):
            getconfig.set_bot_status("yes")
            time.sleep(5)
            simpleprint.display_connection_done()

        if(response == False):
            simpleprint.display_connection_error()
            getconfig.set_bot_status("no")
            process.kill_webriver_task()
            helper.delete_folder_contents()
            answer = pyInquirer.return_to_menu()
            if(answer == launcher_arg.RETURN_BACK):
                answer = pyInquirer.display_activate_bot()

        time.sleep(8)
    except Exception as e:
        print(e)

def disconnect_bot_from_account():
    try:
        response = helper.delete_folder_contents()
        process.kill_webriver_task()
        getconfig.set_bot_status("no")
        simpleprint.display_bot_disconnect()
        time.sleep(5)
    except Exception as e:
        print(e)
        getconfig.set_bot_status("yes")


def get_account_information(driver):
    try:
        instagram_manager.go_profile(driver)

        publication_number = account_module.get_number_publications(driver)
        follower_number = account_module.get_number_followers(driver)
        subscription_number = account_module.get_number_subscriptions(driver)
        simpleprint.display_account_information(publication_number, follower_number, subscription_number)
        instagram_manager.go_home(driver)
    except Exception as e:
        print(e)