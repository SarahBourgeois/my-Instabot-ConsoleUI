# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.constants.launcher_arg as launcher_arg


def launch_instabot_menu():
    print(Fore.CYAN, '   Welcome to Instabot !')
    print(Fore.WHITE)
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        Separator("\n"),
                        Separator("======== " + launcher_arg.SEPARATOR_CONNECTION +' ======== \n'),
                        launcher_arg.CONNECT_INSTABOT_ACCOUNT,
                        launcher_arg.DISCONNECT_INSTABOT_ACCOUNT, 

                        Separator("======== " + launcher_arg.SEPARATOR_MODULES + " ======== \n"),

                        launcher_arg.LAUNCH_LIKE_MODULE,
                        launcher_arg.LAUNCH_FOLLOWER_MODULE,
                        launcher_arg.LAUNCH_HYBRID_MODULE,
                        launcher_arg.LAUNCH_UNFOLLOW_MODULE,
                        launcher_arg.LAUNCH_MUTE_MODULE,

                        Separator("======== " +launcher_arg.SEPARATOR_CONFIG_HELPER + " ======== \n"),

                        launcher_arg.OPEN_CONFIG_HELPER],
        },
    ]

    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')


def display_bot_already_connect():
    print('\n')
    print(Fore.RED + " - - - - The InstaBot is already connect to your account. - - - - ")
    print(Fore.WHITE)

    questions = [
    {
        'type': 'list',
        'name': 'response',
        'message': 'Do you really want to remove the instabot from your account ?',
        'choices': ['Yes', 'No'],
        'filter': lambda val: val.lower()
    },
]
    answer = prompt(questions, style=custom_style_3)
    response = answer.get('response')
    if(response == "yes"):
        return True
    else:
        return False


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