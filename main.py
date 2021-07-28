'''
Name: Robert Brzostek
Date started: 1/7/2019
Date submitted: 1/18/2019
ICS3U/C ISU game
Title: Aqua Adventure 2
Goal: Find a new planet to save humanity
Challenges: Time limits, resource management, random encounters, system failures
'''

#import needed modules, functions, and settings
import time
from core import newsector
from misc import clear,introtext
from settings import stime,sstime,tutlist

#simple function to ask user if they want to start the game, or return to main menu
def returntomain():
  while True:
    returnchoice = raw_input("\nStart the game? (y/n)\n>")
    if returnchoice == "y":
      storytext()
      break
    elif returnchoice == "n":
      mainmenu()
      break
    else:
      print "Please enter either y or n"

#shows neat ASCII logo, prints welcome text
introtext()
print "Welcome to Aqua Adventure 2!"

#simple function displaying game credits
def credits():
  print "\n\n  Made by Robert Brzostek for Ms. Yi's Gr.11 computer science class (ICS3U/C), see goo.gl/H3Xgpv for additional info. Special thanks to geeksforgeeks.org for providing a clear screen function, and Lukas M., Matthew C., and Jacob A. for beta testing.\n\n  This game is made up of 1171 lines of code, with 28 total functions, and 32 global variables and lists, spread across 4 Python files. It was specifically designed with modularity in mind, so that additional rooms, resources, systems, and more can be added to the game with minimal change to pre-existing code."
  time.sleep(2)
  returntomain()

#function to teach user game controls and provide additional help/info
def controls():
  #interactive game tutorial using if/else and indexing
  print "  Welcome to the Tutorial.\n  This tutorial will teach you the basic controls of the game.\n    1) Continue\n    2) Return\n"
  while True:
    tutchoice = raw_input("  Select a dialog option by typing in the number associated with your choice.\n  >")
    if tutchoice == "1":
      print tutlist[0]
      tutchoice2 = raw_input("\n  What do you want to do?\n    1) Continue [2 days]\n    2) Continue [-1 drone]\n    3) Continue [-10 cryo pods]\n  >")
      if tutchoice2 == "1":
        print tutlist[1]
        time.sleep(8)
        print tutlist[2]
        time.sleep(8)
      elif tutchoice2 == "2" or "3":
        print tutlist[2]
        time.sleep(8)
        print tutlist[1]
        time.sleep(8)
      print tutlist[3]
      time.sleep(4)
      returntomain()
      break
    elif tutchoice == "2":
      returntomain() 
      break
    else:
      print "When you enter an option that is not displayed on screen, the game will simply ask you to choose a valid option.\nPlease enter a valid choice."
  returntomain() 


#function that starts the game & provides background story
def storytext():
  clear() #clear the screen
  time.sleep(0.25)
  introtext() #display ASCII logo
  time.sleep(1)
  print "2132."
  time.sleep(sstime)
  print "Humanity has deprived the Earth of it's natural resources, resulting in several world wars that destroy the majority of life on Earth."
  time.sleep(stime)
  print "\n2150."
  time.sleep(sstime)
  print "Astronomers working with what remains of several world governments detect an asteroid large enough to destroy the fragile remains of humanity."
  time.sleep(stime)
  print "\n2152."
  time.sleep(sstime)
  print "The final phase of humanity's survival is deployed. You have been chosen to pilot this vessel, the Ark, to a new world."
  time.sleep(sstime)
  print "\nBefore departing, you have heard rumors about a planet known as Speronova. This planet may have what it takes to rebuild mankind."
  time.sleep(2)
  print ""
  newsector() #starts the actual game

#main menu function
def mainmenu():
  print "This is the main menu.\n  1) Start\n  2) Controls\n  3) Credits\n"
  while True:
    mmchoice = raw_input("Select a number to continue: ")
    if mmchoice == "1": #start game (with intro)
      storytext()
      break
    elif mmchoice == "2": #tutorial
      controls()
      break
    elif mmchoice == "3": #game credits
      credits()
      break
    elif mmchoice == "9": #skip straight to game (no intro)
      clear()
      newsector()
      break
    else:
      print "Please enter a valid choice."

#display main menu (after introtext)
mainmenu()