# SDB Stands for static database. It contains all the information about the game that does not change, like the stats
# for individual buildings, ships, defenses....

import Classes

# This is all information about buildings
# Note: In C++ I would use a struct here. The tech tree would just be a method .getTech(). Less of a headache, I admit.
MasterBuildingsList = {
    "Metal Mine": Classes.Building("Metal Mine",
                                   [60, 15, 0, 22],
                                   [1.5, 1.1],
                                   108,
                                   [45, 0, 0, 0]),
    "Crystal Mine": Classes.Building("Crystal Mine",
                                     [48, 24, 0, 22],
                                     [1.6, 1.1],
                                     104,
                                     [0, 30, 0, 0]),
    "Deuterium Synthesizer": Classes.Building("Deuterium Synthesizer",
                                              [225, 75, 0, 33],
                                              [1.5, 1.2],
                                              432,
                                              [0, 0, 20, 0]),
    "Solar Plant": Classes.Building("Solar Plant",
                                    [75, 30, 0, 0],
                                    [1.5, 0],
                                    151,
                                    [0, 0, 0, 22]),
    "Fusion Reactor": Classes.Building("Fusion Reactor",
                                       [900, 160, 380, 0],
                                       [1.8, 0],
                                       1526,
                                       [0, 0, 0, 50]),
    "Robotics Factory": Classes.Building("Robotics Factory",
                                         [400, 100, 200, 0],
                                         [2, 0],
                                         720,
                                         [0, 0, 0, 0]),
    "Nanite Factory": Classes.Building("Nanite Factory",
                                       [1e6, 5e5, 1e5, 0],
                                       [2, 0],
                                       216000,
                                       [0, 0, 0, 0]),
    "Shipyard": Classes.Building("Shipyard",
                                 [400, 200, 100, 0],
                                 [2, 0],
                                 864,
                                 [0, 0, 0, 0]),
    "Metal Storage": Classes.Building("Metal Storage",
                                      [1000, 0, 0, 0],
                                      [2, 0],
                                      1440,
                                      [0, 0, 0, 0]),
    "Crystal Storage": Classes.Building("Crystal Storage",
                                        [1000, 500, 0, 0],
                                        [2, 0],
                                        2160,
                                        [0, 0, 0, 0]),
    "Deuterium Tank": Classes.Building("Deuterium Tank",
                                       [1000, 1000, 0, 0],
                                       [2, 0],
                                       2880,
                                       [0, 0, 0, 0]),
    "Research Laboratory": Classes.Building("Research Laboratory",
                                            [200, 400, 200, 0],
                                            [2, 0],
                                            864,
                                            [0, 0, 0, 0]),
    "Terraformer": Classes.Building("Terraformer",
                                    [0, 5e4, 1e5, 1e3],
                                    [2, 0],
                                    72000,
                                    [0, 0, 0, 0]),
    "Missile Silo": Classes.Building("Missile Silo",
                                     [2e4, 2e4, 1e3, 0],
                                     [2, 0],
                                     57600,
                                     [0, 0, 0, 0])
}

# This is all information about research
MasterResearchList = {
    "Espionage Technology": Classes.Research("Espionage Technology",
                                             [1e2, 1e3, 1e2, 0],
                                             3960),
    "Computer Technology": Classes.Research("Computer Technology",
                                            [0, 400, 600, 0],
                                            1440),
    "Weapons Technology": Classes.Research("Weapons Technology",
                                           [800, 200, 0, 0],
                                           3600),
    "Shielding Technology": Classes.Research("Shielding Technology",
                                             [200, 600, 0, 0],
                                             2880),
    "Armor Technology": Classes.Research("Armor Technology",
                                         [1e3, 0, 0, 0],
                                         3600),
    "Energy Technology": Classes.Research("Energy Technology",
                                          [0, 800, 400, 0],
                                          2880),
    "Hyperspace Technology": Classes.Research("Hyperspace Technology",
                                              [0, 4000, 2000, 0],
                                              14400),
    "Combustion Drive": Classes.Research("Combustion Drive",
                                         [400, 0, 600, 0],
                                         1440),
    "Impulse Drive": Classes.Research("Impulse Drive",
                                      [2000, 4000, 600, 0],
                                      21600),
    "Hyperspace Drive": Classes.Research("Hyperspace Drive",
                                         [10000, 20000, 6000, 0],
                                         108e3),
    "Laser Technology": Classes.Research("Laser Technology",
                                         [200, 100, 0, 0],
                                         1080),
    "Ion Technology": Classes.Research("Ion Technology",
                                       [1000, 300, 100, 0],
                                       4680),
    "Plasma Technology": Classes.Research("Plasma Technology",
                                          [2000, 4000, 1000, 0],
                                          21600),
    "Intergalactic Research Network": Classes.Research("Intergalactic Research Network",
                                                       [240000, 100000, 160000, 0],
                                                       1224e3),
    "Astrophysics": Classes.Research("Astrophysics",
                                     [4000, 8000, 4000, 0],
                                     43200),
    "Graviton Technology": Classes.Research("Graviton Technology",
                                            [0, 0, 0, 300000],
                                            1)
}

