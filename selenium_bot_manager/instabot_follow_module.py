# internal
import selenium_bot_manager.instagram_manager as common_module
import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.text_display.simpleprint as simpleprint
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
# system
import time
import re

def is_already_follow(driver):
    try: 
        is_follow_input = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").get_attribute("innerHTML")
        pattern = "\">(.*?)\</d"
        follow_response = re.search(pattern, is_follow_input).group(1)
        if(follow_response == 'Abonné(e)'):
           return True
        else:
            return False
    except:
        print("Can't know if already follow or not")


def get_followed_person_name(driver):
    return driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text

def follow(driver):
    follow_element = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div')
    follow_element.click()

