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
universeSpeed = 1


#Keeps track of all players (and bots) in the game
playerList = {}


#Keeps track of all occupied planets in the universe
planetList = {}


# Keeps track of all unoccupied planets in the universe
uninhabited = [[i+1,j+1,k+1] for i in range(galaxies) for j in range(solarSystems) for k in range(planets)]


#Keeps track of all fleet activity in the universe
fleetAcitivity = []


#Keeps track of all buildings, research, ships, and defense building/ deconstructing activity in the universe
# [planet (instance), commodity (instance), increment, end time]
internalActivity = []


def verifyTechRequirements(planet, commodity):
    techNeeded = commodity.getTech()
    for tech in techNeeded:
        if planet.commodities[tech] != techNeeded[tech]:
            return False
    return True

def verifyResourceRequirements(planet, commodity, amount = 1):
    resourcesAvaliable = planet.resources
    price = planet.getPrice(1, commodity)
    for i in range(3):
        if resourcesAvaliable[i] < price[i] * amount:
            return False
    return True

# If the customer can make the payment, the cashier executes the purchase. This function takes care of that matter.
def buildingCashier(planet, commodity):
    startTime = time.time()
    if len(planet.buildingQueue) == 5:
        return
    elif len(planet.buildingQueue) > 0:
        startTime = planet.buildingQueue[-1][2]
    timeNeeded = planet.getTime("Building", commodity, universeSpeed)
    endTime = startTime + timeNeeded
    if verifyTechRequirements(planet, commodity) and verifyResourceRequirements(planet, commodity):
        internalActivity.append([planet, commodity, 1, endTime])


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

newPlayer("Piggy", "Pig Farm")
buildingCashier(planetList["Pig Farm"], SDB.MasterBuildingsList["Solar Plant"])
# for commodity in SDB.MasterBuildingsList.values():
#     print(planetList["Pig Farm"].getTime("Building", commodity, universeSpeed))