from sympy import Symbol, S
from sympy.calculus.util import continuous_domain
from sympy.sets import Interval
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function

class way:
    def simpson(self, func, a, b, puntos) -> (str, float):
        pass
    def trapecio(self, func, a, b, puntos) -> (str, float):
        pass
    def boole(self, func, a, b, puntos) -> (str, float):
        pass

class simple(way):
    def simpson(self, func, a, b, puntos = 0) -> (str, float):
        return func,0.0
    def trapecio(self, func, a, b, puntos = 0) -> (str, float):
        return func,0.0
    def boole(self, func, a, b, puntos = 0) -> (str, float):
        h = (b - a)/4
        f = lambdify(x, func)

        y = [0, 0, 0, 0, 0]
        for n in range(len(y)):
            xs = a + n * h
            y[n] = f(xs)
        
            
        value = 2 * h / 45 * (7 * y[0] + 32 * y[1] + 12 * y[2] + 32 * y[3] + 7 * y[4])
        return str(value),0.0

class compuesto(way):
    def simpson(self, func, a, b, puntos) -> (str, float):
        return func,0.0
    def trapecio(self, func, a, b, puntos) -> (str, float):
        return func,0.0
    def boole(self, func, a, b, puntos) -> (str, float):
        return func,0.0


cosa = simple()
print(cosa.boole("cos(x)", -1, 1))