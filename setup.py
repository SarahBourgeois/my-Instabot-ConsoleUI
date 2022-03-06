
import bots.instagram_bot as instagram_bot
import Ui.console.asciitext as asciitext
import Ui.console.textdisplay as textdisplay
import configuration.getconfig as getconfig
import getopt, sys
# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]
# Options
options = "hiac"
# Long options
long_options = ["instagram", "account", "help"]

asciitext.display_instabot_title()

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            asciitext.display_helper()
            textdisplay.display_help_args()
        
        if currentArgument in ("-c", "--connect"):
            if(getconfig.get_bot_is_activate() == True):
                response = textdisplay.display_bot_already_connect()
                if (response == True):
                    instagram_bot.disconnect_bot_from_account()
            else:
                asciitext.display_connection()
                instagram_bot.connect_account_to_instabot()
                getconfig.set_bot_status("yes")
             
        if currentArgument in ("-i", "--instagram"):
            if(getconfig.get_bot_is_activate() == True):
                instagram_bot.launch_instagram_bot()
            else:
                textdisplay.display_activation_mandatory()
        
        if currentArgument in ("-a", "--account"):
            asciitext.display_account_info()
            instagram_bot.get_account_information()
             
except getopt.error as err:
    print (str(err))

