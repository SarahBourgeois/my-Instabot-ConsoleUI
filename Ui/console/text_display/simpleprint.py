from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
from colorama import Fore, Back, Style

import json


####### BOT DISCONNECTION ############
def display_connection_done():
    print("\n")
    print(Fore.GREEN,"Congratulations. Your account is now connect to the InstaBot !")
    print(Fore.WHITE)

def display_connection_error():
    print(Fore.RED, "There is a problem to connect your account. Verify your login/password and retry.")
    print(Fore.WHITE)
    
def display_bot_disconnect():
    print("\n")
    print(Fore.GREEN, "Instabot is correctly remove from your account.")
    print("\n")
    print(Fore.WHITE)


def display_account_information(publication_number, follower_number, subscription_number):
    print("------------------------------------")
    print('\n')
    print("Your number of publications : " + publication_number)
    print("Number of follower you have : " + follower_number)
    print("Your number of subscriptions : " + subscription_number)
    print('\n')
    print("------------------------------------")


def error_login_account():
    print(Fore.RED, "There is a problem to connect your account to Instabot")
    print("Please, retry the connection. If the error persists send an email to the support :")
    print(Fore.WHITE, "beanyovertech@gmail.com")