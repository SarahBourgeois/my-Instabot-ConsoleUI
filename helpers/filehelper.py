# system internal
import csv
from collections import defaultdict
import os
import sys
import shutil

def readCsvFile():
    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, 'Contacts.csv')
    columns = defaultdict(list) # each value in each column is appended to a list
    with open(full_path,  encoding= 'unicode_escape') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
    return columns


def registerData(follower):
    print("register followed people")
    file1 = open('registers/followedPeople.txt','a') # a is to not override current content
    file1.write(follower + "\n")
    print("Stored successfully")

def delete_folder_contents():
    folder_path = './User_Data'
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

def get_file_content():
    myfile = open("registers/followedPeople.txt", "rt")
    contents = myfile.read()         
    myfile.close()      
    content_list = contents.split('\n')            
    return content_list                 

def delete_user(user):
    a_file = open("registers/followedPeople.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    new_file = open("registers/followedPeople.txt", "w")
    for line in lines:
        if line.strip("\n") != user:
            new_file.write(line)

    new_file.close()





