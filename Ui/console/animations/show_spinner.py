import time
import sys
import os
  
def launch(sentence):
    # String to be displayed when the application is loading
    load_str = sentence
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
  
    while (counttime != 100):
        time.sleep(0.075) 
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
        # y->for storing altered ASCII code
        y = 0                             
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string to the resultant string
        load_str = res

        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
    # for windows OS
    if os.name =="nt":
        os.system("cls")   
    # for linux / Mac OS
    else:
        os.system("clear")
  

  
 