from typing import List
from dataclasses import dataclass

@dataclass
class MIUUltraRegion:
    short_name: str
    full_name: str
    chapter_number: int

class Regions:
    ch1 = MIUUltraRegion("ch1", "Get Moving", 1)
    ch2 = MIUUltraRegion("ch2", "The Subtle Joy of Rolling", 2)
    ch3 = MIUUltraRegion("ch3", "Focus on Flow", 3)
    ch4 = MIUUltraRegion("ch4", "Kick It Up a Notch", 4)
    ch5 = MIUUltraRegion("ch5", "Show Me What You Got", 5)
    ch6 = MIUUltraRegion("ch6", "Play for Keeps", 6)
    ba1 = MIUUltraRegion("ba1", "Keep on Rolling", 1)
    ba2 = MIUUltraRegion("ba2", "The Way of the Marble", 2)
    ba3 = MIUUltraRegion("ba3", "Keep Your Cool", 3)
    ba4 = MIUUltraRegion("ba4", "Challenge Accepted", 4)

    all_regions: List[MIUUltraRegion] = [
        ch1, ch2, ch3, ch4, ch5, ch6, ba1, ba2, ba3, ba4
    ]
