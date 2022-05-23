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


##### Hybrid config ######
def module_activation_speed():
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

