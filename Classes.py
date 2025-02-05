# Here we define the necessary classes for the game to run properly

import tkinter as tk

# Oddly enough, we need this here for this to work correctly
technologyTree = {}


# Bots can be players too
class Player:
    def __init__(self, name, planets, researchQueue=[], fleets=None, messages=None):
        if fleets is None:
            fleets = []
        if messages is None:
            messages = []
        self.name = name  # Name
        self.planets = planets  # List of all planets (instances) owned by player
        self.researchQueue = []  # List of all ongoing research [research (instance), current Level + 1, start time]
        for i in range(len(researchQueue)):
            self.researchQueue.append([Research(**researchQueue[i][0]), researchQueue[i][1], researchQueue[i][2]])
        self.fleets = fleets  # All fleet action owned by the player
        self.messages = messages  # List of messages in player's inbox

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "planets": [planet.toDict() for planet in self.planets],
            "researchQueue": [[item[0].toDict(), item[1], item[2]] for item in self.researchQueue],
            "fleets": [mission.toDict() for mission in self.fleets],
            "messages": [message.toDict() for message in self.messages],
            }


# class Bot(Player):
#     def __init__(self, name, ID, planets, faction, speed, size, aggro):
#         Player.__init__(self, name, ID, planets, faction)
#         self.speed = speed                                       #How quickly a bot moves from one goal to the next
#         self.size = size                                         #How large the bot is allowed to grow
#         self.aggro = aggro                                       #How aggressive the bot is
#         self.Goals = []                                          #What is the bot focusing on next?


