import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
import selenium_bot_manager.instagram_manager as common_module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import re


def unfollow_from_list(driver, user_to_unfollow):
    common_module.select_search_box(driver)
    select_search_box = common_module.select_second_search_box(driver)
    time.sleep(2)
    common_module.write_and_push_text(driver, select_search_box, user_to_unfollow)
    time.sleep(4)
    unfollow_button = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[2]/div/span/span[1]/button')
    unfollow_button.click()
    time.sleep(2)
    confirm = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[3]/button[1]')
    confirm.click()
    time.sleep(2)
