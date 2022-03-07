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
import time
import re


def select_search_box(driver):
    input_box_searchContact = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')
    input_box_searchContact.click()
    print("search box ok")
    return input_box_searchContact

def select_second_search_box(driver):
    input_box_searchContact = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    input_box_searchContact.click()
    return input_box_searchContact

def write_and_push_text(driver, contentBoxToApply, wordToWrite):
    box = select_second_search_box(driver)
    box.click()
    box.send_keys(wordToWrite)
    time.sleep(2)
    selected_contact = driver.find_element(by=By.XPATH, value="//input[@value='"+wordToWrite+"']")
    selected_contact.send_keys(Keys.ENTER)
    selected_contact.send_keys(Keys.ENTER)
    print("write and push ok")
    return selected_contact


def open_publication(driver):
    pic = driver.find_element_by_class_name("kIKUG")  
    pic.click()   # clicks on the first picture
    print("Publication is open")



def close_publication_page(driver):
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/div').click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/div/div/div/button[3]').click()



def next_page(driver):
    next_page_input = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[2]/div/div/button')
    next_page_input.send_keys(Keys.ENTER)

def next_pageafter(driver):
    next_pageafter = ' /html/body/div[6]/div[2]/div/div[2]/button'      
    next_page_input = driver.find_element(by=By.XPATH, value=next_pageafter)
    next_page_input.send_keys(Keys.ENTER)

def go_profile(driver):
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
    time.sleep(2)

def go_home(driver):
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div').click()

def quit_selenium():
    webdriver.Chrome().quit()
                              




