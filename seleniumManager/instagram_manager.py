import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import time
import re

driver = webdriver
is_follow = False
silencer = False

def init_service():
    global driver
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    print(silencer)
    if (silencer == True):
        chrome_options.add_argument("--headless")

    chrome_options.add_argument('--user-data-dir=./User_Data')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block notifications
    chrome_options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 1 
    })
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.get("https://instagram.com")
    driver.get_screenshot_as_file("screenshot.png")
    return driver


def connect_user():
    try:
        # accept cookies
        driver.find_element(by=By.XPATH, value ='/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        # login
        login = getconfig.get_login()
        user = driver.find_element_by_xpath("//input[@name='username']")
        user.send_keys(login)
        # password
        password = textdisplay.ask_password(login)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        # click connect button
        driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(4)
        # click register login/pwd 
        registelogin_input = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        registelogin_input.click()
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def select_search_box():
    input_box_searchContact = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')
    input_box_searchContact.click()
    return input_box_searchContact

def select_second_search_box():
    input_box_searchContact = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    input_box_searchContact.click()
    return input_box_searchContact

def write_and_push_text(contentBoxToApply, wordToWrite):
    box = select_second_search_box()
    box.click()
    box.send_keys(wordToWrite)
    time.sleep(2)
    selected_contact = driver.find_element(by=By.XPATH, value="//input[@value='"+wordToWrite+"']")
    selected_contact.send_keys(Keys.ENTER)
    selected_contact.send_keys(Keys.ENTER)
    return selected_contact


def open_publication():
    pic = driver.find_element_by_class_name("kIKUG")  
    pic.click()   # clicks on the first picture
        
def like_publication():
    time.sleep(2)
    like_element = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]')
    like_element.click()

def is_already_follow():
    try: 
        global is_follow
        is_follow_input = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").get_attribute("innerHTML")
        pattern = "\">(.*?)\</d"
        follow_response = re.search(pattern, is_follow_input).group(1)
        if(follow_response == 'Abonné(e)'):
            is_follow = True
        else:
            is_follow = False
    except:
        print("Can't know if already follow or not")

def register_followed_person():
    follow = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text
    sliced_follow = follow[2:]
    print(sliced_follow)
    filehelper.registerData(sliced_follow)

def follow():
    if(is_follow == False):
        follow_element = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div')
        follow_element.click()
        register_followed_person()

def next_page():
    next_page_input = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[2]/div/div/button')
    next_page_input.send_keys(Keys.ENTER)

def next_pageafter():
    next_pageafter = ' /html/body/div[6]/div[2]/div/div[2]/button'      
    next_page_input = driver.find_element(by=By.XPATH, value=next_pageafter)
    next_page_input.send_keys(Keys.ENTER)

def go_profile():
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
    time.sleep(2)

def get_number_publications():
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/div/span').text

def get_number_followers():
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').text

def get_number_subscriptions():
    return driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div/span').text

                                     
def quit_selenium():
    quit
    print("quit")





