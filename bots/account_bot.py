# internal 
import selenium_bot_manager.instagram_manager as instagram_manager
import selenium_bot_manager.instabot_driver_service as instabot_driver_service
import selenium_bot_manager.instabot_account_module as account_module
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
import helpers.filehelper as helper
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
    try:
        account_module.connect_user_to_instabot(driver)
        textdisplay.display_connection_done()
        getconfig.set_bot_status("yes")
    except Exception as e:
        print(e)
        getconfig.set_bot_status("no")

def disconnect_bot_from_account():
    try:
        response = helper.delete_folder_contents()
        getconfig.set_bot_status("no")
        textdisplay.display_bot_disconnect()
    except Exception as e:
        print(e)
        getconfig.set_bot_status("yes")


def get_account_information(driver):
    try:
        instagram_manager.go_profile(driver)

        publication_number = account_module.get_number_publications(driver)
        follower_number = account_module.get_number_followers(driver)
        subscription_number = account_module.get_number_subscriptions(driver)
        textdisplay.display_account_information(publication_number, follower_number, subscription_number)
        instagram_manager.go_home(driver)
    except Exception as e:
        print(e)