# This is all information about ships
MasterShipsList = {"Small Cargo": Classes.Ship("Small Cargo",
                                               [2000, 2000, 0, 0],
                                               10,
                                               5,
                                               5000,
                                               5000,
                                               10),

                   "Large Cargo": Classes.Ship("Large Cargo",
                                               [6000, 6000, 0, 0],
                                               25,
                                               5,
                                               7500,
                                               25000,
                                               50),

                   "Light Fighter": Classes.Ship("Light Fighter",
                                                 [3000, 1000, 0, 0],
                                                 10,
                                                 50,
                                                 12500,
                                                 50,
                                                 20),

                   "Heavy Fighter": Classes.Ship("Heavy Fighter",
                                                 [6000, 4000, 0, 0],
                                                 25,
                                                 150,
                                                 10000,
                                                 100,
                                                 75),

                   "Cruiser": Classes.Ship("Cruiser",
                                           [20000, 7000, 2000, 0],
                                           50,
                                           400,
                                           15000,
                                           800,
                                           300),

                   "Battleship": Classes.Ship("Battleship",
                                              [45000, 15000, 0, 0],
                                              200,
                                              1000,
                                              10000,
                                              1500,
                                              500),

                   "Colony Ship": Classes.Ship("Colony Ship",
                                               [10000, 20000, 10000, 0],
                                               100,
                                               50,
                                               2500,
                                               7500,
                                               1000),

                   "Recycler": Classes.Ship("Recycler",
                                            [10000, 6000, 2000, 0],
                                            10,
                                            0,
                                            2000,
                                            20000,
                                            300),

                   "Espionage Probe": Classes.Ship("Espionage Probe",
                                                   [0, 1000, 0, 0],
                                                   0,
                                                   0,
                                                   100000000,
                                                   5,
                                                   1),

                   "Bomber": Classes.Ship("Bomber",
                                          [50000, 25000, 10000, 0],
                                          500,
                                          1000,
                                          4000,
                                          500,
                                          1000),

                   "Solar Satellite": Classes.Ship("Solar Satellite",
                                                   [0, 2000, 500, 0],
                                                   1,
                                                   0,
                                                   0,
                                                   0,
                                                   0),

                   "Destroyer": Classes.Ship("Destroyer",
                                             [60000, 50000, 15000, 0],
                                             500,
                                             2000,
                                             5000,
                                             2000,
                                             1000),

                   "Deathstar": Classes.Ship("Deathstar",
                                             [5000000, 4000000, 1000000, 0],
                                             50000,
                                             200000,
                                             100,
                                             1000000,
                                             1),

                   "Battlecruiser": Classes.Ship("Battlecruiser",
                                                 [30000, 40000, 15000, 0],
                                                 400,
                                                 700,
                                                 10000,
                                                 750,
                                                 250),

                   "Mega Cargo": Classes.Ship("Mega Cargo",
                                              [30000, 70000, 20000, 0],
                                              75,
                                              10,
                                              800,
                                              250000,
                                              500)
                   }

