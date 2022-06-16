'''
Name: Robert Brzostek
Date created: 1/7/2019
ICS3U/C ISU game
Aqua Adventure 2
'''

#import modules, functions, and settings
import time
import random
from misc import clear,introtext
from settings import *

#update number of days (dayspassed and daysremaining), based on given value (x)
def updatedays(x):
  global dayspassed,daysremaining
  dayspassed += x
  daysremaining -= x

#function that is called whenever the player enters a new sector
def newsector():
  global dayspassed,daysremaining,ended,warpcost,coresys_status,current_room,passed_rooms,warnings,story_list
  if current_room not in passed_rooms:
    randomevent()
  #checks if player failed yet
  endingchecker()
  while ended == False:
    #display detailed sector description, # of days remaining/passed, and options
    print(story_list[current_room])
    if warnings == []:
      pass
    else:
      print("")
      for i in range(len(warnings)):
        print("WARNING:",warnings[i])
    print("\nIt has been",dayspassed,"days since departure. You will run out of water in",daysremaining,"days. You can collect more water with exploration drones.")
    print("\nWhat would you like to do?\n  1) Initiate scanning protocols\n  2) Check ship status\n  3) Deploy exploration drone\n  4) Colonize planet\n  5) Navigate to next sector\n  6) View ship log")
    while True:
      #handles player choice; sends to correct function
      nschoice = input("Enter an option: ")
      if nschoice == "1":
        scanning()
        break
      elif nschoice == "2":
        status()
        break
      elif nschoice == "3":
        drone()
        break
      elif nschoice == "4":
        colonize()
        break
      elif nschoice == "5":
        if coresys_status[1] == "Damaged":
          warpcost = 2
          print("\n  WARNING: Due to reactor damage, warp jumps will now take",warpcost,"days to complete. Repair systems in the Ship Status screen.")
          navigation()
        else:
          warpcost = 1
          navigation()
        break
      elif nschoice == "6":
        shiplog()
        break
      else:
        "Please enter a valid choice."



#allows player to experience random events that occur upon entering a sector 
def randomevent():
  global rngevents,rnghelp,cryopods,dronenum,scrap,daysremaining
  x = random.randint(0,len(rngevents)-1)
  print("\n\n  ========== Encounter ==========")
  print(rngevents[x][0]) #print event description
  while True:
    randchoice = int(input(rngevents[x][1]))
    #handles resource gains/losses for the 'good' ending
    if randchoice == 1:
      cryopods += rngevents[x][2][2]
      dronenum += rngevents[x][2][3]
      scrap += rngevents[x][2][4]
      daysremaining += rngevents[x][2][5]
      break
    
    #handles resource gains/losses for the 'bad' ending
    elif randchoice == 2:
      cryopods += rngevents[x][3][2]
      dronenum += rngevents[x][3][3]
      scrap += rngevents[x][3][4]
      daysremaining += rngevents[x][3][5]
      break

    #loops around if player chooses anything other than 1 or 2
    else:
      print("Please enter a valid choice.")

  #after action report
  print("\n  ========== Encounter Report ==========")
  if randchoice == 1:
    print("  {0:20}{1:20}".format("Resources","Amount"))
    for i in range(2,len(rngevents[x][2])):
      print("  {0:20}{1:1}".format(rnghelp[i],rngevents[x][2][i]))
  elif randchoice == 1:
    print("  {0:20}{1:20}".format("Resources","Amount"))
    for i in range(2,len(rngevents[x][3])):
      print("  {0:20}{1:1}".format(rnghelp[i],rngevents[x][3][i]))
    
  print("  System Damage:") 
  if randchoice == 1:
    randsysdamgood(x)
  elif randchoice == 2:
    randsysdambad(x)

  passed_rooms.append(current_room) #updates passed_rooms to include the current sector, AFTER completion of random evnt

  #IMPORTANT: this code must remain at the end of the randomevent handler. if code is removed, players may experience the same event several times in the game.
  rngevents.remove(rngevents[x])


