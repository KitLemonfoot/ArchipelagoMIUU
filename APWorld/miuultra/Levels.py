from typing import List, Optional, Callable
from BaseClasses import CollectionState
from dataclasses import dataclass
from .Regions import Regions, MIUUltraRegion
from rule_builder.rules import Rule, True_, Has, HasAll

# NOTE: higherCompletionLogic and treasureBoxLogic are ADDED to existing logic, not replacing.
@dataclass
class MIUULevel():
    name: str
    homeRegion: MIUUltraRegion
    internalLevelId: str
    baseCompletionLogic: Rule
    higherCompletionLogic: Rule
    treasureBoxLogic: Rule
    gemCount: int = 0

# List of every level in the game.
# Thank god for =CONCAT().
level_info_dict = {
    #Ultra Arc
    #Chapter 1
    "learning_to_roll_update": MIUULevel("Learning to Roll", Regions.ch1, "learning_to_roll_update", True_(), True_(), True_(), 0),
    "learning_to_turn_update": MIUULevel("Learning to Turn", Regions.ch1, "learning_to_turn_update", True_(), True_(), True_(), 0),
    "bunny_slope": MIUULevel("Bunny Slope", Regions.ch1, "bunny_slope", True_(), True_(), True_(), 0),
    "learning_to_jump_update": MIUULevel("Learning to Jump", Regions.ch1, "learning_to_jump_update", Has("Super Jump"), True_(), True_(), 0),
    "fsa_update": MIUULevel("Full Speed Ahead", Regions.ch1, "fsa_update", True_(), Has("Boost"), Has("Boost"), 0),
    "treasure_update": MIUULevel("Treasure Trove", Regions.ch1, "treasure_update", True_(), True_(), Has("Blue Moving Platforms"), 0),
    "frosty_update": MIUULevel("Stay Frosty", Regions.ch1, "frosty_update", True_(), True_(), True_(), 0),
    "roundbend": MIUULevel("Round the Bend", Regions.ch1, "roundbend", Has("Gravity Surfaces"), True_(), True_(), 0),
    "leaf_on_the_wind": MIUULevel("Leaf on the Wind", Regions.ch1, "leaf_on_the_wind", True_(), Has("Feather Fall"), Has("Feather Fall"), 0),
    #Chapter 2
    "duality_v2": MIUULevel("Duality", Regions.ch2, "duality_v2", True_(), True_(), Has("Feather Fall"), 0),
    "L2bounce": MIUULevel("Learning to Bounce", Regions.ch2, "L2bounce", Has("Bounce Surfaces"), True_(), True_(), 0),
    "greatWall": MIUULevel("Great Wall", Regions.ch2, "greatWall", True_(), True_(), True_(), 0),
    "carom_v2": MIUULevel("Carom", Regions.ch2, "carom_v2", True_(), True_(), True_(), 0),
    "rush_hour": MIUULevel("Rush Hour", Regions.ch2, "rush_hour", True_(), True_(), True_(), 0),
    "otgw_update": MIUULevel("Over the Garden Wall", Regions.ch2, "otgw_update", HasAll("Super Jump", "Boost", "Bounce Surfaces"), True_(), True_(), 0),
    "intothearctic_v2": MIUULevel("Into the Arctic", Regions.ch2, "intothearctic_v2", True_(), True_(), True_(), 0),
    "wave_pool_update": MIUULevel("Wave Pool", Regions.ch2, "wave_pool_update", True_(), HasAll("Super Jump", "Boost"), Has("Super Jump"), 0),
    "bigeasy": MIUULevel("Big Easy", Regions.ch2, "bigeasy", True_(), True_(), True_(), 0),
    "transit_mayhem": MIUULevel("Transit", Regions.ch2, "transit_mayhem", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "gravityknot_v2": MIUULevel("Gravity Knot", Regions.ch2, "gravityknot_v2", Has("Gravity Surfaces"), True_(), True_(), 0),
    "steppingstones_update": MIUULevel("Stepping Stones", Regions.ch2, "steppingstones_update", HasAll("Gravity Surfaces", "Super Jump", "Boost", "Blue Moving Platforms"), True_(), True_(), 0),
    #Chapter 3
    "speedball_v2": MIUULevel("Speedball", Regions.ch3, "speedball_v2", True_(), True_(), True_(), 0),
    "mountmarblius_v2": MIUULevel("Mount Marblius", Regions.ch3, "mountmarblius_v2", Has("Bounce Surfaces"), True_(), True_(), 0),
    "transmission_v2": MIUULevel("Transmission", Regions.ch3, "transmission_v2", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "archipelago": MIUULevel("Archipelago", Regions.ch3, "archipelago", Has("Feather Fall"), True_(), True_(), 0),
    "sugarRush": MIUULevel("Sugar Rush", Regions.ch3, "sugarRush", Has("Boost"), True_(), Has("Super Jump"), 0),
    "slalom_v2": MIUULevel("Slalom", Regions.ch3, "slalom_v2", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "outskirts": MIUULevel("Outskirts", Regions.ch3, "outskirts", True_(), True_(), True_(), 0),
    "offkilter": MIUULevel("Off Kilter", Regions.ch3, "offkilter", Has("Gravity Surfaces"), True_(), True_(), 0),
    "icyascent": MIUULevel("Icy Ascent", Regions.ch3, "icyascent", HasAll("Boost", "Blue Moving Platforms"), True_(), True_(), 0),
    "badcompany_v2": MIUULevel("Bad Company", Regions.ch3, "badcompany_v2", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "tubular": MIUULevel("Totally Tubular", Regions.ch3, "tubular", Has("Feather Fall"), True_(), True_(), 0),
    "overclocked_update": MIUULevel("Overclocked", Regions.ch3, "overclocked_update", Has("Blue Moving Platforms"), True_(), True_(), 0),
    #Chapter 4
    "tether": MIUULevel("Tether", Regions.ch4, "tether", Has("Gravity Surfaces"), True_(), True_(), 0),
    "aqueduct": MIUULevel("Aqueduct", Regions.ch4, "aqueduct", True_(), True_(), True_(), 0),
    "ricochet_v2": MIUULevel("Ricochet", Regions.ch4, "ricochet_v2", HasAll("Boost", "Bounce Surfaces"), True_(), True_(), 0),
    "braid_update": MIUULevel("Braid", Regions.ch4, "braid_update", HasAll("Boost", "Bounce Surfaces"), True_(), Has("Feather Fall"), 0),
    "sun_spire": MIUULevel("Sun Spire", Regions.ch4, "sun_spire", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "thunderdrome": MIUULevel("Thunderdrome", Regions.ch4, "thunderdrome", Has("Boost"), True_(), True_(), 0),
    "hyperloop": MIUULevel("Hyperloop", Regions.ch4, "hyperloop", True_(), Has("Boost"), Has("Boost"), 0),
    "gearing_up": MIUULevel("Gearing Up", Regions.ch4, "gearing_up", True_(), True_(), True_(), 0),
    "acrophobia": MIUULevel("Acrophobia", Regions.ch4, "acrophobia", True_(), True_(), True_(), 0),
    "rime": MIUULevel("Rime", Regions.ch4, "rime", True_(), True_(), True_(), 0),
    "cogValley": MIUULevel("Cog Valley", Regions.ch4, "cogValley", True_(), True_(), True_(), 0),
    "citadel": MIUULevel("Citadel", Regions.ch4, "citadel", HasAll("Super Jump", "Boost", "Blue Moving Platforms"), True_(), True_(), 0),
    #Chapter 5
    "newtonscradle": MIUULevel("Newton's Cradle", Regions.ch5, "newtonscradle", True_(), True_(), True_(), 0),
    "exmachina": MIUULevel("Ex Machina", Regions.ch5, "exmachina", Has("Feather Fall"), True_(), True_(), 0),
    "gearheart": MIUULevel("Gearheart", Regions.ch5, "gearheart", True_(), True_(), True_(), 0),
    "kleinsche": MIUULevel("Kleinsche", Regions.ch5, "kleinsche", Has("Gravity Surfaces"), True_(), True_(), 0),
    "direstraits": MIUULevel("Dire Straits", Regions.ch5, "direstraits", Has("Super Jump"), True_(), True_(), 0),
    "diamond": MIUULevel("Diamond in the Sky", Regions.ch5, "diamond", True_(), True_(), True_(), 0),
    "glacier_v2": MIUULevel("Glacier", Regions.ch5, "glacier_v2", True_(), Has("Boost"), Has("Boost"), 0),
    "shift": MIUULevel("Shift", Regions.ch5, "shift", True_(), True_(), True_(), 0),
    "conduit_v2": MIUULevel("Conduit", Regions.ch5, "conduit_v2", HasAll("Bounce Surfaces", "Boost"), True_(), True_(), 0),
    "flip_the_table_v2": MIUULevel("Flip the Table", Regions.ch5, "flip_the_table_v2", Has("Gravity Surfaces"), True_(), True_(), 0),
    "energy_v2": MIUULevel("Energy", Regions.ch5, "energy_v2", HasAll("Bounce Surfaces", "Super Jump"), True_(), True_(), 0),
    "mobiusmadness_v2": MIUULevel("Mobius Madness", Regions.ch5, "mobiusmadness_v2", HasAll("Gravity Surfaces", "Boost"), True_(), True_(), 0),
    #Chapter 6
    "amethyst_v2": MIUULevel("Amethyst", Regions.ch6, "amethyst_v2", True_(), True_(), True_(), 0),
    "rondure": MIUULevel("Rondure", Regions.ch6, "rondure", Has("Gravity Surfaces"), True_(), True_(), 0),
    "isaacs_apple": MIUULevel("Isaac's Apple", Regions.ch6, "isaacs_apple", True_(), True_(), True_(), 0),
    "penrosepass": MIUULevel("Penrose Pass", Regions.ch6, "penrosepass", Has("Gravity Surfaces"), True_(), True_(), 0),
    "siege": MIUULevel("Siege", Regions.ch6, "siege", HasAll("Super Jump", "Boost", "Feather Fall"), True_(), True_(), 0),
    "flywheel_v2": MIUULevel("Flywheel", Regions.ch6, "flywheel_v2", Has("Boost"), True_(), True_(), 0),
    "symbiosis": MIUULevel("Symbiosis", Regions.ch6, "symbiosis", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "tesseract": MIUULevel("Tesseract", Regions.ch6, "tesseract", Has("Gravity Surfaces"), True_(), True_(), 0),
    "leapsandbounds_v2": MIUULevel("Leaps and Bounds", Regions.ch6, "leapsandbounds_v2", HasAll("Super Jump", "Blue Moving Platforms"), True_(), True_(), 0),
    "vertigo_mayhem": MIUULevel("Vertigo", Regions.ch6, "vertigo_mayhem", True_(), True_(), True_(), 0),
    "tossedabout_v2": MIUULevel("Tossed About", Regions.ch6, "tossedabout_v2", HasAll("Bounce Surfaces", "Feather Fall"), True_(), True_(), 0),
    "apogee_v2": MIUULevel("Apogee", Regions.ch6, "apogee_v2", HasAll("Super Jump", "Boost", "Feather Fall", "Gravity Surfaces", "Bounce Surfaces"), True_(), True_(), 0),
    # Bonus Arc
    #BA Chapter 1
    "rosenbridge_update": MIUULevel("Rosen Bridge", Regions.ba1, "rosenbridge_update", True_(), True_(), True_(), 0),
    "onward_and_upward_mayhem": MIUULevel("Onward and Upward", Regions.ba1, "onward_and_upward_mayhem", HasAll("Super Jump", "Gravity Surfaces"), Has("Boost"), True_(), 0),
    "permutation": MIUULevel("Permutation", Regions.ba1, "permutation", Has("Bounce Surfaces"), True_(), True_(), 0),
    "elevatoraction": MIUULevel("Elevator Action", Regions.ba1, "elevatoraction", True_(), True_(), True_(), 0),
    "timecapsule": MIUULevel("Time Capsule", Regions.ba1, "timecapsule", Has("Gravity Surfaces"), True_(), True_(), 0),
    "3divide": MIUULevel("Triple Divide", Regions.ba1, "3divide", True_(), HasAll("Super Jump", "Boost"), HasAll("Super Jump", "Feather Fall"), 0),
    "4stairs": MIUULevel("Four Stairs", Regions.ba1, "4stairs", Has("Super Jump"), True_(), True_(), 0),
    "need_for_speed": MIUULevel("The Need for Speed", Regions.ba1, "need_for_speed", Has("Boost"), True_(), True_(), 0),
    "rivervantage": MIUULevel("River Vantage", Regions.ba1, "rivervantage", HasAll("Super Jump", "Boost"), True_(), True_(), 0),
    "gravitycube_update": MIUULevel("Gravity Cube", Regions.ba1, "gravitycube_update", HasAll("Super Jump", "Gravity Surfaces", "Bounce Surfaces"), True_(), True_(), 0),
    "epoch": MIUULevel("Epoch", Regions.ba1, "epoch", True_(), Has("Boost"), Has("Boost"), 0),
    "platinum_playground_mayhem": MIUULevel("Platinum Playground", Regions.ba1, "platinum_playground_mayhem", Has("Boost"), True_(), Has("Feather Fall"), 0),
    #BA Chapter 2
    "ribbon_v2": MIUULevel("Ribbon", Regions.ba2, "ribbon_v2", Has("Gravity Surfaces"), True_(), True_(), 0),
    "castlechaos": MIUULevel("Castle Chaos", Regions.ba2, "castlechaos", Has("Bounce Surfaces"), True_(), Has("Feather Fall"), 0),
    "threadNeedle": MIUULevel("Thread the Needle", Regions.ba2, "threadNeedle", HasAll("Super Jump", "Boost", "Gravity Surfaces", "Blue Moving Platforms"), True_(), True_(), 0),
    "gordian_mayhem": MIUULevel("Gordian", Regions.ba2, "gordian_mayhem", HasAll("Super Jump", "Gravity Surfaces"), True_(), True_(), 0),
    "bumperinvasion": MIUULevel("Bumper Invasion", Regions.ba2, "bumperinvasion", True_(), True_(), True_(), 0),
    "bash_tion": MIUULevel("Bash-tion", Regions.ba2, "bash_tion", HasAll("Super Jump", "Boost", "Feather Fall"), True_(), True_(), 0),
    "runout": MIUULevel("Runout", Regions.ba2, "runout", True_(), True_(), True_(), 0),
    "archiarchy": MIUULevel("Archiarchy", Regions.ba2, "archiarchy", HasAll("Feather Fall", "Blue Moving Platforms"), True_(), Has("Super Jump"), 0),
    "crystalmatrix": MIUULevel("Crystalline Matrix", Regions.ba2, "crystalmatrix", True_(), HasAll("Super Jump", "Boost"), Has("Super Jump"), 0),
    "stayinalive_mayhem": MIUULevel("Stayin' Alive", Regions.ba2, "stayinalive_mayhem", Has("Blue Moving Platforms"), True_(), True_(), 0),
    "machinations_update": MIUULevel("Medieval Machinations", Regions.ba2, "machinations_update", Has("Super Jump"), True_(), True_(), 0),
    "pitofdespair": MIUULevel("The Pit of Despair", Regions.ba2, "pitofdespair", Has("Super Jump"), True_(), True_(), 0),
    #BA Chapter 3
    "contraption": MIUULevel("Contraption", Regions.ba3, "contraption", True_(), True_(), Has("Gravity Surfaces"), 0),
    "uphill": MIUULevel("Uphill Both Ways", Regions.ba3, "uphill", HasAll("Gravity Surfaces", "Boost", "Super Jump"), True_(), True_(), 0),
    "retro": MIUULevel("Retrograde Rally", Regions.ba3, "retro", True_(), Has("Boost"), Has("Boost"), 0),
    "warpcore": MIUULevel("Warp Core", Regions.ba3, "warpcore", Has("Gravity Surfaces"), True_(), True_(), 0),
    "bash_faster": MIUULevel("Cross Traffic", Regions.ba3, "bash_faster", Has("Boost"), True_(), True_(), 0),
    "prime_v2": MIUULevel("Prime", Regions.ba3, "prime_v2", True_(), True_(), True_(), 0),
    "halfpipeheaven_v2": MIUULevel("Halfpipe Heaven", Regions.ba3, "halfpipeheaven_v2", Has("Boost"), True_(), True_(), 0),
    "wanderlust_v2": MIUULevel("Wanderlust", Regions.ba3, "wanderlust_v2", HasAll("Gravity Surfaces", "Super Jump"), True_(), True_(), 0),
    "boomerang": MIUULevel("Boomerang", Regions.ba3, "boomerang", Has("Bounce Surfaces"), True_(), True_(), 0),
    "kendama": MIUULevel("Kendama", Regions.ba3, "kendama", Has("Boost"), True_(), True_(), 0),
    "cirrus_update": MIUULevel("Cirrus", Regions.ba3, "cirrus_update", HasAll("Feather Fall", "Gravity Surfaces", "Blue Moving Platforms"), True_(), True_(), 0),
    "zenith": MIUULevel("Zenith", Regions.ba3, "zenith", HasAll("Bounce Surfaces", "Super Jump", "Blue Moving Platforms"), True_(), True_(), 0),
    #BA Chapter 4
    "alldownhill": MIUULevel("All Downhill From Here", Regions.ba4, "alldownhill", Has("Gravity Surfaces"), True_(), True_(), 0),
    "dangerzone": MIUULevel("Danger Zone", Regions.ba4, "dangerzone", HasAll("Gravity Surfaces", "Boost"), True_(), True_(), 0),
    "olympus": MIUULevel("Olympus", Regions.ba4, "olympus", True_(), True_(), True_(), 0),
    "headintheclouds_mayhem": MIUULevel("Head in the Clouds", Regions.ba4, "headintheclouds_mayhem", True_(), True_(), True_(), 0),
    "centripitalforce": MIUULevel("Centripetal Force", Regions.ba4, "centripitalforce", True_(), True_(), True_(), 0),
    "slickshtick": MIUULevel("Slick Shtick", Regions.ba4, "slickshtick", True_(), True_(), True_(), 0),
    "network": MIUULevel("Network", Regions.ba4, "network", HasAll("Gravity Surfaces", "Super Jump"), True_(), True_(), 0),
    "radius": MIUULevel("Radius", Regions.ba4, "radius", HasAll("Gravity Surfaces", "Super Jump"), True_(), True_(), 0),
    "escalation": MIUULevel("Escalation", Regions.ba4, "escalation", HasAll("Super Jump", "Blue Moving Platforms"), True_(), True_(), 0),
    "torque": MIUULevel("Torque", Regions.ba4, "torque", Has("Boost"), True_(), True_(), 0),
    "tangle_mayhem": MIUULevel("Tangle", Regions.ba4, "tangle_mayhem", HasAll("Gravity Surfaces", "Super Jump"), True_(), True_(), 0),
    "stratosphere": MIUULevel("Stratosphere", Regions.ba4, "stratosphere", HasAll("Boost", "Feather Fall", "Gravity Surfaces", "Blue Moving Platforms"), True_(), True_(), 0)
}

#Levels with no starting logic.
logicless_base_complete_levels = [
    "learning_to_roll_update", "learning_to_turn_update", "bunny_slope", "fsa_update", "treasure_update", "frosty_update", "leaf_on_the_wind",
    "duality_v2", "greatWall", "carom_v2", "rush_hour", "intothearctic_v2", "wave_pool_update", "bigeasy", "transit_mayhem",
    "speedball_v2", "outskirts",
    "aqueduct", "gearing_up", "acrophobia", "rime", "cogValley",
    "newtonscradle", "gearheart", "diamond", "shift",
    "amethyst_v2", "isaacs_apple", "vertigo_mayhem",
    "rosenbridge_update", "elevatoraction",
    "bumperinvasion", "runout",
    "contraption", "prime_v2",
    "olympus", "headintheclouds_mayhem", "centripitalforce", "slickshtick"
]
