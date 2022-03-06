import seleniumManager.instagram_manager as instagram_manager
import seleniumManager.instabot_driver_service as instabot_driver_service
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
import helpers.filehelper as helper
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

TIME_SLEEP = 2

def connect_account_to_instabot():
    global driver
    try:
        driver = instabot_driver_service.init_bot_connection_service()
        time.sleep(2)
        instagram_manager.connect_user(driver)
        textdisplay.display_connection_done()
    except Exception as e:
        print(e)
def disconnect_bot_from_account():
    driver = instabot_driver_service.create_driver_session(getconfig.get_bot_session_id(), getconfig.get_bot_url_executor())
    try:
        time.sleep(2)
        response = helper.delete_folder_contents()
        getconfig.set_bot_status("no")
        textdisplay.display_bot_disconnect()
    except Exception as e:
        print(e)
    finally:
        instagram_manager.quit_selenium()

def get_account_information():
    session_id = getconfig.get_bot_session_id()
    exectutor_url = getconfig.get_bot_url_executor()
    print(session_id)
    driver = instabot_driver_service.create_driver_session(session_id,exectutor_url)
    try:       
        instagram_manager.go_profile(driver)
        publication_number = instagram_manager.get_number_publications(driver)
        follower_number = instagram_manager.get_number_followers(driver)
        subscription_number = instagram_manager.get_number_subscriptions(driver)
        textdisplay.display_account_information(publication_number, follower_number, subscription_number)
    except Exception as e:
        print(e)



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

    for i in range(5):
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

    print("End of instabot work")
  

    