#updates system status based on good outcome of random encounter
def randsysdamgood(x):
  global coresys_names,coresys_status,auxsys_names,auxsys_status

  #displays any systems damaged in the encounter, if player chooses 'good' ending
  if rngevents[x][2][1] == "Damaged": 
    print(" " + rngevents[x][2][0] + "has been damaged.")
    if rngevents[x][2][0] in coresys_names:
      system = coresys_names.index(rngevents[x][2][0])
      coresys_status[system] = "Damaged"
    elif rngevents[x][2][0] in auxsys_names:
      system = auxsys_names.index(rngevents[x][2][0])
      auxsys_status[system] = "Damaged"

  #displays any systems damaged in the encounter, if player chooses 'good' ending
  elif rngevents[x][2][1] == "Offline": 
    print(" " + rngevents[x][2][0] + "has been heavily damaged, and is no longer functional.")
    if rngevents[x][2][0] in coresys_names:
      system = coresys_names.index(rngevents[x][2][0])
      coresys_status[system] = "Offline"
    elif rngevents[x][2][0] in auxsys_names:
      system = auxsys_names.index(rngevents[x][2][0])
      auxsys_status[system] = "Offline"

  else:
    print("  No systems have been damaged.")


#updates system status based on bad outcome of random encounter
def randsysdambad(x):
  global coresys_names,coresys_status,auxsys_names,auxsys_status

  #displays any systems damaged in the encounter, if player chooses 'bad' ending
  if rngevents[x][3][1] == "Damaged": 
    print(" " + rngevents[x][3][0] + "has been damaged.")
    #applies damage to correct system (checks for core/aux)
    if rngevents[x][3][0] in coresys_names:
      system = coresys_names.index(rngevents[x][3][0])
      coresys_status[system] = "Damaged"
    elif rngevents[x][3][0] in auxsys_names:
      system = auxsys_names.index(rngevents[x][3][0])
      auxsys_status[system] = "Damaged"

  #displays any systems damaged in the encounter, if player chooses 'bad' ending
  elif rngevents[x][3][1] == "Offline": 
    print(" " + rngevents[x][3][0] + "has been heavily damaged, and is no longer functional.")
    #applies damage to correct system (checks for core/aux)
    if rngevents[x][3][0] in coresys_names:
      system = coresys_names.index(rngevents[x][3][0])
      coresys_status[system] = "Offline"
    elif rngevents[x][3][0] in auxsys_names:
      system = auxsys_names.index(rngevents[x][3][0])
      auxsys_status[system] = "Offline"
  else:
    print("  No systems have been damaged.")


#function to perform scans of current sector or nearby sectors
def scanning():
  global scanlog,dayspassed,daysremaining,auxsys_status,scanresults_short,current_room,rettime
  print("\n  ============ Scanning Subsystem ============\n  Scan types available:\n    1) Long Distance Scan [2 days]\n    2) Short Range Scan [1 day]\n    3) Cancel Scanning Protocol\n  What would you like to do?")
  while True:
    scanchoice = input("  >")
    if scanchoice == "1": #gives player a pre-made report that indicates ideal travel direction, and hints about nearby sectors
      if auxsys_status[3] == "Damaged":
        if random.randint(0,2) == 1:
          print("\n  ERROR: Unable to scan due to system damage. Repair systems in the Ship Status screen. Try again.")
          time.sleep(rettime)
        else:
          longscan()
      elif auxsys_status[3] == "Offline":
        print("\n  ERROR: System offline. Repair systems in the Ship Status screen.")
        time.sleep(rettime)
      else:
        longscan()
      break
    #gives player a pre-made report indicating planet availability (good or not), potential resources, and/or potential random encounters
    elif scanchoice == "2":
      if auxsys_status[2] == "Damaged":
        if random.randint(0,2) == 1:
          print("\n  ERROR: Unable to scan due to system damage. Repair systems in the Ship Status screen. Try again. ")
          time.sleep(rettime)
        else:
          shortscan()
      elif auxsys_status[2] == "Offline":
        print("\n  ERROR: System offline. Repair systems in the Ship Status screen.")
        time.sleep(rettime)
      else:
        shortscan()
      break
    elif scanchoice == "3":
      newsector()
      break
    else:
      print("  Enter a valid choice.")


