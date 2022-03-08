from __future__ import print_function, unicode_literals
import Ui.constants.launcher_arg as launcher_arg
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
from colorama import Fore, Back, Style


def launch_instabot_menu():
    print(Fore.CYAN, '   Welcome to Instabot. Choose an action please :  ')
    print(Fore.WHITE)
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': '\n',
            'choices': [
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