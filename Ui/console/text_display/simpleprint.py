from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError
from examples import custom_style_3
from colorama import Fore, Back, Style

import json

# Connection is OK 
def display_connection_done():
    print("\n")
    print(Fore.GREEN,"Félicitations ! Ton Instabot est maintenant connecté à ton compte !")
    print(Fore.WHITE)

def install():
    print(Fore.GREEN,"Initialisation en cours ...")
    

# Connection Error 
def display_connection_error():
    print(Fore.RED, "Un problème est survenu lors de la connexion à ton compte. Vérifie ton login/password et réessaye !")
    print(Fore.WHITE)

# Disconnect instabot OK
def display_bot_disconnect():
    print("\n")
    print(Fore.GREEN, "L\'Instabot a été correctement supprimé de ton compte.")
    print("\n")
    print(Fore.WHITE)

# Processing display
def display_processing():
    print("\n")
    print("Processing ...")

# Account Information
def display_account_information(publication_number, follower_number, subscription_number):
    print("------------------------------------")
    print('\n')
    print("Ton nombre de publication : " + publication_number)
    print("Ton nombre de follower : " + follower_number)
    print("Ton nombre d'abonnements : " + subscription_number)
    print('\n')
    print("------------------------------------")

# Error Login
def error_main_message():
    print(Fore.RED, "Un problème est survenu avec ton Instabot.")
    print("Réessaie de nouveau, et si le problème persiste, déconnecte et reconnecte l'Instabot de ton compte. Sinon, envoie un mail au support : ")
    print(Fore.WHITE, "beanyovertech@gmail.com")