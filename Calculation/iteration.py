from dataclasses import dataclass

from interval import Interval

@dataclass
class Iteration:
    number: int
    interval: Interval
    average: float
    calculation_average: float

    def __init__(self, number: int, interval: Interval, average: float, calculation_average: float) -> None:
        self.number = number
        self.interval = interval
        self.average = average
        self.calculation_average = calculation_average