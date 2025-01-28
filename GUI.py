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

currentPlanet = Classes.Planet("Zebulon", [-1,-1,-1], -1, [9999999,9999999,9999999,9999999])
currentPlayer = Classes.Player("Pig Farmer", [currentPlanet])
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

             "Info Frame" : tk.Frame(root, bg="grey")
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

    "Cancel Building": tk.Button(allFrames["Queue Frame"], text=" "),

    "Resource Management" : tk.Button(resourcesFrame, text = "Resources"),

    "Exit Info Frame" : tk.Button(allFrames["Info Frame"], text = "Exit"),

    # Constructions buttons
    "Purchase Button" : tk.Button(mainFrame, text="Purchase"),
    "Commodity Info Info": tk.Button(mainFrame, text="Information"),

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
    "Resource Settings Production Rate 11" : tk.Label(root, text = "Confirm"),

    "Commodity Tech Label" : tk.Label(allFrames["Info Frame"], text = " "),
    "Commodity Info Label" : tk.Label(allFrames["Info Frame"], text = " "),

    "Commodity Info Title" : tk.Label(mainFrame, text = " "),
    "Commodity Info Metal": tk.Label(mainFrame, text=" "),
    "Commodity Info Crystal": tk.Label(mainFrame, text=" "),
    "Commodity Info Deuterium": tk.Label(mainFrame, text=" "),
    "Commodity Info Energy": tk.Label(mainFrame, text=" "),
    "Commodity Info Time": tk.Label(mainFrame, text=" "),
    "Commodity Info Level": tk.Label(mainFrame, text=" "),
    "Commodity Info Tech": tk.Label(mainFrame, text="Tech Tree"),

    "Picture Frame": tk.Label(mainFrame, bg="sky blue", text = " "),
    "Shop Panel 1": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 2": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 3": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 4": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 5": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 6": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 7": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 8": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 9": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 10": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 11": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 12": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 13": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 14": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 15": tk.Label(root, bg="grey", text = " "),
    "Shop Panel 16": tk.Label(root, bg="grey", text = " "),
}

metalRate = tk.StringVar(root)
metalRate.set(str(currentPlanet.resourceSettings[0]*100.0)+"%")
crystalRate = tk.StringVar(root)
crystalRate.set(str(currentPlanet.resourceSettings[1]*100.0)+"%")
deuteriumRate = tk.StringVar(root)
deuteriumRate.set(str(currentPlanet.resourceSettings[2]*100.0)+"%")
solarRate = tk.StringVar(root)
solarRate.set(str(currentPlanet.resourceSettings[3]*100.0)+"%")
fusionRate = tk.StringVar(root)
fusionRate.set(str(currentPlanet.resourceSettings[4]*100.0)+"%")
satelliteRate = tk.StringVar(root)
satelliteRate.set(str(currentPlanet.resourceSettings[5]*100.0)+"%")

