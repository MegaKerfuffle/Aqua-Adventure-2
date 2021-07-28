'''
Name: Robert Brzostek
Date: 1/7/2019
ICS3U/C ISU game
Aqua Adventure 2
'''

#This file is used to define the variables that all other files within this project use, in order to easily change certain characteristics of the game and to make sure that functions from one file work with functions from another

#Time variables
global stime
stime = 2.5 #time between story text
global sstime
sstime = 1 #time between short story text
global rettime
rettime = 1 #time to pass when returning from a function
global dayspassed 
dayspassed = 0 #number of days passed since game start
global daysremaining 
daysremaining = 12 #number of days remaining before player loses

#Navigation variables
global warpjumps
warpjumps = 0 #tracks number of jumps made since game start
global warpcost
warpcost = 1 #number of days it takes to warp from one sector to another
global current_room
current_room = 0 #tracks current sector number (minus 1, technically)

#Resource variables
global dronenum 
dronenum = 5  #number of deployable drones to start with(planetary scans)
global cryopods
cryopods = 30 #number of remaining cryopods to start with (final colonization; need at least 10 to win)
global scrap
scrap = 25 #amount of scrap to start with (repairs; building drones)

#Scan variables
global scanlog
scanlog = "  No scan logs are available." #keeps last made scan (either close, short, or far)

#Misc variables
global ended
ended = False #check if game has ended yet

#Navigation lists
global room_list
room_list = [] #names, descriptions, and navigation instructions for each room (sector) in the game
global story_list
story_list = [] #story-based descriptions for each sector
global passed_rooms
passed_rooms = [0] #tracks which rooms the player has passed already

#Scan lists
global scanresults_close
scanresults_close = [] #results of drone exploration scan
global scanresults_short
scanresults_short = [] #results of sector (short range) scan
global scanresults_long
scanresults_long = [] #results of next sector (long distance) scan

#System lists
#Core
global coresys_names
coresys_names = ["Bridge","Reactor","Life Support"] #core system names
#0,1,2
global coresys_status
coresys_status = ["Online","Online","Online"] #current system status (can be Online, Damaged, or Offline)
global coresys_damaged
coresys_damaged = [10,20,15] #scrap cost to repair damaged core system

#Aux
global auxsys_names
auxsys_names = ["Cryogenic Storage","Drone Dispatcher","Short Range Scanner","Long Distance Scanner"]
#0,1,2,3
global auxsys_status
auxsys_status = ["Online","Online","Online","Online"] #current system status (can be Online, Damaged, or Offline)
global auxsys_damaged
auxsys_damaged = [20,10,15,20,15] #scrap cost to repair damaged aux system
global auxsys_offline
auxsys_offline = [35,20,20,30,25] #scrap cost to repair offline aux system

#Misc lists
global tutlist
tutlist = [] #text to print during the tutorial
global rngevents
rngevents = [] #used to provide random encounter information and options
global rnghelp
rnghelp = [None,None,"Cryo Pods","Drones","Scrap","Water"] #used to simplify printing
global colonizelist
colonizelist = [] #used to provide end-game planet colonization reports
global warnings
warnings = [] #used to store any active system warnings

#list provides scanning results for objects in the current sector
scanresults_short = ["  This sector has been abandoned by humanity for at least the last 20 years, when the Great War ravaged the surface and surrounding space of Earth. Scans indicate the presence of four planets, one of which may be suitable for human habitation (CBP-SA-1). Drone scan of planet recommended.","  This sector is mostly empty, with very few resources available. A few asteroids orbit around silently, with a single planet (likely hostile to life) and its moon.",
"  Short scan indicates the presence of an asteroid field in this sector, providing cover for a single planet (CBP-SC-1). Previous signs of life are clearly visible on the surface of said planet, and some leftover water may be available. Drone scan of planet recommended.",
"  This sector is constantly being pummeled by extremely deadly amounts of cosmic radiation from the pulsar at it's core. One lonely planet orbits around the star, with few resources available on its surface.",
"  Short scan has successfully identified three celestial bodies within this sector, including two planets and one moon. Planets do not appear to be habitable at first glance, however a drone scan may provide more information.",
"  This sector appears to be remarkably similar to Sector A, and may be the ideal location for the rebirth of humanity. One planet in particular (CBP-SF-2) appears to be specifically optimized for life. Drone scan of planet recommended."]

