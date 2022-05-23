import time
import sys
import os
import subprocess
import shlex

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

  

#id_cmd='xdotool getactivewindow'
#resize_cmd='xdotool windowsize --usehints {id} 100 30'

#proc=subprocess.Popen(shlex.split(id_cmd),stdout=subprocess.PIPE)
#windowid,err=proc.communicate()
#proc=subprocess.Popen(shlex.split(resize_cmd.format(id=windowid)))
#proc.communicate()