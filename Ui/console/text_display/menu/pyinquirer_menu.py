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
    print("Statut actuel de ton Instabot : ", Fore.GREEN, "ACTIF")
    print(Fore.WHITE)
    print("Account connected :  ", Fore.MAGENTA,  getconfig.get_login())
    print("\n")
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        Separator("\n"),
                        Separator("======== " + launcher_arg.SEPARATOR_MODULES + " ======== \n"),
                        launcher_arg.LAUNCH_AUTOMATIC_MODULE,
                        launcher_arg.LAUNCH_MANUAL_MODULE,

                        Separator("======== " +launcher_arg.SEPARATOR_CONFIG_HELPER + " ======== \n"),
                        launcher_arg.OPEN_CONFIG_HELPER,
                        
                        Separator("======== " + launcher_arg.SEPARATOR_DISCONNECT +' ======== \n'),
                        launcher_arg.DISCONNECT_INSTABOT_ACCOUNT
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')


def display_module():
    print("Statut actuel de ton Instabot : ", Fore.GREEN, "ACTIF")
    print(Fore.WHITE)
    print("Account connected :  ", Fore.MAGENTA,  getconfig.get_login())
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
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')