#list provides scanning results for nearby sectors (directions) and potential objects in nearby sectors
scanresults_far = ["  Long-distance scans indicate the presence of a sector to the South, home to one large celestial body, and a sector to the East, home to two large celestial bodies.","  Long-distance scans indicate the presence of a sector to the West, home to four large celestial bodies, a sector to the South, home to three large celestial bodies, and a sector the East, home to one large celestial body.","  Long-distance scans indicate the presence of a sector to the West, home to two large celestial bodies, and a sector to the South, home to three large celestial bodies.","  Long-distance scans indicate the presence of a sector to the North, home to four large celestial bodies, and a sector to the East, home to three large celestial bodies.","  Long-distance scans indicate the presence of a sector to the West, home to one large celestial bodies, a sector to the North, home to two large celestial bodies, and a sector to the East, home to three large celestial bodies.","  Long-distance scans indicate the presence of a sector to the West, home to three large celestial bodies, and a sector to the North, home to one large celestial body."]


#Populate room_list with room info
room = ["\nSector A - Your ship returns to humanity's original home. Earth, now barren and void of life, is visible far in the distance, and the remains of human spaceflight remain floating ominously in orbit.",None,1,3,None]
room_list.append(room)
room = ["\nSector B - Your ship arrives in a mostly empty sector. Looking out of the bridge, you see a lonely red planet with a small moon orbiting a dying star.",None,2,4,0]
room_list.append(room)
room = ["\nSector C - You hear the sound of your ship's warp drive spooling down as it arrives in another sector. You recall that humanity once had great ambitions for this sector.",None,None,5,1]
room_list.append(room)
room = ["\nSector D - Upon completing the warp into this sector, your ship is bombarded with severe cosmic radiation. Stepping outside of the confines of the ship would result in immediate death, but you are safe within the strong hull of the Ark.",0,4,None,None]
room_list.append(room)
room = ["\nSector E - According to humanity's final map of the cosmos, the sector that you've arrived in does not exist. You must have warped to the very edge of the continually expanding universe.",1,5,3,None]
room_list.append(room)
room = ["\nSector F - Your ship arrives in Sector F. Reports indicate the presence of at least two planets in orbit around a red dwarf star.",2,None,4,None]
room_list.append(room)


#Populate story_list with necessary story elements
sectstory = "\n=== Sector A ===\nA sector thoroughly ravaged by war and desperation, Sector A now bears the remains of humanity. Old burnt out ships and satellites still float around the dead sector, awaiting their eventual destruction."
story_list.append(sectstory)
sectstory = "\n=== Sector B ===\nThis sector, being only 1 warp day away from humanity's original home, has seen a decent amount of post-war traffic. A destroyed Remnant space station orbits around the Sector's star."
story_list.append(sectstory)
sectstory = "\n=== Sector C ===\nBefore the war, some governments had planned to convert Sector C into a military testing ground. After the war, a faction known as the Remnants had their primary research base set up on a planet here, before moving their research away to a new Sector."
story_list.append(sectstory)
sectstory = "\n=== Sector D ===\nSector D, being the home of a deadly pulsar, has always been more or less ignored by astronomers both pre-war and post-war. Intense radiation prevents human habitation in this sector."
story_list.append(sectstory)
sectstory = "\n=== Sector E ===\nA newly-created sector, in terms of universal time. Before the war, this area of space had not existed, or was not visible with any scanning methods available to mankind at the time."
story_list.append(sectstory)
sectstory = "\n=== Sector F ===\nIn previous years, the Remnants seemed to have some sort of fascination with this sector, before their eventual disappearance into deep space."
story_list.append(sectstory)


#Populate scanresults_close with planet names, reports, and additional info

#Intermediary list of lists for planets in each sector
sector0p = []
sector1p = []
sector2p = []
sector3p = []
sector4p = []
sector5p = []
#Consolidates list of lists into a final list (scanresults_close)
scanresults_close = [sector0p,sector1p,sector2p,sector3p,sector4p,sector5p]

