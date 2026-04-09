from typing import Optional
from BaseClasses import CollectionState
from .Options import MIUUltraOptions

class MIUUExtraLogic:
    player:int
    options:MIUUltraOptions

    def __init__(self, player:int, options:Optional[MIUUltraOptions]):
        self.player = player
        self.options = options

    def has_medals(self, chapternumber, state:CollectionState) -> bool:
        #Handle no options (first pass) or Chapter 1.
        if not self.options or chapternumber < 2:
            return True
        #Handle permanent 5 medals for Chapter 2.
        if chapternumber==2:
            return state.has('Completion Medal', self.player, 5)
        #Calculate required medal count for chapters 3-6.
        medals = 5 + (self.options.medals_per_chapter.value * (chapternumber-2))
        return state.has('Completion Medal', self.player, medals)
    
    def has_gold_medals(self, chapternumber, state:CollectionState) -> bool:
        if not self.options:
            return True
        goldmedals = self.options.medals_per_chapter.value * chapternumber
        return state.has('Gold Completion Medal', self.player, goldmedals)

        
        