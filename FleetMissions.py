# This file is where we handle all of the code involved in fleet missions.

import Classes
import SDB
import DDB
import math
import time
import random


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
    flyTime = (10 + 35 / speed * math.sqrt(10 * distance / velocity)) / DDB.universeSpeed
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
        fuelNeeded += fleet.ships[ship] * fuelPerShip(departurePlanetCoords, arrivalPlanetCoords,
                                                      SDB.MasterShipsList[ship], speed)
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
    if len(DDB.playerList[departurePlanet.owner].fleets) == departurePlanet.commodities["Computer Technology"] + 1:
        return False
    # print("Check 5 passed")

    # 6. Mission specific problems
    if missionType == "Select Mission":
        return False

    # 6a. For transport, attack, hold position, espionage, the planet may not be inhabited.
    planetExists = False
    destination = arrivalPlanetCoords
    for planet in DDB.planetList.values():
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
        for planet in DDB.planetList.values():
            if arrivalPlanetCoords == planet.coords:
                return False
        if fleet.ships["Colony Ship"] == 0:
            return False
        if len(DDB.playerList[departurePlanet.owner].planets) == 1 + math.ceil(
                departurePlanet.commodities["Astrophysics"] / 2):
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

    # 6e. For espionage, the fleet must consist entirely of espionage probes
    if missionType == "Espionage":
        if fleet.ships["Espionage Probe"] <= 0:
            return False
        for ship in fleet.ships:
            if ship == "Espionage Probe":
                continue
            elif fleet.ships[ship] > 0:
                return False
    # print("Check 6 passed!")
    return True


# This function makes the mission and sticks it into the database
def scheduleMission(departurePlanet, destination, fleet, missionType, speed, cargo, fuel, arrivalTime, returnTime):
    mission = Classes.Mission(departurePlanet.owner,
                              departurePlanet,
                              destination,
                              fleet,
                              missionType,
                              cargo,
                              speed,
                              time.time(),
                              arrivalTime,
                              returnTime,
                              fuel)

    if missionType == "Deploy":
        fuel = fuel / 2

    # Subtract ships from planet
    for ship in fleet.ships:
        departurePlanet.commodities[ship] -= fleet.ships[ship]

    # Subtract fuel from planet
    departurePlanet.resources[2] -= fuel

    # Subtract resources from planet
    for i in range(3):
        departurePlanet.resources[i] -= cargo[i]

    # Send a message notifying defender
    # Fill in code later. Not pressing.

    # Add mission to database
    DDB.fleetActivity[departurePlanet.name + str(arrivalTime)] = mission
    DDB.playerList[departurePlanet.owner].fleets.append(mission)


# This mission is created if the user cancels a mission or if a mission gets completed.
def scheduleReturn(mission):
    mission.returnTime = 2 * time.time() + mission.returnTime - 2 * mission.arrivalTime
    mission.missionType = "Return"


def executeReturn(mission):
    if time.time() > mission.returnTime:
        owner = DDB.playerList[mission.owner]
        for ship in mission.fleet.ships:
            DDB.planetList[mission.departurePlanet.name].commodities[ship] += mission.fleet.ships[ship]
        for i in range(3):
            mission.departurePlanet.resources[i] += mission.cargo[i]
        del DDB.fleetActivity[mission.departurePlanet.name + str(mission.arrivalTime)]
        for i in range(len(owner.fleets)):
            if mission == owner.fleets[i]:
                owner.fleets.pop(i)
                break


def transport(mission):
    planetExists = False
    arrivalPlanet = 0
    for planet in DDB.planetList.values():
        if planet.coords == mission.destination:
            planetExists = True
            arrivalPlanet = planet
    if time.time() > mission.arrivalTime:
        if planetExists:
            for i in range(3):
                DDB.planetList[arrivalPlanet.name].resources[i] += mission.cargo[i]
                mission.cargo[i] = 0
        scheduleReturn(mission)


def deploy(mission):
    planetExists = False
    arrivalPlanet = 0
    for planet in DDB.planetList.values():
        if planet.coords == mission.destination:
            planetExists = True
            arrivalPlanet = planet
    if time.time() > mission.arrivalTime:
        owner = DDB.playerList[mission.owner]
        if planetExists:
            for ship in mission.fleet.ships:
                arrivalPlanet.commodities[ship] += mission.fleet.ships[ship]
            for i in range(3):
                DDB.planetList[arrivalPlanet.name].resources[i] += mission.cargo[i]
                mission.cargo[i] = 0
            arrivalPlanet.resources[2] += mission.fuel / 2
            del DDB.fleetActivity[mission.departurePlanet.name + str(mission.arrivalTime)]
            for i in range(len(owner.fleets)):
                if mission == owner.fleets[i]:
                    owner.fleets.pop(i)
        else:
            scheduleReturn(mission)


