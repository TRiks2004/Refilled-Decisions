from dataclasses import dataclass
from typing import Literal

@dataclass
class Interval:
    interval_start: float
    interval_end: float

    increasing: Literal[True, False, None] = None