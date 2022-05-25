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
        hybrid = "non"
        checked = "oui"
    else:
        hybrid = "oui"
        checked = "non"
    print(Fore.LIGHTYELLOW_EX)
    print("[HYBRID_SECTION]", Fore.WHITE)
    questions = [ 
            {
                'type': 'checkbox',
                'message': 'Selectionne tes choix :',
                'name': 'is_active',
                'choices': [ 
                        Separator('==== Activation du mode Hybride : ===='),
                        {
                            'name': str(checked),
                            'checked': True
                        },
                        {
                            'name': str(hybrid)
                        },
                        Separator('==== Speed ===='),
                        {
                            'name': 'Manuel'
                        },
                        {
                            'name': 'Lent',
                            'checked': True
                        },
                        {
                            'name': 'Moyen'
                        },
                        {
                            'name': 'Rapide'
                        },
            ],
            'validate': lambda answer: 'Tu dois faire au moins un choix.' \
            if len(answer) == 0 else True
            }
    ] 

    answers = prompt(questions, style=custom_style_2)
    return answers.get('is_active')


##### Want new config ######
def is_want_new_config():
    print(Fore.YELLOW, "Veux-tu configurer un autre module ? ", Fore.WHITE)
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Action : ',
            'choices': [
                        "\n",
                        "Oui",
                        "Non"
                        ],
        },
    ]
    answers = prompt(questions, style=custom_style_3)
    return answers.get('choice')    

##### Module choice #####
def choose_module_configure():
    print(Fore.YELLOW, "CHOISIS UN MODULE A CONFIGURER : ", Fore.WHITE)
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
            'message': 'Entre les Hashtags cibles (sépare les par des ESPACES. Exemple : #movie #bar #food',
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers.get('hashtag')

