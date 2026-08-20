from typing import List, Optional, Callable
from BaseClasses import CollectionState
from dataclasses import dataclass
from .Levels import MIUULevel, level_info_dict
from .Regions import Regions, MIUUltraRegion
from .Options import MIUUltraOptions
from .MIUUExtraLogic import MIUUExtraLogic
from rule_builder.rules import Rule, Has, And, True_

@dataclass
class MIUUltraLocation:
    name: str
    region: MIUUltraRegion
    game_id: str
    logic: Rule

def get_location_data(player: Optional[int], options: Optional[MIUUltraOptions]):
    logic = MIUUExtraLogic(player, options)
    locations: List[MIUUltraLocation] = []

    for lvl in level_info_dict:
        level: MIUULevel = level_info_dict[lvl]

        #Should handle both arcs
        if (not options) or (level.homeRegion.short_name.startswith("ch") and options.final_chapter+3 >= level.homeRegion.chapter_number) or (level.homeRegion.short_name.startswith("ba") and options.bonus_arc_chapters >= level.homeRegion.chapter_number):
            #Base
            if(level.homeRegion.short_name.startswith("ch")):
                medalLogic = logic.has_medals(level.homeRegion.chapter_number)
            else:
                medalLogic = logic.has_gold_medals(level.homeRegion.chapter_number)
            lvlLogic = And(level.baseCompletionLogic, medalLogic)
            locations.append(
                MIUUltraLocation(level.name+" Complete", level.homeRegion, level.internalLevelId+"-c", lvlLogic)
            )
            #Silver
            if not options or options.medal_types>0:
                lvlLogic = And(level.baseCompletionLogic, level.higherCompletionLogic, medalLogic)
                locations.append(
                    MIUUltraLocation(level.name+" Silver Medal", level.homeRegion, level.internalLevelId+"-s", lvlLogic)
                )
            #Gold
            if not options or options.medal_types>1:
                locations.append(
                    MIUUltraLocation(level.name+" Gold Medal", level.homeRegion, level.internalLevelId+"-g", lvlLogic)
                )
            #Diamond
            if not options or options.medal_types>2:
                locations.append(
                    MIUUltraLocation(level.name+" Diamond Medal", level.homeRegion, level.internalLevelId+"-d", lvlLogic)
                )
            #Treasurebox
            if not options or options.treasureboxsanity:
                lvlLogic = And(level.baseCompletionLogic, level.treasureBoxLogic, medalLogic)
                locations.append(
                    MIUUltraLocation(level.name+" Treasure Box", level.homeRegion, level.internalLevelId+"-tb", lvlLogic)
                )
            continue

    return locations
