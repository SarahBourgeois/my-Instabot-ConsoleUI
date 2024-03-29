# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3, custom_style_2
from pprint import pprint
from PyInquirer import prompt, Separator
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.text_display.asciitext as asciitext
import Ui.console.text_display.config.pyInquirer_configuration as ui_configuration
import configuration.getconfig as getconfig
import commands.terminal as terminal_command
import Ui.console.constants.module as module_const
import Ui.console.constants.hashtags_actions as hashtag_const
# system
import sys

def launch_configuration():
    terminal_command.clear()
    print("\n")
    print("\n")
    asciitext.display_configuration()
    print("\n")
    display_readme_helper()
    module_choice = ui_configuration.choose_module_configure()
    terminal_command.clear()
    manage_options(module_choice)

def display_readme_helper():
    print(Fore.LIGHTMAGENTA_EX)
    print("Si tu n'as jamais configuré ton Instabot avant, ")
    print("Vas sur la documentation officielle pour les tips :" + Fore.LIGHTYELLOW_EX, "wwww.my-instabot.com/documentation")
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

def module_activation_speed():     
    choice = ui_configuration.module_activation_speed()
    # register all options
    getconfig.set_module_activation(choice, module_const.HYBRID_MODULE)
    getconfig.set_module_speed(choice, module_const.HYBRID_MODULE)

def hashtag_choice(module, isRestart):
    if (isRestart == False):
        print(Fore.MAGENTA)
        print("Hashtags Configuration \n")
    
    exist_hashtag = getconfig.get_hashtag(module)

    if(exist_hashtag != "" and isRestart == False):
        print(Fore.YELLOW, "Tu as déjà configuré des Hashtags cibles : \n.")
        print(Fore.RED, exist_hashtag, Fore.YELLOW)
        print("\n" + "Que veux-tu faire ?", Fore.WHITE)
        choice =  ui_configuration.hastags_choice_options()
        manage_hastag_choice(choice, exist_hashtag, module)
    
    if(exist_hashtag != "" and isRestart == True):
        choice =  ui_configuration.hastags_choice_options()
        manage_hastag_choice(choice, exist_hashtag, module)


    else:
        ui_configuration.enter_hashtags()
        getconfig.set_hashtag(choice, module)


def manage_hastag_choice(choice, exist_hashtag, module):
    if (choice == hashtag_const.HASHTAGS_ADD_NEW):
        new_hashtag = ui_configuration.enter_hashtags()
        hashtag = exist_hashtag + " " + new_hashtag
        getconfig.set_hashtag(hashtag, module)
        terminal_command.clear()
        print(Fore.GREEN, "Les hashtags suivants ont bien été ajoutés : " + new_hashtag, Fore.WHITE)
        print(Fore.WHITE, "\n Tu veux modifier de nouveau les Hashtags ?")
        hashtag_choice(module_const.HYBRID_MODULE, True)
    
    if (choice == hashtag_const.HASHTAGS_FINISH_EXIT):
        terminal_command.clear()
        print(Fore.GREEN, " \n Cette configuration de module est fini ! \n", Fore.WHITE)
        isContinue = ui_configuration.is_want_new_config()
        print(isContinue)
        if(isContinue == "Oui"):
            terminal_command.clear()
            module_choice = ui_configuration.choose_module_configure()
            manage_options(module_choice)
        else:
            return


def manage_options(choice):
    #terminal_command.clear()
    if(choice == module_const.HYBRID_MODULE):
        module_activation_speed()
        hashtag_choice(module_const.HYBRID_MODULE, False)