#function for short-range (current sector) scans
def shortscan():
  global scanresults_short,current_room,dayspassed,scanlog,rettime
  print("\n  Beginning scan...\n")
  time.sleep(1)
  print("  ========== Scan Result ==========")
  print("  Scan completed. Generating sector report...\n")
  time.sleep(0.75)
  print("{0:100}".format(scanresults_short[current_room]))
  print("  ==================================")
  #appends scan info to log for quicker future viewing
  scanlog = ["short", dayspassed, scanresults_short[current_room], current_room] 
  #pushes game time forward 1 day
  updatedays(1)
  time.sleep(1)
  ret = input("\n  Press [Enter] to continue.")
  if ret:
    print("\n Returning...")
    time.sleep(rettime)
    newsector()

#function for long distance (sector) scans
def longscan():
  global scanresults_far,current_room,dayspassed,scanlog,rettime
  print("\n  Beginning scan...\n")
  time.sleep(1)
  print("  ========== Scan Result ==========")
  print("  Scan completed. Generating nearby sector report...\n")
  time.sleep(0.75)
  print("{0:100}".format(scanresults_far[current_room]))
  print("  ==================================")
  #appends scan info to log for quick future viewing
  scanlog = "far", dayspassed, scanresults_far[current_room]
  #pushes game time forward 2 days
  updatedays(2)
  time.sleep(1)
  ret = input("\n  Press [Enter] to continue.")
  if ret:
    print("\n Returning...")
    time.sleep(rettime)
    newsector()



#ship status reporting. shows current status of core and aux systems, and remaining on-board resources
def status():
  global coresys_names,coresys_status,auxsys_names,auxsys_status,daysremaining,dronenum,cryopods,scrap,rettime
  print("\n  ============ Core Systems ============")
  print("  {0:30}{1:20}".format("System:", "Status:"))
  for i in range(len(coresys_names)):
    print("  {0:30}{1:20}".format(coresys_names[i], coresys_status[i]))
  print("  ============ Aux. Systems ============")
  print("  {0:30}{1:20}".format("System:", "Status:"))
  for i in range(len(auxsys_names)):
    print("  {0:30}{1:20}".format(auxsys_names[i], auxsys_status[i]))
  print("  ============= Other Info =============")
  print("  {0:30}{1:1} days".format("Water Supply", daysremaining))
  print("  {0:30}{1:1} drones".format("Drone Supply", dronenum))
  print("  {0:30}{1:1} pods".format("Cryo Pods", cryopods))
  print("  {0:30}{1:1} scrap".format("Scrap", scrap))
  time.sleep(0.5)
  while True: #choice menu. allow player to repair broken systems or build drones
    statchoice = input("\n  What would you like to do?\n    1) Repair a system \n    2) Build a drone [+1 drone, -10 scrap, 1 day]\n    3) Return\n  >")
    if statchoice == "1":
      sysrepair()
      break
    elif statchoice == "2":
      if scrap >= 10:
        print("  Building exploration drone...")
        time.sleep(0.5)
        updatedays(1)
        scrap -= 10
        dronenum += 1
        print("\n  Drone built. Returning...")
      else:
        print("\n  Not enough scrap. Collect more with exploration drones and try again. ")
      time.sleep(rettime)
      break
    elif statchoice == "3":
      print("\n  Returning...")
      time.sleep(rettime)
      newsector()
      break