class Planet:
    def __init__(self, name, coords, ownerName, resources, resourceSettings=None,
                 commodities=None, buildingQueue=[], shipyardQueue=[], debris = None):
        if resourceSettings is None:
            resourceSettings = [1, 1, 1, 1, 1, 1]
        if commodities is None:
            commodities = {"Metal Mine": 0,
                            "Crystal Mine": 0,
                            "Deuterium Synthesizer": 0,
                            "Solar Plant": 0,
                            "Fusion Reactor": 0,
                            "Robotics Factory": 0,
                            "Nanite Factory": 0,
                            "Shipyard": 0,
                            "Metal Storage": 0,
                            "Crystal Storage": 0,
                            "Deuterium Tank": 0,
                            "Research Laboratory": 0,
                            "Terraformer": 0,
                            "Missile Silo": 0,

                            "Espionage Technology": 0,
                            "Computer Technology": 0,
                            "Weapons Technology": 0,
                            "Shielding Technology": 0,
                            "Armor Technology": 0,
                            "Energy Technology": 0,
                            "Hyperspace Technology": 0,
                            "Combustion Drive": 0,
                            "Impulse Drive": 0,
                            "Hyperspace Drive": 0,
                            "Laser Technology": 0,
                            "Ion Technology": 0,
                            "Plasma Technology": 0,
                            "Intergalactic Research Network": 0,
                            "Astrophysics": 0,
                            "Graviton Technology": 0,

                            "Small Cargo": 0,
                            "Large Cargo": 0,
                            "Light Fighter": 0,
                            "Heavy Fighter": 0,
                            "Cruiser": 0,
                            "Battleship": 0,
                            "Colony Ship": 0,
                            "Recycler": 0,
                            "Espionage Probe": 0,
                            "Bomber": 0,
                            "Solar Satellite": 0,
                            "Destroyer": 0,
                            "Deathstar": 0,
                            "Battlecruiser": 0,
                            "Mega Cargo": 0,

                            "Rocket Launcher": 0,
                            "Light Laser": 0,
                            "Heavy Laser": 0,
                            "Gauss Cannon": 0,
                            "Ion Cannon": 0,
                            "Plasma Turret": 0,
                            "Small Shield Dome": 0,
                            "Large Shield Dome": 0,
                            "Antiballistic Missile": 0,
                            "Interplanetary Missile": 0}  # Make sure emptyCommoditiesList is defined elsewhere
        if debris is None:
            debris = [0, 0, 0]

        self.name = name  # Name of planet
        self.coords = coords  # Location of planet
        self.owner = ownerName  # Owner of planet (string)
        self.resources = resources  # Resources on planet
        self.resourceSettings = resourceSettings  # Metal, Crystal, Deuterium, Solar, Fusion, Satellite rates
        self.commodities = commodities  # List of buildings, research, ships, and defenses
        self.buildingQueue = [[Building(**buildingQueue[i][0]), buildingQueue[i][1], buildingQueue[i][2]] for i in range(len(buildingQueue))]
            # [commodity (instance), currentLevel + 1, endTime] to initialize, pass the commodity as commodity.toDict()
        self.shipyardQueue = []  # [commodity (instance), i, startTime] List of all ships/defenses in production  (Max 15)
        for i in range(len(shipyardQueue)):
            if len(shipyardQueue[i][0]) == 4:
                self.shipyardQueue.append([Defense(**shipyardQueue[i][0]), shipyardQueue[i][1], shipyardQueue[i][2]])
            else:
                self.shipyardQueue.append([Ship(**shipyardQueue[i][0]), shipyardQueue[i][1], shipyardQueue[i][2]])
        self.debris = debris   # Resources in debris field
        # Planet.moons = []      # Moons belonging to planet

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "coords": self.coords,
            "ownerName": self.owner,
            "resources": self.resources,
            "resourceSettings": self.resourceSettings,
            "commodities": self.commodities,
            "buildingQueue": [[item[0].toDict(), item[1], item[2]] for item in self.buildingQueue],
            "shipyardQueue": [[item[0].toDict(), item[1], item[2]] for item in self.shipyardQueue],
            "debris": self.debris,
            # Planet.moons = []      # Moons belonging to planet
        }

    def storage(self):
        capacityList = [10000, 20000, 40000, 75000, 140000, 255000]
        for i in range(15):
            capacityList.append(2 * capacityList[-1] - capacityList[-5])
        return [capacityList[self.commodities["Metal Storage"]], capacityList[self.commodities["Crystal Storage"]],
                capacityList[self.commodities["Deuterium Tank"]]]

    def getPrice(self, commodity, currentLevel):
        if type(commodity).__name__ == "Building":  # Building type
            metal = commodity.baseCost[0] * (commodity.upgradeMultipliers[0] ** currentLevel)
            crystal = commodity.baseCost[1] * (commodity.upgradeMultipliers[0] ** currentLevel)
            deuterium = commodity.baseCost[2] * (commodity.upgradeMultipliers[0] ** currentLevel)
            energy = commodity.baseCost[3] * (currentLevel + 1) * (commodity.upgradeMultipliers[1] ** currentLevel)
            return [int(metal), int(crystal), int(deuterium), int(energy)]
        elif type(commodity).__name__ == "Research":
            metal = commodity.baseCost[0] * (2 ** currentLevel)
            crystal = commodity.baseCost[1] * (2 ** currentLevel)
            deuterium = commodity.baseCost[2] * (2 ** currentLevel)
            energy = commodity.baseCost[3] * (2 ** currentLevel)
            return [int(metal), int(crystal), int(deuterium), int(energy)]
        else:
            return commodity.baseCost

    def getTime(self, commodity, currentLevel, universeSpeed):
        if type(commodity).__name__ == "Building":
            upgradePrice = self.getPrice(commodity, currentLevel)
            timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (
                    2500 * (1 + self.commodities["Robotics Factory"]) * universeSpeed * (
                        2 ** self.commodities["Nanite Factory"]))
            return max(1, int(3600 * timeNeeded))
        elif type(commodity).__name__ == "Research":
            upgradePrice = self.getPrice(commodity, currentLevel)
            timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (
                        1000 * (1 + self.commodities["Research Laboratory"]) * universeSpeed)
            return max(1, int(3600 * timeNeeded))
        elif type(commodity).__name__ == "Ship" or type(commodity).__name__ == "Defense":
            upgradePrice = self.getPrice(commodity, currentLevel)
            timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (
                        2500 * (1 + self.commodities["Shipyard"]) * universeSpeed * (
                            2 ** self.commodities["Nanite Factory"]))
            return max(1, int(3600 * timeNeeded))


    def resourceProductionRate(self):
        metalEnergy = int(-1 * 22 * self.commodities["Metal Mine"] * 1.1 ** (self.commodities["Metal Mine"] - 1) *
                          self.resourceSettings[0])
        crystalEnergy = int(
            -1 * 22 * self.commodities["Crystal Mine"] * 1.1 ** (self.commodities["Crystal Mine"] - 1) *
            self.resourceSettings[1])
        deuteriumEnergy = int(
            -1 * 33 * self.commodities["Deuterium Synthesizer"] * 1.1 **
            (self.commodities["Deuterium Synthesizer"] - 1) * self.resourceSettings[2])
        solarProduction = int(
            20 * self.commodities["Solar Plant"] * 1.1 ** self.commodities["Solar Plant"] * self.resourceSettings[3])
        fusionProduction = 0
        if self.resources[2] >= 1:
            fusionProduction = int(
                30 * self.commodities["Fusion Reactor"] * 1.05 ** self.commodities["Fusion Reactor"] *
                self.resourceSettings[4])
        satelliteProduction = int(20 * self.commodities["Solar Satellite"] * self.resourceSettings[5])
        energyNeeded = metalEnergy + crystalEnergy + deuteriumEnergy
        energyProduced = solarProduction + fusionProduction + satelliteProduction
        netEnergy = energyProduced + energyNeeded
        energyCoefficient = min((0.001 + energyProduced) / (0.001 - energyNeeded), 1)

        metalRate = int((30 * self.commodities["Metal Mine"] * (1.1 ** self.commodities["Metal Mine"])) * min(
            energyCoefficient, self.resourceSettings[0]))
        crystalRate = int((20 * self.commodities["Crystal Mine"] * (1.1 ** self.commodities["Crystal Mine"])) * min(
            energyCoefficient, self.resourceSettings[1]))
        deuteriumRate = int(10 * (self.commodities["Deuterium Synthesizer"] * (
                1.1 ** self.commodities["Deuterium Synthesizer"])) * min(energyCoefficient, self.resourceSettings[2]))
        fusionRate = int(
            -10 * (self.commodities["Fusion Reactor"] * (1.1 ** self.commodities["Fusion Reactor"])) *
            self.resourceSettings[4])
        return {"Metal Energy": metalEnergy,
                "Crystal Energy": crystalEnergy,
                "Deuterium Energy": deuteriumEnergy,
                "Solar Production": solarProduction,
                "Fusion Production": fusionProduction,
                "Satellite Production": satelliteProduction,
                "Net Energy": netEnergy,
                "Metal Rate": metalRate,
                "Crystal Rate": crystalRate,
                "Deuterium Rate": deuteriumRate,
                "Fusion Rate": fusionRate,
                "Net Deuterium": deuteriumRate + fusionRate}


