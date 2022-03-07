
import bots.instagram_bot as instagram_bot
import bots.launcher as launcher
import Ui.console.asciitext as asciitext
import Ui.console.textdisplay as textdisplay
import configuration.getconfig as getconfig
import getopt, sys
# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]
# Options
options = "hiacu"
# Long options
long_options = ["instagram", "account", "help", "unfollow"]

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
                    launcher.disconnect_bot_from_account()
            else:
                asciitext.display_connection()
                launcher.connect_account_to_instabot()
                getconfig.set_bot_status("yes")
             
        if currentArgument in ("-i", "--instagram"):
            if(getconfig.get_bot_is_activate() == True):
                launcher.launch_follower_and_liker_module()
            else:
                textdisplay.display_activation_mandatory()
        
        if currentArgument in ("-a", "--account"):
            asciitext.display_account_info()
            launcher.get_account_information()
        
        if currentArgument in ("-u", "--unfollow"):
            launcher.launch_unfollow_module()
             
except getopt.error as err:
    print (str(err))

