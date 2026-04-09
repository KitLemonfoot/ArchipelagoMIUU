from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
from BaseClasses import ItemClassification

#Changing the way games are made and played.
base_id = 12506

class ItemType(Enum):
    Medal = 0
    Powerup = 1
    Gem = 2
    Filler = 3
    Trap = 4
    End = 5

@dataclass
class MIUUltraItem:
    name: str
    classification: ItemClassification
    itemType: ItemType

# Item List
item_list: List[MIUUltraItem] = [
    MIUUltraItem("Super Jump", ItemClassification.progression, ItemType.Powerup), 
    MIUUltraItem("Boost", ItemClassification.progression, ItemType.Powerup), 
    MIUUltraItem("Feather Fall", ItemClassification.progression, ItemType.Powerup), 
    MIUUltraItem("Gravity Surfaces", ItemClassification.progression, ItemType.Powerup), 
    MIUUltraItem("Bounce Surfaces", ItemClassification.progression, ItemType.Powerup), 

    #Medals
    MIUUltraItem("Completion Medal", ItemClassification.progression_deprioritized, ItemType.Medal),
    MIUUltraItem("Gold Completion Medal", ItemClassification.progression_deprioritized, ItemType.Medal),

    #Filler
    MIUUltraItem("5 Second Time Freeze", ItemClassification.filler, ItemType.Filler),

    MIUUltraItem("Final Level Complete", ItemClassification.progression_skip_balancing, ItemType.End),
]