#function for repairing broken systems (restore game functionality)
def sysrepair():
  print("\n  Which type of system would you like to repair?\n    1) Core Systems [2 days]\n    2) Aux. Systems [1 day]\n    3) Return")
  while True:
    repchoice1 = input("  >")
    if repchoice1 == "1":
      coresysrepair() #send to core system repair function
      break
    elif repchoice1 == "2":
      auxsysrepair() #send to aux system repair function
      break
    elif repchoice1 == "3":
      print("\n  Returning...")
      time.sleep(rettime)
      newsector()
      break
    else:
      print("  Please enter a valid choice.")


#function to repair core systems
def coresysrepair():
  global coresys_names,coresys_status,coresys_damaged,scrap,rettime
  repairlist = []
  coresys_numed = [0,1,2] #local list that acts as an index for the several lists related to coresys
  x = -1 #tracks how many systems need repairs
  for i in range(len(coresys_names)): #scans systems and appends to repairlist if damaged 
    if coresys_status[i] == "Damaged":
      repairs = str(coresys_names[i]) + str(coresys_status[i]) + str(coresys_damaged[i]) + str(coresys_numed[i])
      repairlist.append(repairs)
      x += 1
  if repairlist == []:
    print("\n  No systems to repair. Returning...")
    time.sleep(rettime)
    status()
  else:
    print("\n  Damaged Core Systems")
    for i in range(x+1): #dynamically list only damaged systems
      corelist = ["    " + str(i+1) + ") " + str(repairlist[i][0]) + " (" + str(repairlist[i][1]) + ")" + " [" + str(repairlist[i][2]) + " scrap]"]
      print("".join(corelist)) #workaround to eliminate extra spaces that python insists on putting in between 
    returnlist = ["    " + str(x+2) + ") Return"]
    print("".join(returnlist))
    while True:
      repchoice2 = int(input("  Which system would you like to repair?\n  >"))
      if 0 <= repchoice2 <= x+1: #dynamically asks user for which sys to repair
        if scrap >= repairlist[repchoice2-1][2]:
          coresys_status[repairlist[repchoice2-1][3]] = "Online"
          print("  " + repairlist[repchoice2-1][0] + "repaired for" + repairlist[repchoice2-1][2] + "scrap.")
          scrap -= repairlist[repchoice2-1][2]
          updatedays(2)
          time.sleep(rettime)
          sysrepair()
          break
        else:
          print("\n  Not enough scrap. Collect more with exploration drones and try again.")
          time.sleep(rettime)
          sysrepair()
          break

#function to repair aux systems
def auxsysrepair():
  global auxsys_names,auxsys_status,auxsys_damaged,auxsys_offline,scrap,rettime
  repairlist = []
  auxsys_numed = [0,1,2,3,4]
  x = -1 #tracks the number of systems that need repairs
  for i in range(len(auxsys_names)):
    if auxsys_status[i] == "Damaged":
      repairs = str(auxsys_names[i]) + str(auxsys_status[i]) + str(auxsys_damaged[i]) + str(auxsys_numed[i])
      repairlist.append(repairs)
      x += 1
    elif auxsys_status[i] == "Offline":
      repairs = str(auxsys_names[i]) + str(auxsys_status[i]) + str(auxsys_offline[i]) + str(auxsys_numed[i])
      repairlist.append(repairs)
      x += 1
  if repairlist == []:
    print("\n  No systems to repair. Returning...")
    time.sleep(rettime)
    status()
  else:
    print("\n  Damaged Aux. Systems")
    for i in range(x+1):
      auxlist = ["  " + str(i+1) + ") " + str(repairlist[i][0]) + " (" + str(repairlist[i][1]) + ")" + " [" + str(repairlist[i][2]) + " scrap]"]
      print("".join(auxlist))
    auxlist2 = ["  ",str(x+2),") Return"]
    print("".join(auxlist2))
    while True:
      repchoice4 = int(input("  Which system would you like to repair?\n  >"))
      if 0 <= repchoice4 <= x+1:
        if repairlist[repchoice4-1][1] == "Damaged":
          if scrap >= repairlist[repchoice4-1][2]:
            auxsys_status[repairlist[repchoice4-1][3]] = "Online" 
            print(" " + repairlist[repchoice4-1][0] + "repaired for" + repairlist[repchoice4-1][2] + "scrap.")
            scrap -= repairlist[repchoice4-1][2]
            updatedays(1)
            time.sleep(rettime)
            sysrepair()
            break
          else:
            print("\n  Not enough scrap. Collect more with exploration drones and try again.")
            time.sleep(rettime)
            sysrepair()
            break
        elif repairlist[repchoice4-1][1] == "Offline":
          if scrap >= repairlist[repchoice4-1][2]:
            auxsys_status[repairlist[repchoice4-1][3]] = "Online" 
            print(" " + repairlist[repchoice4-1][0] + "repaired for" + repairlist[repchoice4-1][2] + "scrap.")
            scrap -= repairlist[repchoice4-1][2]
            updatedays(1)
            time.sleep(rettime)
            sysrepair()
            break
          else:
            print("\n  Not enough scrap. Collect more with exploration drones and try again.")
            time.sleep(rettime)
            sysrepair()
            break