#Sector 0 planets (initial)
planet = ["CBP-SA-1 - Earth","Once a thriving planet full of life, resources and hope, the Earth that humanity has left behind is now a festering wasteland.\n  All major oceans have since dried up, with limited amounts of water available within the toxic atmosphere. Substantial amounts of scrap are available from the remains of civilization, both on the surface and in orbit.\n  Had it not been destroyed by both humanity and nature, Earth would be the ideal planet to colonize.",3,8,2,2]
scanresults_close[0].append(planet)
planet = ["CBM-SA-2 - Moon","Humans had never really bothered to return to the Moon, apart from a few scientific missions that experimented with terraforming at a large scale.\n  Despite the overall failure of the terraforming experiments, some success was found with the creation of a small artificial ocean. Some scrap is available from the abandoned terraforming equipment left behind by Remnant scientists.\n  Realistically speaking, the Moon was never really a viable option for human colonization.",3,3,1,3]
scanresults_close[0].append(planet)
planet = ["CBP-SA-3 - Mars","Despite a few early attempts in the 21st Century, humanity had never successfully colonized the planet of Mars.\n  Trace amounts of water can still be found in the Martian soil, even after the desperate attempts of the Remnants to restore the environment of Earth using the resources of Mars. Failed small scale colonization efforts have left behind a decent amount of scrap.\n  Had conditions improved, Mars could have been a viable option for human habitation.",2,2,2,2]
scanresults_close[0].append(planet)
planet = ["CBP-SA-4 - Venus","Venus, one of the few remaining planets free from the grasp of humanity, has always proven to be a worth adversary for humans searching for a new home.\n  Due to the hot nature of the planet, drones have a difficult time collecting the gaseous water from the atmosphere. Some scrap remains on the surface in the form of an early unmanned exploration mission.\n  Venus continues to be the hostile planet that it has always been, although some pre-war rumors indicate that a human colony may exist somewhere on the planet.",3,4,1,1]
scanresults_close[0].append(planet)

#Sector 1 planets
planet = ["CBP-SB-1 - Dorcus","A large, red planet composed mainly of gases and a relatively small, dense core. Remnant research vessels used to periodically orbit Dorcus, searching for potential sources of energy and water, and signs of life.\n  Due to the gaseous nature of the planet, significant amounts of water can be found in the atmosphere. Plenty of old Remnanat exploration drones still float around the surrounding area, supplying ample amounts of scrap.\n  As a gas planet, Dorcus is inhospitable to most lifeforms, including humans.",3,5,2,1]
scanresults_close[1].append(planet)
planet = ["CBM-SB-2 - Concordia","Dorcus' single moon. Extremely prone to meteor strikes and solar flares.\n  Thanks to the countless meteor strikes that this moon experiences, some amount of water is obtainable on the surface. The rocks on Concordia have a unique property that allows them to easily form into scrap metals.\n  Due to it's dangerous environment and proximity to a sun, Concordia is an inadequate location for human habitation.",3,4,1,1]
scanresults_close[1].append(planet)

#Sector 2 planets
planet = ["CBP-SC-1 - Deltia","One of the few planets that humanity had managed to establish a foothold on out in deep space, Deltia was used by the Remnants as a weapons testing ground and research base.\n  After building their now-abandoned research facility, Remnant scientists had managed to produce small amounts of water that they then released into the atmosphere. The scattered remains of the research facility provide an excellent amount of scrap.\n  Deltia's location far away from it's sun rules it out as the future home of humanity.",3,8,2,3]
scanresults_close[2].append(planet)

#Sector 3
planet = ["CBM-SD-1 - Hibernia","An old moon surrounded by a massive asteroid belt, stretching out across the sector. Scans of the asteroids indicate that the belt is the remains of an old planet.\n  Despite a thorough search, no water could be found on the surface or in the atmosphere of this moon. Since humanity had never quite made it this far before, very little scrap is available on Hibernia.\n  Being surrounded by a hostile environment, including the severe radiation in this sector, Hibernia would not be a suitable location for the last bastion of mankind.",1,3,2,1]
scanresults_close[3].append(planet)