allOptionMenus = {"Metal Menu" : tk.OptionMenu(root, metalRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"),
    "Crystal Menu" : tk.OptionMenu(root, crystalRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"),
    "Deuterium Menu" : tk.OptionMenu(root, deuteriumRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"),
    "Solar Menu" : tk.OptionMenu(root, solarRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"),
    "Fusion Menu" : tk.OptionMenu(root, fusionRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"),
    "Satellite Menu" : tk.OptionMenu(root, satelliteRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%")}


allThumbnails = {"Metal Mine" : tk.PhotoImage(file = "Metal_Mine1.png").subsample(12,7),
            "Crystal Mine" : tk.PhotoImage(file = "Crystal_Mine1.png").subsample(7,7),
             # "Deuterium Synthesizer" : tk.PhotoImage(file = "Crystal_Mine1.png").subsample(7,7),
             "Solar Plant" : tk.PhotoImage(file = "Solar_Plant6.png").subsample(6,7)}


# def resize_font(event=None):
#     for button in allButtons.values():
#         buttonWidth = button.winfo_width()
#         textLength = len(button["text"])
#         buttonHeight = button.winfo_height()
#         a = int(buttonWidth/textLength)
#         b = int(0.75 * buttonHeight)
#         button.config(font=("Arial",min(a,b)))
#     for button in allLabels.values():
#         buttonWidth = button.winfo_width()
#         textLength = len(button["text"])
#         buttonHeight = button.winfo_height()
#         a = int(buttonWidth / textLength)
#         b = int(0.75 * buttonHeight)
#         button.config(font=("Arial", min(a, b)))
#     for button in allOptionMenus.values():
#         buttonWidth = button.winfo_width()
#         textLength = len(button["text"])
#         buttonHeight = button.winfo_height()
#         a = int(buttonWidth / textLength)
#         b = int(0.75 * buttonHeight)
#         button.config(font=("Arial", min(a, b)))


def clearGUI():
    for button in allButtons.values():
        button.place_forget()
    for frame in allFrames.values():
        frame.place_forget()
    for label in allLabels.values():
        label.place_forget()
    for menu in allOptionMenus.values():
        menu.place_forget()

def displayQueue():
    allFrames["Queue Frame"].place(relx=0.01, rely = 0.685, relwidth = 0.19, relheight = 0.275)
    allLabels["Queue Title"].place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.18)
    if len(currentPlanet.buildingQueue) == 0:
        allLabels["Buildings Queue"].configure(text="Buildings: None")
        allLabels["Buildings Queue"].place(relx=0.01, rely = 0.21, relwidth = 0.98, relheight = 0.18)
    else:
        allLabels["Buildings Queue"].configure(text="Buildings: " + currentPlanet.buildingQueue[0][0].name + ", " + str(
            int(currentPlanet.buildingQueue[0][2] - time.time())))
        allButtons["Cancel Building"].place(relx=0.01, rely=0.21, relwidth=0.18, relheight=0.18)
        allButtons["Cancel Building"].configure(text = "X", command = lambda:DDB.cancelConstruction(currentPlanet, "Building"))
        allLabels["Buildings Queue"].place(relx=0.2, rely = 0.21, relwidth = 0.78, relheight = 0.18)
        

def sideNav():
    allButtons["Overview"].place(relx=0.01, rely=0, relwidth=0.19, relheight=0.075)
    allButtons["View Buildings"].place(relx=0.01, rely=.1, relwidth=0.19, relheight=0.06)
    allButtons["View ResearchLab"].place(relx=0.01, rely=.2, relwidth=0.19, relheight=0.06)
    allButtons["View Shipyard"].place(relx=0.01, rely=.3, relwidth=0.19, relheight=0.06)
    allButtons["View Defenses"].place(relx=0.01, rely=.4, relwidth=0.19, relheight=0.06)
    allButtons["View Galaxy"].place(relx=0.01, rely=.5, relwidth=0.19, relheight=0.06)
    allButtons["Manage Fleets"].place(relx=0.01, rely=.6, relwidth=0.19, relheight=0.06)
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


def infoPage(commodityName):
    def update_wraplength(event):
        allLabels["Commodity Info Label"].configure(wraplength=allLabels["Commodity Info Label"].winfo_width())
        allLabels["Commodity Tech Label"].configure(wraplength=allLabels["Commodity Tech Label"].winfo_width())

    allFrames["Info Frame"].tkraise()
    allFrames["Info Frame"].place(relx = 0.37, rely = 0.01, relwidth = 0.45, relheight = 0.85)
    allButtons["Exit Info Frame"].place(relx = 0.91, rely = 0.01, relwidth = 0.08, relheight = 0.04)
    allButtons["Exit Info Frame"].configure(command = allFrames["Info Frame"].place_forget)
    allLabels["Commodity Info Label"].place(relx = 0.01, rely = 0.06, relwidth = 0.98, relheight =0.73)
    allLabels["Commodity Info Label"].bind("<Configure>", update_wraplength)
    allLabels["Commodity Info Label"].configure(text = SDB.MasterDescriptionList[commodityName], anchor = "nw", justify = "left")
    allLabels["Commodity Tech Label"].place(relx = 0.01, rely = 0.81, relwidth = 0.98, relheight = 0.18)
    allLabels["Commodity Tech Label"].bind("<Configure>", update_wraplength)
    techRequired = Classes.technologyTree[commodityName]
    string = "Technology required: "
    for item in techRequired:
        string = string  + str(item) + " level " + str(techRequired[item])+ "\n"
    allLabels["Commodity Tech Label"].configure(text = string, anchor = "nw", justify = "right")


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


def purchaseCommodity(commodityName, purchaseType):
    DDB.buildingCashier(currentPlanet, SDB.MasterCommoditiesList[commodityName], purchaseType)
    viewDictionary[currentView]
    examineCommodity(root, purchaseType, commodityName)


def examineCommodity(event, purchaseType, commodityName):
    # Make building info pop up in the buildings overview frame
    allLabels["Commodity Info Title"].place(relx = 0.6, rely = 0.01, relwidth = 0.39, relheight = 0.2)
    allLabels["Commodity Info Title"].configure(text = commodityName)
    allLabels["Picture Frame"].place(relx = 0.01, rely = 0.01, relwidth = 0.58, relheight = .88)

    # Access databases for player-specific information
    price = currentPlanet.getPrice(purchaseType, SDB.MasterCommoditiesList[commodityName],
                                   currentPlanet.commodities[commodityName])
    timeNeeded = currentPlanet.getTime(purchaseType, SDB.MasterCommoditiesList[commodityName],
                                       currentPlanet.commodities[commodityName], universeSpeed)
    # Display buttons like upgrade, dconstruct, exit
    if (DDB.verifyTechRequirements(currentPlanet, SDB.MasterCommoditiesList[commodityName])
            and DDB.verifyResourceRequirements(purchaseType, currentPlanet, SDB.MasterCommoditiesList[commodityName])):
        if purchaseType == "Building" and len(currentPlanet.buildingQueue) == 0:
            allButtons["Purchase Button"].place(relx=0.75, rely=0.875, relwidth=0.225, relheight=0.1)
            allButtons["Purchase Button"].configure(command=lambda: purchaseCommodity(commodityName, purchaseType))
        elif purchaseType == "Research" and len(currentPlayer.researchQueue) == 0:
            allButtons["Purchase Button"].place(relx=0.75, rely=0.875, relwidth=0.225, relheight=0.1)
            allButtons["Purchase Button"].configure(command=lambda: purchaseCommodity(commodityName, purchaseType))
        else:
            allButtons["Purchase Button"].place_forget()
    else:
        allButtons["Purchase Button"].place_forget()

    allLabels["Commodity Info Metal"].place(relx=0.6, rely=0.225, relwidth=0.39, relheight=0.1)
    allLabels["Commodity Info Metal"].configure(text="Metal: " + str(price[0]))
    allLabels["Commodity Info Crystal"].place(relx=0.6, rely=0.35, relwidth=0.39, relheight=0.1)
    allLabels["Commodity Info Crystal"].configure(text="Crystal: " + str(price[1]))
    allLabels["Commodity Info Deuterium"].place(relx=0.6, rely=0.475, relwidth=0.39, relheight=0.1)
    allLabels["Commodity Info Deuterium"].configure(text="Deuterium: " + str(price[2]))
    allLabels["Commodity Info Energy"].place(relx=0.6, rely=0.6, relwidth=0.39, relheight=0.1)
    allLabels["Commodity Info Energy"].configure(text="Energy: " + str(price[3]))
    allLabels["Commodity Info Time"].place(relx=0.6, rely=0.725, relwidth=0.39, relheight=0.1)
    allLabels["Commodity Info Time"].configure(text=str(timeNeeded) + " seconds")
    allLabels["Commodity Info Level"].place(relx=0.01, rely=0.9, relwidth=0.18, relheight=0.09)
    allLabels["Commodity Info Level"].configure(text="Current Level: " +
                                                     str(currentPlanet.commodities[commodityName]))
    allButtons["Commodity Info Info"].place(relx=0.21, rely=0.9, relwidth=0.38, relheight=0.09)
    allButtons["Commodity Info Info"].configure(command=lambda: infoPage(commodityName))
    # resize_font()


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
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allLabels["Shop Panel 1"].place(relx=0.25, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 2"].place(relx=0.3375, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 3"].place(relx=0.425, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 4"].place(relx=0.5125, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 5"].place(relx=0.6, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 6"].place(relx=0.6875, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 7"].place(relx=0.775, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 8"].place(relx=0.8625, rely=.625, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 9"].place(relx=0.25, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 10"].place(relx=0.3375, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 11"].place(relx=0.425, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 12"].place(relx=0.5125, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 13"].place(relx=0.6, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 14"].place(relx=0.6875, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 15"].place(relx=0.775, rely=.81, relwidth=.085, relheight=.175)
    allLabels["Shop Panel 16"].place(relx=0.8625, rely=.81, relwidth=.085, relheight=.175)

    allLabels["Shop Panel 1"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Espionage Technology"))
    allLabels["Shop Panel 2"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Computer Technology"))
    allLabels["Shop Panel 3"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Weapons Technology"))
    allLabels["Shop Panel 4"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Shielding Technology"))
    allLabels["Shop Panel 5"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Armor Technology"))
    allLabels["Shop Panel 6"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Energy Technology"))
    allLabels["Shop Panel 7"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Hyperspace Technology"))
    allLabels["Shop Panel 8"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Combustion Drive"))
    allLabels["Shop Panel 9"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Impulse Drive"))
    allLabels["Shop Panel 10"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Hyperspace Drive"))
    allLabels["Shop Panel 11"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Laser Technology"))
    allLabels["Shop Panel 12"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Ion Technology"))
    allLabels["Shop Panel 13"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Plasma Technology"))
    allLabels["Shop Panel 14"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Intergalactic Research Network"))
    allLabels["Shop Panel 15"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Astrophysics"))
    allLabels["Shop Panel 16"].bind("<Button-1>", lambda event: examineCommodity(event, "Research", "Graviton Technology"))

    # Display research
    # Place all the buttons we can use


#######################################################################################################################

### Button: Constructions Screen

#######################################################################################################################



def constructionScreen():
    global currentView
    currentView = "Construction"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx = 0.25, rely = .1, relwidth=.695, relheight=0.5)
    allLabels["Shop Panel 1"].place(relx=0.25, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 2"].place(relx=0.35, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 3"].place(relx=0.45, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 4"].place(relx=0.55, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 5"].place(relx=0.65, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 6"].place(relx=0.75, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 7"].place(relx=0.85, rely=.625, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 8"].place(relx=0.25, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 9"].place(relx=0.35, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 10"].place(relx=0.45, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 11"].place(relx=0.55, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 12"].place(relx=0.65, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 13"].place(relx=0.75, rely=.81, relwidth=.095, relheight=.175)
    allLabels["Shop Panel 14"].place(relx=0.85, rely=.81, relwidth=.095, relheight=.175)

    allLabels["Shop Panel 1"].configure(image=allThumbnails["Metal Mine"])
    allLabels["Shop Panel 1"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Metal Mine"))
    allLabels["Shop Panel 2"].configure(image=allThumbnails["Crystal Mine"])
    allLabels["Shop Panel 2"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Crystal Mine"))
    # allLabels["Deuterium Synthesizer"].configure(image = allThumbnails["Deuterium Synthesizer"])
    allLabels["Shop Panel 3"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Deuterium Synthesizer"))
    allLabels["Shop Panel 4"].configure(image=allThumbnails["Solar Plant"])
    allLabels["Shop Panel 4"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Solar Plant"))
    allLabels["Shop Panel 5"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Fusion Reactor"))
    allLabels["Shop Panel 6"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Robotics Factory"))
    allLabels["Shop Panel 7"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Nanite Factory"))
    allLabels["Shop Panel 8"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Shipyard"))
    allLabels["Shop Panel 9"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Metal Storage"))
    allLabels["Shop Panel 10"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Crystal Storage"))
    allLabels["Shop Panel 11"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Deuterium Tank"))
    allLabels["Shop Panel 12"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Research Laboratory"))
    allLabels["Shop Panel 13"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Terraformer"))
    allLabels["Shop Panel 14"].bind("<Button-1>", lambda event: examineCommodity(event, "Building", "Missile Silo"))


#######################################################################################################################

### Button: Resource Settings

#######################################################################################################################

def changeResourceSettings():
    currentPlanet.resourceSettings[0] = float(metalRate.get().strip("%"))/100
    currentPlanet.resourceSettings[1] = float(crystalRate.get().strip("%"))/100
    currentPlanet.resourceSettings[2] = float(deuteriumRate.get().strip("%"))/100
    currentPlanet.resourceSettings[3] = float(solarRate.get().strip("%"))/100
    currentPlanet.resourceSettings[4] = float(fusionRate.get().strip("%"))/100
    currentPlanet.resourceSettings[5] = float(satelliteRate.get().strip("%"))/100
    resourceSettings()


def resourceSettings():
    global currentView
    global metalRate, crystalRate, deuteriumRate, solarRate, fusionRate, satelliteRate
    currentView = "Resource Settings"
    clearGUI()
    metalRate.set(str(currentPlanet.resourceSettings[0] * 100.0) + "%")
    crystalRate.set(str(currentPlanet.resourceSettings[1] * 100.0) + "%")
    deuteriumRate.set(str(currentPlanet.resourceSettings[2] * 100.0) + "%")
    solarRate.set(str(currentPlanet.resourceSettings[3] * 100.0) + "%")
    fusionRate.set(str(currentPlanet.resourceSettings[4] * 100.0) + "%")
    satelliteRate.set(str(currentPlanet.resourceSettings[5] * 100.0) + "%")
    allLabels["Resource Settings Metal 2"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Metal Rate"]))
    allLabels["Resource Settings Metal 8"].configure(
        text=str(universeSpeed * (100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 9"].configure(
        text=str(universeSpeed * 24 * (100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 10"].configure(
        text=str(universeSpeed * 24 * 7 * (100 + currentPlanet.resourceProductionRate()["Metal Rate"])))
    allLabels["Resource Settings Metal 11"].configure(text=str(currentPlanet.storage()[0]))
    allLabels["Resource Settings Crystal 3"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Crystal Rate"]))
    allLabels["Resource Settings Crystal 8"].configure(
        text=str(universeSpeed*(33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 9"].configure(
        text=str(universeSpeed*24 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 10"].configure(
        text=str(universeSpeed*24 * 7 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 11"].configure(text=str(currentPlanet.storage()[1]))
    allLabels["Resource Settings Deuterium 4"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Deuterium Rate"]))
    allLabels["Resource Settings Deuterium 6"].configure(
        text=str(universeSpeed*currentPlanet.resourceProductionRate()["Fusion Rate"]))
    allLabels["Resource Settings Deuterium 8"].configure(
        text=str(universeSpeed*currentPlanet.resourceProductionRate()["Net Deuterium"]))
    allLabels["Resource Settings Deuterium 9"].configure(
        text=str(universeSpeed*24 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
    allLabels["Resource Settings Deuterium 10"].configure(
        text=str(universeSpeed*24 * 7 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
    allLabels["Resource Settings Deuterium 11"].configure(text=str(currentPlanet.storage()[2]))
    allLabels["Resource Settings Energy 2"].configure(text=str(currentPlanet.resourceProductionRate()["Metal Energy"]))
    allLabels["Resource Settings Energy 3"].configure(
        text=str(currentPlanet.resourceProductionRate()["Crystal Energy"]))
    allLabels["Resource Settings Energy 4"].configure(
        text=str(currentPlanet.resourceProductionRate()["Deuterium Energy"]))
    allLabels["Resource Settings Energy 5"].configure(
        text=str(currentPlanet.resourceProductionRate()["Solar Production"]))
    allLabels["Resource Settings Energy 6"].configure(
        text=str(currentPlanet.resourceProductionRate()["Fusion Production"]))
    allLabels["Resource Settings Energy 7"].configure(
        text=str(currentPlanet.resourceProductionRate()["Satellite Production"]))
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
    allOptionMenus["Metal Menu"].place(relx=5/6+0.01, rely = 2/12 + 0.005, relwidth = 1/6 - 0.02, relheight = 1/12 - 0.01)
    allOptionMenus["Crystal Menu"].place(relx=5 / 6 + 0.01, rely=3 / 12 + 0.005, relwidth=1 / 6 - 0.02, relheight=1 / 12 - 0.01)
    allOptionMenus["Deuterium Menu"].place(relx=5 / 6 + 0.01, rely=4 / 12 + 0.005, relwidth=1 / 6 - 0.02, relheight=1 / 12 - 0.01)
    allOptionMenus["Solar Menu"].place(relx=5 / 6 + 0.01, rely=5 / 12 + 0.005, relwidth=1 / 6 - 0.02, relheight=1 / 12 - 0.01)
    allOptionMenus["Fusion Menu"].place(relx=5 / 6 + 0.01, rely=6 / 12 + 0.005, relwidth=1 / 6 - 0.02, relheight=1 / 12 - 0.01)
    allOptionMenus["Satellite Menu"].place(relx=5 / 6 + 0.01, rely=7 / 12 + 0.005, relwidth=1 / 6 - 0.02, relheight=1 / 12 - 0.01)


allButtons["Resource Management"].configure(command = resourceSettings)
allLabels["Resource Settings Production Rate 11"].bind("<Button-1>", lambda event:changeResourceSettings())


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
    global currentPlayer
    global currentPlanet
    DDB.newPlayer("Piggy", "Pig Farm")
    currentPlayer = DDB.playerList["Piggy"]
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
# root.bind('<Configure>', resize_font)
root.mainloop()
