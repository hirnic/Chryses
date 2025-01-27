# This is Chryses, a variant of the online game Ogame. As this is version 1, I am going to try to clone the game
# mechanics manually, except for moons. We will deal with moons in version 2. Also in version 1 I will implement a
# simple bot to automatically play the game alongside the player. The name of the game comes from Greek mythology.
# It was my dad's idea to name it Chryses, and I liked it.

# This is the main page and it takes care of the Graphical User Interface (GUI). We will start very basic and make it
# more difficult once we flesh out the major details (see other three files). The biggest headache is that Python reads
# code line-by-line, so the main menu starts at the bottom and the more deeply-nested commands are at the top.

import Classes
import SDB
import DDB
import tkinter as tk
import time


# from tkinter import ttk
player = 0
currentPlanet = Classes.Planet("Zebulon", [-1,-1,-1], -1, [9999999,9999999,9999999,9999999])
currentView = "Overview"  #What screen is the player looking at?
screen = 0
universeSpeed = DDB.universeSpeed

# The GUI will be a window with a bunch of buttons. Some text boxes for entering numbers, but mostly buttons.
root = tk.Tk()
root.title("Chryses GUI")
canvas = tk.Canvas(root)
canvas.pack()

mainFrame = tk.Frame(root,  bg="grey")
resourcesFrame = tk.Frame(root, bg="grey")
allFrames = {"Main Frame" : mainFrame,

            "planetsFrame1" : tk.Frame(root, bg="grey"),
             "planetsFrame2" : tk.Frame(root, bg="grey"),
             "planetsFrame3" : tk.Frame(root, bg="grey"),
             "planetsFrame4" : tk.Frame(root, bg="grey"),

             "Resources Frame" : resourcesFrame,

             "Queue Frame" : tk.Frame(root, bg="grey"),
             }

allButtons = { # Main Menu Buttons
    "New Game Button": tk.Button(root, text="New Game", pady = 1),
    "Load Game Button" : tk.Button(root, text="Load Game", pady = 1),
    "Options Button" :tk.Button(root, text="Options", pady = 1),
    "Quit Button" : tk.Button(root, text="Quit", pady = 1),

    # Player Overview buttons
    "Overview" : tk.Button(root, text = "Overview", height = 1),
    "View Buildings" : tk.Button(root, text = "View Buildings", padx= 1, pady = 1),
    "View ResearchLab" : tk.Button(root, text ="View Research", padx= 1, pady = 1),
    "View Shipyard" : tk.Button(root, text = "View Shipyard", padx= 1, pady = 1),
    "View Defenses" : tk.Button(root,text = "View Defenses", padx= 1, pady = 1),
    "View Galaxy" : tk.Button(root, text = "View Galaxy", padx= 1, pady = 1),
    "Manage Fleets" : tk.Button(root, text = "Manage Fleets", padx= 1, pady = 1),
    "Left Arrow" : tk.Button(root, text = "<", padx= 1, pady = 1),
    "Right Arrow" : tk.Button(root, text = ">", padx= 1, pady = 1),

    "Resource Management" : tk.Button(resourcesFrame, text = "Resources"),

    # Constructions buttons
    "Buildings Purchase Button" : tk.Button(mainFrame, text="Purchase")
}

