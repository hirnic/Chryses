# This file is where we handle all of the code involved in fleet missions.

import Classes
import SDB
from DDB import universeSpeed
from DDB import planetList
from DDB import playerList
import math
import time

# This function computes the "distance" from one planet to another. Inputs are instances of planets (not just names).
def flightDistance(departurePlanetCoords, arrivalPlanetCoords):
    if departurePlanetCoords[0] != arrivalPlanetCoords[0]:
        return 20000 * abs(departurePlanetCoords[0] - arrivalPlanetCoords[0])
    elif departurePlanetCoords[1] != arrivalPlanetCoords[1]:
        return 2700 + 95 * abs(departurePlanetCoords[1] - arrivalPlanetCoords[1])
    else:
        return 1000 + 5 * abs(departurePlanetCoords[2] - arrivalPlanetCoords[2])

# This function finds the speed of a single ship
# planet = departure planet (instance)
# ship = ship we want to find the speed of (instance)
def shipSpeed(ownerPlanet, ship):
    speed = 0
    if "Combustion Drive" in ship.getTech():
        driveLevel = ownerPlanet.commodities["Combustion Drive"]
        speed = ship.baseSpeed * (1 + driveLevel / 10)
    elif "Impulse Drive" in ship.getTech():
        driveLevel = ownerPlanet.commodities["Impulse Drive"]
        speed = ship.baseSpeed * (1 + 2 * driveLevel / 10)
    elif "Hyperspace Drive" in ship.getTech():
        driveLevel = ownerPlanet.commodities["Hyperspace Drive"]
        speed = ship.baseSpeed * (1 + 3 * driveLevel / 10)
    return speed

# This finds the speed of the fleet, that is the speed of the slowest ship in the fleet
# fleet is an instance of a fleet
def fleetSpeed(fleet):
    speed = 1e8
    for ship in fleet.ships:
        if fleet.ships[ship] > 0:
            speed = min(speed, shipSpeed(fleet.ownerPlanet, SDB.MasterShipsList[ship]))
    return speed

# This function determines how long a fleet will be in flight
# fleet is an instance of a fleet
# speed is a float between 0 and 1
def flightTime(departurePlanetCoords, arrivalPlanetCoords, fleet, speed):
    velocity = fleetSpeed(fleet)
    distance = flightDistance(departurePlanetCoords, arrivalPlanetCoords)
    flyTime = (10 + 35 / speed * math.sqrt(10 * distance / velocity)) / universeSpeed
    return flyTime

# This function computes the amount of deuterium required by each ship.
# ship is an instance of a ship
def fuelPerShip(departurePlanetCoords, arrivalPlanetCoords, ship, speed):
    distance = flightDistance(departurePlanetCoords, arrivalPlanetCoords)
    fuelNeeded = 1 + round((ship.baseFuel * distance * (1 + speed) ** 2) / 35000)
    return fuelNeeded

# This function computes the amount of deuterium required by the entire fleet.
def flightFuel(departurePlanetCoords, arrivalPlanetCoords, fleet, speed):
    fuelNeeded = 0
    for ship in fleet.ships:
        fuelNeeded += fleet.ships[ship] * fuelPerShip(departurePlanetCoords, arrivalPlanetCoords, SDB.MasterShipsList[ship], speed)
    return fuelNeeded

# This function computes the amount of cargo space the fleet has.
def cargoSpace(fleet):
    cargo = 0
    for ship in fleet.ships:
        cargo += fleet.ships[ship] * SDB.MasterShipsList[ship].baseCargo
    return cargo

# This function goes through and checks all the reasons a mission might not be allowed to proceed.
def missionViability(departurePlanet, arrivalPlanetCoords, fleet, speed, cargo, cargoCapacity, missionType):
    # 1. Not enough fuel
    if departurePlanet.resources[2] < flightFuel(departurePlanet.coords, arrivalPlanetCoords, fleet, speed):
        return False
    # print("Check 1 passed")

    # 2. Fleet has smaller capacity than cargo load specified by user
    if cargoCapacity < cargo[0] + cargo[1] + cargo[2]:
        return False
    # print("Check 2 passed")

    # 3. Planet has less resources than cargo load specified by user
    for i in range(3):
        if departurePlanet.resources[i] < cargo[i]:
            return False
    # print("Check 3 passed")

    # 4. Planet has fewer ships than fleet specified by user
    total = 0
    for ship in fleet.ships:
        total += fleet.ships[ship]
        if departurePlanet.commodities[ship] < fleet.ships[ship]:
            return False

    # 4a. There are no ships in the fleet
    if total == 0:
        return False
    # print("Check 4 passed")

    # 5. User has maximum number of missions currently ongoing (computer technology)
    if len(playerList[departurePlanet.owner].fleets) == departurePlanet.commodities["Computer Technology"] + 1:
        return False
    # print("Check 5 passed")

    # 6. Mission specific problems
    if missionType == "Select Mission":
        return False

    # 6a. For transport, attack, hold position, espionage, the planet may not be inhabited.
    planetExists = False
    destination = arrivalPlanetCoords
    for planet in planetList.values():
        if arrivalPlanetCoords == planet.coords:
            planetExists = True
            destination = planet
        if planetExists:
            break

    if missionType in ["Transport", "Attack", "Hold Position", "Espionage"]:
        if not planetExists:
            return False


    # 6b. For colonize, the planet may be inhabited.
    if missionType == "Colonize":
        for planet in planetList.values():
            if arrivalPlanetCoords == planet.coords:
                return False
        if fleet.ships["Colony Ship"] == 0:
            return False

    # 6c. For recycling, the debris field may be empty.
    if missionType == "Recycle":
        if destination.debris[0] == 0 or destination.debris[1] == 0 or destination.debris[2] == 0:
            return False
        if fleet.ships["Recycler"] == 0:
            return False

    # 6d. For deployment, the planet may be uninhabited or may not belong to user.
    if missionType == "Deploy":
        if departurePlanet.owner != destination.owner:
            return False

    return True

# This function makes the mission and sticks it into the database
def scheduleMission(departurePlanet, arrivalPlanet, fleet, missionType, speed, cargo, fuel, arrivalTime, returnTime):
    Classes.Mission(playerList[departurePlanet.owner],
                    departurePlanet,
                    arrivalPlanet,
                    fleet,
                    missionType,
                    cargo,
                    speed,
                    time.time(),
                    arrivalTime,
                    returnTime)

    # Subtract ships from planet
    for ship in fleet.ships:
        departurePlanet.commodities[ship] -= fleet.ships[ship]

    # Subtract fuel from planet
    departurePlanet.resources[2] -= fuel

    # Subtract resources from planet
    for i in range(3):
        departurePlanet.resources[i] -= cargo[i]

    # Send a message notifying defender
