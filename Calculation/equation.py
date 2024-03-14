class Equation:

    def __init__(self, a: float = 1, b: float = 1, c: float = 1, d: float = 1) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
        self.equation = lambda x: (a * (x**3) + b * (x**2) + c * x + d)

    async def first_derivative(self) -> 'Equation':
        return Equation(a = 0, b = 3 * self.a, c = 2 * self.b, d = self.c) 

    async def __call__(self, x: float) -> float:
        return self.equation(x)