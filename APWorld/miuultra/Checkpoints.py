from typing import List, Optional, Callable
from BaseClasses import CollectionState
from dataclasses import dataclass
from .Regions import Regions, MIUUltraRegion
from rule_builder.rules import Rule, True_, Has, HasAll

@dataclass
class MIUUCheckpoint():
    name: str
    homeRegion: MIUUltraRegion
    checkpointID: str
    logic: Rule


checkpoint_dict: dict[str, List[MIUUCheckpoint]] = {
    #
    # Chapter 1
    #
    "learning_to_jump_update": [MIUUCheckpoint("Checkpoint Before Super Jump", Regions.ch1, "-61-12176.25", True_())],
    "fsa_update": [MIUUCheckpoint("Checkpoint Before Goal Jump", Regions.ch1, "11431.5000552.75", True_())],
    "leaf_on_the_wind": [
        MIUUCheckpoint("Checkpoint Before Second Jump", Regions.ch1, "509.5-85-8.999939", True_()),
        MIUUCheckpoint("Checkpoint Before Last Jump", Regions.ch1, "697.25-103.5-25.49992", True_())
    ],
    #
    # Chapter 2
    #
    "duality_v2": [MIUUCheckpoint("Checkpoint Under Archway", Regions.ch2, "53024.00002", True_())],
    "L2bounce": [
        MIUUCheckpoint("Checkpoint At Left Turn", Regions.ch2, "139.5922-13.04", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Goal", Regions.ch2, "5931.541", Has("Bounce Surfaces"))
    ],
    "greatWall": [MIUUCheckpoint("Checkpoint Near Second Gem", Regions.ch2, "201.812539", True_())],
    "carom_v2": [
        MIUUCheckpoint("Checkpoint After Bumper Staircase", Regions.ch2, "34.27721-4.557.91943", True_()),
        MIUUCheckpoint("Checkpoint Before Third Gem", Regions.ch2, "48.75-8.5130.1875", True_()),
        MIUUCheckpoint("Checkpoint After Third Gem", Regions.ch2, "-14.0625-8.5156.1875", True_()),
    ],
    "rush_hour": [MIUUCheckpoint("Checkpoint Before Left Curve", Regions.ch2, "-470.36-9.57-119.22", True_())],
    "intothearctic_v2": [
        MIUUCheckpoint("Checkpoint Before Large Area", Regions.ch2, "381.625-16.25146.375", True_()),
        MIUUCheckpoint("Checkpoint After Orange Moving Platforms", Regions.ch2, "400-16.25-34.00006", True_())
    ],
    "transit_mayhem": [
        MIUUCheckpoint("Checkpoint Before First Pendulum", Regions.ch2, "942.524", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Before Ending Pendulum", Regions.ch2, "196450", Has("Blue Moving Platforms"))
    ],
    "gravityknot_v2": [
        MIUUCheckpoint("Checkpoint Before Bumper Staircase", Regions.ch2, "4.00005327.6329397", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Before Right Turn with Bumper", Regions.ch2, "61-28.597", Has("Gravity Surfaces"))
    ],
    "steppingstones_update": [
        MIUUCheckpoint("Checkpoint After First Super Jump", Regions.ch2, "9610-88", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint Before First Basher", Regions.ch2, "181.759432.68901-156.6488", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint In Front of Large Rock", Regions.ch2, "82.4824628-223.2638", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint Before First Bumper Staircase", Regions.ch2, "-127.41530.10583-149.9872", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint After Second Super Jump", Regions.ch2, "-160.655553.15015-285.9724", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint Before Feather Fall", Regions.ch2, "-2077-424", HasAll("Blue Moving Platforms", "Gravity Surfaces", "Super Jump"))
    ],
    #
    # Chapter 3
    #
    "speedball_v2": [MIUUCheckpoint("Checkpoint Before Final Slope", Regions.ch3, "-243-63.99994181.5", True_())],
    "mountmarblius_v2": [
        MIUUCheckpoint("Checkpoint After First Area", Regions.ch3, "-74111.5114.5", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint After Second Area", Regions.ch3, "-40115188.5", Has("Bounce Surfaces"))
    ],
    "transmission_v2": [
        MIUUCheckpoint("Checkpoint After First Large Gear", Regions.ch3, "-439.3275-1.5-191.1293", True_()),
        MIUUCheckpoint("Checkpoint At Third Large Gear", Regions.ch3, "-312.75-4.5-108.25", True_()),
        MIUUCheckpoint("Checkpoint After Fourth Large Gear", Regions.ch3, "-341.757-164.75", Has("Blue Moving Platforms"))
    ],
    "archipelago": [
        MIUUCheckpoint("Checkpoint After Red Moving Platforms", Regions.ch3, "109.01221114.75", True_()),
        MIUUCheckpoint("Checkpoint Before Final Launch", Regions.ch3, "207.75633.25", True_())
    ],
    "sugarRush": [MIUUCheckpoint("Checkpoint At Midway Point", Regions.ch3, "-199.1314.6444.03", True_())],
    "slalom_v2": [
        MIUUCheckpoint("Checkpoint After First Runoff", Regions.ch3, "-53.725-5-50.294", True_()),
        MIUUCheckpoint("Checkpoint After Second Runoff and Blue Platform", Regions.ch3, "7216.5-118", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After Third Runoff and Blue Platform", Regions.ch3, "-110.105766-77.19424", Has("Blue Moving Platforms"))
    ],
    "outskirts": [
        MIUUCheckpoint("Checkpoint At Two Rotating Platform Area", Regions.ch3, "01583.5", True_()),
        MIUUCheckpoint("Checkpoint At Surrounded Rising Floor Area", Regions.ch3, "72.3815-41.79", True_()),
        MIUUCheckpoint("Checkpoint At Large Rising Floor Area", Regions.ch3, "-72.3615-41.77", True_())
    ],
    "offkilter": [
        MIUUCheckpoint("Checkpoint Before Sloped Terrain Area", Regions.ch3, "-57.028227.541.5", True_()),
        MIUUCheckpoint("Checkpoint Before Dedicated Corkscrew", Regions.ch3, "-180.84241941.5", True_()),
        MIUUCheckpoint("Checkpoint After Dedicated Corkscrew", Regions.ch3, "-350.7518.542", Has("Gravity Surfaces"))
    ],
    "icyascent": [MIUUCheckpoint("Checkpoint After Second Large Slope", Regions.ch3, "-1.00794994.4999829.65746", True_())],
    "badcompany_v2": [
        MIUUCheckpoint("Checkpoint After First Basher Set", Regions.ch3, "1.195782E-05596", True_()),
        MIUUCheckpoint("Checkpoint Before First Blue Moving Platform", Regions.ch3, "120596", True_()),
        MIUUCheckpoint("Checkpoint After Gem Platform", Regions.ch3, "12020.51.5", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Before Basher Archway", Regions.ch3, "9615104", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Before Second Blue Moving Platform", Regions.ch3, "-161984", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpint Before Final Slope", Regions.ch3, "-1619-15", Has("Blue Moving Platforms"))
    ],
    "tubular": [MIUUCheckpoint("Checkpoint Before Final Tube", Regions.ch3, "20.53574-100.4387", True_())],
    "overclocked_update": [
        MIUUCheckpoint("Checkpoint After Starting Gears", Regions.ch3, "-615123.5-179.5", True_()),
        MIUUCheckpoint("Checkpoint Near First Gem", Regions.ch3, "-631137-307.5", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After First Gear Elevator", Regions.ch3, "-598.75140.25-249.75", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After Second Gem", Regions.ch3, "-635163.5-225.75", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Before Final Slide to Goal", Regions.ch3, "-625.25163.5-303.75", Has("Blue Moving Platforms"))
    ],
    #
    #Chapter 4
    #
    "tether": [
        MIUUCheckpoint("Checkpoint After First Hill", Regions.ch4, "6244.54-84", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Before Floating Platforms", Regions.ch4, "-51.31252.95-56", Has("Gravity Surfaces")),
    ],
    "aqueduct": [MIUUCheckpoint("Checkpoint At Bottom of Level", Regions.ch4, "1.947397E-06-31368", True_())],
    "ricochet_v2": [MIUUCheckpoint("Checkpoint Before Final Straightaway", Regions.ch4, "106.537.750", True_())],
    "braid_update": [MIUUCheckpoint("Checkpoint At Level Intersection", Regions.ch4, "54.2761832.25-161.9564", True_())],
    "sun_spire": [
        MIUUCheckpoint("Checkpoint At Fork in the Road", Regions.ch4, "17.999994488", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Near Top of Spire", Regions.ch4, "-329968", Has("Blue Moving Platforms")),
    ],
    "thunderdrome": [
        MIUUCheckpoint("Checkpoint On Right of Three Gem Bridge", Regions.ch4, "0657", True_()),
        MIUUCheckpoint("Checkpoint On Left of Three Gem Bridge", Regions.ch4, "-112657", True_()),
        MIUUCheckpoint("Checkpoint Atop U-Shaped Slope", Regions.ch4, "-1881625", Has("Boost")),
        MIUUCheckpoint("Checkpoint Near Half-Pipe", Regions.ch4, "-221.04681.55", True_()),
    ],
    "hyperloop": [
        MIUUCheckpoint("Checkpoint Before First Pipe", Regions.ch4, "964.58287-22.16", True_()),
        MIUUCheckpoint("Checkpoint Before Second Pipe", Regions.ch4, "152.619638-315.1177", True_()),
        MIUUCheckpoint("Checkpoint On Slope Within Second Pipe", Regions.ch4, "-649.2623-238.4767-596.1896", True_()),
    ],
    "gearing_up": [
        MIUUCheckpoint("Checkpoint Atop First Gear", Regions.ch4, "11.339.500002-10.7", True_()),
        MIUUCheckpoint("Checkpoint Before Second Gear", Regions.ch4, "59.0513.579.36", True_()),
        MIUUCheckpoint("Checkpoint Atop Second Gear", Regions.ch4, "92.517.75131.5", True_()),
        MIUUCheckpoint("Checkpoint Before Third Gear", Regions.ch4, "-12.8221.5135.89", True_()),
        MIUUCheckpoint("Checkpoint Atop Third Gear", Regions.ch4, "-74.1600325.5139.49", True_()),
    ],
    "acrophobia": [
        MIUUCheckpoint("Checkpoint Near First Gem", Regions.ch4, "-72.53.5-2", True_()),
        MIUUCheckpoint("Checkpoint Near Second Gem", Regions.ch4, "-117.5242", True_()),
        MIUUCheckpoint("Checkpoint Near Third Gem", Regions.ch4, "-18248", True_()),
    ],
    "rime": [
        MIUUCheckpoint("Checkpoint After Icy Left Curve", Regions.ch4, "-132-17690.5", True_()),
        MIUUCheckpoint("Checkpoint Before Icy Right Curve", Regions.ch4, "-552-23.5690.5", True_()),
    ],
    "cogValley": [
        MIUUCheckpoint("Checkpoint Before Small Gears", Regions.ch4, "86320.5", True_()),
        MIUUCheckpoint("Checkpoint After Small Gears", Regions.ch4, "86392", True_()),
        MIUUCheckpoint("Checkpoint Before Large Goal Gear Wheel", Regions.ch4, "58.585137.5", True_()),
    ],
    "citadel": [
        MIUUCheckpoint("Checkpoint After First Super Jump Tower", Regions.ch4, "64.12-7.252293.69", Has("Super Jump")),
        MIUUCheckpoint("Checkpoint Before Moving Platform Tower", Regions.ch4, "-46.06-7.7572.23", HasAll("Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint After Moving Platform Tower", Regions.ch4, "-48.37528.2498664", HasAll("Super Jump", "Boost", "Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After Sloped Boost Wall", Regions.ch4, "-85.58-2.5414.24", HasAll("Super Jump", "Boost", "Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Before Basher Towers", Regions.ch4, "-428.954938.93676292.0625", HasAll("Super Jump", "Boost", "Blue Moving Platforms")),
    ],
    #
    #Chapter 5
    #
    "newtonscradle": [
        MIUUCheckpoint("Checkpoint Before Five Pendulums", Regions.ch5, "812.2539", True_()),
        MIUUCheckpoint("Checkpoint Before Colliding Pendulums", Regions.ch5, "178.271915.2541.34804", True_()),
    ],
    "exmachina": [
        MIUUCheckpoint("Checkpoint After First Feather Fall", Regions.ch5, "-45-16-141", Has("Feather Fall")),
        MIUUCheckpoint("Checkpoint Before Second Feather Fall", Regions.ch5, "24115.5-129", Has("Feather Fall")),
        MIUUCheckpoint("Checkpoint After Second Feather Fall", Regions.ch5, "425.5-29.5-131.5", Has("Feather Fall")),
    ],
    "gearheart": [
        MIUUCheckpoint("Checkpoint At Spinning Ice Pit", Regions.ch5, "64.4-6.52-156.29", True_()),
        MIUUCheckpoint("Checkpoint At Slope With Rising Walls", Regions.ch5, "118.5265-6.5-162.7052", True_()),
        MIUUCheckpoint("Checkpoint At Tilting Platforms", Regions.ch5, "76-6.5-86", True_()),
    ],
    "kleinsche": [
        MIUUCheckpoint("Checkpoint Before First Intersection", Regions.ch5, "-12471.2515.51", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint After Second Intersection", Regions.ch5, "-116.75-16.91-30.9", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint After Third Intersection", Regions.ch5, "-56.29-14.365.43", Has("Gravity Surfaces")),
    ],
    "direstraits": [
        MIUUCheckpoint("Checkpoint After First Super Jump", Regions.ch5, "23.5233121.8413658.47124", Has("Super Jump")),
        MIUUCheckpoint("Checkpoint Near Second Gem", Regions.ch5, "6022-78.75", Has("Super Jump")),
    ],
    "diamond": [
        MIUUCheckpoint("Checkpoint Before First Left Turn", Regions.ch5, "56-52252", True_()),
        MIUUCheckpoint("Checkpoint Before First Right Turn", Regions.ch5, "-148-76440", True_()),
        MIUUCheckpoint("Checkpoint Within Second Right Turn", Regions.ch5, "-152-1601173", True_()),
        MIUUCheckpoint("Checkpoint Before Final Jump", Regions.ch5, "72-2081541", True_()),
    ],
    "glacier_v2": [
        MIUUCheckpoint("Checkpoint In Bottom Left Of Map", Regions.ch5, "5812.562", True_()),
        MIUUCheckpoint("Checkpoint In Top Left Of Map", Regions.ch5, "1068.5-38", True_()),
        MIUUCheckpoint("Checkpoint In Top Right Of Map", Regions.ch5, "-6612.5-54", True_()),
        MIUUCheckpoint("Checkpoint In Bottom Right Of Map", Regions.ch5, "-1228.538", True_()),
    ],
    "shift": [
        MIUUCheckpoint("Checkpoint Before First Horizontal Swaying Platform", Regions.ch5, "-808.25-116", True_()),
        MIUUCheckpoint("Checkpoint Before Second Horizontal Swaying Platform", Regions.ch5, "5613.25-136", True_()),
        MIUUCheckpoint("Checkpoint Before Final Horizontal Swaying Platform", Regions.ch5, "-1631-116", True_()),
    ],
    "conduit_v2": [
        MIUUCheckpoint("Checkpoint After First Bounce Surface Jump", Regions.ch5, "12-2.875-138", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Boost Halfpipe", Regions.ch5, "12-10.875641", Has("Bounce Surfaces")),
    ],
    "flip_the_table_v2": [
        MIUUCheckpoint("Checkpoint On Upper Surface Near Start of Level", Regions.ch5, "-15.539.513", True_()),
        MIUUCheckpoint("Checkpoint On Underside Near Three Bumpers", Regions.ch5, "-1.540.5-15", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint On Underside Near Single Bumper", Regions.ch5, "12.540.527", Has("Gravity Surfaces")),
    ],
    "energy_v2": [
        MIUUCheckpoint("Checkpoint Near Fourth Gem", Regions.ch5, "-10840-325.4976", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Large Spinning Ring", Regions.ch5, "844-326", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Time Travel and Eighth Gem Bowl", Regions.ch5, "15.2555-124.25", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Near Final Bowl", Regions.ch5, "-154.138782.25-100.0275", HasAll("Bounce Surfaces", "Super Jump")),
    ],
    "mobiusmadness_v2": [
        MIUUCheckpoint("Checkpoint At First Gem Bumpers", Regions.ch5, "2600-74", HasAll("Gravity Surfaces", "Boost")),
        MIUUCheckpoint("Checkpoint At Second Gem Holes", Regions.ch5, "260-740", HasAll("Gravity Surfaces", "Boost")),
        MIUUCheckpoint("Checkpoint At Third Gem Slopes", Regions.ch5, "260074", HasAll("Gravity Surfaces", "Boost")),
        MIUUCheckpoint("Checkpoint Before Fourth Gem Bounce Surfaces", Regions.ch5, "260740", HasAll("Gravity Surfaces", "Boost")),
    ],
    #
    #Chapter 6
    #
    "amethyst_v2": [
        MIUUCheckpoint("Checkpoint After Start on Left Side", Regions.ch6, "79-2-153", True_()),
        MIUUCheckpoint("Checkpoint On Left Before Upward Launch", Regions.ch6, "6614-277.5", True_()),
        MIUUCheckpoint("Checkpoint After Start on Right Side", Regions.ch6, "-721-130", True_()),
        MIUUCheckpoint("Checkpoint On Right Before Upward Launch", Regions.ch6, "-78.214-284", True_()),
    ],
    "rondure": [
        MIUUCheckpoint("Checkpoint One Near Dual Bridge", Regions.ch6, "-34.13-15.28914.195", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Two Near Dual Bridge", Regions.ch6, "-34.19715.257-14.187", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Near Orange-Blue Sloped Bridge", Regions.ch6, "015.31-36.95", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint One Near Bumper Circle", Regions.ch6, "36.9715.2720", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Two Near Bumper Circle", Regions.ch6, "36.979-15.2730", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint One Near Green-Blue Sloped Bridge", Regions.ch6, "015.30536.94", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Two Near Green-Blue Sloped Bridge", Regions.ch6, "0-15.30736.954", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Under Bumper Circle", Regions.ch6, "33.75", Has("Gravity Surfaces")),
    ],
    "isaacs_apple": [
        MIUUCheckpoint("Checkpoint After First Pendulums", Regions.ch6, "-252.25", True_()),
        MIUUCheckpoint("Checkpoint Before Fork In The Road", Regions.ch6, "-329.5", True_()),
        MIUUCheckpoint("Checkpoint At Intersection Left Side", Regions.ch6, "-374.5", True_()),
        MIUUCheckpoint("Checkpoint At Intersection Right Side", Regions.ch6, "-397.5", True_()),
        MIUUCheckpoint("Checkpoint Before C-Shaped Pendulums", Regions.ch6, "-517.75", True_()),
        MIUUCheckpoint("Checkpoint Before Y-Shaped Pendulums", Regions.ch6, "-654.5", True_()),
    ],
    "penrosepass": [
        MIUUCheckpoint("Checkpoint After First Jump", Regions.ch6, "-61.95699157.0396-51.46082", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Before Upward Curve", Regions.ch6, "-344.72276157", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Before Two Time-Travel Slopes", Regions.ch6, "-535.23064", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint After Left Turn Before Gem", Regions.ch6, "19.940712.717354-505.6976", Has("Gravity Surfaces")),
    ],
    "siege": [
        MIUUCheckpoint("Checkpoint At Middle Gem", Regions.ch6, "431-137", HasAll("Super Jump", "Boost", "Feather Fall")),
        MIUUCheckpoint("Checkpoint At Right Gem", Regions.ch6, "-2956.33334", HasAll("Super Jump", "Boost", "Feather Fall")),
        MIUUCheckpoint("Checkpoint At Left Gem", Regions.ch6, "2828.66657-101", HasAll("Super Jump", "Boost", "Feather Fall")),
    ],
    "flywheel_v2": [
        MIUUCheckpoint("Checkpoint After First Loop", Regions.ch6, "1616.5161", True_()),
        MIUUCheckpoint("Checkpoint After Large Upward Slope", Regions.ch6, "19638.5177", Has("Boost")),
        MIUUCheckpoint("Checkpoint After Second Loop", Regions.ch6, "850161", Has("Boost")),
        MIUUCheckpoint("Checkpoint After Third Loop", Regions.ch6, "-1002.5", Has("Boost")),
    ],
    "symbiosis": [
        MIUUCheckpoint("Checkpoint Before First Platform Raise", Regions.ch6, "100136", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After First Basher Section", Regions.ch6, "-1817151", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After Staircase and Slope", Regions.ch6, "-9.9708517.0314", Has("Blue Moving Platforms")),
    ],
    "tesseract": [
        MIUUCheckpoint("Checkpoint on Higher Green Surfaces", Regions.ch6, "-4968", True_()),
        MIUUCheckpoint("Checkpoint on Lower Green Surfaces", Regions.ch6, "-270", True_()),
        MIUUCheckpoint("Checkpoint on Lower Blue Surfaces", Regions.ch6, "-3132", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint on Higher Blue Surfaces", Regions.ch6, "-459", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint on Higher Red Surfaces", Regions.ch6, "-881", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint on Red Surfaces 2", Regions.ch6, "-4463", Has("Gravity Surfaces")),
    ],
    "leapsandbounds_v2": [
        MIUUCheckpoint("Checkpoint After Second Super Jump", Regions.ch6, "18.7529.99999-32", HasAll("Super Jump", "Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint Under Straight Archway", Regions.ch6, "-32.562.99998-16", HasAll("Super Jump", "Blue Moving Platforms")),
    ],
    "vertigo_mayhem": [
        MIUUCheckpoint("Checkpoint After First Walkway", Regions.ch6, "-30.6", True_()),
        MIUUCheckpoint("Checkpoint After Spinning Bashers", Regions.ch6, "-43.429998", True_()),
        MIUUCheckpoint("Checkpoint After Rising Walkways", Regions.ch6, "-15.995211.6875-54.71939", True_()),
        MIUUCheckpoint("Checkpoint After Walkway With Time Travels", Regions.ch6, "-13.259383.630736-114.2674", True_()),
        MIUUCheckpoint("Checkpoint After Winding Walkway With Spinning Bashers", Regions.ch6, "29.544623.375-119.5074", True_()),
    ],
    "tossedabout_v2": [
        MIUUCheckpoint("Checkpoint After First Moving Wall Pinch", Regions.ch6, "8048199.75", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint After Large Jump", Regions.ch6, "4468-48", HasAll("Bounce Surfaces", "Feather Fall")),
        MIUUCheckpoint("Checkpoint After Last Feather Fall", Regions.ch6, "466.977866.25-203.9632", HasAll("Bounce Surfaces", "Feather Fall")),
    ],
    "apogee_v2": [
        MIUUCheckpoint("Checkpoint Before First Gem Area", Regions.ch6, "85.29267-171.024952.5584", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint After First Gem Area", Regions.ch6, "61.25659-106.142565.82552", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint Before Boost Surface and Super Jump Area", Regions.ch6, "-1.83-53.52132.14", HasAll("Gravity Surfaces", "Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Second Gem Area", Regions.ch6, "-88.52-4.4378.49", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint After Second Gem Area", Regions.ch6, "-150.3995-5.584.87501", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump")),
        MIUUCheckpoint("Checkpoint Before Spinning Cylinder", Regions.ch6, "-227.82-54.61129.63", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint Before Third Gem Area", Regions.ch6, "-291.0605-106.272964.4476", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint After Third Gem Area", Regions.ch6, "-420.91", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint Before Ice Half-Pipe", Regions.ch6, "-447.91", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint Before Fourth Gem Area", Regions.ch6, "-546.1495", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint After Fourth Gem Area", Regions.ch6, "-581.65182", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")()),
        MIUUCheckpoint("Checkpoint Before Feather Fall Jump", Regions.ch6, "-572.553479", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint In Center of Fifth Gem Area", Regions.ch6, "-107.7329-395.806563.31092", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost", "Feather Fall")),
        MIUUCheckpoint("Checkpoint After Fifth Gem Area", Regions.ch6, "-107.4269-395.0334103.1099", HasAll("Gravity Surfaces", "Bounce Surfaces", "Super Jump", "Boost", "Feather Fall")),
    ],
    #
    #Bonus 1
    #
    "rosenbridge_update": [
        MIUUCheckpoint("Checkpoint After First Large Rock", Regions.ba1, "653.587", True_()),
        MIUUCheckpoint("Checkpoint After Second Large Rock With Treasure Box", Regions.ba1, "-397.5190.5", True_()),
        MIUUCheckpoint("Checkpoint After Dual Large Rocks", Regions.ba1, "5014.2533", True_()),
    ],
    "onward_and_upward_mayhem": [
        MIUUCheckpoint("Checkpoint After Gem Staircase", Regions.ba1, "-1625115.75", Has("Super Jump")),
        MIUUCheckpoint("Checkpoint Before Upward Gravity Surface", Regions.ba1, "-125.525947.75", Has("Super Jump")),
    ],
    "permutation": [
        MIUUCheckpoint("Checkpoint Before First Bounce Surface", Regions.ba1, "-87.403824", True_()),
        MIUUCheckpoint("Checkpoint After Second Bounce Surface", Regions.ba1, "18.0577715-136.5452", Has("Bounce Surfaces")),
        MIUUCheckpoint("Checkpoint Before Third Gem and Ice Surfaces", Regions.ba1, "74.950426-37.91706", Has("Bounce Surfaces")),
    ],
    "elevatoraction": [MIUUCheckpoint("Checkpoint On Higher Curve Platform", Regions.ba1, "39.515.5-25.40009", True_())],
    "timecapsule": [
        MIUUCheckpoint("Checkpoint On Left Side of Ring", Regions.ba1, "-321162", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint On Right Side of Ring", Regions.ba1, "161162", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint On Top Side of Ring", Regions.ba1, "-83562", Has("Gravity Surfaces")),
    ],
    "4stairs": [
        MIUUCheckpoint("Checkpoint On Left of Upper Layer", Regions.ba1, "320-4", True_()),
        MIUUCheckpoint("Checkpoint On Right of Upper Layer", Regions.ba1, "0.07855242027.88083", True_()),
        MIUUCheckpoint("Checkpoint On Center of Lower Layer", Regions.ba1, "16-2412", True_()),
    ],
    "need_for_speed": [
        MIUUCheckpoint("Checkpoint At Hard Left Turn", Regions.ba1, "-418.56", True_()),
        MIUUCheckpoint("Checkpoint Before Large Jump", Regions.ba1, "-1763190.75", True_()),
        MIUUCheckpoint("Checkpoint Near Large Rock", Regions.ba1, "2431333.5", Has("Boost")),
    ],
    "rivervantage": [
        MIUUCheckpoint("Checkpoint At Bottom of Wavy Slope", Regions.ba1, "53.986922-168.9359", True_()),
        MIUUCheckpoint("Checkpoint At Top of Green Wavy Slope", Regions.ba1, "63.931117.5-162.0346", True_()),
        MIUUCheckpoint("Checkpoint After Boost Jump", Regions.ba1, "68272", Has("Boost")),
    ],
    "gravitycube_update": [
        MIUUCheckpoint("Checkpoint On Lower Purple Level", Regions.ba1, "240.7514", True_()),
        MIUUCheckpoint("Checkpoint On Lower Blue Level", Regions.ba1, "243043.5", Has("Gravity Surfaces")),
        MIUUCheckpoint("Checkpoint On Lower Green Level", Regions.ba1, "65.530-10", Has("Gravity Surfaces")),
    ],
    "platinum_playground_mayhem": [
        MIUUCheckpoint("Checkpoint On Left of Level", Regions.ba1, "-144", True_()),
        MIUUCheckpoint("Checkpoint At Back Right On Purple Slope", Regions.ba1, "-175.5", True_()),
        MIUUCheckpoint("Checkpoint On Right of Level", Regions.ba1, "-235.5", True_()),
        MIUUCheckpoint("Checkpoint At Back Right On Green Slope", Regions.ba1, "-218.5", True_()),
    ],
    #
    #Bonus 2
    #
    "ribbon_v2": [
        MIUUCheckpoint("Checkpoint Before First Hole", Regions.ba2, "29.000353-43.00016", True_()),
        MIUUCheckpoint("Checkpoint Before Gravity Ribbon", Regions.ba2, "-116329", True_()),
        MIUUCheckpoint("Checkpoint After Ice Curve", Regions.ba2, "-2286", Has("Gravity Surfaces")),
    ],
    "threadNeedle": [
        MIUUCheckpoint("Checkpoint After Super Jump", Regions.ba2, "19.0945530-9.900337", Has("Super Jump")),
        MIUUCheckpoint("Checkpoint After Floor with Holes", Regions.ba2, "35.094545254.09965", HasAll("Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint Before Upward Curve", Regions.ba2, "98.256625", HasAll("Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint After Spinning Orange Platform", Regions.ba2, "10.749997825", HasAll("Super Jump", "Boost")),
        MIUUCheckpoint("Checkpoint Before Gravity Surface Downward Slope", Regions.ba2, "38.00476158.5-12.89029", HasAll("Super Jump", "Boost")),
    ],
    "bumperinvasion": [
        MIUUCheckpoint("Checkpoint Before Blue Ice Platform", Regions.ba2, "6132", True_()),
        MIUUCheckpoint("Checkpoint On Bumper Side Road", Regions.ba2, "101378", True_()),
        MIUUCheckpoint("Checkpoint Before Icy Bumper Curves", Regions.ba2, "-43336", True_()),
    ],
    "bash_tion": [
        MIUUCheckpoint("Checkpoint On Left of Tower Near Start", Regions.ba2, "-1031.5", True_()),
        MIUUCheckpoint("Checkpoint Near Back Wall With Bashers", Regions.ba2, "-897.5", True_()),
        MIUUCheckpoint("Checkpoint Near Front Wall With Bashers", Regions.ba2, "-1013.5", True_()),
        MIUUCheckpoint("Checkpoint At Back of Tower", Regions.ba2, "-880", True_()),
    ],
    "runout": [
        MIUUCheckpoint("Checkpoint At Start of Purple Slope", Regions.ba2, "864-120-24", True_()),
        MIUUCheckpoint("Checkpoint Near Middle of Purple Slope", Regions.ba2, "1528-160-24", True_()),
        MIUUCheckpoint("Checkpoint After Launch onto Red Slope", Regions.ba2, "2008-212-24", True_()),
        MIUUCheckpoint("Checkpoint Near Middle of Red Slope", Regions.ba2, "2664-276-24", True_()),
    ],
    "archiarchy": [
        MIUUCheckpoint("Checkpoint At South Fork and Upward Slope", Regions.ba2, "32.5915", True_()),
        MIUUCheckpoint("Checkpoint At East Upward Slope", Regions.ba2, "-23.51799", True_()),
        MIUUCheckpoint("Checkpoint At West Fork", Regions.ba2, "0.285869617-29.37888", True_()),
        MIUUCheckpoint("Checkpoint At North Fork and Upward Slope", Regions.ba2, "-83.517111727.05806", True_()),
    ],
    "crystalmatrix": [
        MIUUCheckpoint("Checkpoint On Lower Level Between Large Crystals", Regions.ba2, "81.9383733.5-105.8814", True_()),
        MIUUCheckpoint("Checkpoint On Lower Level Overlooking Goal Fork", Regions.ba2, "1434.5-146", True_()),
        MIUUCheckpoint("Checkpoint After Left Fork Option", Regions.ba2, "-2246.5", True_()),
        MIUUCheckpoint("Checkpoint After Center Fork Option", Regions.ba2, "1042.58", True_()),
        MIUUCheckpoint("Checkpoint After Right Fork Option", Regions.ba2, "4242.58.5", True_()),
    ],
    "stayinalive_mayhem": [
        MIUUCheckpoint("Checkpoint Before Basher Curved Track", Regions.ba2, "61-48-332.25", Has("Blue Moving Platforms")),
        MIUUCheckpoint("Checkpoint After Basher Curved Track", Regions.ba2, "-414.50001", Has("Blue Moving Platforms")),
    ],
    "machinations_update": [
        MIUUCheckpoint("Checkpoint At Level Start", Regions.ba2, "1613-31.25", True_()),
        MIUUCheckpoint("Checkpoint Near Super Jump Hole", Regions.ba2, "631721.5", True_()),
        MIUUCheckpoint("Checkpoint At Dual Gears and Super Jump Slope", Regions.ba2, "161763", True_()),
        MIUUCheckpoint("Checkpoint Near Wall Gear and Super Jump Stairs", Regions.ba2, "-314.515.75", True_()),
        MIUUCheckpoint("Checkpoint Near Perpendicular and Clockwise Gears", Regions.ba2, "1613-31.25", True_()),
    ],
    "pitofdespair": [
        MIUUCheckpoint("Checkpoint Before First Pendulum", Regions.ba2, "-46.7512.25-87.75", True_()),
        MIUUCheckpoint("Checkpoint Near Ice Floor and Basher", Regions.ba2, "-50.7520.25-31.75", True_()),
        MIUUCheckpoint("Checkpoint Before Upward Ice Slope with Bashers", Regions.ba2, "-10.7499822.25-79.75001", True_()),
        MIUUCheckpoint("Checkpoint After Triple Pendulum Before Goal", Regions.ba2, "-86.7735432.25-71.75", Has("Super Jump")),
    ],
    #
    #Bonus 3
    #
    #
    #Bonus 4
    #
}