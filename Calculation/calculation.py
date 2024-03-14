from math import *


from typing import List

import asyncio

from typing import Iterable

from answer import (
    AnswerBisectionMethod, AnswerChordMethod, AnswerNewtonMethod
)

from equation import Equation
from interval import Interval

from iteration import (
    IterationBisectionMethod, IterationChordMethod, IterationNewtonMethod
)




class Calculation:

    def __init__(self, equation: Equation, interval: Interval, tol: float = 1e-6) -> None:
        self.equation = equation
        self.interval = interval
        self.tol = tol
        
    async def bisection_method(self) -> AnswerBisectionMethod:
        
        interval_end = self.interval.end
        interval_start = self.interval.start
        
        print(await self.equation(interval_start), await self.equation(interval_end))
        
        if await self.equation(interval_start) * await self.equation(interval_end) >= 0:
            print("Метод половинного деления не применим: функция не меняет знак на интервале [a, b].")
            return None

        iterationBisectionMethodList: List[IterationBisectionMethod] = []

        tol_int = len(f'{self.tol:f}'.split('.')[1])
        
        iter_count = 0
        while iter_count < 100000:
            avg = (interval_start + interval_end) / 2
               
            equation_avg = await self.equation(avg)    
                     
            iterationBisectionMethodList.append(
                IterationBisectionMethod(
                    number=iter_count, 
                    interval=Interval(
                        start=round(interval_start, tol_int), 
                        end=round(interval_end, tol_int)
                    ), 
                    average=round(avg, tol_int), 
                    calculation_average=round(equation_avg, tol_int)
                )
            )
            
            if abs(interval_end - interval_start) < self.tol or equation_avg == 0: 
                break
            
            if equation_avg * await self.equation(interval_start) < 0:
                interval_end = avg
            else:
                interval_start = avg
            iter_count += 1
     
        self.answer_bisection_method: AnswerBisectionMethod = AnswerBisectionMethod(iterations=iterationBisectionMethodList, answer=avg) 

        return self.answer_bisection_method

    async def chord_method(self) -> AnswerChordMethod:
        interval_end = self.interval.end
        interval_start = self.interval.start
        
        if await self.equation(interval_start) * await self.equation(interval_end) >= 0:
            print("Метод хорд не может быть применен, так как функция не меняет знак на данном интервале.")
            return None

        iterationChordMethodList: Iterable[IterationChordMethod] = []
        
        iteration = 0
        while True:
            
            equation_start = await self.equation(interval_start)
            equation_end = await self.equation(interval_end)
            
            x_n = interval_start - (equation_start * (interval_end - interval_start)) / (equation_end - equation_start)
            
            iterationChordMethodList.append(
                IterationChordMethod(
                    interval=Interval(
                        start=round(interval_start, 6), 
                        end=round(interval_end, 6)
                    ),
                    interval_equation=Interval(
                        start=round(equation_start, 6), 
                        end=round(equation_end, 6)
                    ),
                    calculation=round(x_n, 6),
                    number=iteration
                )
            )
                
            if abs(x_n - interval_end) < self.tol or iteration >= 1_000:
                break
            
            
            interval_start = interval_end
            interval_end = x_n
            iteration += 1
        return AnswerChordMethod(iterations=iterationChordMethodList, answer=x_n)

    async def newton_method(self) -> AnswerNewtonMethod:
        interval_end = self.interval.end
        
        iterationNewtonMethodList: Iterable[IterationNewtonMethod] = []
        
        iter_count = 0
        while iter_count < 1_000:
            equation_x = await self.equation(interval_end)
            first_derivative = await self.equation.first_derivative()
            first_derivative_equation = await first_derivative(interval_end)
            
            equation_x_n = interval_end - (equation_x / first_derivative_equation)
            
            iterationNewtonMethodList.append(
                IterationNewtonMethod(
                    number=iter_count, 
                    end=round(interval_end, 6), 
                    equation_x=round(equation_x, 6), 
                    first_derivative_equation=round(first_derivative_equation, 6), 
                    calculation=round(equation_x_n, 6)
                )
            )
            
            if abs(equation_x_n - interval_end) < self.tol:
                break
            
            interval_end = equation_x_n
            iter_count += 1
            
        return AnswerNewtonMethod(iterations=iterationNewtonMethodList, answer=equation_x_n)
  
async def __test():
    eq = Equation(a=.3, b=0, c=-4.2, d=-2)
    
    intervals = [
        Interval(start=-4,  end=-3 ),
        Interval(start=-1,  end= 0 ),
        Interval(start= 3,  end= 5 )
    ]
    
    
    calc = Calculation(equation=eq, interval=intervals[2], tol=1e-15)
    
    answer = await calc.bisection_method()
    
    from prettytable import PrettyTable
    
    table = PrettyTable()
    table.field_names = ['number', 'start', 'end', 'avg', 'f(avg)']
    table.align = "r"
    
    for iteration in answer.iterations:
        table.add_row([iteration.number + 1, iteration.interval.start, iteration.interval.end, iteration.average, iteration.calculation_average])
    
    print(table)
    
    print("Результаты метода половинного деления:", answer.answer)
    print()
    
    
    answer = await calc.chord_method()
    
    table = PrettyTable()
    table.field_names = ["number", 'start', 'end', 'e_start', 'e_end', 'cal']
    table.align = "r"
    
    for iteration in answer.iterations:
        table.add_row([iteration.number + 1, iteration.interval.start, iteration.interval.end, iteration.interval_equation.start, iteration.interval_equation.end, iteration.calculation])
    
    print(table)
    
    print("Результаты метода хорд:", answer.answer)
    print()
    
    
    answer = await calc.newton_method()
    
    table = PrettyTable()
    table.field_names = ["number", 'end', 'f(x)', 'f\'(x)', 'cal']
    table.align = "r"

    

    for iteration in answer.iterations:
        table.add_row([iteration.number, iteration.end, iteration.equation_x, iteration.first_derivative_equation, iteration.calculation])
    
    print(table)
    
    print("Результаты метода Ньютона:", answer.answer)
    print()
    
    

if __name__ == "__main__":
    asyncio.run(__test())
