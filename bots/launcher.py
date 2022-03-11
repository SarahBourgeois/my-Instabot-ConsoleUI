# internal
import selenium_bot_manager.instagram_manager as instagram_manager
import selenium_bot_manager.instabot_driver_service as instabot_driver_service
import bots.hybrid_bot as hybrid_bot
import bots.account_bot as account_bot
import bots.unfollow_bot as unfollow_bot
import configuration.getconfig as getconfig
import Ui.console.text_display.simpleprint as simpleprint
import Ui.console.text_display.pyInquirer as pyInquirer_text
import Ui.console.animations.show_spinner as show_spinner
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
# scheduler
from apscheduler.schedulers.blocking import BlockingScheduler
# system
import time


def return_session_driver():
    session_id = getconfig.get_bot_session_id()
    exectutor_url = getconfig.get_bot_url_executor()
    return instabot_driver_service.create_driver_session(session_id,exectutor_url)

# Connect the instabot to the user account
def connect_account_to_instabot():
    driver = instabot_driver_service.init_bot_connection_service()
    time.sleep(2)
    print("\n")
    account_bot.connect_account_to_instabot(driver)

# disconnect the instabot from the user account
def disconnect_bot_from_account():
    try:
        print("\n")
        show_spinner.launch("begin disconnect bot from your account...")
        account_bot.disconnect_bot_from_account()
    except Exception as e:
        print(e)

# get all account information
def get_account_information():
    try:
        print("Getting information about your account...")
        driver = return_session_driver()
        account_bot.get_account_information(driver)
    except Exception as e:
        print(e)

# MODULE LIKE_SECTION : launch the module for automatic like
def launch_liker_module():
    print("LIKE_MODULE is running...")

# MODULE FOLLOWER_SECTION : launch the module to automatic follow
def launch_follower_module():
    print("FOLLOWER_MODULE is running...")
    time.sleep(5)

# MODULE HYBRYD_SECTION : launch the module to automatic like and follow
def launch_follower_and_liker_module():
    print("HYBRID_MODULE is running.")
    driver = return_session_driver()
    hybrid_bot.like_follow(driver)

# MODULE UNFOLLOW_SECTION : launch the module to unfollow followed people with the instabot
def launch_unfollow_module():
    print("UNFOLLOW_MODULE is running...")
    driver = return_session_driver()
    is_module_unfollow_activated = getconfig.get_unfollow_module_authorization()
    if(is_module_unfollow_activated == True):
        unfollow_bot.unfollow_people(driver)