#drone deployment function. allows for more detailed planet scans, at the price of resource: drones
def drone():
  global auxsys_status,rettime
  print("\n  Initializing...")
  time.sleep(1)
  if auxsys_status[1] == "Damaged":
    if random.randint(0,2) == "1":
      dronedispatch()
    else:
      print("\n  ERROR: System damaged. Repair systems in the Ship Status screen. Try again later.")
      time.sleep(rettime)
  elif auxsys_status[1] == "Offline":
    print("\n  ERROR: System offline. Repair systems in the Ship Status screen.")
    time.sleep(rettime)
  else:
    dronedispatch()


#function responsible for close range drone scans
def dronedispatch():
  global dronenum,dayspassed,sectorplanets,current_room,drchoice2,rettime,scanresults_close
  drchoicelist = []
  print("\n  ========== Drone Dispatcher ==========")
  print(" " + str(dronenum) + " drones are available for deployment.")
  if dronenum > 0:
    drchoice1 = input("  Deploy a drone?\n    1) Yes [-1 drone]\n    2) No\n  >")
    if drchoice1 == "1":
      #pulls list of planets in current sector and displays it
      print("\n  The following planets are within deployment range:")
      x = 0 #local variable to track options and indexing
      for planets in scanresults_close[current_room]:
        drlist = ["    " + str(x+1) + ") " + str(scanresults_close[current_room][x][0]) + " [" + str(scanresults_close[current_room][x][4]) + " days]"]
        print("".join(drlist)) #displays as list to improve UI
        drchoicelist.append(x+1)
        x += 1
      drlist2 = ["    " + str(x+1) + ") Return"]
      print("".join(drlist2)) #displays as list to improve UI
      while True:
        drchoice2 = int(input("  Select a planet to deploy to.\n  >"))
        if 0 <= drchoice2 <= x:
          deploydrone(drchoice2 - 1)
          dronenum -= 1
          newsector()
          break
        elif drchoice2 == x+1:
          newsector()
          break
        else:
          print("  Please enter a valid choice.")
    else:
      print("\n  Shutting down drone dispatcher...")
      time.sleep(rettime)
      newsector()
  else:
    print("\n  No drones to deploy. Build more in the Ship Status screen. Returning...")
    time.sleep(rettime)
    newsector


