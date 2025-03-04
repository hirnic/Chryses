# This is Chryses, a variant of the online game Ogame. As this is version 1, I am going to try to clone the game
# mechanics manually, except for moons. We will deal with moons in version 2. Also in version 1 I will implement a
# simple bot to automatically play the game alongside the player. The name of the game comes from Greek mythology.
# It was my dad's idea to name it Chryses, and I liked it.

# This is the main page, and it takes care of the Graphical User Interface (GUI). We will start very basic and make it
# more difficult once we flesh out the major details (see other three files). The biggest headache is that Python reads
# code line-by-line, so the main menu starts at the bottom and the more deeply-nested commands are at the top.

import Classes
import FleetMissions
import SDB
import DDB
import tkinter as tk
import time
from tkinter import font
from tkinter.font import Font
from tkinter import ttk
import os
import sys

currentPlanet = DDB.currentPlanet
currentPlayer = DDB.currentPlayer
currentView = "Overview"  # What is the player looking at?
currentCommodity = None
universeSpeed = DDB.universeSpeed

# The GUI
root = tk.Tk()
root.title("Chryses GUI")
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.config(family="Courier", size=12)

canvas = tk.Canvas(root)
canvas.pack()

mainFrame = tk.Frame(root, bg="grey")
resourcesFrame = tk.Frame(root, bg="grey")
allFrames = {"Main Frame": mainFrame,
             "Resources Frame": resourcesFrame,
             "Queue Frame": tk.Frame(root, bg="grey"),
             "Info Frame": tk.Frame(root, bg="grey")
             }

allButtons = {  # Main Menu Buttons
    "New Game Button": tk.Button(root, text="New Game"),
    "Load Game Button": tk.Button(root, text="Load Game"),
    "Options Button": tk.Button(root, text="Options"),
    "Quit Button": tk.Button(root, text="Quit"),

    "Save Button": tk.Button(mainFrame, text="Save Game"),
    "Messages Button": tk.Button(mainFrame, text="Messages"),

    # Player Overview buttons
    "Overview": tk.Button(root, text="Overview", height=1),
    "View Buildings": tk.Button(root, text="View Buildings"),
    "View ResearchLab": tk.Button(root, text="View Research"),
    "View Shipyard": tk.Button(root, text="View Shipyard"),
    "View Defenses": tk.Button(root, text="View Defenses"),
    "View Galaxy": tk.Button(root, text="View Galaxy"),
    "Manage Fleets": tk.Button(root, text="Manage Fleets"),
    "Left Arrow": tk.Button(root, text="<"),
    "Right Arrow": tk.Button(root, text=">"),

    "Cancel Building": tk.Button(allFrames["Queue Frame"], text=" "),
    "Cancel Research": tk.Button(allFrames["Queue Frame"], text=" "),

    "Resource Management": tk.Button(resourcesFrame, text="Resources"),

    "Exit Info Frame": tk.Button(allFrames["Info Frame"], text="Exit"),

    # Constructions buttons
    "Purchase Button": tk.Button(mainFrame, text="Purchase"),
    "Commodity Info Info": tk.Button(mainFrame, text="Information"),

    "Galaxy Left": tk.Button(root, text="<"),
    "Galaxy Right": tk.Button(root, text=">"),
    "System Left": tk.Button(root, text="<"),
    "System Right": tk.Button(root, text=">"),
    "Navigate": tk.Button(root, text="Navigate")

}

