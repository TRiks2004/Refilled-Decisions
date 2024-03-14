from typing import Tuple
from typing import Iterable, TypeVar, Generic, TypeAlias

from iteration import IterationBisectionMethod, IterationChordMethod, IterationNewtonMethod

IterationMethod = TypeVar('IterationMethod')  # Define a generic type variable

class Answer(Generic[IterationMethod], Tuple):
    def __init__(self, iterations: Iterable[IterationMethod], answer: float) -> None:
        self.iterations = iterations
        self.answer = answer


AnswerBisectionMethod: TypeAlias = Answer[IterationBisectionMethod]
AnswerChordMethod: TypeAlias = Answer[IterationChordMethod]
AnswerNewtonMethod: TypeAlias = Answer[IterationNewtonMethod]


class AnswerBisectionMethod(AnswerBisectionMethod):
    def __init__(self, iterations: AnswerBisectionMethod, answer: float) -> None:
        super().__init__(iterations, answer)

class AnswerChordMethod(AnswerChordMethod):
    def __init__(self, iterations: AnswerChordMethod, answer: float) -> None:
        super().__init__(iterations, answer)

class AnswerNewtonMethod(AnswerNewtonMethod):
    def __init__(self, iterations: AnswerNewtonMethod, answer: float) -> None:
        super().__init__(iterations, answer)
