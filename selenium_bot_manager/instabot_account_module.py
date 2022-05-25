# internal
import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.text_display.simpleprint as simpleprint
import Ui.console.text_display.pyInquirer as pyInquirer_text
import Ui.console.text_display.asciitext as ascciitext

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import configuration.getconfig as config
import time

def connect_user_to_instabot(driver):
    ascciitext.display_connection2()
    try:
        # accept cookies
        driver.find_element(by=By.XPATH, value ='/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        # login
        login = pyInquirer_text.ask_login()
        user = driver.find_element_by_xpath("//input[@name='username']")
        user.send_keys(login)
        config.set_login(login)
        # password
        password = pyInquirer_text.ask_password()
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        # click connect button
        driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
        simpleprint.display_processing()
        time.sleep(4)
        # click register login/pwd 
        registelogin_input = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        registelogin_input.click()
        time.sleep(5)
        return True
    except Exception as e:
        print(e)
        config.set_login('')
        return False
        

def get_number_publications(driver):
    time.sleep(2)
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/div/span').text
# already copy paste
def get_number_followers(driver):
    time.sleep(2)
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').text
# already copy paste
def get_number_subscriptions(driver):
    time.sleep(2)
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div/span').text