allLabels = {
    "Metal Title": tk.Label(resourcesFrame, text="Metal"),
    "Crystal Title": tk.Label(resourcesFrame, text="Crystal"),
    "Deuterium Title": tk.Label(resourcesFrame, text="Deuterium"),
    "Energy Title": tk.Label(resourcesFrame, text="Energy"),
    "Time Title": tk.Label(resourcesFrame, text="Current Time"),
    "Metal Amount": tk.Label(resourcesFrame, text=""),
    "Crystal Amount": tk.Label(resourcesFrame, text=""),
    "Deuterium Amount": tk.Label(resourcesFrame, text=""),
    "Energy Amount": tk.Label(resourcesFrame, text=""),
    "Time Amount": tk.Label(resourcesFrame, text=""),

    "Planet 1 Picture": tk.Label(root, text=" "),
    "Planet 2 Picture": tk.Label(root, text=" "),
    "Planet 3 Picture": tk.Label(root, text=" "),
    "Planet 4 Picture": tk.Label(root, text=" "),

    "Queue Title": tk.Label(allFrames["Queue Frame"], text="Production Queue", font=("Courier", 16)),
    "Buildings Queue": tk.Label(allFrames["Queue Frame"], text="Buildings: None"),
    "Research Queue": tk.Label(allFrames["Queue Frame"], text="Research: None"),
    "Shipyard Queue": tk.Label(allFrames["Queue Frame"], text="Shipyard: None"),

    "Resource Settings Source 0": tk.Label(root, text="Exit"),
    "Resource Settings Source 1": tk.Label(root, text="Basic Income"),
    "Resource Settings Source 2": tk.Label(root, text="Metal Mine"),
    "Resource Settings Source 3": tk.Label(root, text="Crystal Mine"),
    "Resource Settings Source 4": tk.Label(root, text="Deuterium Synthesizer"),
    "Resource Settings Source 5": tk.Label(root, text="Solar Plant"),
    "Resource Settings Source 6": tk.Label(root, text="Fusion Plant"),
    "Resource Settings Source 7": tk.Label(root, text="Solar Satellites"),
    "Resource Settings Source 8": tk.Label(root, text="Hourly Income"),
    "Resource Settings Source 9": tk.Label(root, text="Daily Income"),
    "Resource Settings Source 10": tk.Label(root, text="Weekly Income"),
    "Resource Settings Source 11": tk.Label(root, text="Storage Capacity"),
    "Resource Settings Metal 0": tk.Label(root, text="Metal"),
    "Resource Settings Metal 1": tk.Label(root, text=str(universeSpeed * 100)),
    "Resource Settings Metal 2": tk.Label(root, text="0"),
    "Resource Settings Metal 3": tk.Label(root, text="0"),
    "Resource Settings Metal 4": tk.Label(root, text="0"),
    "Resource Settings Metal 5": tk.Label(root, text="0"),
    "Resource Settings Metal 6": tk.Label(root, text="0"),
    "Resource Settings Metal 7": tk.Label(root, text="0"),
    "Resource Settings Metal 8": tk.Label(root, text="0"),
    "Resource Settings Metal 9": tk.Label(root, text="0"),
    "Resource Settings Metal 10": tk.Label(root, text="0"),
    "Resource Settings Metal 11": tk.Label(root, text="0"),
    "Resource Settings Crystal 0": tk.Label(root, text="Crystal"),
    "Resource Settings Crystal 1": tk.Label(root, text=str(universeSpeed * 33)),
    "Resource Settings Crystal 2": tk.Label(root, text="0"),
    "Resource Settings Crystal 3": tk.Label(root, text="0"),
    "Resource Settings Crystal 4": tk.Label(root, text="0"),
    "Resource Settings Crystal 5": tk.Label(root, text="0"),
    "Resource Settings Crystal 6": tk.Label(root, text="0"),
    "Resource Settings Crystal 7": tk.Label(root, text="0"),
    "Resource Settings Crystal 8": tk.Label(root, text="0"),
    "Resource Settings Crystal 9": tk.Label(root, text="0"),
    "Resource Settings Crystal 10": tk.Label(root, text="0"),
    "Resource Settings Crystal 11": tk.Label(root, text="0"),
    "Resource Settings Deuterium 0": tk.Label(root, text="Deuterium"),
    "Resource Settings Deuterium 1": tk.Label(root, text="0"),
    "Resource Settings Deuterium 2": tk.Label(root, text="0"),
    "Resource Settings Deuterium 3": tk.Label(root, text="0"),
    "Resource Settings Deuterium 4": tk.Label(root, text="0"),
    "Resource Settings Deuterium 5": tk.Label(root, text="0"),
    "Resource Settings Deuterium 6": tk.Label(root, text="0"),
    "Resource Settings Deuterium 7": tk.Label(root, text="0"),
    "Resource Settings Deuterium 8": tk.Label(root, text="0"),
    "Resource Settings Deuterium 9": tk.Label(root, text="0"),
    "Resource Settings Deuterium 10": tk.Label(root, text="0"),
    "Resource Settings Deuterium 11": tk.Label(root, text="0"),
    "Resource Settings Energy 0": tk.Label(root, text="Energy"),
    "Resource Settings Energy 1": tk.Label(root, text="0"),
    "Resource Settings Energy 2": tk.Label(root, text="0"),
    "Resource Settings Energy 3": tk.Label(root, text="0"),
    "Resource Settings Energy 4": tk.Label(root, text="0"),
    "Resource Settings Energy 5": tk.Label(root, text="0"),
    "Resource Settings Energy 6": tk.Label(root, text="0"),
    "Resource Settings Energy 7": tk.Label(root, text="0"),
    "Resource Settings Energy 8": tk.Label(root, text="0"),
    "Resource Settings Energy 9": tk.Label(root, text="0"),
    "Resource Settings Energy 10": tk.Label(root, text="0"),
    "Resource Settings Energy 11": tk.Label(root, text=" "),
    "Resource Settings Production Rate 0": tk.Label(root, text="Set Rate"),
    "Resource Settings Production Rate 1": tk.Label(root, text=" "),
    "Resource Settings Production Rate 2": tk.Label(root, text=" "),
    "Resource Settings Production Rate 3": tk.Label(root, text=" "),
    "Resource Settings Production Rate 4": tk.Label(root, text=" "),
    "Resource Settings Production Rate 5": tk.Label(root, text=" "),
    "Resource Settings Production Rate 6": tk.Label(root, text=" "),
    "Resource Settings Production Rate 7": tk.Label(root, text=" "),
    "Resource Settings Production Rate 8": tk.Label(root, text=" "),
    "Resource Settings Production Rate 9": tk.Label(root, text=" "),
    "Resource Settings Production Rate 10": tk.Label(root, text=" "),
    "Resource Settings Production Rate 11": tk.Label(root, text="Confirm"),

    "Commodity Tech Label": tk.Label(allFrames["Info Frame"], text=" "),
    "Commodity Info Label": tk.Label(allFrames["Info Frame"], text=" "),

    "Commodity Info Title": tk.Label(mainFrame, text=" "),
    "Commodity Price 1": tk.Label(mainFrame, text=" "),
    "Commodity Price 2": tk.Label(mainFrame, text=" "),
    "Commodity Price 3": tk.Label(mainFrame, text=" "),
    "Commodity Price 4": tk.Label(mainFrame, text=" "),
    "Commodity Info Time": tk.Label(mainFrame, text=" "),
    "Commodity Info Level": tk.Label(mainFrame, text=" "),
    "Commodity Info Tech": tk.Label(mainFrame, text="Tech Tree"),

    "Picture Frame": tk.Label(mainFrame, bg="grey", text=" "),
    "Shop Panel 1": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 2": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 3": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 4": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 5": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 6": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 7": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 8": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 9": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 10": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 11": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 12": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 13": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 14": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 15": tk.Label(root, bg="grey", text=" "),
    "Shop Panel 16": tk.Label(root, bg="grey", text=" "),

    "Fleet Missions Title": tk.Label(mainFrame, text=" "),
    "Fleet Mission 1": tk.Label(mainFrame, text=" "),
    "Fleet Mission 2": tk.Label(mainFrame, text=" "),
    "Fleet Mission 3": tk.Label(mainFrame, text=" "),
    "Fleet Mission 4": tk.Label(mainFrame, text=" "),
    "Fleet Mission 5": tk.Label(mainFrame, text=" "),
    "Mission Cancel 1": tk.Label(mainFrame, text=" "),
    "Mission Cancel 2": tk.Label(mainFrame, text=" "),
    "Mission Cancel 3": tk.Label(mainFrame, text=" "),
    "Mission Cancel 4": tk.Label(mainFrame, text=" "),
    "Mission Cancel 5": tk.Label(mainFrame, text=" "),

    "Galaxy": tk.Label(root, text="Galaxy"),
    "System": tk.Label(root, text="System"),
}

metalRate = tk.StringVar(root)
metalRate.set(str(currentPlanet.resourceSettings[0] * 100.0) + "%")
crystalRate = tk.StringVar(root)
crystalRate.set(str(currentPlanet.resourceSettings[1] * 100.0) + "%")
deuteriumRate = tk.StringVar(root)
deuteriumRate.set(str(currentPlanet.resourceSettings[2] * 100.0) + "%")
solarRate = tk.StringVar(root)
solarRate.set(str(currentPlanet.resourceSettings[3] * 100.0) + "%")
fusionRate = tk.StringVar(root)
fusionRate.set(str(currentPlanet.resourceSettings[4] * 100.0) + "%")
satelliteRate = tk.StringVar(root)
satelliteRate.set(str(currentPlanet.resourceSettings[5] * 100.0) + "%")
missionType = tk.StringVar(mainFrame)
missionType.set("Select Mission")
missionSpeed = tk.StringVar(mainFrame)
missionSpeed.set("Select Speed")

allOptionMenus = {
    "Metal Menu": tk.OptionMenu(root, metalRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%",
                                "0%"),
    "Crystal Menu": tk.OptionMenu(root, crystalRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%",
                                  "10%", "0%"),
    "Deuterium Menu": tk.OptionMenu(root, deuteriumRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%",
                                    "10%", "0%"),
    "Solar Menu": tk.OptionMenu(root, solarRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%",
                                "0%"),
    "Fusion Menu": tk.OptionMenu(root, fusionRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%",
                                 "10%", "0%"),
    "Satellite Menu": tk.OptionMenu(root, satelliteRate, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%",
                                    "10%", "0%"),
    "Mission Type": tk.OptionMenu(mainFrame, missionType, "Select Mission", "Transport", "Deploy", "Recycle",
                                  "Colonize", "Espionage",
                                  "Hold Position", "Attack"),
    "Mission Speed": tk.OptionMenu(mainFrame, missionSpeed, "100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%",
                                   "20%", "10%")}

allPEntries = {
    "purchaseAmount": Classes.EntryWithPlaceholder(mainFrame, "Enter a whole number."),
    "Galaxy Destination": Classes.EntryWithPlaceholder(mainFrame, "Galaxy"),
    "Solar System Destination": Classes.EntryWithPlaceholder(mainFrame, "Solar System"),
    "Planet Destination": Classes.EntryWithPlaceholder(mainFrame, "Planet"),
    "Metal Transport": Classes.EntryWithPlaceholder(mainFrame, "Metal"),
    "Crystal Transport": Classes.EntryWithPlaceholder(mainFrame, "Crystal"),
    "Deuterium Transport": Classes.EntryWithPlaceholder(mainFrame, "Deuterium"),
    "Fleet Amount 1": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 2": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 3": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 4": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 5": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 6": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 7": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 8": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 9": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 10": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 11": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 12": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 13": Classes.EntryWithPlaceholder(root, "Available: 0"),
    "Fleet Amount 14": Classes.EntryWithPlaceholder(root, "Available: 0"),
}


