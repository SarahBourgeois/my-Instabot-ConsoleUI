# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.text_display.asciitext as asciitext
import configuration.getconfig as getconfig

def launch():
    print("\n")
    print("\n")
    asciitext.display_configuration()
    print("\n")
    display_readme_helper()
    manage_options()
    
def display_readme_helper():
    print(Fore.LIGHTMAGENTA_EX)
    print("If you never configure Instabot before, ")
    print("Please open the documentation page on :" + Fore.LIGHTYELLOW_EX, "wwww.my-instabot.com/documentation")
    print(Fore.WHITE)


def bot_status():
    status = ""
    botstatus = getconfig.get_bot_is_activate()
    if (botstatus == True):
        status = "yes"
    else:
        status = "no" 
    
    print(Fore.LIGHTYELLOW_EX)
    print("[BOT_STATUS]", Fore.WHITE)
    print("is activate : ", Fore.LIGHTMAGENTA_EX, status, Fore.WHITE)
    print("connected user : " , Fore.LIGHTMAGENTA_EX, getconfig.get_login())
    print("\n")

def hybrid_module():
    print(Fore.LIGHTYELLOW_EX)
    print("[HYBRID_SECTION]", Fore.WHITE)



def manage_options():
    bot_status()