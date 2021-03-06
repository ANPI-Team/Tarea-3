import numpy as np
from numpy.lib.function_base import append
from sympy import *

x = Symbol('x')


def trapecio(f, a, b):
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
    return (aprox, error)


def simpson(f, a, b):
    '''
        Recibe como parámetro una función f en forma de string
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: simpson("exp(2*x)+2",1,2)
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
    return (aprox, error)


def Boole(f, a, b):
    '''
        Recibe como parámetro una función f en forma de string
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: Boole("exp(2*x)+2",1,2)
    '''
    fun = sympify(f)
    xVector = []
    h = (b-a)/4
    for i in range(0,5):
        xTemp = a+(i*h)
        xVector.append(xTemp)

    first = (7*fun.subs(x,xVector[0]))
    second = (32*fun.subs(x,xVector[1]))
    third = (12*fun.subs(x,xVector[2]))
    fourth = (32*fun.subs(x,xVector[3]))
    fifth = (7*fun.subs(x,xVector[4]))
    aprox = ((2*h)/(45))*(first+second+third+fourth+fifth)
    sixth_deriv = diff(fun, x,x,x,x,x,x)

    if(sixth_deriv.subs(x, a) > sixth_deriv.subs(x, b)):
        e = -((b-a)**7/1935360)*abs(diff(fun, x,x,x,x,x,x).subs(x, b))
        error = e.evalf()
    else:
        e = -((b-a)**7/1935360)*abs(diff(fun, x,x,x,x,x,x).subs(x, a))
        error = e.evalf()

    return aprox, error

def trapecioCompuesto(f, a, b, N):
    '''
        Recibe como parámetro una función f en forma de string,
        los valores "a" y "b" del intervalo donde se desea integrar
        asi como la cantidad de puntos necesaria para la aproximacion.
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: trapecioCompuesto("exp(2*x)+2",1,2,5)
        '''
    fun = sympify(f)
    h = (b-a)/(N-1)

    xVector = []
    
    aprox = 0
    
    for i in range(0, N):
        xVector.append(a+(i*h))
  
    for i in range(0, N-1):
        aprox = aprox + (fun.subs(x, xVector[i])+fun.subs(x, xVector[i+1]))

    aprox = (h/2)*aprox.evalf()

    second_deriv = diff(fun, x, x)
    if(second_deriv.subs(x, a) > second_deriv.subs(x, b)):
        e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, b))
        error = e.evalf()

    else:
        e = (((b-a)*(h**2))/12)*abs(diff(fun, x, x).subs(x, a))
        error = e.evalf()

    return (aprox, error)


def simpsonCompuesto(f, a, b, N):
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

            pairAprox = pairAprox + fun.subs(x, xVector[i])

        else:

            impairAprox = impairAprox + fun.subs(x, xVector[i])

    aprox = (h/3)*((fun.subs(x, xVector[0]))+2 *
                   (pairAprox)+4*(impairAprox)+fun.subs(x, b))
    aprox = aprox.evalf()

    fourth_deriv = diff(fun, x, x,x,x)
    if(fourth_deriv.subs(x, a) > fourth_deriv.subs(x, b)):
        e = (((b-a)*(h**4))/180)*abs(diff(fun, x, x,x,x).subs(x, b))
        error = e.evalf()

    else:
        e = (((b-a)*(h**4))/180)*abs(diff(fun, x, x,x,x).subs(x, a))
        error = e.evalf()

    return (aprox, error)


def cuadratura_Gaussiana(f, a, b, N):
    '''
        Recibe como parámetro una función f en forma de string,
        los valores "a" y "b" del intervalo donde se desea integrar
        asi como el orden del polinomio a utilizar (Pn).
        En caso de necesitar funciones específicas (como sin, cos)
        debe usar las propias de sympy, por ejemplo, e^x = exp(x) 
        Caso de ejemplo: cuadraturasGaussianas("exp(2*x)+2",1,2,5)
    '''
    fun = sympify(f)
    tmpFun = sympify("(x**2)-1")
    tmpFun = tmpFun**N
    aprox = 0
    wVector = []
    Pn = (diff(tmpFun, x, N))
   
    
    Pn = (1/(factorial(N)*2**(N))*Pn)
    
    xi = solve(Pn)
    xi = sorted(xi)
    Pi = diff(Pn,x)
    #print(xi)
    for i in range(0, N):
        tmpW = 2/((1-((xi[i])**2))*((Pi.subs(x,xi[i]))**2))
        wVector.append(tmpW)

    for i in range(0, N):
        
        tmpXi = (((b-a)/2)*xi[i].evalf())+((a+b)/2)
        aprox = aprox + (wVector[i]* fun.subs(x,tmpXi))
    
    aprox = ((b-a)/2) *aprox.evalf()
    
    fourth_deriv = diff(fun, x, x,x,x)
    if(fourth_deriv.subs(x, a) > fourth_deriv.subs(x, b)):
        e = abs(diff(fun, x, x,x,x).subs(x, b))/135
        error = e.evalf()

    else:
        e = abs(diff(fun, x, x,x,x).subs(x, a))/135
        error = e.evalf()
    return (aprox, error)
