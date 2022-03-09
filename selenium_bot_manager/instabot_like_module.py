# internal
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

def like_publication(driver):
    time.sleep(2)
    like_element = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]')
    like_element.click()
    print("like publication is ok")

# TODO 
# check if a publication is already like or not 

