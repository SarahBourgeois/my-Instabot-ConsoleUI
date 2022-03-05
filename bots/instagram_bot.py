import seleniumManager.instagram_manager as instagram_manager
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
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
SILENCER = False

def connect_account_to_instabot():
    try:
        instagram_manager.init_service(SILENCER)
        time.sleep(2)
        instagram_manager.connect_user()
        textdisplay.display_connection_done()
    except Exception as e:
        print(e)

def get_account_information():
    try:       
        instagram_manager.init_service(SILENCER)
        instagram_manager.go_profile()
        publication_number = instagram_manager.get_number_publications()
        follower_number = instagram_manager.get_number_followers()
        subscription_number = instagram_manager.get_number_subscriptions()
        textdisplay.display_account_information(publication_number, follower_number, subscription_number)

    except Exception as e:
        print(e)

def launch_instagram_bot():
    first_open = True
    # init service
    instagram_manager.init_service(SILENCER)
    time.sleep(4)
    # search general element
    searchBox = instagram_manager.select_search_box()
    # write text in search box
    box = instagram_manager.write_and_push_text(searchBox, 'beany_artworks')
    time.sleep(4)
    # open publication
    instagram_manager.open_publication()

    for i in range(5):
        # like publication 
        if(getconfig.get_automatic_like_authorization() == True):
            instagram_manager.like_publication()
            time.sleep(5)
        else :
           print("Automatic like is disable")
        # check if you already follow
        instagram_manager.is_already_follow()
        # follow 
        instagram_manager.follow()
        time.sleep(5)

        if(first_open == True):
            instagram_manager.next_page()
        else:
            instagram_manager.next_pageafter()
            
        first_open = False

    print("End of instabot work")
    instagram_manager.quit_selenium()
  

    