def colonize(mission):
    for planet in DDB.planetList.values():
        if mission.destination == planet.coords:
            scheduleReturn(mission)
            return
    if time.time() > mission.arrivalTime:
        owner = DDB.playerList[mission.owner]
        planetName = "Colony" + str(time.time())
        DDB.createPlanet(planetName, mission.owner, mission.destination)
        while DDB.planetList[planetName].owner != mission.owner:
            planetName = planetName + "0"
        for i in range(3):
            DDB.planetList[planetName].resources[i] += mission.cargo[i]
        for ship in mission.fleet.ships:
            DDB.planetList[planetName].commodities[ship] += mission.fleet.ships[ship]
        DDB.planetList[planetName].commodities["Colony Ship"] -= 1
        DDB.planetList[planetName].resources[2] += mission.fuel / 2
        owner.planets.append(DDB.planetList[planetName])
        del DDB.fleetActivity[mission.departurePlanet.name + str(mission.arrivalTime)]
        for i in range(len(owner.fleets)):
            if mission == owner.fleets[i]:
                DDB.playerList[owner.name].fleets.pop(i)


defenseList = ["Small Cargo", "Large Cargo", "Light Fighter", "Heavy Fighter", "Cruiser", "Battleship", "Colony Ship",
               "Recycler", "Espionage Probe", "Bomber", "Solar Satellite", "Destroyer", "Deathstar", "Battlecruiser",
               "Mega Cargo", "Rocket Launcher", "Light Laser", "Heavy Laser", "Gauss Cannon", "Ion Cannon",
               "Plasma Turret", "Small Shield Dome", "Large Shield Dome", "Antiballistic Missile",
               "Interplanetary Missile"]


def attack(mission):
    target = 0
    for planet in DDB.planetList.values():
        if mission.destination == planet.coords:
            target = planet
    hasDefense = False
    for item in defenseList:
        if target.commodities[item] > 0:
            hasDefense = True
            break
    if not hasDefense:
        cargoCapacity = cargoSpace(mission.fleet) - sum(mission.cargo)
        totalResources = sum(target.resources)
        if totalResources < cargoCapacity:
            for i in range(3):
                mission.cargo[i] += target.resources[i]
                target.resources[i] = 0
        else:
            for i in range(3):
                mission.cargo[i] += cargoCapacity * target.resources[i] / totalResources
                target.resources[i] -= cargoCapacity * target.resources[i] / totalResources
    scheduleReturn(mission)


def counterEspionage(mission, spyOffset):
    target = 0
    for planet in DDB.planetList.values():
        if mission.destination == planet.coords:
            target = planet
    fleetSize = 0
    for ship in defenseList[:14]:
        fleetSize += target.commodities[ship]
    counterChance = min(2**(-spyOffset-2) * mission.fleet.ships["Espionage Probe"] * fleetSize/100, 1)
    destroyed = False
    rand = random.uniform(0, 1)
    if rand < counterChance:
        destroyed = True
        for i in range(len(DDB.playerList[mission.departurePlanet.owner].fleets)):
            if DDB.playerList[mission.departurePlanet.owner].fleets[i] == mission:
                DDB.playerList[mission.departurePlanet.owner].fleets.pop(i)
    return [counterChance, destroyed]


def espionage(mission):
    target = 0
    for planet in DDB.planetList.values():
        if mission.destination == planet.coords:
            target = planet
    spyOffset = mission.departurePlanet.commodities["Espionage Technology"] - target.commodities["Espionage Technology"]
    spyResult = mission.fleet.ships["Espionage Probe"] + abs(spyOffset) * spyOffset
    counterStats = counterEspionage(mission, spyOffset)

    message = {"Resources": target.resources, "Fleet": {}, "Defense": {}, "Buildings": {}, "Research": {}}
    if spyResult > 1:  # Resources + Fleet
        for ship in defenseList[:14]:
            message["Fleet"] [ship] = target.commodities[ship]
    if spyResult > 2:  # Resources + Fleet + Defense
        for item in defenseList[14:]:
            message["Defense"][item] = target.commodities[item]
    if spyResult > 4:  # Resources + Fleet + Defense + Buildings
        for building in SDB.MasterBuildingsList:
            message["Buildings"][building] = target.commodities[building]
    if spyResult > 6:  # Resources + Fleet + Defense + Buildings + Research
        for tech in SDB.MasterResearchList:
            message["Research"][tech] = target.commodities[tech]
    if not counterStats[1]:
        message["Counter Espionage"] = str(counterStats[0])
    else:
        message["Counter Espionage"] = "Fleet Destroyed Espionage."
    print(message)
    scheduleReturn(mission)


missionDictionary = {"Colonize": colonize,
                     "Transport": transport,
                     "Deploy": deploy,
                     "Attack": attack,
                     "Recycle": scheduleReturn,
                     "Espionage": espionage,
                     "Hold Position": scheduleReturn,
                     "Return": executeReturn}


# Execute the missions!
def executeMissions():
    for mission in DDB.fleetActivity.copy().values():
        if time.time() > mission.arrivalTime:
            missionDictionary[mission.missionType](mission)
