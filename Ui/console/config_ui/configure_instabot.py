# pyInquirer
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
# colorama
from colorama import Fore, Back, Style
# internal
import Ui.console.text_display.asciitext as asciitext





def launch():
    print("\n")
    print("\n")
    asciitext.display_configuration()
    print("\n")
    display_readme_helper()
    manage_options()
    


def display_readme_helper():
    print(Fore.LIGHTMAGENTA_EX)
    print("If you never configure Instabot before, ")
    print("Please open the documentation file :" + Fore.LIGHTYELLOW_EX, "wwww.instabot.com")
    print("\n")
    print("\n")

def manage_options():
    questions = [
    {
        'type': 'expand',
        'message': 'Conflict on `file.js`: ',
        'name': 'overwrite',
        'default': 'a',
        'choices': [
            {
                'key': 'y',
                'name': 'Overwrite',
                'value': 'overwrite'
            },
            {
                'key': 'a',
                'name': 'Overwrite this one and all next',
                'value': 'overwrite_all'
            },
            {
                'key': 'd',
                'name': 'Show diff',
                'value': 'diff'
            },
            Separator(),
            {
                'key': 'x',
                'name': 'Abort',
                'value': 'abort'
            }
        ]
    }
]

 
    result = prompt(questions)
