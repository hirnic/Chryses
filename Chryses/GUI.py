# This is Chryses, a variant of the online game Ogame. As this is version 1, I am going to try to clone the game
# mechanics manually, except for moons. We will deal with moons in version 2. Also in version 1 I will implement a
# simple bot to automatically play the game alongside the player. The name of the game comes from Greek mythology.
# It was my dad's idea to name it Chryses, and I liked it.

# This is the main page and it takes care of the Graphical User Interface (GUI). We will start very basic and make it
# more difficult once we flesh out the major details (see other three files). The biggest headache is that Python reads
# code line-by-line, so the main menu starts at the bottom and the more deeply-nested commands are at the top.

import DDB
import tkinter as tk

import SDB

# from tkinter import ttk

player = 0
planet = 0
screen = 0
universeSpeed = DDB.universeSpeed

# The GUI will be a window with a bunch of buttons. Some text boxes for entering numbers, but mostly buttons.
root = tk.Tk()
root.title("Chryses GUI")
canvas = tk.Canvas(root)
canvas.pack()
buildingsOverviewFrame = tk.Frame(root,  bg="grey")
allFrames = {"overviewFrame" : tk.Frame(root,  bg="grey"),
            "planetsFrame1" : tk.Frame(root, bg="grey"),
             "planetsFrame2" : tk.Frame(root, bg="grey"),
             "planetsFrame3" : tk.Frame(root, bg="grey"),
             "planetsFrame4" : tk.Frame(root, bg="grey"),
             "planetsFrame5" : tk.Frame(root, bg="grey"),

             "Buildings Overview" : buildingsOverviewFrame,
             "Buildings Picture Frame" : tk.Frame(buildingsOverviewFrame, bg="sky blue"),
             "Metal Mine": tk.Frame(root, bg="grey"),
             "Crystal Mine": tk.Frame(root, bg="grey"),
             "Deuterium Synthesizer": tk.Frame(root, bg="grey"),
             "Solar Plant": tk.Frame(root, bg="grey"),
             "Fusion Reactor": tk.Frame(root, bg="grey"),
             "Robotics Factory": tk.Frame(root, bg="grey"),
             "Nanite Factory": tk.Frame(root, bg="grey"),
             "Shipyard": tk.Frame(root, bg="grey"),
             "Metal Storage": tk.Frame(root, bg="grey"),
             "Crystal Storage": tk.Frame(root, bg="grey"),
             "Deuterium Tank": tk.Frame(root, bg="grey"),
             "Research Laboratory": tk.Frame(root, bg="grey"),
             "Terraformer": tk.Frame(root, bg="grey"),
             "Missile Silo": tk.Frame(root, bg="grey"),
             }

allButtons = { # Main Menu Buttons
    "New Game Button": tk.Button(root, text="New Game", pady = 1),
    "Load Game Button" : tk.Button(root, text="Load Game", pady = 1),
    "Options Button" :tk.Button(root, text="Options", pady = 1),
    "Quit Button" : tk.Button(root, text="Quit", pady = 1),

    # Player Overview buttons
    "Small Overview" : tk.Button(root, text = "Overview", height = 1),
    "View Buildings" : tk.Button(root, text = "View Buildings", padx= 1, pady = 1),
    "View ResearchLab" : tk.Button(root, text ="View Research", padx= 1, pady = 1),
    "View Shipyard" : tk.Button(root, text = "View Shipyard", padx= 1, pady = 1),
    "View Defenses" : tk.Button(root,text = "View Defenses", padx= 1, pady = 1),
    "View Galaxy" : tk.Button(root, text = "View Galaxy", padx= 1, pady = 1),
    "Manage Fleets" : tk.Button(root, text = "Manage Fleets", padx= 1, pady = 1),
    "Left Arrow" : tk.Button(root, text = "<", padx= 1, pady = 1),
    "Right Arrow" : tk.Button(root, text = ">", padx= 1, pady = 1),

    # Constructions buttons
    "Buildings Purchase Button" : tk.Button(buildingsOverviewFrame, text="Purchase")
}

