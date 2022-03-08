
from __future__ import print_function, unicode_literals

import bots.launcher as launcher
import Ui.console.asciitext as asciitext
import Ui.console.textdisplay as textdisplay
import Ui.constants.launcher_arg as arg
import Ui.console.pyInquirer_text as pyInquirer_text

asciitext.display_instabot_title()


def setup_instabot():       
    choice = pyInquirer_text.launch_instabot_menu()
    print(choice)
    switcher_action(choice)


def switcher_action(choice):
    if(choice ==  arg.CONNECT_INSTABOT_ACCOUNT):
        launcher.connect_account_to_instabot()
    if(choice == arg.DISCONNECT_INSTABOT_ACCOUNT):
        launcher.disconnect_bot_from_account()
    if(choice == arg.LAUNCH_LIKE_MODULE):
        launcher.launch_liker_module()
    if(choice == arg.LAUNCH_FOLLOWER_MODULE):
        launcher.launch_follower_module()
    if(choice == arg.LAUNCH_HYBRID_MODULE):
        launcher.launch_follower_and_liker_module()
    if(choice == arg.LAUNCH_UNFOLLOW_MODULE):
        launcher.launch_unfollow_module()
    if(choice == arg.LAUNCH_MUTE_MODULE):
        print("todo")
    if(choice == arg.OPEN_CONFIG_HELPER):
        textdisplay.display_help_args()
 

setup_instabot()

