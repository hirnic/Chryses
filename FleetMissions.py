# This file is where we handle all of the code involved in fleet missions.

import Classes
import SDB
from DDB import universeSpeed
import math

# This function computes the "distance" from one planet to another. Inputs are instances of planets (not just names).
def flightDistance(departurePlanet, arrivalPlanet):
    if departurePlanet.coords[0] != arrivalPlanet.coords[0]:
        return 20000 * abs(departurePlanet.coords[0] - arrivalPlanet.coords[0])
    elif departurePlanet.coords[1] != arrivalPlanet.coords[1]:
        return 2700 + 95 * abs(departurePlanet.coords[1] - arrivalPlanet.coords[1])
    else:
        return 1000 + 5 * abs(departurePlanet.coords[2] - arrivalPlanet.coords[2])

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
def flightTime(departurePlanet, arrivalPlanet, fleet, speed):
    velocity = fleetSpeed(fleet)
    distance = flightDistance(departurePlanet, arrivalPlanet)
    time = (10 + 35 / speed * math.sqrt(10 * distance / velocity)) / universeSpeed
    return time

# This function computes the amount of deuterium required by each ship.
# ship is an instance of a ship
def fuelPerShip(departurePlanet, arrivalPlanet, ship, speed):
    distance = flightDistance(departurePlanet, arrivalPlanet)
    fuelNeeded = 1 + round((ship.baseFuel * distance * (1 + speed) ** 2) / 35000)
    return fuelNeeded

# This function computes the amount of deuterium required by the entire fleet.
def flightFuel(departurePlanet, arrivalPlanet, fleet, speed):
    fuelNeeded = 0
    for ship in fleet.ships:
        fuelNeeded += fleet.ships[ship] * fuelPerShip(departurePlanet, arrivalPlanet, SDB.MasterShipsList[ship], speed)
    return fuelNeeded

# This function computes the amount of cargo space the fleet has.
def cargoSpace(fleet):
    cargo = 0
    for ship in fleet.ships:
        cargo += fleet.ships[ship] * SDB.MasterShipsList[ship].baseCargo
    return cargo

# This function makes the mission and sticks it into the database
def scheduleMission(missionType, departurePlanet, arrivalPlanet, fleet, speed, cargo):
    pass
    def __init__(self, owner, departure, destination, fleet, occasion, cargo, speed, start):
        self.owner = owner  # Owner of fleet (player name)
        self.departure = departure  # Coordinates of planet where fleet starts
        self.destination = destination  # Coordinates of planet where fleet is going
        self.fleet = fleet  # See instance below
        self.occasion = occasion  # Explore, Transport, Attack, Return, etc.
        self.cargo = cargo  # Resources on ship
        self.speed = speed  # Relative speed of fleet
        self.start = start  # Start time of mission