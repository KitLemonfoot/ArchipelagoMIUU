from dataclasses import dataclass
from Options import Toggle, Choice, Range, DeathLink, PerGameCommonOptions, OptionGroup

class EnableBlast(Toggle):
    """
    Allow the ability to Blast behind a useful item.
    NOTE: Logic is NOT written with Blast in mind.
    """
    display_name = "Enable Blast"

class MIUUDeathLink(DeathLink):
    """
    When you die by falling out of bounds, everyone dies. The reverse is also true.
    """

class DeathLinkAmnesty(Range):
    """
    How many deaths it takes to send a Death Link.
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 20
    default = 5

class TreasureBoxSanity(Toggle):
    """
    Enables collecting Treasure Boxes as checks.
    NOTE: Some Treasure Boxes require intentional death to collect. Be mindful of this if you are enabling Death Link.
    """
    display_name = "Treasureboxsanity"

class MedalsPerChapter(Range):
    """
    Determine how many Completion Medals are needed to unlock each chapter.
    (Chapter 2 will always require 5 medals to unlock.)
    """
    display_name = "Medals Per Chapter"
    range_start = 5
    range_end = 8
    default = 8

class ExtraMedals(Range):
    """
    Determine how many extra Completion Medals per enabled chapter to add to the item pool.
    """
    display_name = "Extra Medals"
    range_start = 0
    range_end = 5
    default = 3

class MedalTypes(Choice):
    """
    Choose which types of level completions to count as checks.
    Enabling a higher tier medal will also enable all tiers below it.
    """
    display_name = "Medal Types"
    option_normal = 0
    option_silver = 1
    option_gold = 2
    option_diamond = 3
    default = 1

class BonusArcChapters(Choice):
    """
    Determine whether or not to include chapters in the Bonus Arc as part of your multiworld.
    Bonus Arc chapters will require Gold Completion Medal items to access, which will be added to the multiworld if this option is enabled.
    All other unlock criteria, such as medals available and how many medals per chapter unlock, will be the same as chapters in the Ultra Arc.
    NOTE: This option will automatically be disabled if you are not playing with Gold Medal completions or above.
    """
    display_name = "Bonus Arc Chapters"
    option_disabled = 0
    option_keep_on_rolling = 1
    option_the_way_of_the_marble = 2
    option_keep_your_cool = 3
    option_challenge_accepted = 4
    default = 0

class FinalChapter(Choice):
    """
    Choose which chapter you would like to be your last logical chapter.
    The final level in this chapter will be your goal level.
    """
    display_name = "Final Chapter"
    option_focus_on_flow = 0
    option_kick_it_up_a_notch = 1
    option_show_me_what_you_got = 2
    option_play_for_keeps = 3
    default = 0

class TrapFillPercentage(Range):
    """
    Determine a percentage of junk items in the item pool to replace with traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class AddTimeTrapWeight(Range):
    """
    This trap will instantly add 5 seconds to your current time.
    """
    display_name = "Add Time Trap Weight"
    range_start = 0
    range_end = 100
    default = 0

class CosmeticShuffleTrapWeight(Range):
    """
    This trap will randomly shuffle what cosmetics your marble is wearing.
    """
    display_name = "Add Time Trap Weight"
    range_start = 0
    range_end = 100
    default = 0

@dataclass
class MIUUltraOptions(PerGameCommonOptions):
    final_chapter: FinalChapter
    bonus_arc_chapters: BonusArcChapters
    medal_types: MedalTypes
    medals_per_chapter: MedalsPerChapter
    extra_medals: ExtraMedals
    treasureboxsanity: TreasureBoxSanity
    enable_blast: EnableBlast
    death_link: MIUUDeathLink
    death_link_amnesty: DeathLinkAmnesty
    trap_percent: TrapFillPercentage
    addtimetrap_weight: AddTimeTrapWeight
    cosmetictrap_weight: CosmeticShuffleTrapWeight


miuu_option_groups = [
    OptionGroup("Chapter Settings", [
        MedalTypes,
        FinalChapter,
        BonusArcChapters
    ]),
    OptionGroup("Medal Settings", [
        MedalsPerChapter,
        ExtraMedals
    ]),
    OptionGroup("Trap Settings", [
        TrapFillPercentage,
        AddTimeTrapWeight,
        CosmeticShuffleTrapWeight
    ]),
    OptionGroup("Game Settings", [
        EnableBlast,
        TreasureBoxSanity,
        MIUUDeathLink,
        DeathLinkAmnesty
    ]),

]