allLabels = {
    "Buildings Info Title" : tk.Label(buildingsOverviewFrame, text = " "),
    "Buildings Info Metal": tk.Label(buildingsOverviewFrame, text=" "),
    "Buildings Info Crystal": tk.Label(buildingsOverviewFrame, text=" "),
    "Buildings Info Deuterium": tk.Label(buildingsOverviewFrame, text=" "),
    "Buildings Info Energy": tk.Label(buildingsOverviewFrame, text=" "),
    "Buildings Info Time": tk.Label(buildingsOverviewFrame, text=" "),
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


#######################################################################################################################

### Button: Manage Fleets

#######################################################################################################################

def fleetsScreen():
    clearGUI()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Galaxy

#######################################################################################################################

def galaxyScreen():
    clearGUI()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Defenses

#######################################################################################################################

def defenseScreen():
    clearGUI()
    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Shipyard

#######################################################################################################################

def shipyardScreen():
    clearGUI()
    # Display ships
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Research

#######################################################################################################################

def researchScreen():
    clearGUI()
    # Display research
    # Place all the buttons we can use


#######################################################################################################################

### Button: Constructions Screen

#######################################################################################################################

def purchaseBuilding(buildingName):
    DDB.buildingCashier(planet, SDB.MasterBuildingsList[buildingName])
    print(DDB.internalActivity)

def examineBuilding(event, buildingName):
    # Make building info pop up in the buildings overview frame
    allLabels["Buildings Info Title"].place(relx = 0.6, rely = 0.01, relwidth = 0.39, relheight = 0.2)
    allLabels["Buildings Info Title"].configure(text = buildingName)
    allFrames["Buildings Picture Frame"].place(relx = 0.05, rely = 0.05, relwidth = 0.5, relheight = .9)

    # Access databases for player-specific information
    price = planet.getPrice("Building", SDB.MasterBuildingsList[buildingName])
    timeNeeded = planet.getTime("Building", SDB.MasterBuildingsList[buildingName], universeSpeed)
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

    # Display buttons like upgrade, deconstruct, exit
    if (DDB.verifyTechRequirements(planet, SDB.MasterBuildingsList[buildingName])
            and DDB.verifyResourceRequirements(planet, SDB.MasterBuildingsList[buildingName],1)):
        allButtons["Buildings Purchase Button"].place(relx = 0.75, rely = 0.875, relwidth = 0.225, relheight = 0.1)
        allButtons["Buildings Purchase Button"].configure(
        command = lambda:purchaseBuilding(buildingName))
    resize_font()

allFrames["Metal Mine"].bind("<Button-1>", lambda event: examineBuilding(event, "Metal Mine"))
allFrames["Crystal Mine"].bind("<Button-1>", lambda event: examineBuilding(event, "Crystal Mine"))
allFrames["Deuterium Synthesizer"].bind("<Button-1>", lambda event: examineBuilding(event, "Deuterium Synthesizer"))
allFrames["Solar Plant"].bind("<Button-1>", lambda event: examineBuilding(event, "Solar Plant"))
allFrames["Fusion Reactor"].bind("<Button-1>", lambda event: examineBuilding(event, "Fusion Reactor"))
allFrames["Robotics Factory"].bind("<Button-1>", lambda event: examineBuilding(event, "Robotics Factory"))
allFrames["Nanite Factory"].bind("<Button-1>", lambda event: examineBuilding(event, "Nanite Factory"))
allFrames["Shipyard"].bind("<Button-1>", lambda event: examineBuilding(event, "Shipyard"))
allFrames["Metal Storage"].bind("<Button-1>", lambda event: examineBuilding(event, "Metal Storage"))
allFrames["Crystal Storage"].bind("<Button-1>", lambda event: examineBuilding(event, "Crystal Storage"))
allFrames["Deuterium Tank"].bind("<Button-1>", lambda event: examineBuilding(event, "Deuterium Tank"))
allFrames["Research Laboratory"].bind("<Button-1>", lambda event: examineBuilding(event, "Research Laboratory"))
allFrames["Terraformer"].bind("<Button-1>", lambda event: examineBuilding(event, "Terraformer"))
allFrames["Missile Silo"].bind("<Button-1>", lambda event: examineBuilding(event, "Missile Silo"))

def constructionScreen():
    clearGUI()
    allButtons["Small Overview"].place(relx = 0, rely = 0, relwidth = 0.1, relheight = 0.075)
    allFrames["Buildings Overview"].place(relx = 0.25, rely = .05, relwidth=.695, relheight=0.55)
    allFrames["Metal Mine"].place(relx=0.25, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Crystal Mine"].place(relx=0.35, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Deuterium Synthesizer"].place(relx=0.45, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Solar Plant"].place(relx=0.55, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Fusion Reactor"].place(relx=0.65, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Robotics Factory"].place(relx=0.75, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Nanite Factory"].place(relx=0.85, rely=.625, relwidth=.095, relheight=.175)
    allFrames["Shipyard"].place(relx=0.25, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Metal Storage"].place(relx=0.35, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Crystal Storage"].place(relx=0.45, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Deuterium Tank"].place(relx=0.55, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Research Laboratory"].place(relx=0.65, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Terraformer"].place(relx=0.75, rely=.81, relwidth=.095, relheight=.175)
    allFrames["Missile Silo"].place(relx=0.85, rely=.81, relwidth=.095, relheight=.175)



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
    clearGUI()
    allButtons["View Buildings"].place(relx = 0, rely = .325, relwidth = 0.2, relheight = 0.06)
    allButtons["View ResearchLab"].place(relx = 0, rely = .4, relwidth = 0.2, relheight = 0.06)
    allButtons["View Shipyard"].place(relx = 0, rely = .475, relwidth = 0.2, relheight = 0.06)
    allButtons["View Defenses"].place(relx = 0, rely = .55, relwidth = 0.2, relheight = 0.06)
    allButtons["View Galaxy"].place(relx = 0, rely = .625, relwidth = 0.2, relheight = 0.06)
    allButtons["Manage Fleets"].place(relx = 0, rely = .7, relwidth = 0.2, relheight = 0.06)
    #
    allFrames["overviewFrame"].place(relx = 0.3, rely = .075, relwidth=.525, relheight=0.625)
    allButtons["Left Arrow"].place(relx=0.2875, rely = 0.725, relwidth = 0.02, relheight = 0.175)
    allFrames["planetsFrame1"].place(relx=0.31, rely=.725, relwidth=.095, relheight=.175)
    allFrames["planetsFrame2"].place(relx=0.4125, rely=.725, relwidth=.095, relheight=.175)
    allFrames["planetsFrame3"].place(relx=0.515, rely=.725, relwidth=.095, relheight=.175)
    allFrames["planetsFrame4"].place(relx=0.6175, rely=.725, relwidth=.095, relheight=.175)
    allFrames["planetsFrame5"].place(relx=0.72, rely=.725, relwidth=.095, relheight=.175)
    allButtons["Right Arrow"].place(relx=0.8175, rely=0.725, relwidth=0.02, relheight=0.175)

allButtons["Small Overview"].configure(command = playerOverview)


#######################################################################################################################

### Button: New Game

#######################################################################################################################

# Carries out the process for beginning a new game.
def newGame():
    global planet
    DDB.newPlayer("Piggy", "Pig Farm")
    planet = DDB.planetList["Pig Farm"]
    playerOverview()


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

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# Bind the window resizing event to the update_font function
root.bind('<Configure>', resize_font)
root.mainloop()
