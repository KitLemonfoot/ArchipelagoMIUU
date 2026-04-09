from typing import Dict, Any
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial, Region, Location, Entrance, Item, ItemClassification
from .Options import MIUUltraOptions, Choice
from .Items import base_id, item_list, ItemType
from .Locations import get_location_data
from .Regions import Regions
import logging

class MIUUltraWeb(WebWorld):
    theme = "ice"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Marble It Up! Ultra game for use with Archipelago.",
        "English",
        "miuultra_en.md",
        "miuultra/en",
        ["KitLemonfoot"]
    )]

class MIUUltraItem(Item):
    game = "Marble It Up! Ultra"

class MIUUltraLocation(Location):
    game = "Marble It Up! Ultra"

class MIUUltraWorld(World):
    """
    Marble It Up! Ultra is a marble platforming game made by the minds behind the Marble Blast series. 
    Roll through an extensive single-player campaign filled with dangerous obstacles, mind-bending paths, shifting gravity, bouncy floors, and potent power-ups.
    """

    game = "Marble It Up! Ultra"

    options_dataclass = MIUUltraOptions
    options: MIUUltraOptions
    web = MIUUltraWeb()

    item_name_to_id = {item.name: (base_id + index) for index, item in enumerate(item_list)}
    location_name_to_id = {loc.name: (base_id + index) for index, loc in enumerate(get_location_data(-1, None))}

    def __init__(self, multiworld, player):
        super(MIUUltraWorld, self).__init__(multiworld, player)
        self.game_id_to_long: Dict[str, int] = {}

    def generate_early(self) -> None:
        # Bonus arc + normal difficulty = 33% failed generation rate. Sorry.
        if self.options.medal_types.value < 2 and self.options.bonus_arc_chapters > 0:
            logging.warning(f"Player {self.player_name} tried to play with Bonus Arc chapters without adequate medal requirements. Disabling.")
            self.options.bonus_arc_chapters.value = 0

    def create_item(self, name:str) -> MIUUltraItem:
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id
        classification = item_list[id].classification
        return MIUUltraItem(name, classification, item_id, self.player)
    
    def create_regions(self):

        player = self.player
        multiworld = self.multiworld

        menu = Region("Menu", player, multiworld)
        for r in Regions.all_regions:
            multiworld.regions += [Region(r.full_name, player, multiworld)]
            menu.add_exits({r.full_name})
        multiworld.regions.append(menu)

        for loc in get_location_data(player, self.options):
            id = self.location_name_to_id[loc.name]
            self.game_id_to_long[loc.game_id] = id
            region = self.get_region(loc.region.full_name)
            location = MIUUltraLocation(player, loc.name, id, region)
            if loc.logic:
                location.access_rule = loc.logic
            region.locations.append(location)

        if self.options.final_chapter.value == 0:
            victory = self.get_location("Overclocked Complete")
        if self.options.final_chapter.value == 1:
            victory = self.get_location("Citadel Complete")
        if self.options.final_chapter.value == 2:
            victory = self.get_location("Mobius Madness Complete")
        if self.options.final_chapter.value == 3:
            victory = self.get_location("Apogee Complete")
        victory.place_locked_item(self.create_item("Final Level Complete"))
        multiworld.completion_condition[player] = lambda state: state.has("Final Level Complete", player)

    def create_items(self):
        pool=[]

        #Handle powerups automatically.
        #Medals and other items are handled manually.
        for item in item_list:
            if(item.itemType != ItemType.Powerup):
                continue
            pool.append(self.create_item(item.name))

        # Handle adding completion medals.
        medals = 5 + ((self.options.final_chapter.value+1)*self.options.medals_per_chapter)
        for _ in range(medals):
            pool.append(self.create_item("Completion Medal"))

        # Handle adding gold medals.
        if self.options.bonus_arc_chapters > 0:
            goldMedals = self.options.medals_per_chapter.value * self.options.bonus_arc_chapters.value
            for _ in range(goldMedals):
                pool.append(self.create_item("Gold Completion Medal"))

        #Handle adding extra medals.
        extraMedals = self.options.extra_medals.value * (self.options.final_chapter.value+3)
        remaining = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
        if remaining < extraMedals:
            logging.warning(f"Player {self.player_name} had more extra medals defined in the YAML ({extraMedals}) than remaining available locations ({remaining}). Reducing.")
            extraMedals = remaining
        for _ in range(extraMedals):
            pool.append(self.create_item("Completion Medal"))

        #Handle adding extra gold medals.
        extraGold = self.options.extra_medals.value * self.options.bonus_arc_chapters.value
        if(extraGold>0):
            remaining = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
            if remaining < extraMedals:
                logging.warning(f"Player {self.player_name} had more extra medals defined in the YAML ({extraMedals}) than remaining available locations ({remaining}). Reducing.")
                extraMedals = remaining
            for _ in range(extraGold):
                pool.append(self.create_item("Gold Completion Medal"))

        # Handle filler items.
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
        for _ in range(junk):
            pool.append(self.create_item("5 Second Time Freeze"))

        self.multiworld.itempool += pool

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "version": "0.1.0",
            "locations": self.game_id_to_long,
            "MedalsPerChapter": self.options.medals_per_chapter.value,
            "MedalTypes": self.options.medal_types.value,
            "FinalChapter": self.options.final_chapter.value,
            "BonusArcChapters": self.options.bonus_arc_chapters.value,
            "death_link": bool(self.options.death_link),
            "death_link_amnesty": self.options.death_link_amnesty.value
        }
        return slot_data

