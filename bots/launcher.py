# internal 
import selenium_bot_manager.instagram_manager as instagram_manager
import selenium_bot_manager.instabot_driver_service as instabot_driver_service
import selenium_bot_manager.instabot_account_module as account_module
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
import helpers.filehelper as helper
import bots.account_bot as account_bot
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

def connect_account_to_instabot():
    driver = instabot_driver_service.init_bot_connection_service()
    time.sleep(2)
    account_bot.connect_account_to_instabot(driver)
   
def disconnect_bot_from_account():
    account_bot.disconnect_bot_from_account()

def get_account_information():
    session_id = getconfig.get_bot_session_id()
    exectutor_url = getconfig.get_bot_url_executor()
    print(session_id)
    driver = instabot_driver_service.create_driver_session(session_id,exectutor_url)
    print("get account_info is running...")
    account_bot.get_account_information(driver)


def launch_liker_module():
    print("like_module is running...")





def launch_instagram_bot():
    session_id = getconfig.get_bot_session_id()
    exectutor_url = getconfig.get_bot_url_executor()
    driver = instabot_driver_service.create_driver_session(session_id,exectutor_url)
    first_open = True
    # init service
    time.sleep(4)
    # search general element
    searchBox = instagram_manager.select_search_box(driver)
    # write text in search box
    box = instagram_manager.write_and_push_text(driver, searchBox, 'beany_artworks')
    time.sleep(4)
    # open publication
    instagram_manager.open_publication(driver)

    for i in range(1):
        # like publication 
        if(getconfig.get_automatic_like_authorization() == True):
            instagram_manager.like_publication(driver)
            time.sleep(5)
        else :
           print("Automatic like is disable")
        # check if you already follow
        instagram_manager.is_already_follow(driver)
        # follow 
        instagram_manager.follow(driver)
        time.sleep(5)

        if(first_open == True):
            instagram_manager.next_page(driver)
        else:
            instagram_manager.next_pageafter(driver)
            
        first_open = False
    instagram_manager.close_publication_page(driver)
    print("End of instabot work")
  

    
