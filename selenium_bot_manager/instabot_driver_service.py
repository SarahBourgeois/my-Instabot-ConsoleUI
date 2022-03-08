import helpers.filehelper as filehelper
import configuration.getconfig as getconfig
import Ui.console.textdisplay as textdisplay
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Allow to init instance of chrome selenium driver
# and reuse the instance until we don't close thanks
# to a sessionId and the executor Url 

silencer = True
driver = webdriver

def init_bot_connection_service():
    global driver
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    if(silencer == True):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument('--user-data-dir=./User_Data')

    # Pass the argument 1 to allow and 2 to block notifications
    chrome_options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 1 
    })
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    getconfig.set_bot_session_id(driver.session_id)
    getconfig.set_bot_executor_url(driver.command_executor._url)
    driver.get("https://instagram.com")
    return driver


def create_driver_session(session_id, executor_url):
    global driver

    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute
    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id
    getconfig.set_bot_session_id(new_driver.session_id)
    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute
    return new_driver

