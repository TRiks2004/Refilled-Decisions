from typing import Tuple
from interval import Interval

class Iteration(Tuple):
    pass
    
class IterationBisectionMethod(Iteration):
    
    def __init__(self, number: int, interval: Interval, average: float, calculation_average: float) -> None:
        
        self.number = number
        self.interval = interval
        self.average = average
        self.calculation_average = calculation_average
        
        super().__init__()

class IterationChordMethod(Iteration):
    
    def __init__(self, number: int, interval: Interval, interval_equation: Interval, calculation: float) -> None:
        self.number = number
        self.interval = interval
        self.interval_equation = interval_equation    
        self.calculation = calculation
        
        super().__init__()

class IterationNewtonMethod(Iteration):
    
    def __init__(self, number: int, end: float, equation_x: float, first_derivative_equation: float, calculation: float) -> None:
        self.number = number
        self.end = end
        self.equation_x = equation_x
        self.first_derivative_equation = first_derivative_equation
        self.calculation = calculation
