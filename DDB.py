# DDB stands for Dynamic DataBase. It contains all the information about the game that can change, like the list of
# players, the list of planets occupied and unoccupied, the list of missions ongoing, etc....
# This file also contains the necessary commands to change these things.

import Classes
# import SDB
import random
import time

galaxies = 3
solarSystems = 5
planets = 5
universeSpeed = 100


# Keeps track of all players (and bots) in the game
playerList = {}


# Keeps track of all occupied planets in the universe
planetList = {}


# Keeps track of all unoccupied planets in the universe
uninhabited = [[i+1, j+1, k+1] for i in range(galaxies) for j in range(solarSystems) for k in range(planets)]


# Keeps track of all fleet activity in the universe
fleetAcitivity = []


# The function returns True if and only if the input planet has the tech required to purchase the input commodity.
def verifyTechRequirements(planet, commodity):
    techNeeded = commodity.getTech()
    for tech in techNeeded:
        if planet.commodities[tech] < techNeeded[tech]:
            return False
    return True


# The function returns True if and only if the input planet has the resources required to purchase the input commodity.
def verifyResourceRequirements(planet, commodity):
    resourcesAvailable = planet.resources
    price = planet.getPrice(commodity, planet.commodities[commodity.name])
    for i in range(3):
        if resourcesAvailable[i] < price[i]:
            return False
    if commodity.name == "Graviton Technology" and resourcesAvailable[3] < price[3]:
        return False
    return True


# If the customer can make the payment, the cashier adds the purchase to the purchaseQueue.
def cashier(planet, commodity, amount=1):
    # This checks that the entry box was not left blank.
    if amount == 0:
        return

    if verifyTechRequirements(planet, commodity) and verifyResourceRequirements(planet, commodity):
        currentLevel = planet.commodities[commodity.name]

        if type(commodity).__name__ == "Building":
            if len(planet.buildingQueue) < 5:
                for item in planet.buildingQueue:
                    if item[0] == commodity:
                        currentLevel = item[1]
                price = commodity.getPrice(currentLevel)
                planet.resources[0] -= price[0]
                planet.resources[1] -= price[1]
                planet.resources[2] -= price[2]
                startTime = time.time()
                if len(planet.buildingQueue) > 0:
                    timeNeeded = planet.getTime(planet.buildingQueue[-1][0], planet.buildingQueue[-1][1], universeSpeed)
                    startTime = planet.buildingQueue[-1][2] + timeNeeded

                planet.buildingQueue.append([commodity, currentLevel + 1, startTime])

        elif type(commodity).__name__ == "Research":
            if len(playerList[planet.owner].researchQueue) < 1:
                price = commodity.getPrice(currentLevel)
                planet.resources[0] -= price[0]
                planet.resources[1] -= price[1]
                planet.resources[2] -= price[2]
                startTime = time.time()
                currentLevel = planet.commodities[commodity.name]
                playerList[planet.owner].researchQueue.append([commodity, currentLevel + 1, startTime])

        elif type(commodity).__name__ == "Ship" or type(commodity).__name__ == "Defense":
            price = commodity.getPrice(currentLevel)
            i = 0
            # If the user accidentally inputs too large a number, this loop ensures they do not overspend.
            while (planet.resources[0] - price[0] >= 0 and planet.resources[1] - price[1] >= 0
                   and planet.resources[2] - price[1] >= 0):
                if i == amount:
                    break
                i += 1
                planet.resources[0] -= price[0]
                planet.resources[1] -= price[1]
                planet.resources[2] -= price[2]
            startTime = time.time()
            if len(planet.shipyardQueue) > 0:
                timeNeeded = planet.getTime(planet.shipyardQueue[-1][0], None, universeSpeed)
                startTime = planet.shipyardQueue[-1][2] + timeNeeded * planet.shipyardQueue[-1][1]
            planet.shipyardQueue.append([commodity, i, startTime])


