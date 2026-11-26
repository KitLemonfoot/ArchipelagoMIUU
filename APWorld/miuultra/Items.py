from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
from BaseClasses import ItemClassification
from .Levels import level_info_dict
from .Checkpoints import checkpoint_dict

#Changing the way games are made and played.
base_id = 12506

class ItemType(Enum):
    Medal = 0
    Powerup = 1
    Gem = 2
    Checkpoint = 3
    Filler = 4
    Trap = 5
    End = 6

@dataclass
class MIUUltraItem:
    name: str
    classification: ItemClassification
    itemType: ItemType
    extraData: Optional[str] = None

# Item List
item_list: List[MIUUltraItem] = [
    MIUUltraItem("Super Jump", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Boost", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Feather Fall", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Gravity Surfaces", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Bounce Surfaces", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Blue Moving Platforms", ItemClassification.progression, ItemType.Powerup),
    MIUUltraItem("Blast", ItemClassification.useful, ItemType.Powerup),

    #Medals
    MIUUltraItem("Completion Medal", ItemClassification.progression_deprioritized, ItemType.Medal),
    MIUUltraItem("Gold Completion Medal", ItemClassification.progression_deprioritized, ItemType.Medal),

    #Filler
    MIUUltraItem("5 Second Time Freeze", ItemClassification.filler, ItemType.Filler),

    #Traps
    MIUUltraItem("Time Add Trap", ItemClassification.trap, ItemType.Trap),
    MIUUltraItem("Cosmetic Shuffle Trap", ItemClassification.trap, ItemType.Trap),

    MIUUltraItem("Ultra Arc Complete", ItemClassification.progression_skip_balancing, ItemType.End),
    MIUUltraItem("Bonus Arc Complete", ItemClassification.progression_skip_balancing, ItemType.End),
]

world_checkpoint_list: List[MIUUltraItem] = [
    MIUUltraItem("Chapter 1: Get Moving - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u1"),
    MIUUltraItem("Chapter 2: The Subtle Joy of Rolling - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u2"),
    MIUUltraItem("Chapter 3: Focus on Flow - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u3"),
    MIUUltraItem("Chapter 4: Kick It Up A Notch - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u4"),
    MIUUltraItem("Chapter 5: Show Me What You Got - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u5"),
    MIUUltraItem("Chapter 6: Play for Keeps - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "u6"),
    MIUUltraItem("Bonus 1: Keep on Rolling - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "b1"),
    MIUUltraItem("Bonus 2: The Way of the Marble - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "b2"),
    MIUUltraItem("Bonus 3: Keep Your Cool - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "b3"),
    MIUUltraItem("Bonus 4: Challenge Accepted - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, "b4"),
]

# Generate the level checkpoint list for items.
def getLevelCheckpointList():
    level_checkpoint_list = []
    for lvl in level_info_dict.keys():
        if lvl in checkpoint_dict.keys():
            level_checkpoint_list.append(MIUUltraItem(f"{level_info_dict[lvl].name} - Checkpoint Access", ItemClassification.useful, ItemType.Checkpoint, lvl))
    return level_checkpoint_list

def getFullItemList():
    return item_list + world_checkpoint_list + getLevelCheckpointList()
