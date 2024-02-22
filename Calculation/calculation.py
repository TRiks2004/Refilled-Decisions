import math
import copy

from typing import List
from types import CodeType

from Calculation.interval import Interval
from Calculation.answer import AnswerSolutionsByIterations
from Calculation.iteration import Iteration

class Calculation:

    def __init__(self, equation_string: str, intervals: List[Interval], accuracy: int) -> None:
        self.equation_string = equation_string
        self.intervals = intervals
        self.accuracy = accuracy

        self.equation_compile = self.equation_parse(self.equation_string)
        self.definitions_monotony()

    def definitions_monotony(self):
        for interval in self.intervals:
            
            if (self.calculate(interval.interval_start) * self.calculate(interval.interval_end) < 0):
                interval.increasing = (
                    self.calculate(interval.interval_start) < 0 and 
                    self.calculate(interval.interval_end) > 0
                )
                continue
                
            interval.increasing = None
    
    def equation_parse(self, str: str) -> CodeType: 
        return compile(str, "<string>", "eval")

    def calculate(self, x: int | float) -> int | float:
        return eval(self.equation_compile)
    

    def solutions_by_iterations(self) -> List[AnswerSolutionsByIterations]:
        answerSolutionsByIterationsList = []

        for interval in self.intervals:
            inter = copy.copy(interval)
            counter = 0

            iterations = []

            while True:
                average = (inter.interval_start + inter.interval_end) / 2
                val = self.calculate(average)

                iteration = Iteration(
                    number=counter,
                    interval=copy.copy(inter),
                    average=average,
                    calculation_average=val
                )


                if inter.increasing:
                    if val > 0: inter.interval_end = average
                    elif val < 0: inter.interval_start = average
                else:
                    if val > 0: inter.interval_start = average
                    elif val < 0: inter.interval_end = average

                inter = Interval(
                    inter.interval_start, inter.interval_end, inter.increasing
                )
                
                iterations.append(iteration)

                counter += 1

                if math.fabs(inter.interval_start - inter.interval_end) < float("0." + "0" * (self.accuracy - 1) + "1" ):
                    break
            
            answerSolutionsByIterations = AnswerSolutionsByIterations(
                original_interval=interval,
                iterations=iterations,
                root=round(average, self.accuracy)
            )

            answerSolutionsByIterationsList.append(answerSolutionsByIterations)

        return answerSolutionsByIterationsList