allLabels = {
    "Metal Title" : tk.Label(resourcesFrame, text = "Metal"),
    "Crystal Title" : tk.Label(resourcesFrame, text = "Crystal"),
    "Deuterium Title" : tk.Label(resourcesFrame, text = "Deuterium"),
    "Energy Title" : tk.Label(resourcesFrame, text = "Energy"),
    "Time Title" : tk.Label(resourcesFrame, text = "Current Time"),
    "Metal Amount" : tk.Label(resourcesFrame, text = ""),
    "Crystal Amount" : tk.Label(resourcesFrame, text = ""),
    "Deuterium Amount" : tk.Label(resourcesFrame, text = ""),
    "Energy Amount" : tk.Label(resourcesFrame, text = ""),
    "Time Amount" : tk.Label(resourcesFrame, text = ""),

    "Queue Title" : tk.Label(allFrames["Queue Frame"], text = "Production Queue"),
    "Buildings Queue" : tk.Label(allFrames["Queue Frame"], text = "Buildings: None"),

    "Resource Settings Source 0" : tk.Label(root, text = "Exit"),
    "Resource Settings Source 1" : tk.Label(root, text = "Basic Income"),
    "Resource Settings Source 2" : tk.Label(root, text = "Metal Mine"),
    "Resource Settings Source 3" : tk.Label(root, text = "Crystal Mine"),
    "Resource Settings Source 4" : tk.Label(root, text = "Deuterium Synthesizer"),
    "Resource Settings Source 5" : tk.Label(root, text = "Solar Plant"),
    "Resource Settings Source 6" : tk.Label(root, text = "Fusion Plant"),
    "Resource Settings Source 7" : tk.Label(root, text = "Solar Satellites"),
    "Resource Settings Source 8" : tk.Label(root, text = "Hourly Income"),
    "Resource Settings Source 9" : tk.Label(root, text = "Daily Income"),
    "Resource Settings Source 10" : tk.Label(root, text = "Weekly Income"),
    "Resource Settings Source 11" : tk.Label(root, text = "Storage Capacity"),
    "Resource Settings Metal 0" : tk.Label(root, text = "Metal"),
    "Resource Settings Metal 1" : tk.Label(root, text = str(universeSpeed*100)),
    "Resource Settings Metal 2" : tk.Label(root, text = "0"),
    "Resource Settings Metal 3" : tk.Label(root, text = "0"),
    "Resource Settings Metal 4" : tk.Label(root, text = "0"),
    "Resource Settings Metal 5" : tk.Label(root, text = "0"),
    "Resource Settings Metal 6" : tk.Label(root, text = "0"),
    "Resource Settings Metal 7" : tk.Label(root, text = "0"),
    "Resource Settings Metal 8" : tk.Label(root, text = "0"),
    "Resource Settings Metal 9" : tk.Label(root, text = "0"),
    "Resource Settings Metal 10" : tk.Label(root, text = "0"),
    "Resource Settings Metal 11" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 0" : tk.Label(root, text = "Crystal"),
    "Resource Settings Crystal 1" : tk.Label(root, text = str(universeSpeed*33)),
    "Resource Settings Crystal 2" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 3" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 4" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 5" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 6" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 7" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 8" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 9" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 10" : tk.Label(root, text = "0"),
    "Resource Settings Crystal 11" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 0" : tk.Label(root, text = "Deuterium"),
    "Resource Settings Deuterium 1" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 2" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 3" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 4" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 5" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 6" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 7" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 8" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 9" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 10" : tk.Label(root, text = "0"),
    "Resource Settings Deuterium 11" : tk.Label(root, text = "0"),
    "Resource Settings Energy 0" : tk.Label(root, text = "Energy"),
    "Resource Settings Energy 1" : tk.Label(root, text = "0"),
    "Resource Settings Energy 2" : tk.Label(root, text = "0"),
    "Resource Settings Energy 3" : tk.Label(root, text = "0"),
    "Resource Settings Energy 4" : tk.Label(root, text = "0"),
    "Resource Settings Energy 5" : tk.Label(root, text = "0"),
    "Resource Settings Energy 6" : tk.Label(root, text = "0"),
    "Resource Settings Energy 7" : tk.Label(root, text = "0"),
    "Resource Settings Energy 8" : tk.Label(root, text = "0"),
    "Resource Settings Energy 9" : tk.Label(root, text = "0"),
    "Resource Settings Energy 10" : tk.Label(root, text = "0"),
    "Resource Settings Energy 11" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 0" : tk.Label(root, text = "Set Rate"),
    "Resource Settings Production Rate 1" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 2" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 3" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 4" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 5" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 6" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 7" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 8" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 9" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 10" : tk.Label(root, text = " "),
    "Resource Settings Production Rate 11" : tk.Label(root, text = " "),

    "Buildings Info Title" : tk.Label(mainFrame, text = " "),
    "Buildings Info Metal": tk.Label(mainFrame, text=" "),
    "Buildings Info Crystal": tk.Label(mainFrame, text=" "),
    "Buildings Info Deuterium": tk.Label(mainFrame, text=" "),
    "Buildings Info Energy": tk.Label(mainFrame, text=" "),
    "Buildings Info Time": tk.Label(mainFrame, text=" "),

    "Buildings Picture Frame": tk.Label(mainFrame, bg="sky blue", text = " "),
    "Metal Mine": tk.Label(root, bg="grey", text = " "),
    "Crystal Mine": tk.Label(root, bg="grey", text = " "),
    "Deuterium Synthesizer": tk.Label(root, bg="grey", text = " "),
    "Solar Plant": tk.Label(root, bg="grey", text = " "),
    "Fusion Reactor": tk.Label(root, bg="grey", text = " "),
    "Robotics Factory": tk.Label(root, bg="grey", text = " "),
    "Nanite Factory": tk.Label(root, bg="grey", text = " "),
    "Shipyard": tk.Label(root, bg="grey", text = " "),
    "Metal Storage": tk.Label(root, bg="grey", text = " "),
    "Crystal Storage": tk.Label(root, bg="grey", text = " "),
    "Deuterium Tank": tk.Label(root, bg="grey", text = " "),
    "Research Laboratory": tk.Label(root, bg="grey", text = " "),
    "Terraformer": tk.Label(root, bg="grey", text = " "),
    "Missile Silo": tk.Label(root, bg="grey", text = " "),
}