#Sector 4
planet = ["CBP-SE-1 - Kattos","An ancient, once-thriving planet, Kattos was home to the largest extraterrestrial forest ever discovered. Now, however, Kattos has been left with no more than the roots of alien trees, and a severely damaged atmosphere.\n  Since this planet was once home to a large forest, some water can still be found underneath the surface of Kattos. Limited amounts of scrap are also available, once harvested from the underground caves of the planet.\n  While it was the origin of the first sightings of extraterrestrial life, Kattos now lies in ruins, making it unsuitable for colonization.",4,3,2,3]
scanresults_close[4].append(planet)
planet = ["CBP-SE-2 - Jestos","One of the planets visited by a deep space exploration probe long before the great war. Jestos is a very hostile planet, with a highly acidic atmosphere that would tear through the hull of any ship that dares attempt a landing.\n  Trace amounts of water can be found within the chemical makeup of the dangerous acid surrounding the surface of this planet. What remains of the ancient exploration drone on the surface may be salvaged for scrap metal.\n  Jestos is quite obviously not a good choice for human habitation.",1,1,1,2]
scanresults_close[4].append(planet)
planet = ["CBM-SE-3 - Nomdia","Jestos' single moon, last seen by a human through the camera of a deep space exploration drone. Nomdia remains a desolate and empty celestial body, with few resources and no surface life.\n  Long ago, when the exploration drone passed overhead, it had dropped some of it's cargo to the surface in order to test the effect of a high-speed impact on the moon's surface, leaving some scrap material behind.\n  Nomdia would be an inadequate choice for human colonization.",3,5,3,1]
scanresults_close[4].append(planet)

#Sector 5 planets (final)
planet = ["CBP-SF-1 - Norga","Sister planet to Speronova (CBP-SF-2), Norga has been free from any sort of life for hundreds of years.\n  This planet was at one point home to a large fresh water ocean, which has since dissipated back into space. A minor amount of scrap is available from the naturally forming resources on the planet.\n   At one point, Norga would have made an excellent home for humanity, but it now lies deformed and void of life.",4,5,3,1]
scanresults_close[5].append(planet)
planet = ["CBP-SF-2 - Speronova","A fairly new planet, born out of the death of an ancient star. Surface scans seem to indicate the presence of foliage, similar to what used to be found on Earth.\n  After piercing through the strong atmosphere, the exploration drone splashed down into a massive fresh water ocean. Subsurface scans indicate the presence of resources that may be used to create scrap building supplies.\n  Thanks to it's ideal placement within Sector F, Speronova is the ideal candidate for humanity's new home. Colonization recommended.",20,10,3,2] #good ending planet
scanresults_close[5].append(planet)
planet = ["CBM-SF-3 - Horus","Speronova's single moon, similar in size and position to Earth's own moon.\n  Since it is a moon, very few samples of water and scrap are available below it's surface.\n  Horus is not an adequate location for colonization.",2,3,2,1]
scanresults_close[5].append(planet)


#Populate tutlist with necessary info
tut = "Aqua Adventure 2 is entirely text-based, and as such is fairly easy to navigate.\n\nThe game will present you with several options often. Each option is associated with a number.\n\nTo select the option you want, enter the number that corresponds with it when the game prompts you to.\n\nAt some points in the game, you may be faced with special dialog options that provide additional functions for the cost of a ship resource, or time." #tutlist[0]
tutlist.append(tut)
tut = "By selecting a time option, you have fewer days to successfully reach your destination. However, most time options will give you navigation hints, addtional resources, or random encounters, so it may be wise to use them on occassion." #tutlist[1]
tutlist.append(tut)
tut = "\nSelecting a resource option results in the loss of a resource or component stored on your ship. If you lose too many resources or components, you will lose the game. These options are commonly found in random encounters." #tutlist[2]
tutlist.append(tut)
tut = "\nCongratulations! You should now know the basic controls and functions of the game!" #tutlist[3]
tutlist.append(tut)


#Populate rngevents with random event details & stats
#sudden asteroid belt
rng = ["  After warping in, a blaring siren is set off in the Ark's bridge. An asteroid belt has formed in this sector, and the onboard AI requests that you activate the defense turrets to protect the ship.\n\n  However, due to a flaw in the ship's design, activating the turrets will result in a loss of power in Cryogenic Storage.","\n  What would you like to do?\n    1) Activate ship defenses [-25 cryo pods, system damage]\n    2) Attempt evasive manueuvers [-10 scrap, -2 drones, system damage]\n  >"]
rnggood = ["Cryogenic Storage","Damaged",-10,0,0,0]
rng.append(rnggood)
rngbad = ["Reactor","Damaged",0,-2,-10,0]
rng.append(rngbad)
rngevents.append(rng)

