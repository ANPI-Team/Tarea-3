import numpy as np
from sympy import *
x = Symbol('x')


class way:
    def simpson(self, f, a, b, N) -> (float, float):
        pass
    def trapecio(self, f, a, b, N) -> (float, float):
        pass
    def boole(self, f, a, b, N) -> (float, float):
        pass
    def cuadraturasGaussianas(self, f, a, b, N) -> (float, float):
        pass

class simple(way):
    def simpson(self, f, a, b, N = 0) -> (float, float):
        '''
        Recibe como parámetro una función f en forma de string
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: Simpson("exp(2*x)+2",1,2)
        '''
        fun = sympify(f)
        h = (b-a)/2
        x1 = (a+b)/2

        result = ((h/3)*(fun.subs(x, a)+(4*fun.subs(x, x1))+fun.subs(x, b)))
        aprox = result.evalf()
        fourth_deriv = diff(f, x, x, x, x)
        if(fourth_deriv.subs(x, a) > fourth_deriv.subs(x, b)):
            e = ((h**5)/90)*abs(diff(fun, x, x, x, x).subs(x, b))
            error = e.evalf()

        else:
            e = ((h**5)/90)*abs(diff(fun, x, x, x, x).subs(x, a))
            error = e.evalf()
        return aprox, error

    def trapecio(self, f, a, b, N = 0) -> (float, float):
        '''
        Recibe como parámetro una función f en forma de string
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: trapecio("exp(2*x)+2",1,2)
        '''
        fun = sympify(f)
        h = b-a
        result = ((h/2)*(fun.subs(x, a)+fun.subs(x, b)))
        aprox = result.evalf()
        second_deriv = diff(fun, x, x)

        if(second_deriv.subs(x, a) > second_deriv.subs(x, b)):
            e = (h**3/12)*abs(diff(fun, x, x).subs(x, b))
            error = e.evalf()
        else:
            e = (h**3/12)*abs(diff(fun, x, x).subs(x, a))
            error = e.evalf()

        return aprox, error

    def boole(self, f, a, b, N = 0) -> (float, float):
        h = (b - a)/4
        f = lambdify(x, f)

        y = [0, 0, 0, 0, 0]
        for n in range(len(y)):
            xs = a + n * h
            y[n] = f(xs)
        
            
        value = 2 * h / 45 * (7 * y[0] + 32 * y[1] + 12 * y[2] + 32 * y[3] + 7 * y[4])
        return float(value),0.0

class compuesto(way):
    def simpson(self, f: str, a, b, N) -> (float, float):
        '''
        Recibe como parámetro una función f en forma de string,
        los valores "a" y "b" del intervalo donde se desea integrar
        asi como la cantidad de puntos necesaria para la aproximacion,
        en este caso, debe ser un número IMPAR de puntos.
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: simpsonCompuesto("exp(2*x)+2",1,2,5)
        '''
        pairAprox = 0
        impairAprox = 0
        fun = sympify(f)
        h = (b-a)/(N-1)

        xVector = []
        xVector.append(a)

        for i in range(1, N):
            xVector.append(a+i*h)
        
        for i in range(1, N-1):
            pair = (i % 2 == 0)
            if(pair):
                print("is pair")
                pairAprox = pairAprox + fun.subs(x, xVector[i])

            else:
                print("is impair")
                impairAprox = impairAprox + fun.subs(x, xVector[i])

        aprox = (h/3)*((fun.subs(x, xVector[0]))+2 *
                    (pairAprox)+4*(impairAprox)+fun.subs(x, b))
        aprox = aprox.evalf()

        second_deriv = diff(fun, x, x)
        if(second_deriv.subs(x, a) > second_deriv.subs(x, b)):
            e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, b))
            error = e.evalf()

        else:
            e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, a))
            error = e.evalf()

        return aprox, error

    def trapecio(self, f, a, b, N) -> (int, float):
        '''
        Recibe como parámetro una función f en forma de string
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: Simpson("exp(2*x)+2",1,2)
        '''

        fun = sympify(f)
        h = (b-a)/(N-1)

        xVector = []
        xVector.append(a)
        aprox = 0
        for i in range(1, N):
            xVector.append(a+i*h)

        for i in range(0, N-1):
            aprox = aprox + (fun.subs(x, xVector[i])+fun.subs(x, xVector[i+1]))

        aprox = 0.5*aprox.evalf()

        second_deriv = diff(fun, x, x)
        if(second_deriv.subs(x, a) > second_deriv.subs(x, b)):
            e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, b))
            error = e.evalf()

        else:
            e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, a))
            error = e.evalf()

        return aprox, error

    def cuadraturasGaussianas(self, f, a, b, N) -> (float, float):
        return f,0.0


cosa = compuesto()
print(cosa.simpson("ln(x)", 2, 5,7))