#function to display planet stats and report
def deploydrone(y):
  global daysremaining,dayspassed,dronenum,scanresults_close,scrap,cryopods,scanlog
  #create easier to use variables w/ needed values
  planetname = scanresults_close[current_room][y][0]
  report = scanresults_close[current_room][y][1]
  watergained = scanresults_close[current_room][y][2]
  scrapgained = scanresults_close[current_room][y][3]
  daysspent = scanresults_close[current_room][y][4]
  y -= 1 #convert user option to machine readable integer
  print("\n  Dispatching exploration drone to: " + planetname)
  time.sleep(0.5)
  print("\n  Collecting data...")
  time.sleep(daysspent)
  print("\n  Final report: " + report)
  print("\n  During exploration, the drone was able to collect " + str(watergained) + " days of water and " + str(scrapgained) + " scrap in " + str(daysspent) + "day(s).")
  daysremaining += watergained
  scrap += scrapgained
  updatedays(daysspent)
  #update scanlog with info from close scan
  scanlog = "close" + str(dayspassed) + str(report) + str(planetname)
  #return to newsector
  ret = input("\n  Press [Enter] to continue.")
  if ret:
    print("\n Returning...")
    time.sleep(rettime)
    newsector()



#function to allow player to colonize a planet (once)
def colonize():
  global rettime,scanlog,current_room
  while True:
    colchoice1 = input("  Colonizing a planet will end the game. Are you sure you want to continue?\n    1) Yes\n    2) No\n  >")
    if colchoice1 == "1":
      print("  ========== Colonization ==========")
      if scanlog[3] == current_room:
        #pulls list of planets in current sector and displays it
        print("  The following planets are within deployment range: ")
        x = 0 #local variable to track options and indexing
        for planets in scanresults_close[current_room]:
          collist1 = ["    ",str(x+1),") ",str(scanresults_close[current_room][x][0])]
          print("".join(collist1)) #displays as list to improve UI
          x += 1
        collist2 = ["    ",str(x+1),") Return"]
        print("".join(collist2))
        while True:
          colchoice2 = int(input("  Where would you like to land?\n  >"))
          print(x)
          if 0 <= colchoice2 <= x-1:
            if scanresults_close[current_room][colchoice2-1][0] == "CBP-SF-2 - Speronova":
              endtype = "good"
              finalplanet = scanresults_close[current_room][colchoice2-1][0]
              goodending(endtype,finalplanet)
            else:
              endtype = "neutral"
              finalplanet = scanresults_close[current_room][colchoice2-1][0]
              goodending(endtype,finalplanet)
            break
          elif colchoice2-1 == x:
            newsector()
            break
          else:
            print("  Please enter a valid choice.")
        break
      else:
        print("  Please conduct a short scan of the current sector to view planets.\n  Returning...")
        time.sleep(rettime)
        break
    elif colchoice1 == "2":
      print("\n  Returning...")
      time.sleep(rettime)
      break
    else:
      print("Please enter a valid choice.")



#shiplog function. allows player to quickly access previously given information. as an additional challenge, players are limited to last created log per section (scan, security)
def shiplog():
  global scanlog,rettime
  print("\n  Accessing...")
  time.sleep(0.5)
  print("\n  ========== Ship Log Database ==========\n  Note: Due to ship memory restrictions, only the last recorded log per section is kept.\n  Available Logs:\n    1) Scan Log\n    2) Cancel")
  while True:
    logchoice = input("  Which log would you like to acccess?\n  >")
    if logchoice == "1":
      print("  Accessing scan log...")
      time.sleep(0.5)
      if scanlog[0] == "short":
        print("  Short Range Scan Log, created " + str(scanlog[1]) + " days after departure:\n  " + scanlog[2])
      elif scanlog[0] == "far":
        print("  Long Distance Scan Log, created " + str(scanlog[1]) + " days after departure:\n  " + scanlog[2])
      elif scanlog[0] == "close":
        print("  Planetary scan of " + scanlog[3] + ", created " + str(scanlog[1]) + " days after departure:\n  " + scanlog[2])
      else:
        print("  No scan logs found. Logs will be stored here after you conduct a short range, long distance, or planetary scan.\n")
        time.sleep(0.5)
      ret = input("\n  Press [Enter] to continue.")
      if ret:
        print("\n Returning...")
        time.sleep(rettime)
        newsector()
      break
    elif logchoice == "2":
      print("\n  Returning...")
      time.sleep(rettime)
      newsector()
      break
    else:
      print("  Please enter a valid choice.")



