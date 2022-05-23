from __future__ import print_function, unicode_literals
import os
# internal
import bots.launcher as launcher
import Ui.console.text_display.asciitext as printascii
import Ui.console.text_display.simpleprint as simpleprint
import Ui.console.constants.launcher_arg as arg
import Ui.console.text_display.pyInquirer as pyInquirer_text
import configuration.getconfig as getconfig
import Ui.console.config_ui.configure_instabot as configure_instabot
import commands.terminal as terminal

def setup_instabot(): 
    choice = "" 
    printascii.display_instabot_title()

    if(getconfig.get_bot_is_activate() == False):
        choice = pyInquirer_text.display_activate_bot()
    else:
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

    if(choice == arg.OPEN_CONFIG_HELPER):
        configure_instabot.launch()
 
setup_instabot()