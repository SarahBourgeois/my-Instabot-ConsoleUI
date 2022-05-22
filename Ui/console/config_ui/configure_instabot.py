# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.text_display.asciitext as asciitext
import Ui.console.text_display.pyInquirer as pyInquirer
import configuration.getconfig as getconfig
import commands.terminal as terminal_command
import Ui.console.constants.module as module_const

def launch():
    terminal_command.clear()
    print("\n")
    print("\n")
    asciitext.display_configuration()
    print("\n")
    display_readme_helper()
    module_choice = pyInquirer.choose_module_configure()
    print(module_choice)
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
    hybrid_choice = answers.get('is_active')
    print(hybrid_choice)
    getconfig.set_hybrid_activation(hybrid_choice)
   # launch()
      
def hashtag_choice():
    questions = [

    {
        'type': 'input',
        'name': 'hashtag',
        'message': 'Enter hashtag you want to target ? (separate by a space. example > #movie #bar #food',
    },
]

    answers = prompt(questions, style=custom_style_2)

def manage_options(choice):
    #terminal_command.clear()
    if(choice == module_const.HYBRID_MODULE):
        hybrid_module()
        hashtag_choice()

