# DDB stands for Dynamic DataBase. It contains all the information about the game that can change, like the list of
# players, the list of planets occupied and unoccupied, the list of missions ongoing, etc....
# This file also contains the necessary commands to change these things.

import Classes
import SDB
import random
import time

galaxies = 3
solarSystems = 5
planets = 5
universeSpeed = 100


#Keeps track of all players (and bots) in the game
playerList = {}


#Keeps track of all occupied planets in the universe
planetList = {}


# Keeps track of all unoccupied planets in the universe
uninhabited = [[i+1,j+1,k+1] for i in range(galaxies) for j in range(solarSystems) for k in range(planets)]


#Keeps track of all fleet activity in the universe
fleetAcitivity = []


#Keeps track of all buildings, research, ships, and defense building/deconstructing activity in the universe
# [planet (instance), commodity (instance), increment (amount), end time (seconds after epoch), purchase type, price]
purchaseQueue = []


# The function returns True if and only if the input planet has the tech required to purchase the input commodity.
def verifyTechRequirements(planet, commodity):
    techNeeded = commodity.getTech()
    for tech in techNeeded:
        if planet.commodities[tech] != techNeeded[tech]:
            return False
    return True


# The function returns True if and only if the input planet has the resources required to purchase the input commodity.
def verifyResourceRequirements(purchaseType, planet, commodity, amount = 1):
    resourcesAvaliable = planet.resources
    price = planet.getPrice(purchaseType, commodity, planet.commodities[commodity.name])
    for i in range(3):
        if resourcesAvaliable[i] < price[i] * amount:
            return False
    return True


# If the customer can make the payment, the cashier adds the purchase to the purchaseQueue.
def buildingCashier(planet, commodity):
    startTime = time.time()
    currentLevel = planet.commodities[commodity.name]
    if verifyTechRequirements(planet, commodity) and verifyResourceRequirements("Building", planet, commodity):
        if len(planet.buildingQueue) > 0:
            print("You are already building something!")
            return
        timeNeeded = planet.getTime("Building", commodity, currentLevel, universeSpeed)
        endTime = startTime + timeNeeded
        price = commodity.getPrice(currentLevel)
        planet.resources[0] -= price[0]
        planet.resources[1] -= price[1]
        planet.resources[2] -= price[2]
        purchaseQueue.append([planet, commodity, 1, endTime, "Building", price])
        planet.buildingQueue.append([commodity, currentLevel + 1, endTime])
        
        
# This function executes the purchases in purchaseQueue.
def updatePurchaseQueue():
    i = 0
    L = len(purchaseQueue)
    while i < L:
        item = purchaseQueue[i]
        if item[3] < time.time():
            item[0].commodities[item[1].name] += 1
            planetList[item[0].name] = item[0]
            if item[4] == "Building":
                planetList[item[0].name].buildingQueue = []
            elif item[4] == "Ships And Defense":
                planetList[item[0].name].shipyardQueue = []
            purchaseQueue.pop(i)
        i+=1


def cancelConstruction(planet, purchaseType):
    i = 0
    L = len(purchaseQueue)
    while i < L:
        if purchaseQueue[i][0] == planet and purchaseQueue[i][4] == purchaseType:
            planetList[planet.name].resources[0] += purchaseQueue[i][5][0]
            planetList[planet.name].resources[1] += purchaseQueue[i][5][1]
            planetList[planet.name].resources[2] += purchaseQueue[i][5][2]
            planetList[planet.name].buildingQueue = []
            purchaseQueue.pop(i)
            return
        i+=1


def updateResources():
    for planet in planetList.values():
        production = planet.resourceProductionRate()
        planet.resources[0] = min(planet.storage()[0], planet.resources[0] + universeSpeed*(100+production["Metal Rate"])/3600)
        planet.resources[1] = min(planet.storage()[1], planet.resources[1] + universeSpeed*(30+production["Crystal Rate"])/3600)
        planet.resources[2] = max(0, min(planet.storage()[2], planet.resources[2] + universeSpeed*production["Net Deuterium"]/3600))
        planet.resources[3] = production["Net Energy"]


def createPlanet(planetName = "Colony",  owner = None, coords = 0):
    planetCoordinates = coords
    if coords == 0:
        index = random.choice(range(len(uninhabited)))
        planetCoordinates = uninhabited[index]
        uninhabited.pop(index)
    newPlanet = Classes.Planet(planetName, planetCoordinates, owner, [500, 300, 0, 0])
    planetList[planetName] = newPlanet
    return newPlanet


def newPlayer(playerName, planetName = "Homeworld"):
    # First we construct the new homeworld for the player
    homePlanet = createPlanet(planetName, owner = playerName)
    # Then we add the player to the dynamic database
    playerList[playerName] = Classes.Player(playerName, [homePlanet])

# newPlayer("Piggy", "Pig Farm")
# buildingCashier(planetList["Pig Farm"], SDB.MasterBuildingsList["Solar Plant"])
# for commodity in SDB.MasterBuildingsList.values():
#     print(planetList["Pig Farm"].getTime("Building", commodity, universeSpeed))