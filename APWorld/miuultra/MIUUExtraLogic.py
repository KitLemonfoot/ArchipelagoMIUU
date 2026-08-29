from typing import Optional
from .Options import MIUUltraOptions
from rule_builder.rules import Rule, Has, True_

class MIUUExtraLogic:
    player:int
    options:MIUUltraOptions

    def __init__(self, player:int, options:Optional[MIUUltraOptions]):
        self.player = player
        self.options = options

    def has_medals(self, chapternumber) -> Rule:
        #Handle no options (first pass) or Chapter 1.
        if not self.options or chapternumber < 2:
            return True_()
        #Handle permanent 5 medals for Chapter 2.
        if chapternumber==2:
            return Has("Completion Medal", count=5)
        #Calculate required medal count for chapters 3-6.
        medals = 5 + (self.options.medals_per_chapter.value * (chapternumber-2))
        return Has("Completion Medal", count=medals)

    def has_gold_medals(self, chapternumber) -> Rule:
        if not self.options or chapternumber < 2:
            return True_()
        goldmedals = self.options.medals_per_chapter.value * (chapternumber - 1)
        return Has("Gold Completion Medal", count=goldmedals)

    def has_all_gems(self, levelname, gemamount) -> Rule:
        if not self.options:
            return True_()
        itemname = levelname + " Gem"
        return Has(itemname, count=gemamount)