def executePurchases():
    for planet in planetList.values():

        for item in planet.buildingQueue:
            if item[2] + planet.getTime(item[0], item[1] - 1, universeSpeed) < time.time():
                planet.commodities[item[0].name] += 1
                # Then update the queues
                planetList[planet.name].buildingQueue.pop(0)
                if len(planet.buildingQueue) > 0:
                    planetList[planet.name].buildingQueue[0][2] = time.time()

        for item in playerList[planet.owner].researchQueue:
            if item[2] + planet.getTime(item[0], item[1]-1, universeSpeed) < time.time():
                planet.commodities[item[0].name] += 1
                playerList[planet.owner].researchQueue.pop(0)

        for item in planet.shipyardQueue:
            timeNeeded = planet.getTime(item[0], None, universeSpeed)
            if item[2] + timeNeeded < time.time():
                planet.commodities[item[0].name] += 1
                planet.shipyardQueue[0][1] -= 1
                planet.shipyardQueue[0][2] += timeNeeded
                if planet.shipyardQueue[0][1] == 0:
                    planet.shipyardQueue.pop(0)


def cancelPurchase(planet, commodity):
    # This ensures only the last upgrade of the building is cancelled.
    currentLevel = 0
    if len(planet.buildingQueue) > 0 and type(commodity).__name__ == "Building":
        firstDeleted = False
        i = -1
        for item in planet.buildingQueue[::-1]:
            if item[0].name == commodity.name:
                currentLevel = item[1]-1
                planet.buildingQueue.pop(i)
                firstDeleted = True
                break
            i -= 1
        if len(planet.buildingQueue) > 0 and not firstDeleted:
            planet.buildingQueue[0][2] = time.time()
    elif len(playerList[planet.owner].researchQueue) > 0 and type(commodity).__name__ == "Research":
        currentLevel = playerList[planet.owner].researchQueue[0][1]-1
        playerList[planet.owner].researchQueue.pop(0)

    # This part refunds the purchase
    price = commodity.getPrice(currentLevel)
    planetList[planet.name].resources[0] += price[0]
    planetList[planet.name].resources[1] += price[1]
    planetList[planet.name].resources[2] += price[2]


def updateResources():
    for planet in planetList.values():
        production = planet.resourceProductionRate()
        planet.resources[0] = max(planet.resources[0],
                                  min(planet.storage()[0],
                                      planet.resources[0] + universeSpeed*(100+production["Metal Rate"])/3600))
        planet.resources[1] = max(planet.resources[1],
                                  min(planet.storage()[1],
                                      planet.resources[1] + universeSpeed*(30+production["Crystal Rate"])/3600))
        planet.resources[2] = max(planet.resources[2],
                                  min(planet.storage()[2],
                                      max(0, planet.resources[2] + universeSpeed*production["Net Deuterium"]/3600)))
        planet.resources[3] = production["Net Energy"]


def createPlanet(planetName="Colony",  owner=None, coords=0):
    planetCoordinates = coords
    if coords == 0:
        index = random.choice(range(len(uninhabited)))
        planetCoordinates = uninhabited[index]
        uninhabited.pop(index)
    newPlanet = Classes.Planet(planetName, planetCoordinates, owner, [5000000, 3000000, 9999990, 0])
    newPlanet.commodities["Research Laboratory"] = 12
    newPlanet.commodities["Shipyard"] = 12
    planetList[planetName] = newPlanet
    return newPlanet


def newPlayer(playerName, planetName="Homeworld"):
    # First we construct the new homeworld for the player
    homePlanet = createPlanet(planetName, owner=playerName)
    # Then we add the player to the dynamic database
    playerList[playerName] = Classes.Player(playerName, [homePlanet])


# newPlayer("Piggy", "Pig Farm")
# print(playerList[planetList["Pig Farm"].owner].researchQueue)
# buildingCashier(planetList["Pig Farm"], SDB.MasterBuildingsList["Solar Plant"])
# for commodity in SDB.MasterBuildingsList.values():
#     print(planetList["Pig Farm"].getTime(commodity, universeSpeed))
