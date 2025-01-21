# Here we define the necessary classes for the game to run properly

# Oddly enough, we need this here for this to work correctly
technologyTree = { }

# Bots can be players too
class Player:
    def __init__(self, name, planets):
        self.name = name                                      # Name
        self.planets = planets                                # List of all planets owned by player
        self.fleets = []                                      # All fleet action owned by the player
        self.friends = []                                     # List of friends
        self.messages = []                                    # List of messages in player's inbox
        # self.faction = faction                                # What faction the player belongs to
    def __repr__(self):
        return f"{self.name}"


# class Bot(Player):
#     def __init__(self, name, ID, planets, faction, speed, size, aggro):
#         Player.__init__(self, name, ID, planets, faction)
#         self.speed = speed                                       #How quickly a bot moves from one goal to the next
#         self.size = size                                         #How large the bot is allowed to grow
#         self.aggro = aggro                                       #How aggressive the bot is
#         self.Goals = []                                          #What is the bot focusing on next?


class Planet:
    def __init__(self, name, coords, owner, resources):
        self.name = name                                      #Name of planet
        self.coords = coords                                  #Location of planet
        self.ownerName = owner                                #Owner of planet
        self.resources = resources                            #Resources on planet
        self.storage = [10000, 10000, 10000]                  #How much of each resource can the planet store
        self.buildings = {"Metal Mine": 0,
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
                          "Missile Silo": 0
                          }                                #List of all building levels on planet
        self.research = {"Espionage Technology": 0,
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
                         "Graviton Technology": 0
                         }                                 #List of all research owned by planet (hence, the player)
        self.shipyard = { "Small Cargo" : 0,
        "Large Cargo" : 0,
        "Light Fighter" : 0,
        "Heavy Fighter" : 0,
        "Cruiser" : 0,
        "Battleship" : 0,
        "Colony Ship" : 0,
        "Recycler" : 0,
        "Espionage Probe" : 0,
        "Bomber" : 0,
        "Solar Satellite" : 0,
        "Destroyer" : 0,
        "Deathstar" : 0,
        "Battlecruiser" : 0,
        "Mega Cargo" : 0
}                                 #List of all ships on planet
        self.defenses = { "Rocket Launcher" : 0,
            "Light Laser" : 0,
            "Heavy Laser" : 0,
            "Gauss Cannon" : 0,
            "Ion Cannon" : 0,
            "Plasma Turret" : 0,
            "Small Shield Dome" : 0,
            "Large Shield Dome" : 0,
            "Antiballistic Missile" : 0,
            "Interplanetary Missile" : 0
            }                                 #List of all defenses on planet
        self.commodities = {**self.buildings,
                            **self.research,
                            **self.shipyard,
                            **self.defenses} #List of technology requirements
        self.buildingQueue = []                               #List of all buildings in production  (Max 5)
        self.shipyardQueue = []                               #List of all ships/defenses in production  (Max 15)
        self.fleets = []                                      #All fleet action planet is involved in
        self.debris = [0, 0, 0]                               #Resources in debris field
        # Planet.moons = []                                     #Moons belonging to planet
    def __repr__(self):
        return f"{self.name}"
    def getPrice(self, type, commodity):
        if type == "Building":  # Building type
            nextLevel = self.buildings[commodity.name]
            metal = commodity.baseCost[0] * (commodity.upgradeMultipliers[0] ** nextLevel)
            crystal = commodity.baseCost[1] * (commodity.upgradeMultipliers[0] ** nextLevel)
            deuterium = commodity.baseCost[2] * (commodity.upgradeMultipliers[0] ** nextLevel)
            energy = commodity.baseCost[3] * (commodity.upgradeMultipliers[1] ** nextLevel)
            return [int(metal), int(crystal), int(deuterium), int(energy)]
        elif type == "Research":
            nextLevel = self.buildings[commodity.name]
            metal = commodity.baseCost[0] * (2 ** nextLevel)
            crystal = commodity.baseCost[1] * (2 ** nextLevel)
            deuterium = commodity.baseCost[2] * (2 ** nextLevel)
            energy = commodity.baseCost[3] * (2 ** nextLevel)
            return [int(metal), int(crystal), int(deuterium), int(energy)]
        else:
            return commodity.baseCost

    def getTime(self, type, commodity, universeSpeed):
        if type == "Building":
            upgradePrice = self.getPrice(type, commodity)
            timeNeeded = (upgradePrice[0] + upgradePrice[1]) / (
                        2500 * (1 + self.buildings["Robotics Factory"]) * universeSpeed * (2 ** self.buildings["Nanite Factory"]))
            return max(1, int(3600 * timeNeeded))


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
        self.name = name                                    # 1 = Metal Mine, 2 = Crystal Mine, ...
        self.baseCost = baseCost                            # Metal, Crystal, Deuterium, Energy costs
        self.upgradeMultipliers = upgradeMultipliers        # This is how much the costs and time increase per level
        self.baseTime = baseTime                            # Time it takes to upgrade building to level 1
        self.baseProduction = baseProduction                # Metal, Crystal, Deuterium, Energy production values
        # self.planetary = True                             # Records whether the building is planetary or lunar
    def __repr__(self):
        return f"{self.name}"
    def getTech(self):
        return technologyTree[self.name]
    def getPrice(self, nextLevel):
        metal = self.baseCost[0]*(self.upgradeMultipliers[0]**nextLevel)
        crystal= self.baseCost[1]*(self.upgradeMultipliers[0]**nextLevel)
        deuterium = self.baseCost[2]*(self.upgradeMultipliers[0]**nextLevel)
        energy = self.baseCost[3]*(self.upgradeMultipliers[1]**nextLevel)
        return [int(metal), int(crystal), int(deuterium), int(energy)]
    def getTime(self, nextLevel, universeSpeed, roboticsFactory, naniteFactory): #in seconds
        upgradePrice = self.getPrice(nextLevel)
        timeNeeded = (upgradePrice[0] + upgradePrice[1])/(2500*(1+roboticsFactory)*universeSpeed*(2**naniteFactory))
        return max(1, int(3600 * timeNeeded))


