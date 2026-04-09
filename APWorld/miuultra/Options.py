from dataclasses import dataclass
from Options import Toggle, Choice, Range, DeathLink, PerGameCommonOptions

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
    default = 10

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

@dataclass
class MIUUltraOptions(PerGameCommonOptions):
    death_link: MIUUDeathLink
    death_link_amnesty: DeathLinkAmnesty
    final_chapter: FinalChapter
    medals_per_chapter: MedalsPerChapter
    extra_medals: ExtraMedals
    medal_types: MedalTypes
    bonus_arc_chapters: BonusArcChapters