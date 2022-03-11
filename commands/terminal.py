import subprocess
import shlex
import os

def resize_console():
    id_cmd='xdotool getactivewindow'
    resize_cmd='xdotool windowsize --usehints {id} 100 100'

    proc=subprocess.Popen(shlex.split(id_cmd),stdout=subprocess.PIPE)
    windowid,err=proc.communicate()
    proc=subprocess.Popen(shlex.split(resize_cmd.format(id=windowid)))
    proc.communicate()