#remnant encounter
rng = ["  Moments after the completion of warp procedure, prelimary scans indicate the presence of a Remnant vessel in the sector. They appear to be closing in on your ship with weapons charging.\n\n  The Ark's AI recommends switching to full combat mode, at the cost of increased Reactor usage and potential overload.","\n  What would you like to do?\n    1) Full Combat Mode [-2 drones, -5 days of water, system damage]\n    2) Shelter in Place [-15 scrap, -5 cryopods, system damage]\n  >"]
rnggood = ["Reactor","Damaged",0,-2,0,-5]
rng.append(rnggood)
rngbad = ["Bridge","Damaged",-5,0,-15,0]
rng.append(rngbad)
rngevents.append(rng)

#desperate survivor encounter
rng = ["  You are hailed on an emergency frequency by a desperate survivor of the destruction of Earth. They introduce themselves as one of mankind's pre-war elite, who managed to escape to a space station before humanity destroyed itself. The survivor demands that you send over a drone full of resources, or they will arm their advanced ship weapons and destroy your ship.","\n  What would you like to do?\n    1) Comply and send the drone [-1 drone, -5 cryo pods, -10 scrap, -5 days of water]\n    2) Arm the Ark's Defense Turrets [-2 drones, -2 days of water, system damage\n  >"]
rnggood = ["None","None",-5,-1,-10,-2]
rng.append(rnggood)
rngbad = ["Bridge","Offline",0,-2,0,-2]
rng.append(rngbad)
rngevents.append(rng)

#automated trade ship 
rng = ["  Upon entering the current sector, your ship's AI informs you that an automated trading vessel is within radio range. It recommends opening up trade dialogs, but your instinct tells you that it's an ambush waiting to happen.","\n  What would you like to do?\n    1) Contact the automated ship [+5 drones, +10 scrap, -5 days of water]\n    2) Ignore it and continue\n  >"]
rnggood = ["None","None",0,5,10,-5]
rng.append(rnggood)
rngbad = ["None","None",0,0,0,0]
rng.append(rngbad)
rngevents.append(rng)

#automated trade ship 
rng = ["  Upon entering the current sector, your ship's AI informs you that an automated trading vessel is within radio range. It recommends opening up trade dialogs, but your instinct tells you that it's an ambush waiting to happen.","\n  What would you like to do?\n    1) Contact the automated ship [-5 cryo pods, -1 drone, -5 scrap]\n    2) Engage it with the Defense Turrets [-1 drone, +10 scrap, system damage\n  >"]
rnggood = ["None","None",-5,-1,-5,0]
rng.append(rnggood)
rngbad = ["Short Range Scanner","Offline",0,-1,+10,0]
rng.append(rngbad)
rngevents.append(rng)

#overstressed reactor (deadly)
rng = ["  After completing your warp sequence, an alarm is sounded on the Ark's bridge. According to the on-board AI, the ship's reactor has been overstressed in the last warp, and is threatening the structural integrity of the vessel. Jettisoning excess cargo and disabling the Drone Dispatcher may prevent a catastrophic explosion. Alternatively, the AI recommends waiting a few days to lower the Reactor's stress level.","\n  What would you like to do?\n    1) Jettison cargo [-5 drones, -10 scrap, -2 days of water]\n    2) Wait a few days [5 days]\n  >"]
rnggood = ["Drone Dispatcher","Offline",0,-5,-10,-2]
rng.append(rnggood)
rngbad = ["Reactor","Offline",0,0,0,0]
rng.append(rngbad)
rngevents.append(rng)

#overstressed reactor 
rng = ["  After completing your warp sequence, an alarm is sounded on the Ark's bridge. According to the on-board AI, the ship's reactor has been overstressed in the last warp, and is threatening the structural integrity of the vessel. Jettisoning excess cargo and disabling the Drone Dispatcher may prevent a catastrophic explosion. Alternatively, the AI recommends waiting a few days to lower the Reactor's stress level.","\n  What would you like to do?\n    1) Jettison cargo [-5 drones, -10 scrap, -2 days of water]\n    2) Wait a few days [5 days]\n  >"]
rnggood = ["Drone Dispatcher","Offline",0,-5,-10,-2]
rng.append(rnggood)
rngbad = ["Reactor","Damaged",0,0,0,-5]
rng.append(rngbad)
rngevents.append(rng)



