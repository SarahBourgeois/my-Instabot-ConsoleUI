from examples import custom_style_3
from colorama import Fore, Back, Style

import json


def display_help_args():
    print("-------------------------------------------------------------------------------")
    print("\n")
    print ("       First, open configuration/config.ini to configure the bot correctly")
    print("\n")
    print ("       -a or --account : Display your account informations")
    print("\n")
    print("        -c or --connect : Connect the instabot to your instagram account")
    print("\n")
    print ("       -h or --instagram : Launch Hybrid Module")
    print("\n")
    print ("       -u or --unfollow : Launch Unfollow Module")
    print("\n")
    print ("       -l or --like : Launch Like Module")
    print("\n")
    print("******** WARNING : ******** ")
    print("To use instagram bot you need to have a safe account with already : ")
    print("- some publications, some followers and a complete profile !!")
    print("This bot is not to spam or must not be use for illegal activities.")
    print("\n")
    print("-------------------------------------------------------------------------------")





def display_connection_done():
    print("\n")
    print("\n")
    print("Congratulations. Your account is now connect to the InstaBot !")
 

 
    
def display_bot_disconnect():
    print("\n" "\n")
    print("Instabot is correctly remove from your account.")

def display_activation_mandatory():
    print("\n" "\n")
    print(Fore.RED + "Instabot is not link to your account.")
    print("please connect it before launch")

def display_account_information(publication_number, follower_number, subscription_number):
    print("------------------------------------")
    print('\n')
    print("Your number of publications : " + publication_number)
    print("Number of follower you have : " + follower_number)
    print("Your number of subscriptions : " + subscription_number)
    print('\n')
    print("------------------------------------")


def display_bot_already_connect():
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