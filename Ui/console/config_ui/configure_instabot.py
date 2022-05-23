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
import Ui.console.text_display.pyInquirer as pyInquirer
import configuration.getconfig as getconfig
import commands.terminal as terminal_command
import Ui.console.constants.module as module_const
import Ui.console.constants.hashtags_actions as hashtag_const
# system
import sys

def launch():
    terminal_command.clear()
    print("\n")
    print("\n")
    asciitext.display_configuration()
    print("\n")
    display_readme_helper()
    module_choice = pyInquirer.choose_module_configure()
    manage_options(module_choice)

    
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
    checked  = ""
    hybrid = ""
    automatic_hybrid = getconfig.automatic_hybrid_authorization()
    if (automatic_hybrid == True):
        hybrid = "no"
        checked = "yes"
    else:
        hybrid = "yes"
        checked = "no"

    print(Fore.LIGHTYELLOW_EX)
    print("[HYBRID_SECTION]", Fore.WHITE)
    questions = [ 
            {
                'type': 'checkbox',
                'message': 'Select choice',
                'name': 'is_active',
                'choices': [ 
                        Separator('==== hybrid mode is active  : ===='),
                        {
                            'name': str(checked),
                            'checked': True
                        },
                        {
                            'name': str(hybrid)
                        },
                        Separator('==== Speed ===='),
                        {
                            'name': 'medium',
                            'checked': True
                        },
                        {
                            'name': 'low'
                        },
                        {
                            'name': 'fast'
                        },
            ],
            'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
            }
    ] 

    answers = prompt(questions, style=custom_style_2)
    choice = answers.get('is_active')
    # register all options
    getconfig.set_module_activation(choice, module_const.HYBRID_MODULE)
    getconfig.set_module_speed(choice, module_const.HYBRID_MODULE)
   # launch()
      
def hashtag_choice(module):
    print(Fore.LIGHTMAGENTA_EX)
    print("=========================")
    print("Hashtags Configuration")
    print("=========================")

    exist_hashtag = getconfig.get_hashtag(module)
    if(exist_hashtag != ""):
        print("\n")
        print(Fore.WHITE, "you already have target hasthags : ")
        print(Fore.RED, exist_hashtag, Fore.WHITE)
        choice =  pyInquirer.hastags_choice_options()
        if (choice == hashtag_const.HASHTAGS_ADD_NEW):
            new_hashtag = pyInquirer.enter_hashtags()
            hashtag = exist_hashtag + " " + new_hashtag
            getconfig.set_hashtag(hashtag, module)
            hashtag_choice(module_const.HYBRID_MODULE)
        if (choice == hashtag_const.HASHTAGS_FINISH_EXIT):
            print(Fore.GREEN, "This module configuration is finish !!", Fore.WHITE)
            isContinue = pyInquirer.is_want_new_config()
            if(isContinue == "Yes"):
                print("exit")
                module_choice = pyInquirer.choose_module_configure()
                manage_options(module_choice)
            else:
                print("exit")

    else:
        pyInquirer.enter_hashtags()
        getconfig.set_hashtag(choice, module)

def manage_options(choice):
    #terminal_command.clear()
    if(choice == module_const.HYBRID_MODULE):
        hybrid_module()
        hashtag_choice(module_const.HYBRID_MODULE)