# This is all information about defense
MasterDefenseList = {"Rocket Launcher": Classes.Defense("Rocket Launcher",
                                                        [2000, 0, 0, 0],
                                                        20,
                                                        80),

                     "Light Laser": Classes.Defense("Light Laser",
                                                    [1500, 500, 0, 0],
                                                    25,
                                                    100),

                     "Heavy Laser": Classes.Defense("Heavy Laser",
                                                    [6000, 2000, 0, 0],
                                                    100,
                                                    250),

                     "Gauss Cannon": Classes.Defense("Gauss Cannon",
                                                     [20000, 15000, 2000, 0],
                                                     200,
                                                     1100),

                     "Ion Cannon": Classes.Defense("Ion Cannon",
                                                   [6000, 2000, 0, 0],
                                                   500,
                                                   150),

                     "Plasma Turret": Classes.Defense("Plasma Turret",
                                                      [50000, 50000, 30000, 0],
                                                      300,
                                                      3000),

                     "Small Shield Dome": Classes.Defense("Small Shield Dome",
                                                          [10000, 10000, 0, 0],
                                                          2000,
                                                          0),

                     "Large Shield Dome": Classes.Defense("Large Shield Dome",
                                                          [50000, 50000, 0, 0],
                                                          10000,
                                                          0),

                     "Antiballistic Missile": Classes.Defense("Antiballistic Missile",
                                                              [6000, 0, 2000, 0],
                                                              0,
                                                              0),

                     "Interplanetary Missile": Classes.Defense("Interplanetary Missile",
                                                               [39500, 7900, 9200, 0],
                                                               0,
                                                               0)
                     }

MasterCommoditiesList = {**MasterBuildingsList, **MasterResearchList, **MasterShipsList, **MasterDefenseList}

