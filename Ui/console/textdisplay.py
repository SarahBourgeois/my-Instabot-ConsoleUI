def display_help_args():
    print("-------------------------------------------------------------------------------")
    print("\n")
    print ("       First, open configuration/config.ini to configure the bot correctly")
    print("\n")
    print("        -c or --connect : Connect the instabot to your instagram account")
    print("\n")
    print ("       -i or --instagram : Launch your InstaBot")
    print("\n")
    print ("       -a or --account : Display your account informations")
    print("\n")
    print("******** WARNING : ******** ")
    print("To use instagram bot you need to have a safe account with already : ")
    print("- some publications, some followers and a complete profile !!")
    print("This bot is not to spam or must not be use for illegal activities.")
    print("\n")
    print("-------------------------------------------------------------------------------")

def ask_password(login):
    return input("Hi. Please enter your password and press Enter.\n ")

def display_connection_done():
    print("\n")
    print("------------------------------------------------------------")
    print("Well done !! Your account is now connect to the InstaBot !")
    print("------------------------------------------------------------")

def display_bot_already_connect():
    print("The InstaBot is already connect to your account.")
    response = input("Do you want to desactivate it ? yes/no \n")
    if (response == "yes"):
        return True
    if (response == "no"):
        return False
    else:
        display_bot_already_connect()
    return response        
    
def display_bot_disconnect():
    print("Instabot is correctly remove from your account.")

def display_activation_mandatory():
    print("Instabot is not link to your account.")
    print("please connect it before launch")

def display_account_information(publication_number, follower_number, subscription_number):
    print("------------------------------------")
    print('\n')
    print("Your number of publications : " + publication_number)
    print("Number of follower you have : " + follower_number)
    print("Your number of subscriptions : " + subscription_number)
    print('\n')
    print("------------------------------------")