def resize_font(event=None):
    for button in allButtons.values():
        buttonWidth = button.winfo_width()
        textLength = len(button["text"])
        buttonHeight = button.winfo_height()
        a = int(buttonWidth/textLength)
        b = int(0.75 * buttonHeight)
        button.config(font=("Arial",min(a,b)))
    for button in allLabels.values():
        buttonWidth = button.winfo_width()
        textLength = len(button["text"])
        buttonHeight = button.winfo_height()
        a = int(buttonWidth / textLength)
        b = int(0.75 * buttonHeight)
        button.config(font=("Arial", min(a, b)))


def clearGUI():
    for button in allButtons.values():
        button.place_forget()
    for frame in allFrames.values():
        frame.place_forget()
    for label in allLabels.values():
        label.place_forget()

def displayQueue():
    allFrames["Queue Frame"].place(relx=0.025, rely = 0.685, relwidth = 0.175, relheight = 0.275)
    allLabels["Queue Title"].place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.18)
    allLabels["Buildings Queue"].place(relx=0.01, rely = 0.21, relwidth = 0.98, relheight = 0.18)
    if len(currentPlanet.buildingQueue) == 0:
        allLabels["Buildings Queue"].configure(text="Buildings: None")
    else:
        allLabels["Buildings Queue"].configure(text="Buildings: " + currentPlanet.buildingQueue[0][0].name + ", " + str(
            int(currentPlanet.buildingQueue[0][2] - time.time())))

def sideNav():
    allButtons["Overview"].place(relx=0, rely=0, relwidth=0.2, relheight=0.075)
    allButtons["View Buildings"].place(relx=0, rely=.1, relwidth=0.2, relheight=0.06)
    allButtons["View ResearchLab"].place(relx=0, rely=.2, relwidth=0.2, relheight=0.06)
    allButtons["View Shipyard"].place(relx=0, rely=.3, relwidth=0.2, relheight=0.06)
    allButtons["View Defenses"].place(relx=0, rely=.4, relwidth=0.2, relheight=0.06)
    allButtons["View Galaxy"].place(relx=0, rely=.5, relwidth=0.2, relheight=0.06)
    allButtons["Manage Fleets"].place(relx=0, rely=.6, relwidth=0.2, relheight=0.06)
    displayQueue()