def resource_path(relative_path):
    try:
        # For bundled app, PyInstaller creates a temporary directory for resources
        base_path = sys._MEIPASS
    except Exception:
        # If running in development environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


allThumbnails = {"Default": tk.PhotoImage(file=resource_path("Photos/Default_Image.png")).subsample(5, 3),
                 "Metal Mine": tk.PhotoImage(file=resource_path("Photos/Metal_Mine1.png")).subsample(12, 7),
                 "Crystal Mine": tk.PhotoImage(file=resource_path("Photos/Crystal_Mine1.png")).subsample(7, 7),
                 "Deuterium Synthesizer": tk.PhotoImage(
                     file=resource_path("Photos/Deuterium_Synthesizer1.png")).subsample(10, 7),
                 "Solar Plant": tk.PhotoImage(file=resource_path("Photos/Solar_Plant6.png")).subsample(6, 7),
                 "Fusion Reactor": tk.PhotoImage(file=resource_path("Photos/Fusion_Reactor2.png")).subsample(7, 7),
                 "Robotics Factory": tk.PhotoImage(file=resource_path("Photos/Robotics_Factory1.png")).subsample(11, 7),
                 "Nanite Factory": tk.PhotoImage(file=resource_path("Photos/Nanite_Factory1.png")).subsample(7, 7),
                 "Shipyard": tk.PhotoImage(file=resource_path("Photos/Shipyard1.png")).subsample(12, 7),
                 "Metal Storage": tk.PhotoImage(file=resource_path("Photos/Metal_Storage1.png")).subsample(7, 7),
                 "Crystal Storage": tk.PhotoImage(file=resource_path("Photos/Crystal_Storage1.png")).subsample(7, 7),
                 "Deuterium Tank": tk.PhotoImage(file=resource_path("Photos/Deuterium_Tank1.png")).subsample(7, 7),
                 "Research Laboratory": tk.PhotoImage(file=resource_path("Photos/Research_Laboratory1.png")).subsample(
                     9, 7),
                 "Terraformer": tk.PhotoImage(file=resource_path("Photos/Terraformer1.png")).subsample(7, 7),
                 "Missile Silo": tk.PhotoImage(file=resource_path("Photos/Missile_Silo1.png")).subsample(7, 7)
                 }

allDisplayPhotos = {"Default": tk.PhotoImage(file=resource_path("Photos/Default_Image.png")).subsample(2, 2),
                    "Planet Overview": tk.PhotoImage(file=resource_path("Photos/Planets_Screen1.png")).subsample(2, 2),

                    "Construction Screen": tk.PhotoImage(file=resource_path("Photos/Construction_Screen1.png")).subsample(2, 2),
                    "Metal Mine": tk.PhotoImage(file=resource_path("Photos/Metal_Mine1.png")).subsample(3, 3),
                    "Crystal Mine": tk.PhotoImage(file=resource_path("Photos/Crystal_Mine1.png")).subsample(2, 2),
                    "Deuterium Synthesizer": tk.PhotoImage(
                        file=resource_path("Photos/Deuterium_Synthesizer1.png")).subsample(3, 3),
                    "Solar Plant": tk.PhotoImage(file=resource_path("Photos/Solar_Plant6.png")).subsample(2, 2),
                    "Fusion Reactor": tk.PhotoImage(file=resource_path("Photos/Fusion_Reactor2.png")).subsample(2, 3),
                    "Robotics Factory": tk.PhotoImage(file=resource_path("Photos/Robotics_Factory1.png")).subsample(3,
                                                                                                                    3),
                    "Nanite Factory": tk.PhotoImage(file=resource_path("Photos/Nanite_Factory1.png")).subsample(2, 2),
                    "Shipyard": tk.PhotoImage(file=resource_path("Photos/Shipyard1.png")).subsample(3, 3),
                    "Metal Storage": tk.PhotoImage(file=resource_path("Photos/Metal_Storage1.png")).subsample(2, 2),
                    "Crystal Storage": tk.PhotoImage(file=resource_path("Photos/Crystal_Storage1.png")).subsample(2, 2),
                    "Deuterium Tank": tk.PhotoImage(file=resource_path("Photos/Deuterium_Tank1.png")).subsample(2, 2),
                    "Research Laboratory": tk.PhotoImage(
                        file=resource_path("Photos/Research_Laboratory1.png")).subsample(3, 3),
                    "Terraformer": tk.PhotoImage(file=resource_path("Photos/Terraformer1.png")).subsample(2, 2),
                    "Missile Silo": tk.PhotoImage(file=resource_path("Photos/Missile_Silo1.png")).subsample(2, 2),

                    "Research Screen": tk.PhotoImage(file=resource_path("Photos/Research_Screen1.png")).subsample(2,2),

                    "Shipyard Screen": tk.PhotoImage(file=resource_path("Photos/Shipyard_Screen1.png")).subsample(2,2)
                    }


def update_wraplength(event):
    allLabels["Commodity Info Title"].configure(wraplength=allLabels["Commodity Info Title"].winfo_width())
    allLabels["Commodity Info Label"].configure(wraplength=allLabels["Commodity Info Label"].winfo_width())
    allLabels["Commodity Tech Label"].configure(wraplength=allLabels["Commodity Tech Label"].winfo_width())
    allLabels["Buildings Queue"].configure(wraplength=allLabels["Buildings Queue"].winfo_width())
    allLabels["Research Queue"].configure(wraplength=allLabels["Research Queue"].winfo_width())
    allLabels["Shipyard Queue"].configure(wraplength=allLabels["Shipyard Queue"].winfo_width())
    allLabels["Time Title"].configure(wraplength=allLabels["Time Title"].winfo_width())


def formatTime(seconds):
    if seconds < 60:
        return time.strftime("%S s", time.gmtime(seconds))
    if seconds < 3600:
        return time.strftime("%M m %S s", time.gmtime(seconds))
    if seconds < 86400:
        return time.strftime("%H h %M m %S s", time.gmtime(seconds))
    try:
        return str(time.strftime("%j d %H h %M m %S s", time.gmtime(seconds)))
    except OSError:
        return "0"
    except OverflowError:
        return "0"


def formatDate(seconds):
    return time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(seconds))

# Create Treeview
tree = ttk.Treeview(root, columns=("Index", "Planet Name", "Player Name"), show="headings")


def clearGUI():
    for button in allButtons.values():
        button.place_forget()
    for frame in allFrames.values():
        frame.place_forget()
    for label in allLabels.values():
        label.place_forget()
    for menu in allOptionMenus.values():
        menu.place_forget()
    for entry in allPEntries.values():
        entry.place_forget()
    tree.place_forget()


