from typing import List, Optional, Callable
from BaseClasses import CollectionState
from dataclasses import dataclass
from .Regions import Regions, MIUUltraRegion
from .Options import MIUUltraOptions
from .MIUUExtraLogic import MIUUExtraLogic

@dataclass
class MIUUltraLocation:
    name: str
    region: MIUUltraRegion
    game_id: str
    logic: Optional[Callable[[CollectionState], bool]] = None

def get_location_data(player: Optional[int], options: Optional[MIUUltraOptions]):

    logic = MIUUExtraLogic(player, options)
    locations: List[MIUUltraLocation] = []

    #Base
    locations += (
        MIUUltraLocation("Learning to Roll Complete", Regions.ch1, "learning_to_roll_update-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Learning to Turn Complete", Regions.ch1, "learning_to_turn_update-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Bunny Slope Complete", Regions.ch1, "bunny_slope-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Learning to Jump Complete", Regions.ch1, "learning_to_jump_update-c", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Full Speed Ahead Complete", Regions.ch1, "fsa_update-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Treasure Trove Complete", Regions.ch1, "treasure_update-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Stay Frosty Complete", Regions.ch1, "frosty_update-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Round the Bend Complete", Regions.ch1, "roundbend-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
        MIUUltraLocation("Leaf on the Wind Complete", Regions.ch1, "leaf_on_the_wind-c", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
        #The Subtle Joy of Rolling
        MIUUltraLocation("Duality Complete", Regions.ch2, "duality_v2-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Learning to Bounce Complete", Regions.ch2, "L2bounce-c", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Great Wall Complete", Regions.ch2, "greatWall-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Carom Complete", Regions.ch2, "carom_v2-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Rush Hour Complete", Regions.ch2, "rush_hour-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Over the Garden Wall Complete", Regions.ch2, "otgw_update-c", lambda state: state.has_all({'Super Jump', 'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Into the Arctic Complete", Regions.ch2, "intothearctic_v2-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Wave Pool Complete", Regions.ch2, "wave_pool_update-c", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Big Easy Complete", Regions.ch2, "bigeasy-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Transit Complete", Regions.ch2, "transit_mayhem-c", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Gravity Knot Complete", Regions.ch2, "gravityknot_v2-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
        MIUUltraLocation("Stepping Stones Complete", Regions.ch2, "steppingstones_update-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
        #Focus On Flow
        MIUUltraLocation("Speedball Complete", Regions.ch3, "speedball_v2-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Mount Marblius Complete", Regions.ch3, "mountmarblius_v2-c", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Transmission Complete", Regions.ch3, "transmission_v2-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Archipelago Complete", Regions.ch3, "archipelago-c", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Sugar Rush Complete", Regions.ch3, "sugarRush-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Slalom Complete", Regions.ch3, "slalom_v2-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Outskirts Complete", Regions.ch3, "outskirts-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Off Kilter Complete", Regions.ch3, "offkilter-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Icy Ascent Complete", Regions.ch3, "icyascent-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Bad Company Complete", Regions.ch3, "badcompany_v2-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Totally Tubular Complete", Regions.ch3, "tubular-c", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
        MIUUltraLocation("Overclocked Complete", Regions.ch3, "overclocked_update-c", lambda state: logic.has_medals(Regions.ch3.chapter_number, state))
    )
    #Silver
    if not options or options.medal_types>0:
        locations += (
            MIUUltraLocation("Learning to Roll Silver Medal", Regions.ch1, "learning_to_roll_update-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Turn Silver Medal", Regions.ch1, "learning_to_turn_update-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Bunny Slope Silver Medal", Regions.ch1, "bunny_slope-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Jump Silver Medal", Regions.ch1, "learning_to_jump_update-s", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Full Speed Ahead Silver Medal", Regions.ch1, "fsa_update-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Treasure Trove Silver Medal", Regions.ch1, "treasure_update-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Stay Frosty Silver Medal", Regions.ch1, "frosty_update-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Round the Bend Silver Medal", Regions.ch1, "roundbend-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Leaf on the Wind Silver Medal", Regions.ch1, "leaf_on_the_wind-s", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            #The Subtle Joy of Rolling
            MIUUltraLocation("Duality Silver Medal", Regions.ch2, "duality_v2-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Learning to Bounce Silver Medal", Regions.ch2, "L2bounce-s", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Great Wall Silver Medal", Regions.ch2, "greatWall-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Carom Silver Medal", Regions.ch2, "carom_v2-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Rush Hour Silver Medal", Regions.ch2, "rush_hour-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Over the Garden Wall Silver Medal", Regions.ch2, "otgw_update-s", lambda state: state.has_all({'Super Jump', 'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Into the Arctic Silver Medal", Regions.ch2, "intothearctic_v2-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Wave Pool Silver Medal", Regions.ch2, "wave_pool_update-s", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Big Easy Silver Medal", Regions.ch2, "bigeasy-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Transit Silver Medal", Regions.ch2, "transit_mayhem-s", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Gravity Knot Silver Medal", Regions.ch2, "gravityknot_v2-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Stepping Stones Silver Medal", Regions.ch2, "steppingstones_update-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            #Focus On Flow
            MIUUltraLocation("Speedball Silver Medal", Regions.ch3, "speedball_v2-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Mount Marblius Silver Medal", Regions.ch3, "mountmarblius_v2-s", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Transmission Silver Medal", Regions.ch3, "transmission_v2-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Archipelago Silver Medal", Regions.ch3, "archipelago-s", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Sugar Rush Silver Medal", Regions.ch3, "sugarRush-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Slalom Silver Medal", Regions.ch3, "slalom_v2-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Outskirts Silver Medal", Regions.ch3, "outskirts-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Off Kilter Silver Medal", Regions.ch3, "offkilter-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Icy Ascent Silver Medal", Regions.ch3, "icyascent-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Bad Company Silver Medal", Regions.ch3, "badcompany_v2-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Totally Tubular Silver Medal", Regions.ch3, "tubular-s", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Overclocked Silver Medal", Regions.ch3, "overclocked_update-s", lambda state: logic.has_medals(Regions.ch3.chapter_number, state))
        )
    #Gold
    if not options or options.medal_types>1:
        locations += (
            MIUUltraLocation("Learning to Roll Gold Medal", Regions.ch1, "learning_to_roll_update-g", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Turn Gold Medal", Regions.ch1, "learning_to_turn_update-g", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Bunny Slope Gold Medal", Regions.ch1, "bunny_slope-g", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Jump Gold Medal", Regions.ch1, "learning_to_jump_update-g", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Full Speed Ahead Gold Medal", Regions.ch1, "fsa_update-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Treasure Trove Gold Medal", Regions.ch1, "treasure_update-g", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Stay Frosty Gold Medal", Regions.ch1, "frosty_update-g", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Round the Bend Gold Medal", Regions.ch1, "roundbend-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Leaf on the Wind Gold Medal", Regions.ch1, "leaf_on_the_wind-g", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            #The Subtle Joy of Rolling
            MIUUltraLocation("Duality Gold Medal", Regions.ch2, "duality_v2-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Learning to Bounce Gold Medal", Regions.ch2, "L2bounce-g", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Great Wall Gold Medal", Regions.ch2, "greatWall-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Carom Gold Medal", Regions.ch2, "carom_v2-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Rush Hour Gold Medal", Regions.ch2, "rush_hour-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Over the Garden Wall Gold Medal", Regions.ch2, "otgw_update-g", lambda state: state.has_all({'Super Jump', 'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Into the Arctic Gold Medal", Regions.ch2, "intothearctic_v2-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Wave Pool Gold Medal", Regions.ch2, "wave_pool_update-g", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Big Easy Gold Medal", Regions.ch2, "bigeasy-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Transit Gold Medal", Regions.ch2, "transit_mayhem-g", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Gravity Knot Gold Medal", Regions.ch2, "gravityknot_v2-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Stepping Stones Gold Medal", Regions.ch2, "steppingstones_update-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            #Focus On Flow
            MIUUltraLocation("Speedball Gold Medal", Regions.ch3, "speedball_v2-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Mount Marblius Gold Medal", Regions.ch3, "mountmarblius_v2-g", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Transmission Gold Medal", Regions.ch3, "transmission_v2-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Archipelago Gold Medal", Regions.ch3, "archipelago-g", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Sugar Rush Gold Medal", Regions.ch3, "sugarRush-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Slalom Gold Medal", Regions.ch3, "slalom_v2-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Outskirts Gold Medal", Regions.ch3, "outskirts-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Off Kilter Gold Medal", Regions.ch3, "offkilter-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Icy Ascent Gold Medal", Regions.ch3, "icyascent-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Bad Company Gold Medal", Regions.ch3, "badcompany_v2-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Totally Tubular Gold Medal", Regions.ch3, "tubular-g", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Overclocked Gold Medal", Regions.ch3, "overclocked_update-g", lambda state: logic.has_medals(Regions.ch3.chapter_number, state))
        )
    #Diamond
    if not options or options.medal_types>2:
        locations += (
            MIUUltraLocation("Learning to Roll Diamond Medal", Regions.ch1, "learning_to_roll_update-d", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Turn Diamond Medal", Regions.ch1, "learning_to_turn_update-d", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Bunny Slope Diamond Medal", Regions.ch1, "bunny_slope-d", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Learning to Jump Diamond Medal", Regions.ch1, "learning_to_jump_update-d", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Full Speed Ahead Diamond Medal", Regions.ch1, "fsa_update-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Treasure Trove Diamond Medal", Regions.ch1, "treasure_update-d", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Stay Frosty Diamond Medal", Regions.ch1, "frosty_update-d", lambda state: logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Round the Bend Diamond Medal", Regions.ch1, "roundbend-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            MIUUltraLocation("Leaf on the Wind Diamond Medal", Regions.ch1, "leaf_on_the_wind-d", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch1.chapter_number, state)),
            #The Subtle Joy of Rolling
            MIUUltraLocation("Duality Diamond Medal", Regions.ch2, "duality_v2-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Learning to Bounce Diamond Medal", Regions.ch2, "L2bounce-d", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Great Wall Diamond Medal", Regions.ch2, "greatWall-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Carom Diamond Medal", Regions.ch2, "carom_v2-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Rush Hour Diamond Medal", Regions.ch2, "rush_hour-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Over the Garden Wall Diamond Medal", Regions.ch2, "otgw_update-d", lambda state: state.has_all({'Super Jump', 'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Into the Arctic Diamond Medal", Regions.ch2, "intothearctic_v2-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Wave Pool Diamond Medal", Regions.ch2, "wave_pool_update-d", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Big Easy Diamond Medal", Regions.ch2, "bigeasy-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Transit Diamond Medal", Regions.ch2, "transit_mayhem-d", lambda state: logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Gravity Knot Diamond Medal", Regions.ch2, "gravityknot_v2-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            MIUUltraLocation("Stepping Stones Diamond Medal", Regions.ch2, "steppingstones_update-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch2.chapter_number, state)),
            #Focus On Flow
            MIUUltraLocation("Speedball Diamond Medal", Regions.ch3, "speedball_v2-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Mount Marblius Diamond Medal", Regions.ch3, "mountmarblius_v2-d", lambda state: state.has('Bounce Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Transmission Diamond Medal", Regions.ch3, "transmission_v2-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Archipelago Diamond Medal", Regions.ch3, "archipelago-d", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Sugar Rush Diamond Medal", Regions.ch3, "sugarRush-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Slalom Diamond Medal", Regions.ch3, "slalom_v2-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Outskirts Diamond Medal", Regions.ch3, "outskirts-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Off Kilter Diamond Medal", Regions.ch3, "offkilter-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Icy Ascent Diamond Medal", Regions.ch3, "icyascent-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Bad Company Diamond Medal", Regions.ch3, "badcompany_v2-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Totally Tubular Diamond Medal", Regions.ch3, "tubular-d", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch3.chapter_number, state)),
            MIUUltraLocation("Overclocked Diamond Medal", Regions.ch3, "overclocked_update-d", lambda state: logic.has_medals(Regions.ch3.chapter_number, state))
        )

    # Kick It Up A Notch
    if not options or options.final_chapter.value>0:
        #Normal
        locations += (
            MIUUltraLocation("Tether Complete", Regions.ch4, "tether-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Aqueduct Complete", Regions.ch4, "aqueduct-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Ricochet Complete", Regions.ch4, "ricochet_v2-c", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Braid Complete", Regions.ch4, "braid_update-c", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Sun Spire Complete", Regions.ch4, "sun_spire-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Thunderdrome Complete", Regions.ch4, "thunderdrome-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Hyperloop Complete", Regions.ch4, "hyperloop-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Gearing Up Complete", Regions.ch4, "gearing_up-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Acrophobia Complete", Regions.ch4, "acrophobia-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Rime Complete", Regions.ch4, "rime-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Cog Valley Complete", Regions.ch4, "cogValley-c", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
            MIUUltraLocation("Citadel Complete", Regions.ch4, "citadel-c", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
        )
        #Silver
        if(not options or options.medal_types>0):
            locations += (
                MIUUltraLocation("Tether Silver Medal", Regions.ch4, "tether-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Aqueduct Silver Medal", Regions.ch4, "aqueduct-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Ricochet Silver Medal", Regions.ch4, "ricochet_v2-s", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Braid Silver Medal", Regions.ch4, "braid_update-s", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Sun Spire Silver Medal", Regions.ch4, "sun_spire-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Thunderdrome Silver Medal", Regions.ch4, "thunderdrome-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Hyperloop Silver Medal", Regions.ch4, "hyperloop-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Gearing Up Silver Medal", Regions.ch4, "gearing_up-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Acrophobia Silver Medal", Regions.ch4, "acrophobia-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Rime Silver Medal", Regions.ch4, "rime-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Cog Valley Silver Medal", Regions.ch4, "cogValley-s", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Citadel Silver Medal", Regions.ch4, "citadel-s", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            )
        #Gold
        if(not options or options.medal_types>1):
            locations += (
                MIUUltraLocation("Tether Gold Medal", Regions.ch4, "tether-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Aqueduct Gold Medal", Regions.ch4, "aqueduct-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Ricochet Gold Medal", Regions.ch4, "ricochet_v2-g", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Braid Gold Medal", Regions.ch4, "braid_update-g", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Sun Spire Gold Medal", Regions.ch4, "sun_spire-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Thunderdrome Gold Medal", Regions.ch4, "thunderdrome-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Hyperloop Gold Medal", Regions.ch4, "hyperloop-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Gearing Up Gold Medal", Regions.ch4, "gearing_up-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Acrophobia Gold Medal", Regions.ch4, "acrophobia-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Rime Gold Medal", Regions.ch4, "rime-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Cog Valley Gold Medal", Regions.ch4, "cogValley-g", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Citadel Gold Medal", Regions.ch4, "citadel-g", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            )
        #Diamond
        if(not options or options.medal_types>2):
            locations += (
                MIUUltraLocation("Tether Diamond Medal", Regions.ch4, "tether-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Aqueduct Diamond Medal", Regions.ch4, "aqueduct-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Ricochet Diamond Medal", Regions.ch4, "ricochet_v2-d", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Braid Diamond Medal", Regions.ch4, "braid_update-d", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Sun Spire Diamond Medal", Regions.ch4, "sun_spire-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Thunderdrome Diamond Medal", Regions.ch4, "thunderdrome-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Hyperloop Diamond Medal", Regions.ch4, "hyperloop-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Gearing Up Diamond Medal", Regions.ch4, "gearing_up-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Acrophobia Diamond Medal", Regions.ch4, "acrophobia-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Rime Diamond Medal", Regions.ch4, "rime-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Cog Valley Diamond Medal", Regions.ch4, "cogValley-d", lambda state: logic.has_medals(Regions.ch4.chapter_number, state)),
                MIUUltraLocation("Citadel Diamond Medal", Regions.ch4, "citadel-d", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_medals(Regions.ch4.chapter_number, state)),
            )
        
    # Show Me What You Got
    if not options or options.final_chapter>1:
        #Normal
        locations += (
            MIUUltraLocation("Newton's Cradle Complete", Regions.ch5, "newtonscradle-c", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Ex Machina Complete", Regions.ch5, "exmachina-c", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Gearheart Complete", Regions.ch5, "gearheart-c", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Kleinsche Complete", Regions.ch5, "kleinsche-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Dire Straits Complete", Regions.ch5, "direstraits-c", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Diamond in the Sky Complete", Regions.ch5, "diamond-c", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Glacier Complete", Regions.ch5, "glacier_v2-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Shift Complete", Regions.ch5, "shift-c", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Conduit Complete", Regions.ch5, "conduit_v2-c", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Flip the Table Complete", Regions.ch5, "flip_the_table_v2-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Energy Complete", Regions.ch5, "energy_v2-c", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            MIUUltraLocation("Mobius Madness Complete", Regions.ch5, "mobiusmadness_v2-c", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
        )
        #Silver
        if(not options or options.medal_types>0):
            locations += (
                MIUUltraLocation("Newton's Cradle Silver Medal", Regions.ch5, "newtonscradle-s", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Ex Machina Silver Medal", Regions.ch5, "exmachina-s", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Gearheart Silver Medal", Regions.ch5, "gearheart-s", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Kleinsche Silver Medal", Regions.ch5, "kleinsche-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Dire Straits Silver Medal", Regions.ch5, "direstraits-s", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Diamond in the Sky Silver Medal", Regions.ch5, "diamond-s", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Glacier Silver Medal", Regions.ch5, "glacier_v2-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Shift Silver Medal", Regions.ch5, "shift-s", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Conduit Silver Medal", Regions.ch5, "conduit_v2-s", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Flip the Table Silver Medal", Regions.ch5, "flip_the_table_v2-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Energy Silver Medal", Regions.ch5, "energy_v2-s", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Mobius Madness Silver Medal", Regions.ch5, "mobiusmadness_v2-s", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            ) 
        #Gold
        if(not options or options.medal_types>1):
            locations += (
                MIUUltraLocation("Newton's Cradle Gold Medal", Regions.ch5, "newtonscradle-g", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Ex Machina Gold Medal", Regions.ch5, "exmachina-g", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Gearheart Gold Medal", Regions.ch5, "gearheart-g", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Kleinsche Gold Medal", Regions.ch5, "kleinsche-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Dire Straits Gold Medal", Regions.ch5, "direstraits-g", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Diamond in the Sky Gold Medal", Regions.ch5, "diamond-g", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Glacier Gold Medal", Regions.ch5, "glacier_v2-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Shift Gold Medal", Regions.ch5, "shift-g", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Conduit Gold Medal", Regions.ch5, "conduit_v2-g", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Flip the Table Gold Medal", Regions.ch5, "flip_the_table_v2-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Energy Gold Medal", Regions.ch5, "energy_v2-g", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Mobius Madness Gold Medal", Regions.ch5, "mobiusmadness_v2-g", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            )
        #Diamond
        if(not options or options.medal_types>2):
            locations += (
                MIUUltraLocation("Newton's Cradle Diamond Medal", Regions.ch5, "newtonscradle-d", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Ex Machina Diamond Medal", Regions.ch5, "exmachina-d", lambda state: state.has('Feather Fall', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Gearheart Diamond Medal", Regions.ch5, "gearheart-d", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Kleinsche Diamond Medal", Regions.ch5, "kleinsche-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Dire Straits Diamond Medal", Regions.ch5, "direstraits-d", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Diamond in the Sky Diamond Medal", Regions.ch5, "diamond-d", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Glacier Diamond Medal", Regions.ch5, "glacier_v2-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Shift Diamond Medal", Regions.ch5, "shift-d", lambda state: logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Conduit Diamond Medal", Regions.ch5, "conduit_v2-d", lambda state: state.has_all({'Bounce Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Flip the Table Diamond Medal", Regions.ch5, "flip_the_table_v2-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Energy Diamond Medal", Regions.ch5, "energy_v2-d", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
                MIUUltraLocation("Mobius Madness Diamond Medal", Regions.ch5, "mobiusmadness_v2-d", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_medals(Regions.ch5.chapter_number, state)),
            )

    # Play For Keeps
    if not options or options.final_chapter>2:
        #Normal
        locations += (
            MIUUltraLocation("Amethyst Complete", Regions.ch6, "amethyst_v2-c", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Rondure Complete", Regions.ch6, "rondure-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Isaac's Apple Complete", Regions.ch6, "isaacs_apple-c", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Penrose Pass Complete", Regions.ch6, "penrosepass-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Siege Complete", Regions.ch6, "siege-c", lambda state: state.has_all({'Super Jump','Boost','Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Flywheel Complete", Regions.ch6, "flywheel_v2-c", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Symbiosis Complete", Regions.ch6, "symbiosis-c", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Tesseract Complete", Regions.ch6, "tesseract-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Leaps and Bounds Complete", Regions.ch6, "leapsandbounds_v2-c", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Vertigo Complete", Regions.ch6, "vertigo_mayhem-c", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Tossed About Complete", Regions.ch6, "tossedabout_v2-c", lambda state: state.has_all({'Bounce Surfaces', 'Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            MIUUltraLocation("Apogee Complete", Regions.ch6, "apogee_v2-c", lambda state: state.has_all({'Super Jump','Boost','Feather Fall','Bounce Surfaces', 'Gravity Surfaces'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
        )
        #Silver
        if(not options or options.medal_types>0):
            locations += (
                MIUUltraLocation("Amethyst Silver Medal", Regions.ch6, "amethyst_v2-s", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Rondure Silver Medal", Regions.ch6, "rondure-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Isaac's Apple Silver Medal", Regions.ch6, "isaacs_apple-s", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Penrose Pass Silver Medal", Regions.ch6, "penrosepass-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Siege Silver Medal", Regions.ch6, "siege-s", lambda state: state.has_all({'Super Jump','Boost','Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Flywheel Silver Medal", Regions.ch6, "flywheel_v2-s", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Symbiosis Silver Medal", Regions.ch6, "symbiosis-s", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tesseract Silver Medal", Regions.ch6, "tesseract-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Leaps and Bounds Silver Medal", Regions.ch6, "leapsandbounds_v2-s", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Vertigo Silver Medal", Regions.ch6, "vertigo_mayhem-s", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tossed About Silver Medal", Regions.ch6, "tossedabout_v2-s", lambda state: state.has_all({'Bounce Surfaces', 'Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Apogee Silver Medal", Regions.ch6, "apogee_v2-s", lambda state: state.has_all({'Super Jump','Boost','Feather Fall','Bounce Surfaces', 'Gravity Surfaces'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            )
        #Gold
        if(not options or options.medal_types>1):
            locations += (
                MIUUltraLocation("Amethyst Gold Medal", Regions.ch6, "amethyst_v2-g", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Rondure Gold Medal", Regions.ch6, "rondure-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Isaac's Apple Gold Medal", Regions.ch6, "isaacs_apple-g", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Penrose Pass Gold Medal", Regions.ch6, "penrosepass-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Siege Gold Medal", Regions.ch6, "siege-g", lambda state: state.has_all({'Super Jump','Boost','Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Flywheel Gold Medal", Regions.ch6, "flywheel_v2-g", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Symbiosis Gold Medal", Regions.ch6, "symbiosis-g", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tesseract Gold Medal", Regions.ch6, "tesseract-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Leaps and Bounds Gold Medal", Regions.ch6, "leapsandbounds_v2-g", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Vertigo Gold Medal", Regions.ch6, "vertigo_mayhem-g", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tossed About Gold Medal", Regions.ch6, "tossedabout_v2-g", lambda state: state.has_all({'Bounce Surfaces', 'Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Apogee Gold Medal", Regions.ch6, "apogee_v2-g", lambda state: state.has_all({'Super Jump','Boost','Feather Fall','Bounce Surfaces', 'Gravity Surfaces'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            )
        #Diamond
        if(not options or options.medal_types>2):
            locations += (
                MIUUltraLocation("Amethyst Diamond Medal", Regions.ch6, "amethyst_v2-d", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Rondure Diamond Medal", Regions.ch6, "rondure-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Isaac's Apple Diamond Medal", Regions.ch6, "isaacs_apple-d", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Penrose Pass Diamond Medal", Regions.ch6, "penrosepass-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Siege Diamond Medal", Regions.ch6, "siege-d", lambda state: state.has_all({'Super Jump','Boost','Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Flywheel Diamond Medal", Regions.ch6, "flywheel_v2-d", lambda state: state.has('Boost', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Symbiosis Diamond Medal", Regions.ch6, "symbiosis-d", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tesseract Diamond Medal", Regions.ch6, "tesseract-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Leaps and Bounds Diamond Medal", Regions.ch6, "leapsandbounds_v2-d", lambda state: state.has('Super Jump', player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Vertigo Diamond Medal", Regions.ch6, "vertigo_mayhem-d", lambda state: logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Tossed About Diamond Medal", Regions.ch6, "tossedabout_v2-d", lambda state: state.has_all({'Bounce Surfaces', 'Feather Fall'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
                MIUUltraLocation("Apogee Diamond Medal", Regions.ch6, "apogee_v2-d", lambda state: state.has_all({'Super Jump','Boost','Feather Fall','Bounce Surfaces', 'Gravity Surfaces'}, player) and logic.has_medals(Regions.ch6.chapter_number, state)),
            )

    #Keep on Rolling
    if not options or options.bonus_arc_chapters>0:
        #Normal
        locations+=(
            MIUUltraLocation("Rosen Bridge Complete", Regions.ba1, "rosenbridge_update-c", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Onward and Upward Complete", Regions.ba1, "onward_and_upward_mayhem-c", lambda state: state.has_all({'Boost', 'Super Jump', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Permutation Complete", Regions.ba1, "permutation-c", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Elevator Action Complete", Regions.ba1, "elevatoraction-c", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Time Capsule Complete", Regions.ba1, "timecapsule-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Triple Divide Complete", Regions.ba1, "3divide-c", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Four Stairs Complete", Regions.ba1, "4stairs-c", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("The Need for Speed Complete", Regions.ba1, "need_for_speed-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("River Vantage Complete", Regions.ba1, "rivervantage-c", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Gravity Cube Complete", Regions.ba1, "gravitycube_update-c", lambda state: state.has_all({'Bounce Surfaces', 'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Epoch Complete", Regions.ba1, "epoch-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            MIUUltraLocation("Platinum Playground Complete", Regions.ba1, "platinum_playground_mayhem-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
        )
        #Silver
        if not options or options.medal_types>0:
            locations+=(
                MIUUltraLocation("Rosen Bridge Silver Medal", Regions.ba1, "rosenbridge_update-s", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Onward and Upward Silver Medal", Regions.ba1, "onward_and_upward_mayhem-s", lambda state: state.has_all({'Boost', 'Super Jump', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Permutation Silver Medal", Regions.ba1, "permutation-s", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Elevator Action Silver Medal", Regions.ba1, "elevatoraction-s", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Time Capsule Silver Medal", Regions.ba1, "timecapsule-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Triple Divide Silver Medal", Regions.ba1, "3divide-s", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Four Stairs Silver Medal", Regions.ba1, "4stairs-s", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("The Need for Speed Silver Medal", Regions.ba1, "need_for_speed-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("River Vantage Silver Medal", Regions.ba1, "rivervantage-s", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Gravity Cube Silver Medal", Regions.ba1, "gravitycube_update-s", lambda state: state.has_all({'Bounce Surfaces', 'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Epoch Silver Medal", Regions.ba1, "epoch-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Platinum Playground Silver Medal", Regions.ba1, "platinum_playground_mayhem-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            )
        #Gold
        if not options or options.medal_types>1:
            locations+=(
                MIUUltraLocation("Rosen Bridge Gold Medal", Regions.ba1, "rosenbridge_update-g", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Onward and Upward Gold Medal", Regions.ba1, "onward_and_upward_mayhem-g", lambda state: state.has_all({'Boost', 'Super Jump', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Permutation Gold Medal", Regions.ba1, "permutation-g", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Elevator Action Gold Medal", Regions.ba1, "elevatoraction-g", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Time Capsule Gold Medal", Regions.ba1, "timecapsule-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Triple Divide Gold Medal", Regions.ba1, "3divide-g", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Four Stairs Gold Medal", Regions.ba1, "4stairs-g", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("The Need for Speed Gold Medal", Regions.ba1, "need_for_speed-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("River Vantage Gold Medal", Regions.ba1, "rivervantage-g", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Gravity Cube Gold Medal", Regions.ba1, "gravitycube_update-g", lambda state: state.has_all({'Bounce Surfaces', 'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Epoch Gold Medal", Regions.ba1, "epoch-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Platinum Playground Gold Medal", Regions.ba1, "platinum_playground_mayhem-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            )
        #Diamond
        if not options or options.medal_types>2:
            locations+=(
                MIUUltraLocation("Rosen Bridge Diamond Medal", Regions.ba1, "rosenbridge_update-d", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Onward and Upward Diamond Medal", Regions.ba1, "onward_and_upward_mayhem-d", lambda state: state.has_all({'Boost', 'Super Jump', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Permutation Diamond Medal", Regions.ba1, "permutation-d", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Elevator Action Diamond Medal", Regions.ba1, "elevatoraction-d", lambda state: logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Time Capsule Diamond Medal", Regions.ba1, "timecapsule-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Triple Divide Diamond Medal", Regions.ba1, "3divide-d", lambda state: state.has_all({'Super Jump', 'Boost'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Four Stairs Diamond Medal", Regions.ba1, "4stairs-d", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("The Need for Speed Diamond Medal", Regions.ba1, "need_for_speed-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("River Vantage Diamond Medal", Regions.ba1, "rivervantage-d", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Gravity Cube Diamond Medal", Regions.ba1, "gravitycube_update-d", lambda state: state.has_all({'Bounce Surfaces', 'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Epoch Diamond Medal", Regions.ba1, "epoch-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
                MIUUltraLocation("Platinum Playground Diamond Medal", Regions.ba1, "platinum_playground_mayhem-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba1.chapter_number, state)),
            )

    # The Way of the Marble
    if not options or options.bonus_arc_chapters>1:
        #Normal
        locations+=(
            MIUUltraLocation("Ribbon Complete", Regions.ba2, "ribbon_v2-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Castle Chaos Complete", Regions.ba2, "castlechaos-c", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Thread the Needle Complete", Regions.ba2, "threadNeedle-c", lambda state: state.has_all({'Super Jump', 'Boost', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Gordian Complete", Regions.ba2, "gordian_mayhem-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Bumper Invasion Complete", Regions.ba2, "bumperinvasion-c", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Bash-tion Complete", Regions.ba2, "bash_tion-c", lambda state: state.has_all({'Super Jump', 'Boost', 'Feather Fall'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Runout Complete", Regions.ba2, "runout-c", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Archiarchy Complete", Regions.ba2, "archiarchy-c", lambda state: state.has('Feather Fall', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Crystalline Matrix Complete", Regions.ba2, "crystalmatrix-c", lambda state: state.has_all({'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Stayin' Alive Complete", Regions.ba2, "stayinalive_mayhem-c", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("Medieval Machinations Complete", Regions.ba2, "machinations_update-c", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            MIUUltraLocation("The Pit of Despair Complete", Regions.ba2, "pitofdespair-c", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
        )
        #Silver
        if not options or options.medal_types>0:
            locations+=(
                MIUUltraLocation("Ribbon Silver Medal", Regions.ba2, "ribbon_v2-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Castle Chaos Silver Medal", Regions.ba2, "castlechaos-s", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Thread the Needle Silver Medal", Regions.ba2, "threadNeedle-s", lambda state: state.has_all({'Super Jump', 'Boost', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Gordian Silver Medal", Regions.ba2, "gordian_mayhem-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bumper Invasion Silver Medal", Regions.ba2, "bumperinvasion-s", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bash-tion Silver Medal", Regions.ba2, "bash_tion-s", lambda state: state.has_all({'Super Jump', 'Boost', 'Feather Fall'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Runout Silver Medal", Regions.ba2, "runout-s", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Archiarchy Silver Medal", Regions.ba2, "archiarchy-s", lambda state: state.has('Feather Fall', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Crystalline Matrix Silver Medal", Regions.ba2, "crystalmatrix-s", lambda state: state.has_all({'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Stayin' Alive Silver Medal", Regions.ba2, "stayinalive_mayhem-s", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Medieval Machinations Silver Medal", Regions.ba2, "machinations_update-s", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("The Pit of Despair Silver Medal", Regions.ba2, "pitofdespair-s", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            )
        #Gold
        if not options or options.medal_types>1:
            locations+=(
                MIUUltraLocation("Ribbon Gold Medal", Regions.ba2, "ribbon_v2-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Castle Chaos Gold Medal", Regions.ba2, "castlechaos-g", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Thread the Needle Gold Medal", Regions.ba2, "threadNeedle-g", lambda state: state.has_all({'Super Jump', 'Boost', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Gordian Gold Medal", Regions.ba2, "gordian_mayhem-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bumper Invasion Gold Medal", Regions.ba2, "bumperinvasion-g", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bash-tion Gold Medal", Regions.ba2, "bash_tion-g", lambda state: state.has_all({'Super Jump', 'Boost', 'Feather Fall'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Runout Gold Medal", Regions.ba2, "runout-g", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Archiarchy Gold Medal", Regions.ba2, "archiarchy-g", lambda state: state.has('Feather Fall', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Crystalline Matrix Gold Medal", Regions.ba2, "crystalmatrix-g", lambda state: state.has_all({'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Stayin' Alive Gold Medal", Regions.ba2, "stayinalive_mayhem-g", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Medieval Machinations Gold Medal", Regions.ba2, "machinations_update-g", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("The Pit of Despair Gold Medal", Regions.ba2, "pitofdespair-g", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            )
        #Diamond
        if not options or options.medal_types>2:
            locations+=(
                MIUUltraLocation("Ribbon Diamond Medal", Regions.ba2, "ribbon_v2-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Castle Chaos Diamond Medal", Regions.ba2, "castlechaos-d", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Thread the Needle Diamond Medal", Regions.ba2, "threadNeedle-d", lambda state: state.has_all({'Super Jump', 'Boost', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Gordian Diamond Medal", Regions.ba2, "gordian_mayhem-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bumper Invasion Diamond Medal", Regions.ba2, "bumperinvasion-d", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Bash-tion Diamond Medal", Regions.ba2, "bash_tion-d", lambda state: state.has_all({'Super Jump', 'Boost', 'Feather Fall'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Runout Diamond Medal", Regions.ba2, "runout-d", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Archiarchy Diamond Medal", Regions.ba2, "archiarchy-d", lambda state: state.has('Feather Fall', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Crystalline Matrix Diamond Medal", Regions.ba2, "crystalmatrix-d", lambda state: state.has_all({'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Stayin' Alive Diamond Medal", Regions.ba2, "stayinalive_mayhem-d", lambda state: logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("Medieval Machinations Diamond Medal", Regions.ba2, "machinations_update-d", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
                MIUUltraLocation("The Pit of Despair Diamond Medal", Regions.ba2, "pitofdespair-d", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba2.chapter_number, state)),
            )

    #Keep Your Cool
    if not options or options.bonus_arc_chapters>2:
        #Normal
        locations+=(
            MIUUltraLocation("Contraption Complete", Regions.ba3, "contraption-c", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Uphill Both Ways Complete", Regions.ba3, "uphill-c", lambda state: state.has_all({'Gravity Surfaces', 'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Retrograde Rally Complete", Regions.ba3, "retro-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Warp Core Complete", Regions.ba3, "warpcore-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Cross Traffic Complete", Regions.ba3, "bash_faster-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Prime Complete", Regions.ba3, "prime_v2-c", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Halfpipe Heaven Complete", Regions.ba3, "halfpipeheaven_v2-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Wanderlust Complete", Regions.ba3, "wanderlust_v2-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Boomerang Complete", Regions.ba3, "boomerang-c", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Kendama Complete", Regions.ba3, "kendama-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Cirrus Complete", Regions.ba3, "cirrus_update-c", lambda state: state.has_all({'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            MIUUltraLocation("Zenith Complete", Regions.ba3, "zenith-c", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
        )
        #Silver
        if not options or options.medal_types>0:
            locations+=(
                MIUUltraLocation("Contraption Silver Medal", Regions.ba3, "contraption-s", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Uphill Both Ways Silver Medal", Regions.ba3, "uphill-s", lambda state: state.has_all({'Gravity Surfaces', 'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Retrograde Rally Silver Medal", Regions.ba3, "retro-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Warp Core Silver Medal", Regions.ba3, "warpcore-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cross Traffic Silver Medal", Regions.ba3, "bash_faster-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Prime Silver Medal", Regions.ba3, "prime_v2-s", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Halfpipe Heaven Silver Medal", Regions.ba3, "halfpipeheaven_v2-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Wanderlust Silver Medal", Regions.ba3, "wanderlust_v2-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Boomerang Silver Medal", Regions.ba3, "boomerang-s", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Kendama Silver Medal", Regions.ba3, "kendama-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cirrus Silver Medal", Regions.ba3, "cirrus_update-s", lambda state: state.has_all({'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Zenith Silver Medal", Regions.ba3, "zenith-s", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            )
        #Gold
        if not options or options.medal_types>1:
            locations+=(
                MIUUltraLocation("Contraption Gold Medal", Regions.ba3, "contraption-g", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Uphill Both Ways Gold Medal", Regions.ba3, "uphill-g", lambda state: state.has_all({'Gravity Surfaces', 'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Retrograde Rally Gold Medal", Regions.ba3, "retro-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Warp Core Gold Medal", Regions.ba3, "warpcore-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cross Traffic Gold Medal", Regions.ba3, "bash_faster-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Prime Gold Medal", Regions.ba3, "prime_v2-g", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Halfpipe Heaven Gold Medal", Regions.ba3, "halfpipeheaven_v2-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Wanderlust Gold Medal", Regions.ba3, "wanderlust_v2-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Boomerang Gold Medal", Regions.ba3, "boomerang-g", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Kendama Gold Medal", Regions.ba3, "kendama-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cirrus Gold Medal", Regions.ba3, "cirrus_update-g", lambda state: state.has_all({'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Zenith Gold Medal", Regions.ba3, "zenith-g", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            )
        #Diamond
        if not options or options.medal_types>2:
            locations+=(
                MIUUltraLocation("Contraption Diamond Medal", Regions.ba3, "contraption-d", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Uphill Both Ways Diamond Medal", Regions.ba3, "uphill-d", lambda state: state.has_all({'Gravity Surfaces', 'Boost', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Retrograde Rally Diamond Medal", Regions.ba3, "retro-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Warp Core Diamond Medal", Regions.ba3, "warpcore-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cross Traffic Diamond Medal", Regions.ba3, "bash_faster-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Prime Diamond Medal", Regions.ba3, "prime_v2-d", lambda state: logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Halfpipe Heaven Diamond Medal", Regions.ba3, "halfpipeheaven_v2-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Wanderlust Diamond Medal", Regions.ba3, "wanderlust_v2-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Boomerang Diamond Medal", Regions.ba3, "boomerang-d", lambda state: state.has('Bounce Surfaces', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Kendama Diamond Medal", Regions.ba3, "kendama-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Cirrus Diamond Medal", Regions.ba3, "cirrus_update-d", lambda state: state.has_all({'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
                MIUUltraLocation("Zenith Diamond Medal", Regions.ba3, "zenith-d", lambda state: state.has_all({'Bounce Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba3.chapter_number, state)),
            )

    #Challenge Accepted
    if not options or options.bonus_arc_chapters>3:
        #Normal
        locations+=(
            MIUUltraLocation("All Downhill From Here Complete", Regions.ba4, "alldownhill-c", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Danger Zone Complete", Regions.ba4, "dangerzone-c", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Olympus Complete", Regions.ba4, "olympus-c", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Head in the Clouds Complete", Regions.ba4, "headintheclouds_mayhem-c", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Centripetal Force Complete", Regions.ba4, "centripitalforce-c", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Slick Shtick Complete", Regions.ba4, "slickshtick-c", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Network Complete", Regions.ba4, "network-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Radius Complete", Regions.ba4, "radius-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Escalation Complete", Regions.ba4, "escalation-c", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Torque Complete", Regions.ba4, "torque-c", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Tangle Complete", Regions.ba4, "tangle_mayhem-c", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            MIUUltraLocation("Stratosphere Complete", Regions.ba4, "stratosphere-c", lambda state: state.has_all({'Boost', 'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
        )
        #Silver
        if not options or options.medal_types>0:
            locations+=(
                MIUUltraLocation("All Downhill From Here Silver Medal", Regions.ba4, "alldownhill-s", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Danger Zone Silver Medal", Regions.ba4, "dangerzone-s", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Olympus Silver Medal", Regions.ba4, "olympus-s", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Head in the Clouds Silver Medal", Regions.ba4, "headintheclouds_mayhem-s", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Centripetal Force Silver Medal", Regions.ba4, "centripitalforce-s", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Slick Shtick Silver Medal", Regions.ba4, "slickshtick-s", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Network Silver Medal", Regions.ba4, "network-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Radius Silver Medal", Regions.ba4, "radius-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Escalation Silver Medal", Regions.ba4, "escalation-s", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Torque Silver Medal", Regions.ba4, "torque-s", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Tangle Silver Medal", Regions.ba4, "tangle_mayhem-s", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Stratosphere Silver Medal", Regions.ba4, "stratosphere-s", lambda state: state.has_all({'Boost', 'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            )
        #Gold
        if not options or options.medal_types>1:
            locations+=(
                MIUUltraLocation("All Downhill From Here Gold Medal", Regions.ba4, "alldownhill-g", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Danger Zone Gold Medal", Regions.ba4, "dangerzone-g", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Olympus Gold Medal", Regions.ba4, "olympus-g", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Head in the Clouds Gold Medal", Regions.ba4, "headintheclouds_mayhem-g", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Centripetal Force Gold Medal", Regions.ba4, "centripitalforce-g", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Slick Shtick Gold Medal", Regions.ba4, "slickshtick-g", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Network Gold Medal", Regions.ba4, "network-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Radius Gold Medal", Regions.ba4, "radius-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Escalation Gold Medal", Regions.ba4, "escalation-g", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Torque Gold Medal", Regions.ba4, "torque-g", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Tangle Gold Medal", Regions.ba4, "tangle_mayhem-g", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Stratosphere Gold Medal", Regions.ba4, "stratosphere-g", lambda state: state.has_all({'Boost', 'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            )
        #Diamond
        if not options or options.medal_types>2:
            locations+=(
                MIUUltraLocation("All Downhill From Here Diamond Medal", Regions.ba4, "alldownhill-d", lambda state: state.has('Gravity Surfaces', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Danger Zone Diamond Medal", Regions.ba4, "dangerzone-d", lambda state: state.has_all({'Gravity Surfaces', 'Boost'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Olympus Diamond Medal", Regions.ba4, "olympus-d", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Head in the Clouds Diamond Medal", Regions.ba4, "headintheclouds_mayhem-d", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Centripetal Force Diamond Medal", Regions.ba4, "centripitalforce-d", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Slick Shtick Diamond Medal", Regions.ba4, "slickshtick-d", lambda state: logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Network Diamond Medal", Regions.ba4, "network-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Radius Diamond Medal", Regions.ba4, "radius-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Escalation Diamond Medal", Regions.ba4, "escalation-d", lambda state: state.has('Super Jump', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Torque Diamond Medal", Regions.ba4, "torque-d", lambda state: state.has('Boost', player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Tangle Diamond Medal", Regions.ba4, "tangle_mayhem-d", lambda state: state.has_all({'Gravity Surfaces', 'Super Jump'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
                MIUUltraLocation("Stratosphere Diamond Medal", Regions.ba4, "stratosphere-d", lambda state: state.has_all({'Boost', 'Feather Fall', 'Gravity Surfaces'}, player) and logic.has_gold_medals(Regions.ba4.chapter_number, state)),
            )
        

    return locations