#function for intersector navigation
def navigation():
  global room_list,current_room,next_room,dayspassed,passed_rooms,warpcost,warpjumps
  #direction handler (input cardinal directions, move ship)
  while True:
    direction = input("\n  ========== Warp Drive ==========\n  Where would you like to warp?\n    1) North\n    2) East\n    3) South\n    4) West\n    5) Return\n  >")
    if direction == "1":
      next_room = room_list[current_room][1]
      if next_room == None:
        print("  Navigating your ship to that sector would result in certain death. Please choose a different direction. \n")
      else:
        print("  Initializing warp drive...")
        time.sleep(0.5)
        print("  Warp drive charged. Commencing warp...")
        time.sleep(1)
        passed_rooms.append(current_room)
        current_room = next_room
        #moves game time forward depending on warpcost
        updatedays(warpcost)
        warpjumps += 1
        clear()
        introtext()
        print("\nNow arriving: " + room_list[current_room][0])
        shipcheck()
        newsector()
        break
    elif direction == "2":
      next_room = room_list[current_room][2]
      if next_room == None:
        print("  Navigating your ship to that sector would result in certain death. Please choose a different direction. \n")
      else:
        print("  Initializing warp drive...")
        time.sleep(0.5)
        print("  Warp drive charged. Commencing warp...")
        time.sleep(1)
        passed_rooms.append(current_room)
        current_room = next_room
        #moves game time forward 
        updatedays(warpcost)
        warpjumps += 1
        clear()
        introtext()
        print("\nNow arriving: " + room_list[current_room][0])
        shipcheck()
        newsector()
        break
    elif direction == "3":
      next_room = room_list[current_room][3]
      if next_room == None:
        print("  Navigating your ship to that sector would result in certain death. Please choose a different direction. \n")
      else:
        print("  Initializing warp drive...")
        time.sleep(0.5)
        print("  Warp drive charged. Commencing warp...")
        time.sleep(1)
        passed_rooms.append(current_room)
        current_room = next_room
        #moves game time forward 
        updatedays(warpcost)
        warpjumps += 1
        clear()
        introtext()
        print("\nNow arriving: " + room_list[current_room][0])
        shipcheck()
        newsector()
        break
    elif direction == "4":
      next_room = room_list[current_room][4]
      if next_room == None:
        print("  Navigating your ship to that sector would result in certain death. Please choose a different direction. \n")
      else:
        print("  Initializing warp drive...")
        time.sleep(0.5)
        print("  Warp drive charged. Commencing warp...")
        time.sleep(1)
        passed_rooms.append(current_room)
        current_room = next_room
        #moves game time forward 
        updatedays(warpcost)
        warpjumps += 1
        clear()
        introtext()
        print("\nNow arriving: " + room_list[current_room][0])
        shipcheck()
        newsector()
        break
    elif direction == "5":
      print("\n  Returning...")
      time.sleep(rettime)
      newsector()
    else:
      print("  Please enter a valid choice.")



#checks for damaged systems & warns player if any found
def shipcheck():
  global coresys_names,coresys_status,auxsys_names,auxsys_status,cryopods,daysremaining,warnings
  if coresys_status[2] == "Damaged": #life support 
    daysremaining -= 1 #subtracts an additional day per warp
    x = 0
    if x == 0:
      if "Due to Life Support system damage, the Ark will lose 1 days worth of water on every jump." not in warnings:
        warnings.append("Due to Life Support system damage, the Ark will lose 1 days worth of water on every jump.")
      x += 1
  elif auxsys_status[0] == "Damaged": #cryo storage
    cryopods -= 1 #subtract a cryopod per warp if damaged
    x = 0
    if x == 0:
      if "Due to Cryogenic Storage system damage, the ark will lose 1 cryo pod per jump. At least 10 cryo pods are required to colonize a new planet." not in warnings:
        warnings.append("Due to Cryogenic Storage system damage, the ark will lose 1 cryo pod per jump. At least 10 cryo pods are required to colonize a new planet.")
      x += 1