def displayQueue():
    allFrames["Queue Frame"].place(relx=0.01, rely=0.485, relwidth=0.19, relheight=0.475)
    allLabels["Queue Title"].place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.09)

    if len(currentPlanet.buildingQueue) == 0:
        allLabels["Buildings Queue"].configure(text="Buildings: None", anchor="center")
        allLabels["Buildings Queue"].place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.19)
    else:
        timeRemaining = currentPlanet.buildingQueue[0][2] + currentPlanet.getTime(
            currentPlanet.buildingQueue[0][0], currentPlanet.buildingQueue[0][1] - 1, universeSpeed) - time.time()
        allLabels["Buildings Queue"].configure(
            text=currentPlanet.buildingQueue[0][0].name + "(Lvl. " + str(currentPlanet.buildingQueue[0][1]) + ")\n"
                 + formatTime(timeRemaining), anchor="nw", justify="left")
        allButtons["Cancel Building"].place(relx=0.01, rely=0.11, relwidth=0.18, relheight=0.19)
        allButtons["Cancel Building"].configure(text="X", command=lambda: DDB.cancelPurchase(
            currentPlanet, currentPlanet.buildingQueue[0][0]))
        allLabels["Buildings Queue"].place(relx=0.2, rely=0.11, relwidth=0.78, relheight=0.19)

    if len(currentPlayer.researchQueue) == 0:
        allLabels["Research Queue"].configure(text="Research: None", anchor="center")
        allLabels["Research Queue"].place(relx=0.01, rely=0.31, relwidth=0.98, relheight=0.19)
    else:
        timeRemaining = int(currentPlayer.researchQueue[0][2] + currentPlanet.getTime(
            currentPlayer.researchQueue[0][0], currentPlayer.researchQueue[0][1] - 1, universeSpeed) - time.time())
        allLabels["Research Queue"].configure(
            text=currentPlayer.researchQueue[0][0].name + "(Lvl. " + str(currentPlayer.researchQueue[0][1])
                 + ")\n" + formatTime(timeRemaining), anchor="nw", justify="left")
        allButtons["Cancel Research"].place(relx=0.01, rely=0.31, relwidth=0.18, relheight=0.19)
        allButtons["Cancel Research"].configure(text="X", command=lambda: DDB.cancelPurchase(
            currentPlanet, currentPlayer.researchQueue[0][0]))
        allLabels["Research Queue"].place(relx=0.2, rely=0.31, relwidth=0.78, relheight=0.19)

    if len(currentPlanet.shipyardQueue) == 0:
        allLabels["Shipyard Queue"].configure(text="Shipyard: None", anchor="center")
        allLabels["Shipyard Queue"].place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.19)
    else:
        timeRemaining = int(currentPlanet.shipyardQueue[0][2]
                            + currentPlanet.shipyardQueue[0][1] * currentPlanet.getTime(
            currentPlanet.shipyardQueue[0][0], None, universeSpeed) - time.time())
        allLabels["Shipyard Queue"].configure(
            text=currentPlanet.shipyardQueue[0][0].name + " (" + str(currentPlanet.shipyardQueue[0][1]) + ")" + ", "''
                 + formatTime(timeRemaining), anchor="nw", justify="left")
        allLabels["Shipyard Queue"].place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.19)

    update_wraplength(root)


def sideNav():
    allButtons["Overview"].place(relx=0.01, rely=.0, relwidth=0.19, relheight=0.05)
    allButtons["View Buildings"].place(relx=0.01, rely=.0667, relwidth=0.19, relheight=0.05)
    allButtons["View ResearchLab"].place(relx=0.01, rely=.1333, relwidth=0.19, relheight=0.05)
    allButtons["View Shipyard"].place(relx=0.01, rely=.2, relwidth=0.19, relheight=0.05)
    allButtons["View Defenses"].place(relx=0.01, rely=.2667, relwidth=0.19, relheight=0.05)
    allButtons["View Galaxy"].place(relx=0.01, rely=.3333, relwidth=0.19, relheight=0.05)
    allButtons["Manage Fleets"].place(relx=0.01, rely=.4, relwidth=0.19, relheight=0.05)
    displayQueue()


def topNav():
    resourcesFrame.place(relx=0.25, rely=0, relwidth=.695, relheight=0.09)
    # mainFrame.place(relx = 0.25, rely = .1, relwidth=.695, relheight=0.5)
    allLabels["Metal Title"].place(relx=0.01, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Metal Amount"].place(relx=0.01, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Metal Amount"].configure(text=str(int(currentPlanet.resources[0])))
    allLabels["Crystal Title"].place(relx=0.1767, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Crystal Amount"].place(relx=0.1767, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Crystal Amount"].configure(text=str(int(currentPlanet.resources[1])))
    allLabels["Deuterium Title"].place(relx=0.3433, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Deuterium Amount"].place(relx=0.3433, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Deuterium Amount"].configure(text=str(int(currentPlanet.resources[2])))
    allLabels["Energy Title"].place(relx=0.51, rely=0.01, relwidth=0.1517, relheight=.49)
    allLabels["Energy Amount"].place(relx=0.51, rely=0.51, relwidth=0.1517, relheight=.49)
    allLabels["Energy Amount"].configure(text=str(currentPlanet.resourceProductionRate()["Net Energy"]))
    allButtons["Resource Management"].place(relx=0.6767, rely=0.01, relwidth=0.1517, relheight=.98)
    allLabels["Time Title"].place(relx=0.8383, rely=0.01, relwidth=0.1517, relheight=0.98)


def infoPage(commodityName):
    allFrames["Info Frame"].tkraise()
    allFrames["Info Frame"].place(relx=0.37, rely=0.01, relwidth=0.45, relheight=0.85)
    allButtons["Exit Info Frame"].place(relx=0.91, rely=0.01, relwidth=0.08, relheight=0.04)
    allButtons["Exit Info Frame"].configure(command=allFrames["Info Frame"].place_forget)
    allLabels["Commodity Info Label"].place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.73)
    allLabels["Commodity Info Label"].bind("<Configure>", update_wraplength)
    allLabels["Commodity Info Label"].configure(text=SDB.MasterDescriptionList[commodityName], anchor="nw",
                                                justify="left")
    allLabels["Commodity Tech Label"].place(relx=0.01, rely=0.81, relwidth=0.98, relheight=0.18)
    allLabels["Commodity Tech Label"].bind("<Configure>", update_wraplength)
    techRequired = Classes.technologyTree[commodityName]
    string = "Technology required: "
    for item in techRequired:
        string = string + str(item) + " level " + str(techRequired[item]) + "\n"
    allLabels["Commodity Tech Label"].configure(text=string, anchor="nw", justify="right")


def update_clock():
    current_time = formatDate(time.time())
    allLabels["Time Title"].config(text=current_time)
    allLabels["Time Title"].bind("<Configure>", update_wraplength)


def updateEverything():
    # start = time.time()
    update_clock()
    allLabels["Metal Amount"].configure(text=str(int(currentPlanet.resources[0])))
    allLabels["Crystal Amount"].configure(text=str(int(currentPlanet.resources[1])))
    allLabels["Deuterium Amount"].configure(text=str(int(currentPlanet.resources[2])))
    allLabels["Energy Amount"].configure(text=str(currentPlanet.resourceProductionRate()["Net Energy"]))
    if currentView != "Resource Settings":
        displayQueue()
    # If a building, research, ship, or defense get completed, then this refreshes the page.
    DDB.executePurchases()
    if currentCommodity is not None:
        examineCommodity(None, currentCommodity)
    else:
        viewDictionary[currentView]()
    FleetMissions.executeMissions()
    DDB.updateResources()
    # print(time.time()-start)
    if time.time()%600 == 0:
        DDB.saveGame()
    canvas.after(DDB.updateNumber, updateEverything)


#######################################################################################################################

### Button: View Galaxy

#######################################################################################################################

# Define headings
tree.heading("Index", text="Planet Number")
tree.heading("Planet Name", text="Planet Name")
tree.heading("Player Name", text="Player Name")
treeRows = {"Row " + str(i + 1): tree.insert("", "end", values=(" ", " ")) for i in range(10)}


def navigate(galaxy, system):
    G = str(min(9, max(1, int(allLabels["Galaxy"].cget("text")[-1]) + galaxy)))
    S = str(min(9, max(1, int(allLabels["System"].cget("text")[-1]) + system)))
    allLabels["Galaxy"].configure(text="Galaxy: " + str(G))
    allLabels["System"].configure(text="System: " + str(S))


