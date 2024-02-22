from typing import List

from interval import Interval
from iteration import Iteration


class Answer: ...

class AnswerSolutionsByIterations(Answer):
    original_interval: Interval
    iterations: List[Iteration]
    root: float

    def __init__(self, original_interval: Interval, iterations: List[Iteration], root: float) -> None:
        self.original_interval = original_interval
        self.iterations = iterations
        self.root = root