#checks if game has ended. if yes, provide ending details
def endingchecker():
  global ended,cryopods,daysremaining,coresys_status,dayspassed,warpjumps
  if cryopods <= 10: #bad end; out of cryopods
    ended = True
    clear()
    introtext()
    time.sleep(1)
    print("  Unfortunately, after " + str(dayspassed) + " day(s) of travel and " + str(warpjumps) + " warp jumps made, your journey to save humanity has come to a close. Due to your recklessness, the Ark no longer has enough cryo pods to jump start humanity.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 1/7]")
  elif daysremaining <= 0: #bad end; out of water
    ended = True
    clear()
    introtext()
    time.sleep(1)
    print("  Unfortunately, after " + str(dayspassed) + " day(s) of travel and " + str(warpjumps) + " warp jumps made, your journey to save humanity has come to a close. Due to a failure in the Ark's Life Support system caused by a lack of water, all life on board the vessel was terminated, along with all " + str(cryopods) + " cryo pods that contained the last of humanity.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 2/7]")
  elif coresys_status[0] == "Offline": #bad end; bridge offline
    ended = True
    clear()
    introtext()
    time.sleep(1)
    print("  Unfortunately, after " + str(dayspassed) + " day(s) of travel and " + str(warpjumps) + " warp jumps made, your journey to save humanity has come to a close. Due to a critical failure in the Ark's Bridge, all core and auxilary systems have overloaded and failed resulting in the loss of all resources, including the " + str(cryopods) + " cryo pods that contained the last hope of humanity.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 3/7]")
  elif coresys_status[1] == "Offline": #bad end; reactor offline
    ended = True
    clear()
    introtext()
    time.sleep(1)
    print("  Unfortunately, after " + str(dayspassed) + " day(s) of travel and " + str(warpjumps) + " warp jumps made, ygour journey to save humanity has come to a close. Due to a critical failure in the Ark's Reactor, all core and auxilary systems have lost power and failed resulting in the loss of all resources, including the " + str(cryopods) + " cryo pods that contained the last of humanity.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 4/7]")
  elif coresys_status[2] == "Offline": #bad end; life support offline
    ended = True
    clear()
    introtext()
    time.sleep(1)
    print("  Unfortunately, after " + str(dayspassed) + " days of travel and " + str(warpjumps) + " warp jumps made, your journey to save humanity has come to a close. Due to the immense amount of damage sustained by the Life Support system, all life on board the vessel was terminated, along with all " + str(cryopods) + " cryo pods on board.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 5/7]")


#called if player has achieved a positive ending. finishes the game.
def goodending(endtype,finalplanet):
  global ended,cryopods,dayspassed,warpjumps,current_room
  if endtype == "good": #good end; landed on correct planet
    clear()
    introtext()
    ended = True
    print("  Congratulations!\n\n  After " + str(dayspassed) + " days of travel and " + str(warpjumps) + " total warp jumps made, your journey to save humanity has come to a successful close. You have landed the Ark on Speronova, humanity's new home for the foreseeable future, repopulating the planet with a group of " + str(cryopods) + " colonists, finally freed from their cryogenic sleep.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 6/7]")
  elif endtype == "neutral": #neutral end; landed on a planet
    clear()
    introtext()
    ended = True
    print("  Well done.\n\n  After " + str(dayspassed) + " days of travel and " + str(warpjumps) + " total warp jumps made, you have chosen to settle on " + str(finalplanet))
    print("\n  For the near future, the remaining " + str(cryopods) + " colonists on board, finally awoken from their cryogenic sleep, can do their best to survive on the planet that you have chosen for them.\n\n  However, there is no telling how long they will last on this planet, where resources are sparse and difficult to use.")
    time.sleep(0.5)
    print("\n  Thank you for playing Aqua Adventure 2. Feel free to play again. [Ending 7/7]")
