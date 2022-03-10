# internal
import selenium_bot_manager.instagram_manager as instagram_manager
import selenium_bot_manager.instabot_driver_service as instabot_driver_service
import selenium_bot_manager.instabot_follow_module as follow_module
import selenium_bot_manager.instabot_like_module as like_module
import configuration.getconfig as getconfig
import Ui.console.text_display.simpleprint as simpleprint
import helpers.filehelper as helper
# Selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# sceduler : 
from apscheduler.schedulers.blocking import BlockingScheduler
# system
import time

def like_follow(driver):
    first_open = True
    time.sleep(4)
    # open profile 
    searchBox = instagram_manager.select_search_box(driver)
    box = instagram_manager.write_and_push_text(driver, searchBox, '#followforfollow')
    time.sleep(4)
    # open publication
    instagram_manager.open_publication(driver)
    time.sleep(2)
    for i in range(10):
        # like publication 
        if(getconfig.get_automatic_like_authorization() == True):
            like_module.like_publication(driver)
            time.sleep(5)
        else :
           print("Automatic like is disable")

        # check if you already follow user. If not, follow
        is_follow = follow_module.is_already_follow(driver)
        if(is_follow == False):
            follow_module.follow(driver)
            name = follow_module.get_followed_person_name(driver)
            helper.registerData(name)
            time.sleep(5)

        if(first_open == True):
            instagram_manager.next_page(driver)
        if(first_open == False):
            instagram_manager.next_pageafter(driver)
        first_open = False

            
    time.sleep(2)
    instagram_manager.close_publication_page(driver)
    time.sleep(2)
    instagram_manager.go_home(driver)

    print("End of instabot work")
  