# class Moon:
#     def __init__(self, name, motherPlanet):
#         Moon.name = name                                        #Name of Moon
#         Moon.motherPlanet = motherPlanet                        #Planet the Moon is orbiting
#         Moon.buildings = []                                     #Buildings on Moon
#         Moon.resources = [0, 0, 0, 0]                           #Resources on Moon
#         Moon.storage = [0, 0, 0]                                # How much of each resource can the Moon store
#         Moon.buildings = []                                     # List of all building levels on Moon
#         Moon.shipyard = []                                      # List of all ships on Moon
#         Moon.defenses = []                                      # List of all defenses on Moon
#         Moon.fleets = []                                        # All fleet action Moon is involved in


class Building:
    def __init__(self, name, baseCost, upgradeMultipliers, baseTime, baseProduction):
        self.name = name  # 1 = Metal Mine, 2 = Crystal Mine, ...
        self.baseCost = baseCost  # Metal, Crystal, Deuterium, Energy costs
        self.upgradeMultipliers = upgradeMultipliers  # This is how much the costs and time increase per level
        self.baseTime = baseTime  # Time it takes to upgrade building to level 1
        self.baseProduction = baseProduction  # Metal, Crystal, Deuterium, Energy production values
        # self.planetary = True                             # Records whether the building is planetary or lunar

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "baseCost": self.baseCost,
            "upgradeMultipliers": self.upgradeMultipliers,
            "baseTime": self.baseTime,
            "baseProduction": self.baseProduction,
            # "planetary": self.planetary
        }

    def getTech(self):
        return technologyTree[self.name]

    def getPrice(self, currentLevel):
        metal = self.baseCost[0] * (self.upgradeMultipliers[0] ** currentLevel)
        crystal = self.baseCost[1] * (self.upgradeMultipliers[0] ** currentLevel)
        deuterium = self.baseCost[2] * (self.upgradeMultipliers[0] ** currentLevel)
        energy = self.baseCost[3] * (self.upgradeMultipliers[1] ** currentLevel)
        return [int(metal), int(crystal), int(deuterium), int(energy)]

    def getTime(self, currentLevel, universeSpeed, roboticsFactory, naniteFactory):  # in seconds
        upgradePrice = self.getPrice(currentLevel)
        timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (
                    2500 * (1 + roboticsFactory) * universeSpeed * (2 ** naniteFactory))
        return max(1, int(3600 * timeNeeded))


