# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
from examples import custom_style_2
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.constants.launcher_arg as launcher_arg
import Ui.console.constants.module as module_const
import Ui.console.constants.hashtags_actions as hashtag_cont
import configuration.getconfig as getconfig

# ============================
#  BOT ACTIVATION
# ============================
def display_activate_bot():
    print("Current Instabot status :")
    print(Fore.RED, "INACTIVE")
    print("\n")
    print(Fore.WHITE)
    questions = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'Action : ',
        'choices': [
                    Separator("\n"),
                    Separator("======== " + launcher_arg.SEPARATOR_CONNECTION +' ======== \n'),
                    launcher_arg.CONNECT_INSTABOT_ACCOUNT
        ]
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')


# ============================
# CONFIGURATION
# ============================

##### Hybrid config ######
def hybrid_config(checked, hybrid):
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
    return answers.get('is_active')


##### Want new config ######
def is_want_new_config():
    print(Fore.YELLOW, "Do you want to configure another Module ? ", Fore.WHITE)
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        "\n",
                        "Yes",
                        "No"
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')    

##### Module choice #####
def choose_module_configure():
    print(Fore.YELLOW, "CHOOSE A MODULE TO CONFIGURE : ", Fore.WHITE)
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        "\n",
                        module_const.HYBRID_MODULE,
                        module_const.LIKE_MODULE,
                        module_const.FOLLOW_MODULE,
                        module_const.UNFOLLOW_MODULE
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')

##### Hashtags choice options ####
def hastags_choice_options():
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        "\n",
                        hashtag_cont.HASHTAGS_ADD_NEW,
                        hashtag_cont.HASHTAGS_REMOVE,
                        hashtag_cont.HASHTAGS_FINISH_EXIT
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')

def enter_hashtags():
    questions = [
        {
            'type': 'input',
            'name': 'hashtag',
            'message': 'Enter hashtag you want to target ? (separate by a space. example > #movie #bar #food',
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers.get('hashtag')


# =========================
# ACCOUNT
# =========================
def ask_password():
    print("\n")
    questions = [
    {
        'type': 'password',
        'name': 'password',
        'message': 'Enter your instagram password',
    }
]
    password = prompt(questions)
    return password.get('password')

def ask_login():
    print("\n")
    questions = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'Enter your instagram username or mail',
    }
] 
    print("\n")
    username = prompt(questions)
    return username.get('username')

# =======================
#   MENU
# ========================
def return_to_menu():
    questions = [
    {
        'type': 'list',
        'name': 'return',
        'message': 'Action : ',
        'choices': [
                    launcher_arg.RETURN_BACK
        ]
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('return')

def launch_instabot_menu():
    print("Current Instabot status :")
    print(Fore.GREEN, "ACTIVE")
    print(Fore.WHITE)
    print("Account connected :  " + getconfig.get_login())
    print("\n")
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        Separator("\n"),
                        Separator("======== " + launcher_arg.SEPARATOR_MODULES + " ======== \n"),
                        launcher_arg.LAUNCH_LIKE_MODULE,
                        launcher_arg.LAUNCH_FOLLOWER_MODULE,
                        launcher_arg.LAUNCH_HYBRID_MODULE,
                        launcher_arg.LAUNCH_UNFOLLOW_MODULE,
                        launcher_arg.LAUNCH_MUTE_MODULE,

                        Separator("======== " +launcher_arg.SEPARATOR_CONFIG_HELPER + " ======== \n"),
                        launcher_arg.OPEN_CONFIG_HELPER,
                        
                        Separator("======== " + launcher_arg.SEPARATOR_DISCONNECT +' ======== \n'),
                        launcher_arg.DISCONNECT_INSTABOT_ACCOUNT
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')
