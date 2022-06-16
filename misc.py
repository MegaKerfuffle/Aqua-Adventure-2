'''
Name: Robert Brzostek
Date: 1/7/2019
ICS3U/C ISU game
Aqua Adventure 2
'''
#import needed modules, functions, and settings
import time
from os import system,name

#function for intro text
def introtext():
  print("     _                      _      _             _                  ___")
  time.sleep(0.1)
  print("    /_\  __ _ _  _ __ _    /_\  __| |_ _____ _ _| |_ _  _ _ _ ___  |_  )")
  time.sleep(0.1)
  print("   / _ \/ _` | || / _` |  / _ \/ _` \ V / -_) ' \  _| || | '_/ -_)  / /")
  time.sleep(0.1) 
  print("  /_/ \_\__, |\_,_\__,_| /_/ \_\__,_|\_/\___|_||_\__|\_,_|_| \___| /___|")
  time.sleep(0.1)
  print("           |_|")
  time.sleep(0.1)
  print("                                                made by robert brzostek \n\n\n\n")
  time.sleep(1)

#function to clear the screen (courtesy of geeksforgeeks.org)
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