class Research:
    def __init__(self, name, baseCost, baseTime):
        self.name = name  # 1 = Metal Mine, 2 = Crystal Mine, ...
        self.baseCost = baseCost  # Metal, Crystal, Deuterium, Energy costs
        self.baseTime = baseTime  # Time it takes to upgrade research to level 1

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "baseCost": self.baseCost,
            "baseTime": self.baseTime
        }

    def getTech(self):
        return technologyTree[self.name]

    def getPrice(self, currentLevel):
        metal = self.baseCost[0] * (2 ** currentLevel)
        crystal = self.baseCost[1] * (2 ** currentLevel)
        deuterium = self.baseCost[2] * (2 ** currentLevel)
        energy = self.baseCost[3] * (2 ** currentLevel)
        return [int(metal), int(crystal), int(deuterium), int(energy)]

    def getTime(self, currentLevel, universeSpeed, researchLab):  # in seconds
        upgradePrice = self.getPrice(currentLevel)
        timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (1000 * (1 + researchLab) * universeSpeed)
        return max(1, int(3600 * timeNeeded))


class Defense:
    def __init__(self, name, baseCost, baseShields, baseDamage):
        self.name = name  # Name of Defense
        self.baseCost = baseCost  # Metal, Crystal, Deuterium, Energy costs
        self.baseArmor = self.baseCost[0] + self.baseCost[1]  # Armor rating of Defense
        self.baseDamage = baseDamage  # Damage rating of Defense
        self.baseShields = baseShields  # Shield rating of Defense

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "baseCost": self.baseCost,
            "baseShields": self.baseShields,
            "baseDamage": self.baseDamage,
        }

    def getTech(self):
        return technologyTree[self.name]

    def getPrice(self, currentLevel=None):
        return self.baseCost

    def getTime(self, universeSpeed, roboticsFactory, naniteFactory):  # in seconds
        timeNeeded = (self.baseCost[0] + self.baseCost[1]) / (
                    2500 * (1 + roboticsFactory) * universeSpeed * (2 ** naniteFactory))
        return max(1, int(3600 * timeNeeded))


class Ship(Defense):
    def __init__(self, name, baseCost, baseShields, baseDamage, baseSpeed, baseCargo, baseFuel):
        Defense.__init__(self, name, baseCost, baseDamage, baseShields)
        self.baseCargo = baseCargo  # Cargo storage of ship
        self.baseFuel = baseFuel  # Fuel consumption of ship
        self.baseSpeed = baseSpeed  # Speed rating of the ship

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        return {
            "name": self.name,
            "baseCost": self.baseCost,
            "baseShields": self.baseShields,
            "baseDamage": self.baseDamage,
            "baseSpeed": self.baseSpeed,
            "baseCargo": self.baseCargo,
            "baseFuel": self.baseFuel
        }


