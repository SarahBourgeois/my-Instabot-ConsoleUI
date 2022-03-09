
from __future__ import print_function, unicode_literals

# internal
import bots.launcher as launcher
import Ui.console.asciitext as asciitext
import Ui.console.textdisplay as textdisplay
import Ui.console.constants.launcher_arg as arg
import Ui.console.pyInquirer_text as pyInquirer_text
import configuration.getconfig as getconfig



def setup_instabot():  
    asciitext.display_instabot_title()
    choice = pyInquirer_text.launch_instabot_menu()
    switcher_action(choice)


def switcher_action(choice):
    bot_status = getconfig.get_bot_is_activate()

    if(choice ==  arg.CONNECT_INSTABOT_ACCOUNT):
        launcher.connect_account_to_instabot()
        setup_instabot()


    if(choice == arg.DISCONNECT_INSTABOT_ACCOUNT):
        launcher.disconnect_bot_from_account()
        setup_instabot()
        return
    
    if(bot_status == True):
        if(choice == arg.LAUNCH_LIKE_MODULE):
            launcher.launch_liker_module()
            setup_instabot()

        if(choice == arg.LAUNCH_FOLLOWER_MODULE):
            launcher.launch_follower_module()
            setup_instabot()

        if(choice == arg.LAUNCH_HYBRID_MODULE):
            launcher.launch_follower_and_liker_module()
            setup_instabot()

        if(choice == arg.LAUNCH_UNFOLLOW_MODULE):
            launcher.launch_unfollow_module()
            setup_instabot()

        if(choice == arg.LAUNCH_MUTE_MODULE):
            print("todo")
            setup_instabot()

    if(bot_status == False):
        print("You have to connect your account to the Instabot before launch module")
        print("Open the configuration helper")
    if(choice == arg.OPEN_CONFIG_HELPER):
        textdisplay.display_help_args()
        setup_instabot()

 

setup_instabot()