class Research:
    def __init__(self, name, baseCost, baseTime):
        self.name = name                                    # 1 = Metal Mine, 2 = Crystal Mine, ...
        self.baseCost = baseCost                            # Metal, Crystal, Deuterium, Energy costs
        self.baseTime = baseTime                            # Time it takes to upgrade research to level 1
    def __repr__(self):
        return f"{self.name}"
    def getTech(self):
        return technologyTree[self.name]
    def getPrice(self, nextLevel):
        metal = self.baseCost[0]*(2**nextLevel)
        crystal= self.baseCost[1]*(2**nextLevel)
        deuterium = self.baseCost[2]*(2**nextLevel)
        energy = self.baseCost[3]*(2**nextLevel)
        return [int(metal), int(crystal), int(deuterium), int(energy)]
    def getTime(self, nextLevel, universeSpeed, researchLab): #in seconds
        upgradePrice = self.getPrice(nextLevel)
        timeNeeded = (upgradePrice[0] + upgradePrice[1])/(1000*(1+researchLab)*universeSpeed)
        return max(1,int(3600*timeNeeded))


class Defense:
    def __init__(self, name, baseCost, baseShields, baseDamage):
        self.name = name                                     # Name of Defense
        self.baseCost = baseCost                             # Metal, Crystal, Deuterium, Energy costs
        self.baseArmor = self.baseCost[0]+self.baseCost[1] # Armor rating of Defense
        self.baseDamage = baseDamage                         # Damage rating of Defense
        self.baseShields = baseShields                       # Shield rating of Defense
    def __repr__(self):
        return f"{self.name}"
    def getTech(self):
        return technologyTree[self.name]
    def getPrice(self, nextLevel):
        return self.baseCost
    def getTime(self, universeSpeed, roboticsFactory, naniteFactory): #in seconds
        timeNeeded = (self.baseCost[0] + self.baseCost[1])/(2500*(1+roboticsFactory)*universeSpeed*(2**naniteFactory))
        return max(1,int(3600*timeNeeded))

class Ship(Defense):
    def __init__(self, name, baseCost, baseDamage, baseShields, baseSpeed, baseCargo,
                baseFuel):
        Defense.__init__(self, name, baseCost, baseDamage, baseShields)
        self.baseCargo = baseCargo                              #Cargo storage of ship
        self.baseFuel = baseFuel                                #Fuel consumption of ship
        self.baseSpeed = baseSpeed                              #Speed rating of the ship
    def __repr__(self):
        return f"{self.name}"

class Mission:
    def __init__(self, owner, departure, arrival, fleet, occasion, cargo, speed, start):
        self.owner = owner                                   #Owner of fleet
        self.departure = departure                           #Coordinates of planet where fleet starts
        self.arrival = arrival                               #Coordinates of planet where fleet is going
        self.fleet = fleet                                   #List of numbers of ships
        self.occasion = occasion                             #Explore, Transport, Attack, Return, etc.
        self.cargo = cargo                                   #Resources on ship
        self.speed = speed                                   #Relative speed of fleet
        self.start = start                                   #Start time of mission


class Message:
    def __init__(self, sender, recipient, body, occasion):
        self.sender = sender                                 #This is the player who sent the message
        self.recipient = recipient                           #This is the intended recipient of the message
        self.body = body                                     #This is the text included in the message
        self.occasion = occasion                             #Construction, mission completion, battle report, etc...

# Zebulon = Planet("Zebulon", [1,1,1], 1, 126)
#
# Randy = Player("Randy", 1, [Zebulon])
#
# Brandy = Bot("Brandy", 1, [Zebulon], 1, 1, 1)
#
# print(Brandy.name)
# print(Brandy.ID)
# print(Brandy.planets[0].name)