MasterDescriptionList = {"Metal Mine": "A metal mine makes metal.",
                         "Crystal Mine": "A crystal mine makes crystal",
                         "Deuterium Synthesizer": "A deuterium synthesizer makes deuterium",
                         "Solar Plant": "A solar plant makes energy",
                         "Fusion Reactor": "A fusion reactor makes energy",
                         "Robotics Factory": "A robotics factory is necessary for the construction of a shipyard "
                                             "and a nanite factory.",
                         "Nanite Factory": "A nanite factory is necessary for the construction of a terraformer. It"
                                           " also makes the construction of buildings, ships, and defenses faster.",
                         "Shipyard": "A shipyard is necessary for making ships and defenses.",
                         "Metal Storage": "A metal storage stores metal.",
                         "Crystal Storage": "A crystal storage stores crystal.",
                         "Deuterium Tank": "A deuterium tank stores deuterium.",
                         "Research Laboratory": "A research laboratory is necessary for researching new"
                                                " technologies.",
                         "Terraformer": "A terraformer gives your planet more space and maybe a cooler look.",
                         "Missile Silo": "A missile silo stores interplanetary and antiballistic missiles. More the"
                                         " merrier!",

                         "Espionage Technology": {"Research Laboratory": 3},
                         "Computer Technology": {"Research Laboratory": 1},
                         "Weapons Technology": {"Research Laboratory": 4},
                         "Shielding Technology": {"Research Laboratory": 6,
                                                  "Energy Technology": 3},
                         "Armor Technology": {"Research Laboratory": 2},
                         "Energy Technology": {"Research Laboratory": 1},
                         "Hyperspace Technology": {"Research Laboratory": 7,
                                                   "Energy Technology": 5,
                                                   "Shielding Technology": 5},
                         "Combustion Drive": {"Research Laboratory": 1,
                                              "Energy Technology": 1},
                         "Impulse Drive": {"Research Laboratory": 2,
                                           "Energy Technology": 1},
                         "Hyperspace Drive": {"Research Laboratory": 7,
                                              "Hyperspace Technology": 3},
                         "Laser Technology": {"Research Laboratory": 1,
                                              "Energy Technology": 2},
                         "Ion Technology": {"Research Laboratory": 4,
                                            "Energy Technology": 4,
                                            "Laser Technology": 4},
                         "Plasma Technology": {"Research Laboratory": 5,
                                               "Energy Technology": 8,
                                               "Laser Technology": 10,
                                               "Ion Technology": 5},
                         "Intergalactic Research Network": {"Research Laboratory": 10,
                                                            "Computer Technology": 8,
                                                            "Hyperspace Technology": 8},
                         "Astrophysics": {"Research Laboratory": 3,
                                          "Espionage Technology": 4,
                                          "Impulse Drive": 3},
                         "Graviton Technology": {"Research Laboratory": 12},

                         "Small Cargo": {"Shipyard": 2,
                                         "Combustion Drive": 2},
                         "Large Cargo": {"Shipyard": 4,
                                         "Combustion Drive": 6},
                         "Light Fighter": {"Shipyard": 1,
                                           "Combustion Drive": 1},
                         "Heavy Fighter": {"Shipyard": 3,
                                           "Armor Technology": 2,
                                           "Impulse Drive": 2},
                         "Cruiser": {"Shipyard": 5,
                                     "Impulse Drive": 2,
                                     "Ion Technology": 2},
                         "Battleship": {"Shipyard": 7,
                                        "Hyperspace Drive": 4},
                         "Colony Ship": {"Shipyard": 4,
                                         "Impulse Drive": 3},
                         "Recycler": {"Shipyard": 4,
                                      "Combustion Drive": 6,
                                      "Shielding Technology": 2},
                         "Espionage Probe": {"Shipyard": 3,
                                             "Combustion Drive": 3,
                                             "Espionage Technology": 2},
                         "Bomber": {"Shipyard": 8,
                                    "Impulse Drive": 3,
                                    "Plasma Technology": 5},
                         "Solar Satellite": {"Shipyard": 1},
                         "Destroyer": {"Shipyard": 9,
                                       "Hyperspace Drive": 6,
                                       "Hyperspace Technology": 5},
                         "Deathstar": {"Shipyard": 12,
                                       "Hyperspace Drive": 7,
                                       "Hpyerspace Technology": 6,
                                       "Graviton Technology": 1},
                         "Battlecruiser": {"Shipyard": 8,
                                           "Hyperspace Technology": 5,
                                           "Hyperspace Drive": 5,
                                           "Laser Technology": 12},
                         "Mega Cargo": {"Shipyard": 4,
                                        "Impulse Drive": 3},

                         "Rocket Launcher": {"Shipyard": 1},
                         "Light Laser": {"Shipyard": 2,
                                         "Energy Technology": 1,
                                         "Laser Technology": 3},
                         "Heavy Laser": {"Shipyard": 4,
                                         "Energy Technology": 3,
                                         "Laser Technology": 6},
                         "Guass Cannon": {"Shipyard": 6,
                                          "Energy Technology": 6,
                                          "Weapons Technology": 3,
                                          "Shielding Technology": 1},
                         "Ion Cannon": {"Shipyard": 4,
                                        "Ion Technology": 4},
                         "Plasma Turret": {"Shipyard": 8,
                                           "Plasma Technology": 7},
                         "Small Shield Dome": {"Shipyard": 1,
                                               "Shielding Technology": 2},
                         "Large Shield Dome": {"Shipyard": 6,
                                               "Shielding Technology": 6},
                         "Antiballistic Missile": {"Shipyard": 1,
                                                   "Missile Silo": 2},
                         "Interplanetary Missile": {"Shipyard": 1,
                                                    "Missile Silo": 4,
                                                    "Hyperspace Drive": 1}
                         }

