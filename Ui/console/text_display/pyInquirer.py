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
    print("Statut actuel de ton Instabot : ", Fore.RED, "INACTIF")
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
        'message': 'Entre ton pseudo Instagram ou ton email : ',
    }
] 
    print("\n")
    username = prompt(questions)
    return username.get('username')

