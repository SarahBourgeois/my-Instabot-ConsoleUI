import time
import sys
import os

def kill_webriver_task():
    try:
        if os.name =="nt":
            os.system("cls")   
        # for linux / Mac OS
        else:
            os.system("killall chromedriver")
    except Exception:
        print("error : can't kill webdriver task")
    finally:
        print("webdriver is remove")

  