def topNav():
    resourcesFrame.place(relx = 0.25, rely = 0, relwidth = .695, relheight = 0.09)
    #mainFrame.place(relx = 0.25, rely = .1, relwidth=.695, relheight=0.5)
    allLabels["Metal Title"].place(relx = 0.01, rely = 0.01, relwidth = 0.1517, relheight = .49)
    allLabels["Metal Amount"].place(relx=0.01, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Metal Amount"].configure(text = str(int(currentPlanet.resources[0])))
    allLabels["Crystal Title"].place(relx = 0.1767, rely = 0.01, relwidth = 0.1517, relheight = .49)
    allLabels["Crystal Amount"].place(relx=0.1767, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Crystal Amount"].configure(text= str(int(currentPlanet.resources[1])))
    allLabels["Deuterium Title"].place(relx=0.3433, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Deuterium Amount"].place(relx=0.3433, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Deuterium Amount"].configure(text= str(int(currentPlanet.resources[2])))
    allLabels["Energy Title"].place(relx=0.51, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Energy Amount"].place(relx=0.51, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Energy Amount"].configure(text= str(currentPlanet.resourceProductionRate()["Net Energy"]))
    allButtons["Resource Management"].place(relx=0.6767, rely=0.01, relwidth=0.1517, relheight=.98)
    allLabels["Time Title"].place(relx = 0.8383, rely = 0.01, relwidth = 0.1517, relheight = 0.49)
    allLabels["Time Amount"].place(relx = 0.8383, rely = 0.51, relwidth = 0.1517, relheight = 0.49)


def update_clock():
    current_time = time.strftime("%H:%M:%S")
    allLabels["Time Amount"].config(text=current_time)


def updateEverything():
    update_clock()
    allLabels["Metal Amount"].configure(text=str(int(currentPlanet.resources[0])))
    allLabels["Crystal Amount"].configure(text=str(int(currentPlanet.resources[1])))
    allLabels["Deuterium Amount"].configure(text= str(int(currentPlanet.resources[2])))
    allLabels["Energy Amount"].configure(text= str(currentPlanet.resourceProductionRate()["Net Energy"]))
    if currentView != "Resource Settings":
        displayQueue()
    # If a building, research, ship, or defense get completed, then this refreshes the page.
    commoditiesList = currentPlanet.commodities.copy()
    DDB.updatePurchaseQueue()
    if currentPlanet.commodities != commoditiesList:
        viewDictionary[currentView]()
    DDB.updateResources()

    canvas.after(1000, updateEverything)

#######################################################################################################################

### Button: Manage Fleets

#######################################################################################################################

def fleetsScreen():
    global currentView
    currentView = "Fleets"
    clearGUI()
    sideNav()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Galaxy

#######################################################################################################################

def galaxyScreen():
    global currentView
    currentView = "Galaxy"
    clearGUI()
    sideNav()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Defenses

#######################################################################################################################

def defenseScreen():
    global currentView
    currentView = "Defense"
    clearGUI()
    sideNav()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Shipyard

#######################################################################################################################

def shipyardScreen():
    global currentView
    currentView = "Shipyard"
    clearGUI()
    sideNav()
    # Display ships
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Research

#######################################################################################################################

def researchScreen():
    global currentView
    currentView = "Research"
    clearGUI()
    sideNav()
    topNav()
    # Display research
    # Place all the buttons we can use


#######################################################################################################################

### Button: Constructions Screen

#######################################################################################################################

def purchaseBuilding(buildingName):
    DDB.buildingCashier(currentPlanet, SDB.MasterBuildingsList[buildingName])
    constructionScreen()
    examineBuilding(root, buildingName)

def examineBuilding(event, buildingName):
    # Make building info pop up in the buildings overview frame
    allLabels["Buildings Info Title"].place(relx = 0.6, rely = 0.01, relwidth = 0.39, relheight = 0.2)
    allLabels["Buildings Info Title"].configure(text = buildingName)
    allLabels["Buildings Picture Frame"].place(relx = 0.05, rely = 0.05, relwidth = 0.5, relheight = .9)
    allLabels["Buildings Picture Frame"].configure(text = "Current Level: " + str(currentPlanet.commodities[buildingName]))

    # Access databases for player-specific information
    price = currentPlanet.getPrice("Building", SDB.MasterBuildingsList[buildingName], currentPlanet.commodities[buildingName])
    timeNeeded = currentPlanet.getTime("Building", SDB.MasterBuildingsList[buildingName],currentPlanet.commodities[buildingName], universeSpeed)
    allLabels["Buildings Info Metal"].place(relx=0.6, rely=0.225, relwidth=0.39, relheight=0.1)
    allLabels["Buildings Info Metal"].configure(text = "Metal: " + str(price[0]))
    allLabels["Buildings Info Crystal"].place(relx=0.6, rely=0.35, relwidth=0.39, relheight=0.1)
    allLabels["Buildings Info Crystal"].configure(text = "Crystal: " + str(price[1]))
    allLabels["Buildings Info Deuterium"].place(relx=0.6, rely=0.475, relwidth=0.39, relheight=0.1)
    allLabels["Buildings Info Deuterium"].configure(text = "Deuterium: " + str(price[2]))
    allLabels["Buildings Info Energy"].place(relx=0.6, rely=0.6, relwidth=0.39, relheight=0.1)
    allLabels["Buildings Info Energy"].configure(text = "Energy: " + str(price[3]))
    allLabels["Buildings Info Time"].place(relx=0.6, rely=0.725, relwidth=0.39, relheight=0.1)
    allLabels["Buildings Info Time"].configure(text = str(timeNeeded) + " seconds")

    # Display buttons like upgrade, dconstruct, exit
    if (DDB.verifyTechRequirements(currentPlanet, SDB.MasterBuildingsList[buildingName])
            and DDB.verifyResourceRequirements("Building", currentPlanet, SDB.MasterBuildingsList[buildingName],1)
            and len(currentPlanet.buildingQueue) == 0):
        allButtons["Buildings Purchase Button"].place(relx = 0.75, rely = 0.875, relwidth = 0.225, relheight = 0.1)
        allButtons["Buildings Purchase Button"].configure(command = lambda:purchaseBuilding(buildingName))
    else:
        allButtons["Buildings Purchase Button"].place_forget()
    resize_font()

allLabels["Metal Mine"].bind("<Button-1>", lambda event: examineBuilding(event, "Metal Mine"))
allLabels["Crystal Mine"].bind("<Button-1>", lambda event: examineBuilding(event, "Crystal Mine"))
allLabels["Deuterium Synthesizer"].bind("<Button-1>", lambda event: examineBuilding(event, "Deuterium Synthesizer"))
solarPhoto = tk.PhotoImage(file = "Solar_Plant3.png").subsample(10,7)
allLabels["Solar Plant"].configure(image = solarPhoto)
allLabels["Solar Plant"].bind("<Button-1>", lambda event: examineBuilding(event, "Solar Plant"))
allLabels["Fusion Reactor"].bind("<Button-1>", lambda event: examineBuilding(event, "Fusion Reactor"))
allLabels["Robotics Factory"].bind("<Button-1>", lambda event: examineBuilding(event, "Robotics Factory"))
allLabels["Nanite Factory"].bind("<Button-1>", lambda event: examineBuilding(event, "Nanite Factory"))
allLabels["Shipyard"].bind("<Button-1>", lambda event: examineBuilding(event, "Shipyard"))
allLabels["Metal Storage"].bind("<Button-1>", lambda event: examineBuilding(event, "Metal Storage"))
allLabels["Crystal Storage"].bind("<Button-1>", lambda event: examineBuilding(event, "Crystal Storage"))
allLabels["Deuterium Tank"].bind("<Button-1>", lambda event: examineBuilding(event, "Deuterium Tank"))
allLabels["Research Laboratory"].bind("<Button-1>", lambda event: examineBuilding(event, "Research Laboratory"))
allLabels["Terraformer"].bind("<Button-1>", lambda event: examineBuilding(event, "Terraformer"))
allLabels["Missile Silo"].bind("<Button-1>", lambda event: examineBuilding(event, "Missile Silo"))

def constructionScreen():
    global currentView
    currentView = "Construction"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx = 0.25, rely = .1, relwidth=.695, relheight=0.5)
    allLabels["Metal Mine"].place(relx=0.25, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Crystal Mine"].place(relx=0.35, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Deuterium Synthesizer"].place(relx=0.45, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Solar Plant"].place(relx=0.55, rely=.625, relwidth=.095, relheight=.175)

    allLabels["Fusion Reactor"].place(relx=0.65, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Robotics Factory"].place(relx=0.75, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Nanite Factory"].place(relx=0.85, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shipyard"].place(relx=0.25, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Metal Storage"].place(relx=0.35, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Crystal Storage"].place(relx=0.45, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Deuterium Tank"].place(relx=0.55, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Research Laboratory"].place(relx=0.65, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Terraformer"].place(relx=0.75, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Missile Silo"].place(relx=0.85, rely=.81, relwidth=.095, relheight=.175)


#######################################################################################################################

### Button: Resource Settings

#######################################################################################################################


def resourceSettings():
    global currentView
    currentView = "Resource Settings"
    clearGUI()

    allLabels["Resource Settings Metal 2"].configure(text= str(universeSpeed*currentPlanet.resourceProductionRate()["Metal Rate"]))
    allLabels["Resource Settings Metal 8"].configure(text=str(universeSpeed*(100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 9"].configure(text=str(universeSpeed*24*(100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 10"].configure(text=str(universeSpeed*24*7*(100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 11"].configure(text=str(currentPlanet.storage[0]))
    allLabels["Resource Settings Crystal 3"].configure(text=str(universeSpeed*currentPlanet.resourceProductionRate()["Crystal Rate"]))
    allLabels["Resource Settings Crystal 8"].configure(
        text=str(universeSpeed*(33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 9"].configure(
        text=str(universeSpeed*24 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 10"].configure(
        text=str(universeSpeed*24 * 7 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 11"].configure(text=str(currentPlanet.storage[1]))
    allLabels["Resource Settings Deuterium 4"].configure(text=str(universeSpeed*currentPlanet.resourceProductionRate()["Deuterium Rate"]))
    allLabels["Resource Settings Deuterium 6"].configure(
        text=str(universeSpeed*currentPlanet.resourceProductionRate()["Fusion Rate"]))
    allLabels["Resource Settings Deuterium 8"].configure(
        text=str(universeSpeed*currentPlanet.resourceProductionRate()["Net Deuterium"]))
    allLabels["Resource Settings Deuterium 9"].configure(
        text=str(universeSpeed*24 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
    allLabels["Resource Settings Deuterium 10"].configure(
        text=str(universeSpeed*24 * 7 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
    allLabels["Resource Settings Deuterium 11"].configure(text=str(currentPlanet.storage[2]))
    allLabels["Resource Settings Energy 2"].configure(text=str(currentPlanet.resourceProductionRate()["Metal Energy"]))
    allLabels["Resource Settings Energy 3"].configure(text=str(currentPlanet.resourceProductionRate()["Crystal Energy"]))
    allLabels["Resource Settings Energy 4"].configure(text=str(currentPlanet.resourceProductionRate()["Deuterium Energy"]))
    allLabels["Resource Settings Energy 5"].configure(text=str(currentPlanet.resourceProductionRate()["Solar Production"]))
    allLabels["Resource Settings Energy 6"].configure(text=str(currentPlanet.resourceProductionRate()["Fusion Production"]))
    allLabels["Resource Settings Energy 7"].configure(text=str(currentPlanet.resourceProductionRate()["Satellite Production"]))
    allLabels["Resource Settings Energy 8"].configure(
        text=str(currentPlanet.resourceProductionRate()["Net Energy"]))
    allLabels["Resource Settings Energy 9"].configure(
        text=str(currentPlanet.resourceProductionRate()["Net Energy"]))
    allLabels["Resource Settings Energy 10"].configure(
        text=str(currentPlanet.resourceProductionRate()["Net Energy"]))

    titleList = ["Source ", "Metal ", "Crystal ", "Deuterium ", "Energy ", "Production Rate "]
    for j in range(6):
        for i in range(12):
            allLabels["Resource Settings " + titleList[j] + str(i)].place(relx=j/6+0.01, rely=i/12+0.005, relwidth=1/6-0.02, relheight = 1/12-0.01)


allButtons["Resource Management"].configure(command = resourceSettings)



#######################################################################################################################

### Button: Player Overview

#######################################################################################################################


allButtons["View Buildings"].configure(command = constructionScreen)
allButtons["View ResearchLab"].configure(command = researchScreen)
allButtons["View Shipyard"].configure(command = shipyardScreen)
allButtons["View Defenses"].configure(command = defenseScreen)
allButtons["View Galaxy"].configure(command = galaxyScreen)
allButtons["Manage Fleets"].configure(command = fleetsScreen)


def playerOverview():
    global currentView
    currentView = "Overview"
    clearGUI()
    sideNav()
    topNav()
    #
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allButtons["Left Arrow"].place(relx=0.3725, rely = 0.625, relwidth = 0.02, relheight = 0.175)
    allFrames["planetsFrame1"].place(relx=0.4, rely=.625, relwidth=.095, relheight=.175)
    allFrames["planetsFrame2"].place(relx=0.5, rely=.625, relwidth=.095, relheight=.175)
    allFrames["planetsFrame3"].place(relx=0.6, rely=.625, relwidth=.095, relheight=.175)
    allFrames["planetsFrame4"].place(relx=0.7, rely=.625, relwidth=.095, relheight=.175)
    allButtons["Right Arrow"].place(relx=0.8, rely=0.625, relwidth=0.02, relheight=0.175)

allButtons["Overview"].configure(command = playerOverview)
allLabels["Resource Settings Source 0"].bind("<Button-1>", lambda event:playerOverview())

#######################################################################################################################

### Button: New Game

#######################################################################################################################

# Carries out the process for beginning a new game.
def newGame():
    global currentPlanet
    DDB.newPlayer("Piggy", "Pig Farm")
    currentPlanet = DDB.planetList["Pig Farm"]
    playerOverview()

viewDictionary = {"Overview" : playerOverview,
                  "Construction" : constructionScreen,
                  "Research" : researchScreen,
                  "Shipyard" : shipyardScreen,
                  "Defense" : defenseScreen,
                  "Galaxy" : galaxyScreen,
                  "Fleets" : fleetsScreen,
                  "Resource Settings" : resourceSettings}



#######################################################################################################################

### Button: Load Game

#######################################################################################################################




#######################################################################################################################

### Button: Options

#######################################################################################################################




#######################################################################################################################

### Main Menu

#######################################################################################################################

# This will be the entry point of the game

# clearGUI()
# allButtons['New Game Button'].configure(command=newGame)
# allButtons['New Game Button'].place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
# allButtons['Load Game Button'].place(relx=0.2, rely=0.31667, relwidth=0.6, relheight=0.15)
# allButtons['Options Button'].place(relx=0.2, rely=0.53333, relwidth=0.6, relheight=0.15)
# allButtons['Quit Button'].configure(command = root.destroy)
# allButtons['Quit Button'].place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.15)
newGame()
updateEverything()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# Bind the window resizing event to the update_font function
root.bind('<Configure>', resize_font)
root.mainloop()
