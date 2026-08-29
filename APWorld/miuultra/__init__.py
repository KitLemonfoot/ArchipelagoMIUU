from typing import Dict, Any
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial, Region, Location, Entrance, Item, ItemClassification
from .Options import MIUUltraOptions, miuu_option_groups
from .Items import base_id, item_list, ItemType
from .Locations import get_location_data
from .Regions import Regions
import logging
import rule_builder

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
    option_groups = miuu_option_groups

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
        # Make sure enough chapters are selected in the chosen goal arc(s)
        if self.options.goal_arc.value in [0, 2] and self.options.ultra_arc_chapters.value < 3:
            logging.warning(f"Player {self.player_name} tried to have an Ultra Arc goal without adequate chapters. Enabling enough chapters.")
            self.options.ultra_arc_chapters.value = 3
        if self.options.goal_arc.value in [1, 2] and self.options.bonus_arc_chapters.value < 2:
            logging.warning(f"Player {self.player_name} tried to have a Bonus Arc goal without adequate chapters. Enabling enough chapters.")
            self.options.bonus_arc_chapters.value = 2

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
            self.set_rule(location, loc.logic)
            region.locations.append(location)

        goal_items = []

        if self.options.goal_arc.value in [0, 2]:
            if self.options.ultra_arc_chapters.value == 3:
                ultra_victory = self.get_location("Overclocked Complete")
            if self.options.ultra_arc_chapters.value == 4:
                ultra_victory = self.get_location("Citadel Complete")
            if self.options.ultra_arc_chapters.value == 5:
                ultra_victory = self.get_location("Mobius Madness Complete")
            if self.options.ultra_arc_chapters.value == 6:
                ultra_victory = self.get_location("Apogee Complete")
            ultra_victory.place_locked_item(self.create_item("Ultra Arc Complete"))
            goal_items.append("Ultra Arc Complete")

        if self.options.goal_arc.value in [1, 2]:
            if self.options.bonus_arc_chapters.value == 2:
                bonus_victory = self.get_location("The Pit of Despair Complete")
            if self.options.bonus_arc_chapters.value == 3:
                bonus_victory = self.get_location("Zenith Complete")
            if self.options.bonus_arc_chapters.value == 4:
                bonus_victory = self.get_location("Stratosphere Complete")
            bonus_victory.place_locked_item(self.create_item("Bonus Arc Complete"))
            goal_items.append("Bonus Arc Complete")

        multiworld.completion_condition[player] = lambda state: state.has_all(goal_items, player)

    def create_items(self):
        pool=[]

        #Handle powerups automatically.
        #Medals and other items are handled manually.
        for item in item_list:
            if(item.itemType != ItemType.Powerup):
                continue
            if(item.name == "Blast" and not self.options.enable_blast.value):
                continue
            pool.append(self.create_item(item.name))

        # Handle adding completion medals.
        if self.options.ultra_arc_chapters.value > 0:
            medals = 5 + ((self.options.ultra_arc_chapters.value - 1) * self.options.medals_per_chapter)
            for _ in range(medals):
                pool.append(self.create_item("Completion Medal"))

        # Handle adding gold medals.
        if self.options.bonus_arc_chapters > 0:
            goldMedals = self.options.medals_per_chapter.value * self.options.bonus_arc_chapters.value
            for _ in range(goldMedals):
                pool.append(self.create_item("Gold Completion Medal"))

        #Handle adding extra medals.
        extraMedals = self.options.extra_medals.value * self.options.ultra_arc_chapters.value
        if extraMedals > 0:
            remaining = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
            if remaining < extraMedals:
                logging.warning(f"Player {self.player_name} had more extra medals defined in the YAML ({extraMedals}) than remaining available locations ({remaining}). Reducing.")
                extraMedals = remaining
            for _ in range(extraMedals):
                pool.append(self.create_item("Completion Medal"))

        #Handle adding extra gold medals.
        extraGold = self.options.extra_medals.value * self.options.bonus_arc_chapters.value
        if extraGold > 0:
            remaining = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
            if remaining < extraGold:
                logging.warning(f"Player {self.player_name} had more extra medals defined in the YAML ({extraGold}) than remaining available locations ({remaining}). Reducing.")
                extraGold = remaining
            for _ in range(extraGold):
                pool.append(self.create_item("Gold Completion Medal"))

        # Handle junk items.
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
        trap: int = round(junk * (self.options.trap_percent / 100))
        #Check weights.
        if(self.options.addtimetrap_weight + self.options.cosmetictrap_weight == 0):
            trap = 0
        filler = junk - trap
        #Traps
        for _ in range(trap):
            pool.append(self.create_item(self.get_trap_name()))
        #Filler
        for _ in range(filler):
            pool.append(self.create_item("5 Second Time Freeze"))

        self.multiworld.itempool += pool

    def get_trap_name(self):
        trap_weights = {
            "Time Add Trap": self.options.addtimetrap_weight,
            "Cosmetic Shuffle Trap": self.options.cosmetictrap_weight
        }
        trap_items = list(trap_weights.keys())
        return self.multiworld.random.choices(trap_items, weights=[trap_weights[i] for i in trap_items])[0]


    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "version": "0.2.0",
            "locations": self.game_id_to_long,
            "MedalsPerChapter": self.options.medals_per_chapter.value,
            "MedalTypes": self.options.medal_types.value,
            "GoalArc": self.options.goal_arc.value,
            "UltraArcChapters": self.options.ultra_arc_chapters.value,
            "BonusArcChapters": self.options.bonus_arc_chapters.value,
            "EnableBlast": bool(self.options.enable_blast.value),
            "Treasureboxsanity": bool(self.options.treasureboxsanity.value),
            "death_link": bool(self.options.death_link),
            "death_link_amnesty": self.options.death_link_amnesty.value
        }
        return slot_data