def galaxyScreen():
    global currentView, treeRows
    currentView = "Galaxy"
    clearGUI()
    sideNav()
    topNav()
    galaxy, system = int(allLabels["Galaxy"].cget("text")[-1]), int(allLabels["System"].cget("text")[-1])
    planets = [item for item in DDB.planetList.values() if (item.coords[0] == galaxy and item.coords[1] == system)]

    for i in range(1,11):
        planetExists = False
        for planet in planets:
            if planet.coords[2] == i:
                tree.item(treeRows["Row " + str(i)],
                          values=(str(i), "|   " + planet.name, "|   " + planet.owner))
                planetExists = True
                break
        if not planetExists:
            tree.item(treeRows["Row " + str(i)], values=(str(i), "| ", "| "))

    # Pack Treeview
    tree.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.50)
    ttk.Style().configure("Treeview", rowheight=36, borderwidth=1)
    allButtons["Galaxy Left"].place(relx=0.25, rely=0.61, relwidth=0.05, relheight=0.1)
    allButtons["Galaxy Left"].configure(command=lambda: navigate(-1, 0))
    allLabels["Galaxy"].place(relx=0.31, rely=0.61, relwidth=0.08, relheight=0.1)
    allButtons["Galaxy Right"].place(relx=0.40, rely=0.61, relwidth=0.05, relheight=0.1)
    allButtons["Galaxy Right"].configure(command=lambda: navigate(1, 0))
    allButtons["System Left"].place(relx=0.50, rely=0.61, relwidth=0.05, relheight=0.1)
    allButtons["System Left"].configure(command=lambda: navigate(0, -1))
    allLabels["System"].place(relx=0.56, rely=0.61, relwidth=0.08, relheight=0.1)
    allButtons["System Right"].place(relx=0.65, rely=0.61, relwidth=0.05, relheight=0.1)
    allButtons["System Right"].configure(command=lambda: navigate(0, 1))


#######################################################################################################################

### Button: Manage Fleets

#######################################################################################################################


def scheduleMission(departurePlanet, arrivalPlanet, fleet, mission, speed, cargo, fuelRequired, arrivalTime,
                    returnTime):
    FleetMissions.scheduleMission(departurePlanet, arrivalPlanet, fleet, mission, speed, cargo, fuelRequired,
                                  arrivalTime, returnTime)
    for item in allPEntries.values():
        item.put_placeholder()


def cancelMission(event, mission):
    pass


