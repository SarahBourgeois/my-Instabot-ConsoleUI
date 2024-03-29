# internal
import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.text_display.simpleprint as simpleprint
import selenium_bot_manager.instagram_manager as common_module
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# system
import time
import re


def unfollow_from_list(driver, user_to_unfollow):
    try: 
        common_module.select_search_box(driver)
        select_search_box = common_module.select_second_search_box(driver)
        time.sleep(2)
        common_module.write_and_push_text(driver, select_search_box, user_to_unfollow)
        time.sleep(4)
        unfollow_button = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[2]/div/span/span[1]').click()
        time.sleep(2)
        confirm = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[3]/button[1]')
        confirm.click()
        time.sleep(2)
        return True
    except Exception:
        print("An error occur during the Unfollow process.")
        return False