class Mission:
    def __init__(self, owner, departurePlanet, destination, fleet, missionType, cargo, speed, start, arrivalTime, returnTime=None, fuel=None):
        self.owner = owner  # Owner of fleet (string)
        self.departurePlanet = departurePlanet  # Planet where fleet starts
        self.destination = destination  # Coordinates of planet where fleet is going
        self.fleet = fleet  # See instance below
        self.missionType = missionType  # Explore, Transport, Attack, Return, etc.
        self.cargo = cargo  # Resources on ship
        self.speed = speed  # Relative speed of fleet
        self.start = start  # Start time of mission
        self.arrivalTime = arrivalTime
        self.returnTime = returnTime
        self.fuel = fuel

    def toDict(self):
        return{
            "owner": self.owner,
            "departurePlanet": self.departurePlanet.toDict(),
            "destination": self.destination,
            "fleet": self.fleet.toDict(),
            "missionType": self.missionType,
            "cargo": self.cargo,
            "speed": self.speed,
            "start": self.start,
            "arrivalTime": self.arrivalTime,
            "returnTime": self.returnTime,
            "fuel": self.fuel,
        }


class Fleet:
    def __init__(self, ownerPlanet, ships):
        self.ownerPlanet = ownerPlanet     # Planet instance
        self.ships = ships                 # Dictionary {"Ship Name": number of ships, "Ship Name2": number of ships...}

    def toDict(self):
        return {
            "ownerPlanet": self.ownerPlanet.name,
            "ships": self.ships
        }


class Message:
    def __init__(self, sender, recipient, body, subject):
        self.sender = sender  #(string) This is the name of the player who sent the message
        self.recipient = recipient  # (string) This is the intended recipient of the message
        self.body = body  #(string) This is the text included in the message
        self.subject = subject  #(string) Construction, mission completion, battle report, etc...

    def toDict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "body": self.body,
            "subject": self.subject
        }

def standardMessage(player):
    message = Message("System", player.name, "Welcome to the game!", "Welcome")
    player.messages.append(message)


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", default="0", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.defaultValue = default
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        # Set the initial content of the entry to the placeholder
        self.put_placeholder()

        # Set up input validation to allow only digits
        validate_command = (self.register(self.validate_input), '%P')
        self.config(validate='key', validatecommand=validate_command)

        # Bind focus events
        self.bind("<FocusIn>", self.foc_in)
        # self.bind("<FocusOut>", self.foc_out)

    def put_placeholder(self):
        self.delete(0, 'end')  # Clear any existing text
        self.insert(0, self.placeholder)  # Insert the placeholder text
        self['fg'] = self.placeholder_color  # Set the placeholder text color

    def foc_in(self, *args):
        # Remove the placeholder when the user clicks in the entry box
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')  # Remove the placeholder
            self['fg'] = self.default_fg_color  # Set the text color back to normal

    # def foc_out(self, *args):
    #     if len(input_value)
    #     self.put_placeholder()

    def get(self):
        value = super().get()
        # If the value is the placeholder, return an empty string instead
        if value == self.placeholder or value == "":
            return self.defaultValue
        return value

    def validate_input(self, input_value):
        # Allow only digits (or empty string for backspace)
        if input_value == "" or input_value.isdigit():
            return True
        return False


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.config(fg="grey")

        # Bind events to manage placeholder text
        self.bind("<FocusIn>", self.remove_placeholder)
        self.bind("<FocusOut>", self.add_placeholder)
        self.bind("<KeyRelease>", self.check_for_empty_text)

    def remove_placeholder(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg="black")

    def add_placeholder(self, event=None):
        if self.get() == "":
            self.insert(0, self.placeholder)
            self.config(fg="grey")

    def check_for_empty_text(self, event=None):
        if self.get() == "":
            self.add_placeholder()

    def specialGet(self):
        value = super().get()
        # If the value is the placeholder, return an empty string instead
        if value == self.placeholder or value == "":
            return "0"
        return value