def fleetsScreen():
    global currentCommodity
    currentCommodity = None
    global currentView
    currentView = "Fleets"
    clearGUI()
    sideNav()
    topNav()

    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    # allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.58, relheight=.88)
    allLabels["Commodity Info Title"].place(relx=0.61, rely=0.01, relwidth=0.18, relheight=0.14)
    allLabels["Commodity Info Title"].configure(text="Enter Destination Coordinates", font=("Courier", 12))
    allPEntries["Galaxy Destination"].place(relx=0.615, rely=0.16, relwidth=0.17, relheight=0.09)
    allPEntries["Solar System Destination"].place(relx=0.615, rely=0.26, relwidth=0.17, relheight=0.09)
    allPEntries["Planet Destination"].place(relx=0.615, rely=0.36, relwidth=0.17, relheight=0.09)
    allLabels["Commodity Price 1"].place(relx=0.81, rely=0.01, relwidth=0.18, relheight=0.14)
    allLabels["Commodity Price 1"].configure(text="Select Cargo")
    allPEntries["Metal Transport"].place(relx=0.815, rely=0.16, relwidth=0.17, relheight=0.09)
    allPEntries["Crystal Transport"].place(relx=0.815, rely=0.26, relwidth=0.17, relheight=0.09)
    allPEntries["Deuterium Transport"].place(relx=0.815, rely=0.36, relwidth=0.17, relheight=0.09)
    allOptionMenus["Mission Type"].place(relx=0.61, rely=0.46, relwidth=0.18, relheight=0.09)
    allOptionMenus["Mission Speed"].place(relx=0.81, rely=0.46, relwidth=0.18, relheight=0.09)
    allLabels["Commodity Price 4"].place(relx=0.61, rely=0.56, relwidth=0.38, relheight=0.34)

    allLabels["Fleet Missions Title"].place(relx=0.11, rely=0.01, relwidth=0.39, relheight=0.15)
    allLabels["Fleet Missions Title"].configure(text="Current Missions", font=("Courier New", 18))
    for i in range(len(currentPlayer.fleets)):
        allLabels["Fleet Mission " + str(i + 1)].place(relx=0.05, rely=0.17 + 0.166 * i, relwidth=0.55, relheight=0.15)
        allLabels["Fleet Mission " + str(i + 1)].configure(
            text=currentPlayer.fleets[i].missionType
                 + "\nOrigin: " + currentPlayer.fleets[i].departurePlanet.name + ", " + str(
                currentPlayer.fleets[i].departurePlanet.coords)
                 + ". Destination: " + str(currentPlayer.fleets[i].destination)
                 + "\nArrival: " + formatDate(currentPlayer.fleets[i].arrivalTime)
                 + ". Return: " + formatDate(currentPlayer.fleets[i].returnTime)
        )
        allLabels["Mission Cancel " + str(i + 1)].place(relx=0.01, rely=0.17 + 0.166 * i, relwidth=0.03, relheight=0.15)
        allLabels["Mission Cancel " + str(i + 1)].configure(text="X")
        allLabels["Mission Cancel " + str(i + 1)].bind("<Button-1>",
                                                       lambda event, idx=currentPlayer.fleets[i]: cancelMission(event,
                                                                                                                idx))

    fleet = Classes.Fleet(currentPlanet,
                          {"Small Cargo": int(allPEntries["Fleet Amount 1"].get()),
                           "Large Cargo": int(allPEntries["Fleet Amount 2"].get()),
                           "Light Fighter": int(allPEntries["Fleet Amount 3"].get()),
                           "Heavy Fighter": int(allPEntries["Fleet Amount 4"].get()),
                           "Cruiser": int(allPEntries["Fleet Amount 5"].get()),
                           "Battleship": int(allPEntries["Fleet Amount 6"].get()),
                           "Colony Ship": int(allPEntries["Fleet Amount 7"].get()),
                           "Recycler": int(allPEntries["Fleet Amount 8"].get()),
                           "Espionage Probe": int(allPEntries["Fleet Amount 9"].get()),
                           "Bomber": int(allPEntries["Fleet Amount 10"].get()),
                           "Destroyer": int(allPEntries["Fleet Amount 11"].get()),
                           "Deathstar": int(allPEntries["Fleet Amount 12"].get()),
                           "Battlecruiser": int(allPEntries["Fleet Amount 13"].get()),
                           "Mega Cargo": int(allPEntries["Fleet Amount 14"].get())})
    arrivalPlanetCoords = [int(allPEntries["Galaxy Destination"].get()),
                           int(allPEntries["Solar System Destination"].get()),
                           int(allPEntries["Planet Destination"].get())]
    speed = 1 if missionSpeed.get() == "Select Speed" else float(missionSpeed.get().strip("%")) / 100

    fuelRequired = FleetMissions.flightFuel(currentPlanet.coords, arrivalPlanetCoords, fleet, speed)
    cargoCapacityRemaining = ((FleetMissions.cargoSpace(fleet) - int(allPEntries["Metal Transport"].get())
                               - int(allPEntries["Crystal Transport"].get())
                               - int(allPEntries["Deuterium Transport"].get()))
                              - fuelRequired)
    flightTime = max(1, FleetMissions.flightTime(currentPlanet.coords, arrivalPlanetCoords, fleet, speed))
    arrivalTime = time.strftime("%H:%M:%S", time.gmtime((time.time() + flightTime) % 86400))
    returnTime = time.strftime("%H:%M:%S", time.gmtime((time.time() + 2 * flightTime) % 86400))

    allLabels["Commodity Price 4"].configure(anchor="nw", justify="left", text="Mission Details\n"
       + "\nFuel Required: " + str(fuelRequired)
       + "\nCargo Capacity: " + str(cargoCapacityRemaining)
       + "\nArrival Time: " + arrivalTime
       + "\nReturn Time: " + returnTime
       + "\nFlight Time (one way): " + formatTime(flightTime))

    cargo = [int(allPEntries["Metal Transport"].get()),
             int(allPEntries["Crystal Transport"].get()),
             int(allPEntries["Deuterium Transport"].get())]
    cargoCapacity = FleetMissions.cargoSpace(fleet) - fuelRequired

    # arrivalPlanet = currentPlanet
    if FleetMissions.missionViability(currentPlanet, arrivalPlanetCoords, fleet, speed, cargo, cargoCapacity,
                                      missionType.get()):
        allButtons["Purchase Button"].place(relx=0.61, rely=0.91, relwidth=0.38, relheight=0.08)
        arrive = time.time() + flightTime
        allButtons["Purchase Button"].configure(
            text="Confirm Mission",
            command=lambda: scheduleMission(
                currentPlanet, arrivalPlanetCoords, fleet, missionType.get(), speed, cargo, fuelRequired, arrive,
                arrive + flightTime
            )
        )

    for i in range(14):
        allLabels["Shop Panel " + str(i + 1)].place(relx=0.25 + 0.1 * (i % 7), rely=0.625 + 0.185 * (i // 7),
                                                    relwidth=.095, relheight=.175)
        allLabels["Shop Panel " + str(i + 1)].unbind("<Button-1>")
    for i in range(14):
        allPEntries["Fleet Amount " + str(i + 1)].place(relx=0.255 + 0.1 * (i % 7), rely=0.76 + 0.185 * (i // 7),
                                                        relwidth=0.085, relheight=0.03)

    # Display defenses
    # Place all the buttons we can use


#######################################################################################################################

### Button: View Defenses

#######################################################################################################################


def purchaseCommodity(commodityName):
    if currentView == "Construction" or currentView == "Research":
        DDB.cashier(currentPlanet, SDB.MasterCommoditiesList[commodityName])
    elif currentView == "Shipyard" or currentView == "Defense":
        DDB.cashier(currentPlanet, SDB.MasterCommoditiesList[commodityName], int(allPEntries["purchaseAmount"].get()))
        allPEntries["purchaseAmount"].put_placeholder()
    viewDictionary[currentView]()
    examineCommodity(root, commodityName)
    allButtons["Purchase Button"].place_forget()


def examineCommodity(event, commodityName):
    global currentCommodity
    currentCommodity = commodityName
    # Make building info pop up in the buildings overview frame
    allLabels["Commodity Info Title"].place(relx=0.6, rely=0.01, relwidth=0.39, relheight=0.2)
    if type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Building" \
            or type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Research":
        allLabels["Commodity Info Title"].configure(
            text=commodityName + "(Lvl. " + str(currentPlanet.commodities[commodityName]) + ")", font=('Courier', 18))
    else:
        allLabels["Commodity Info Title"].configure(
            text=commodityName + "(" + str(currentPlanet.commodities[commodityName]) + " Owned)", font=('Courier', 18))

    allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.58, relheight=.98)
    try:
        allLabels["Picture Frame"].configure(image=allDisplayPhotos[commodityName])
    except KeyError:
        allLabels["Picture Frame"].configure(image=allDisplayPhotos["Default"])

    # Access databases for player-specific information
    price = currentPlanet.getPrice(SDB.MasterCommoditiesList[commodityName], currentPlanet.commodities[commodityName])
    timeNeeded = currentPlanet.getTime(SDB.MasterCommoditiesList[commodityName],
                                       currentPlanet.commodities[commodityName], universeSpeed)

    # Display buttons like upgrade, dconstruct, exit
    if (DDB.verifyTechRequirements(currentPlanet, SDB.MasterCommoditiesList[commodityName])
            and DDB.verifyResourceRequirements(currentPlanet, SDB.MasterCommoditiesList[commodityName])):

        if (type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Building"
                and len(currentPlanet.buildingQueue) < 5):
            allButtons["Purchase Button"].place(relx=0.70, rely=0.875, relwidth=0.29, relheight=0.1)
            allButtons["Purchase Button"].configure(text="Upgrade (" + formatTime(timeNeeded) + ")",
                                                    command=lambda: purchaseCommodity(commodityName))
            if ((commodityName == "Robotics Factory" or commodityName == "Shipyard"
                 or commodityName == "Nanite Factory")
                    and len(currentPlanet.shipyardQueue) > 0):
                allButtons["Purchase Button"].place_forget()
            if commodityName == "Research Laboratory" and len(currentPlayer.researchQueue) > 0:
                allButtons["Purchase Button"].place_forget()

        elif (type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Research"
              and len(currentPlayer.researchQueue) == 0):
            allButtons["Purchase Button"].place(relx=0.70, rely=0.875, relwidth=0.29, relheight=0.1)
            allButtons["Purchase Button"].configure(text="Upgrade (" + formatTime(timeNeeded) + ")",
                                                    command=lambda: purchaseCommodity(commodityName))
            for planet in currentPlayer.planets:
                for item in planet.buildingQueue:
                    if item[0].name == "Research Laboratory":
                        allButtons["Purchase Button"].place_forget()

        elif ((type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Ship"
               or type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Defense")):
            allButtons["Purchase Button"].place(relx=0.70, rely=0.875, relwidth=0.29, relheight=0.1)
            allButtons["Purchase Button"].configure(text="Purchase (" + formatTime(timeNeeded) + ")",
                                                    command=lambda: purchaseCommodity(commodityName))
            for item in currentPlanet.buildingQueue:
                if item[0].name == "Shipyard" or item[0].name == "Robotics Factory" or item[0].name == "Nanite Factory":
                    allButtons["Purchase Button"].place_forget()
        else:
            allButtons["Purchase Button"].place_forget()
            allPEntries["purchaseAmount"].place_forget()
    else:
        allButtons["Purchase Button"].place_forget()

    resourcesNames = ["Metal: ", "Crystal: ", "Deuterium: ", "Energy: "]
    j = 0
    for i in range(4):
        if price[i] != 0:
            allLabels["Commodity Price " + str(i + 1)].place(
                relx=0.6 + 0.2 * (j % 2), rely=0.225 + 0.125 * (j // 2), relwidth=0.19, relheight=0.1)
            allLabels["Commodity Price " + str(i + 1)].configure(text=resourcesNames[i] + str(price[i]))
            j += 1
        else:
            allLabels["Commodity Price " + str(i + 1)].place_forget()
            allLabels["Commodity Price " + str(i + 1)].configure(text="")
    if (type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Ship"
            or type(SDB.MasterCommoditiesList[commodityName]).__name__ == "Defense"):
        allPEntries["purchaseAmount"].place(relx=0.70, rely=0.825, relwidth=0.13, relheight=0.05)
    allButtons["Commodity Info Info"].place(relx=0.8, rely=0.35, relwidth=0.19, relheight=0.1)
    allButtons["Commodity Info Info"].configure(command=lambda: infoPage(commodityName))
    update_wraplength(root)
    # resize_font()


defenseList = ["Rocket Launcher", "Light Laser", "Heavy Laser", "Gauss Cannon", "Ion Cannon", "Plasma Turret",
               "Small Shield Dome", "Large Shield Dome", "Antiballistic Missile", "Interplanetary Missile"]


def defenseScreen():
    global currentCommodity
    currentCommodity = None
    global currentView
    currentView = "Defense"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    allLabels["Picture Frame"].configure(image=allDisplayPhotos["Default"])
    for i in range(10):
        allLabels["Shop Panel " + str(i + 1)].place(
            relx=0.275 + 0.13 * (i % 5), rely=0.625 + 0.185 * (i // 5), relwidth=0.11, relheight=0.175)
        try:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails[defenseList[i]])
        except KeyError:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails["Default"])
        allLabels["Shop Panel " + str(i + 1)].bind(
            "<Button-1>", lambda event, idx=i: examineCommodity(event, defenseList[idx]))
    for i in range(11, 17):
        allLabels["Shop Panel " + str(i)].place_forget()


#######################################################################################################################

### Button: View Shipyard

#######################################################################################################################

shipyardList = ["Small Cargo", "Large Cargo", "Light Fighter", "Heavy Fighter", "Cruiser", "Battleship", "Colony Ship",
                "Recycler", "Espionage Probe", "Bomber", "Solar Satellite", "Destroyer", "Deathstar", "Battlecruiser",
                "Mega Cargo"]


def shipyardScreen():
    global currentCommodity
    currentCommodity = None
    global currentView
    currentView = "Shipyard"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    allLabels["Picture Frame"].configure(image=allDisplayPhotos["Shipyard Screen"])
    for i in range(15):
        allLabels["Shop Panel " + str(i + 1)].place(
            relx=0.25 + 0.0875 * (i % 8), rely=0.625 + 0.185 * (i // 8), relwidth=0.085, relheight=0.175)
        try:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails[shipyardList[i]])
        except KeyError:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails["Default"])
        allLabels["Shop Panel " + str(i + 1)].bind(
            "<Button-1>", lambda event, idx=i: examineCommodity(event, shipyardList[idx]))
    allLabels["Shop Panel 16"].place_forget()


#######################################################################################################################

### Button: View Research

#######################################################################################################################

researchList = ["Espionage Technology", "Computer Technology", "Weapons Technology", "Shielding Technology",
                "Armor Technology", "Energy Technology", "Hyperspace Technology", "Combustion Drive", "Impulse Drive",
                "Hyperspace Drive", "Laser Technology", "Ion Technology", "Plasma Technology",
                "Intergalactic Research Network", "Astrophysics", "Graviton Technology"]


def researchScreen():
    global currentCommodity
    currentCommodity = None
    global currentView
    currentView = "Research"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    allLabels["Picture Frame"].configure(image=allDisplayPhotos["Research Screen"])
    for i in range(16):
        allLabels["Shop Panel " + str(i + 1)].place(
            relx=0.25 + 0.0875 * (i % 8), rely=0.625 + 0.185 * (i // 8), relwidth=0.085, relheight=0.175)
        try:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails[researchList[i]])
        except KeyError:
            allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails["Default"])
        allLabels["Shop Panel " + str(i + 1)].bind(
            "<Button-1>", lambda event, idx=i: examineCommodity(event, researchList[idx]))


#######################################################################################################################

### Button: Constructions Screen

#######################################################################################################################

buildingsList = ["Metal Mine", "Crystal Mine", "Deuterium Synthesizer", "Solar Plant", "Fusion Reactor",
                 "Robotics Factory", "Nanite Factory", "Shipyard", "Metal Storage", "Crystal Storage", "Deuterium Tank",
                 "Research Laboratory", "Terraformer", "Missile Silo"]


def constructionScreen():
    global currentCommodity
    currentCommodity = None
    global currentView
    currentView = "Construction"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.5)
    allLabels["Picture Frame"].place(relx=0.01, rely=0.01, relwidth=0.98, relheight = 0.98)
    allLabels["Picture Frame"].configure(image=allDisplayPhotos["Construction Screen"])
    for i in range(14):
        allLabels["Shop Panel " + str(i + 1)].place(
            relx=0.25 + 0.1 * (i % 7), rely=0.625 + 0.185 * (i // 7), relwidth=.095, relheight=.175)
        allLabels["Shop Panel " + str(i + 1)].configure(image=allThumbnails[buildingsList[i]])
        allLabels["Shop Panel " + str(i + 1)].bind(
            "<Button-1>", lambda event, idx=i: examineCommodity(event, buildingsList[idx]))
    allLabels["Shop Panel 15"].place_forget()
    allLabels["Shop Panel 16"].place_forget()


#######################################################################################################################

### Button: Resource Settings

#######################################################################################################################

def changeResourceSettings():
    currentPlanet.resourceSettings[0] = float(metalRate.get().strip("%")) / 100
    currentPlanet.resourceSettings[1] = float(crystalRate.get().strip("%")) / 100
    currentPlanet.resourceSettings[2] = float(deuteriumRate.get().strip("%")) / 100
    currentPlanet.resourceSettings[3] = float(solarRate.get().strip("%")) / 100
    currentPlanet.resourceSettings[4] = float(fusionRate.get().strip("%")) / 100
    currentPlanet.resourceSettings[5] = float(satelliteRate.get().strip("%")) / 100
    resourceSettings()


def resourceSettings():
    global currentCommodity
    currentCommodity = None
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
        text=str(universeSpeed * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 9"].configure(
        text=str(universeSpeed * 24 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 10"].configure(
        text=str(universeSpeed * 24 * 7 * (33 + currentPlanet.resourceProductionRate()["Crystal Rate"])))
    allLabels["Resource Settings Crystal 11"].configure(text=str(currentPlanet.storage()[1]))
    allLabels["Resource Settings Deuterium 4"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Deuterium Rate"]))
    allLabels["Resource Settings Deuterium 6"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Fusion Rate"]))
    allLabels["Resource Settings Deuterium 8"].configure(
        text=str(universeSpeed * currentPlanet.resourceProductionRate()["Net Deuterium"]))
    allLabels["Resource Settings Deuterium 9"].configure(
        text=str(universeSpeed * 24 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
    allLabels["Resource Settings Deuterium 10"].configure(
        text=str(universeSpeed * 24 * 7 * (currentPlanet.resourceProductionRate()["Net Deuterium"])))
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
            allLabels["Resource Settings " + titleList[j] + str(i)].place(relx=j / 6 + 0.01, rely=i / 12 + 0.005,
                                                                          relwidth=1 / 6 - 0.02,
                                                                          relheight=1 / 12 - 0.01)
    allOptionMenus["Metal Menu"].place(relx=5 / 6 + 0.01, rely=2 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                       relheight=1 / 12 - 0.01)
    allOptionMenus["Crystal Menu"].place(relx=5 / 6 + 0.01, rely=3 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                         relheight=1 / 12 - 0.01)
    allOptionMenus["Deuterium Menu"].place(relx=5 / 6 + 0.01, rely=4 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                           relheight=1 / 12 - 0.01)
    allOptionMenus["Solar Menu"].place(relx=5 / 6 + 0.01, rely=5 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                       relheight=1 / 12 - 0.01)
    allOptionMenus["Fusion Menu"].place(relx=5 / 6 + 0.01, rely=6 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                        relheight=1 / 12 - 0.01)
    allOptionMenus["Satellite Menu"].place(relx=5 / 6 + 0.01, rely=7 / 12 + 0.005, relwidth=1 / 6 - 0.02,
                                           relheight=1 / 12 - 0.01)


allButtons["Resource Management"].configure(command=resourceSettings)
allLabels["Resource Settings Production Rate 11"].bind("<Button-1>", lambda event: changeResourceSettings())

#######################################################################################################################

### Button: Player Overview

#######################################################################################################################

allButtons["View Buildings"].configure(command=constructionScreen)
allButtons["View ResearchLab"].configure(command=researchScreen)
allButtons["View Shipyard"].configure(command=shipyardScreen)
allButtons["View Defenses"].configure(command=defenseScreen)
allButtons["View Galaxy"].configure(command=galaxyScreen)
allButtons["Manage Fleets"].configure(command=fleetsScreen)


def changePlanet(event, planet):
    global currentPlanet
    currentPlanet = planet
    allLabels["Galaxy"].configure(text="Galaxy: " + str(currentPlanet.coords[0]))
    allLabels["System"].configure(text="System: " + str(currentPlanet.coords[1]))


def saveGame():
    DDB.saveGame()
    allButtons["Save Button"].configure(text="Game saved successfully!")


def checkMessages():
    global currentView
    currentView = "Messages"
    clearGUI()
    mainFrame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    allButtons["Messages Button"].place(relx=0.01, rely =0.01, relwidth=0.09, relheight=0.09)
    allButtons["Messages Button"].configure(text="Exit", command=playerOverview)
    allLabels["Commodity Info Title"].place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.09)
    allLabels["Commodity Info Title"].configure(text="No messages")
    for i in range(len(currentPlayer.messages)):
            localFont = Font(family="Courier New", size=12)
            line_height = localFont.metrics("linespace")
            text = currentPlayer.messages[i].body
            num_lines = len(text.splitlines())
            textHeight = line_height * num_lines
            mainFrameHeight = mainFrame.winfo_height()
            labelRelHeight = textHeight/mainFrameHeight+0.05
            print(labelRelHeight)
            allLabels["Commodity Info Title"].place(relx=0.01, rely=0.11, relwidth=0.98, relheight=labelRelHeight)
            allLabels["Commodity Info Title"].configure(
                text="From: " + currentPlayer.messages[i].sender
                + "    Subject: " + currentPlayer.messages[i].subject
                + "\n Message: " + currentPlayer.messages[i].body,
            font = ("Courier New", 12))


def playerOverview():
    global currentCommodity, currentView
    currentCommodity = None
    currentView = "Overview"
    clearGUI()
    sideNav()
    topNav()
    mainFrame.place(relx=0.25, rely=.1, relwidth=.695, relheight=0.69)
    allLabels["Picture Frame"].place(relx=0.25, rely=0.01, relwidth=0.50, relheight=0.98)
    allLabels["Picture Frame"].configure(image=allDisplayPhotos["Planet Overview"])
    allLabels["Commodity Info Title"].place(relx=0.01, rely=0.01, relwidth=0.23, relheight=0.1)
    allLabels["Commodity Info Title"].configure(text=currentPlanet.name, font=("Courier New", 18))
    allLabels["Commodity Price 1"].place(relx=0.01, rely=0.12, relwidth=0.23, relheight=0.08)
    allLabels["Commodity Price 1"].configure(
        text="Coordinates: ("
             + str(currentPlanet.coords[0])
             + ":" + str(currentPlanet.coords[1])
             + ":" + str(currentPlanet.coords[2])
             + ")")
    allButtons["Save Button"].place(relx=0.76, rely=0.85, relwidth=0.23, relheight=0.14)
    allButtons["Save Button"].configure(text="Save Game", command=saveGame)
    allButtons["Messages Button"].place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.14)
    allButtons["Messages Button"].configure(text="Read Messages", command=checkMessages)

    for i in range(4):
        try:
            allLabels["Planet " + str(i + 1) + " Picture"].bind(
                "<Button-1>", lambda event, idx=currentPlayer.planets[i]: changePlanet(event, idx))
        except IndexError:
            break
        allLabels["Planet " + str(i + 1) + " Picture"].place(relx=0.4 + 0.1 * i, rely=.8, relwidth=.095, relheight=.175)
        allLabels["Planet " + str(i + 1) + " Picture"].configure(image=allThumbnails["Default"])
    if len(currentPlayer.planets) > 4:
        allButtons["Left Arrow"].place(relx=0.3725, rely=0.8, relwidth=0.02, relheight=0.175)
        allButtons["Right Arrow"].place(relx=0.8, rely=0.8, relwidth=0.02, relheight=0.175)

    # allLabels["Planet 4 Picture"].place(relx=0.8, rely=.8, relwidth=.095, relheight=.175)
    # allLabels["Planet 4 Picture"].configure(image=allThumbnails["Default"])
    # allLabels["Planet 4 Picture"].bind("<Button-1>", lambda event: changePlanet(event, DDB.planetList["Tree House"]))

    allLabels["Galaxy"].configure(text="Galaxy: " + str(currentPlanet.coords[0]))
    allLabels["System"].configure(text="System: " + str(currentPlanet.coords[1]))





allButtons["Overview"].configure(command=playerOverview)
allLabels["Resource Settings Source 0"].bind("<Button-1>", lambda event: playerOverview())


#######################################################################################################################

### Button: New Game

#######################################################################################################################

# Carries out the process for beginning a new game.
def newGame():
    global currentPlayer
    global currentPlanet
    DDB.newPlayer("Piggy", "Planet Piggie")
    DDB.newPlayer("Evil Squirrel", "Tree House")
    DDB.currentPlayer = DDB.playerList["Piggy"]
    currentPlayer = DDB.playerList["Piggy"]
    currentPlanet = DDB.planetList["Planet Piggie"]
    Classes.standardMessage(DDB.playerList["Piggy"])
    DDB.planetList["Planet Piggie"].commodities["Espionage Probe"] = 10
    for i in range(50):
        DDB.newPlayer("Bot " + str(i), "Planet " + str((2 ^ i) % 53))
    playerOverview()
    updateEverything()


viewDictionary = {
    "Overview": playerOverview,
    "Messages": checkMessages,
    "Construction": constructionScreen,
    "Research": researchScreen,
    "Shipyard": shipyardScreen,
    "Defense": defenseScreen,
    "Galaxy": galaxyScreen,
    "Fleets": fleetsScreen,
    "Resource Settings": resourceSettings
}


#######################################################################################################################

### Button: Load Game

#######################################################################################################################

def loadGame():
    DDB.loadGame()
    global currentPlayer, currentPlanet
    currentPlayer = DDB.currentPlayer
    currentPlanet = currentPlayer.planets[0]
    playerOverview()
    updateEverything()


#######################################################################################################################

### Button: Options

#######################################################################################################################


#######################################################################################################################

### Main Menu

#######################################################################################################################

# This will be the entry point of the game

def overwriteWarning():
    clearGUI()
    allLabels["Planet 1 Picture"].place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    allLabels["Planet 1 Picture"].configure(text="Overwrite previously saved game?")
    allButtons['New Game Button'].configure(text="I don't care. Start new game.", command=newGame)
    allButtons['New Game Button'].place(relx=0.2, rely=0.26, relwidth=0.6, relheight=0.14)
    allButtons['Load Game Button'].configure(text="Go back.", command=mainMenu)
    allButtons['Load Game Button'].place(relx=0.2, rely=0.41, relwidth=0.6, relheight=0.14)



def mainMenu():
    clearGUI()
    allButtons['New Game Button'].configure(text="New Game", command=overwriteWarning)
    allButtons['New Game Button'].place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    allButtons['Load Game Button'].place(relx=0.2, rely=0.31, relwidth=0.6, relheight=0.15)
    allButtons['Load Game Button'].configure(text="Load Game", command=loadGame)
    # allButtons['Options Button'].place(relx=0.2, rely=0.53333, relwidth=0.6, relheight=0.15)
    # allButtons['Quit Button'].configure(command = root.destroy)
    # allButtons['Quit Button'].place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.15)


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

mainMenu()
root.mainloop()