# This is the comprehensive technology tree. It is constructed using the previous dictionaries.
Classes.technologyTree = {"Metal Mine": {},
                          "Crystal Mine": {},
                          "Deuterium Synthesizer": {},
                          "Solar Plant": {},
                          "Fusion Reactor": {"Deuterium Synthesizer": 5,
                                             "Energy Technology": 3},
                          "Robotics Factory": {},
                          "Nanite Factory": {"Robotics Factory": 10,
                                             "Computer Technology": 10},
                          "Shipyard": {"Robotics Factory": 2},
                          "Metal Storage": {},
                          "Crystal Storage": {},
                          "Deuterium Tank": {},
                          "Research Laboratory": {},
                          "Terraformer": {"Nanite Factory": 1,
                                          "Energy Technology": 12},
                          "Missile Silo": {"Shipyard": 1},

                          "Espionage Technology": {"Research Laboratory": 3},
                          "Computer Technology": {"Research Laboratory": 1},
                          "Weapons Technology": {"Research Laboratory": 4},
                          "Shielding Technology": {"Research Laboratory": 6,
                                                   "Energy Technology": 3},
                          "Armor Technology": {"Research Laboratory": 2},
                          "Energy Technology": {"Research Laboratory": 1},
                          "Hyperspace Technology": {"Research Laboratory": 7,
                                                    "Energy Technology": 5,
                                                    "Shielding Technology": 5},
                          "Combustion Drive": {"Research Laboratory": 1,
                                               "Energy Technology": 1},
                          "Impulse Drive": {"Research Laboratory": 2,
                                            "Energy Technology": 1},
                          "Hyperspace Drive": {"Research Laboratory": 7,
                                               "Hyperspace Technology": 3},
                          "Laser Technology": {"Research Laboratory": 1,
                                               "Energy Technology": 2},
                          "Ion Technology": {"Research Laboratory": 4,
                                             "Energy Technology": 4,
                                             "Laser Technology": 4},
                          "Plasma Technology": {"Research Laboratory": 5,
                                                "Energy Technology": 8,
                                                "Laser Technology": 10,
                                                "Ion Technology": 5},
                          "Intergalactic Research Network": {"Research Laboratory": 10,
                                                             "Computer Technology": 8,
                                                             "Hyperspace Technology": 8},
                          "Astrophysics": {"Research Laboratory": 3,
                                           "Espionage Technology": 4,
                                           "Impulse Drive": 3},
                          "Graviton Technology": {"Research Laboratory": 12},

                          "Small Cargo": {"Shipyard": 2,
                                          "Combustion Drive": 2},
                          "Large Cargo": {"Shipyard": 4,
                                          "Combustion Drive": 6},
                          "Light Fighter": {"Shipyard": 1,
                                            "Combustion Drive": 1},
                          "Heavy Fighter": {"Shipyard": 3,
                                            "Armor Technology": 2,
                                            "Impulse Drive": 2},
                          "Cruiser": {"Shipyard": 5,
                                      "Impulse Drive": 2,
                                      "Ion Technology": 2},
                          "Battleship": {"Shipyard": 7,
                                         "Hyperspace Drive": 4},
                          "Colony Ship": {"Shipyard": 4,
                                          "Impulse Drive": 3},
                          "Recycler": {"Shipyard": 4,
                                       "Combustion Drive": 6,
                                       "Shielding Technology": 2},
                          "Espionage Probe": {"Shipyard": 3,
                                              "Combustion Drive": 3,
                                              "Espionage Technology": 2},
                          "Bomber": {"Shipyard": 8,
                                     "Impulse Drive": 3,
                                     "Plasma Technology": 5},
                          "Solar Satellite": {"Shipyard": 1},
                          "Destroyer": {"Shipyard": 9,
                                        "Hyperspace Drive": 6,
                                        "Hyperspace Technology": 5},
                          "Deathstar": {"Shipyard": 12,
                                        "Hyperspace Drive": 7,
                                        "Hpyerspace Technology": 6,
                                        "Graviton Technology": 1},
                          "Battlecruiser": {"Shipyard": 8,
                                            "Hyperspace Technology": 5,
                                            "Hyperspace Drive": 5,
                                            "Laser Technology": 12},
                          "Mega Cargo": {"Shipyard": 4,
                                         "Impulse Drive": 3},

                          "Rocket Launcher": {"Shipyard": 1},
                          "Light Laser": {"Shipyard": 2,
                                          "Energy Technology": 1,
                                          "Laser Technology": 3},
                          "Heavy Laser": {"Shipyard": 4,
                                          "Energy Technology": 3,
                                          "Laser Technology": 6},
                          "Gauss Cannon": {"Shipyard": 6,
                                           "Energy Technology": 6,
                                           "Weapons Technology": 3,
                                           "Shielding Technology": 1},
                          "Ion Cannon": {"Shipyard": 4,
                                         "Ion Technology": 4},
                          "Plasma Turret": {"Shipyard": 8,
                                            "Plasma Technology": 7},
                          "Small Shield Dome": {"Shipyard": 1,
                                                "Shielding Technology": 2},
                          "Large Shield Dome": {"Shipyard": 6,
                                                "Shielding Technology": 6},
                          "Antiballistic Missile": {"Shipyard": 1,
                                                    "Missile Silo": 2},
                          "Interplanetary Missile": {"Shipyard": 1,
                                                     "Missile Silo": 4,
                                                     "Hyperspace Drive": 1}
                          }
