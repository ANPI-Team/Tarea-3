from tkinter import *
from tkinter import ttk
import tkinter
from enum import Enum
from parte1_p2 import compuesto, simple, way
from sympy import Symbol, S
from sympy.calculus.util import continuous_domain
from sympy.sets import Interval
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function

# Manejo de errores


class Error(Enum):
    DIG_FUNC = "Error tipo 1: Función mal digitada"
    CONT = "Error, funcion no continua en [a,b]. Por favor escoja otro intervalo."
    NUM = "Por favor ingresar numeros en los intervalos"
    EMPTY = "TODOS LOS VALORES ESTAN VACIOS AIUUUDA!"
    NOT_METHOD = "Por favor seleccione un Metodo"


def popupmsg(msg: Error):
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()

    # Gets the requested values of the height and widht.
    windowWidth = popup.winfo_reqwidth()
    windowHeight = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2) - 100
    positionDown = int(popup.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(positionRight, positionDown))

    popup.wm_title("!")
    label = ttk.Label(popup, text=str(msg.value), font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def continua(func: str, a: int, b: int) -> bool:
    x = Symbol("x")
    value = continuous_domain(parse_expr(func), x, Interval(a, b))
    if(not isinstance(value, Interval)):
        popupmsg(Error.CONT)
        return False
    return True

# conexión con métodos


class TipoOperacion(Enum):
    SIMPLE = 1
    COMPUESTO = 2


class Metodo(Enum):
    SIMPSON = 1
    TRAPECIO = 2
    BOOLE_O_GAUSSIANA = 3

def interfaz_operacion():
    global oper
    global etiqueta_cant
    global ing_puntos
    
    if oper == TipoOperacion.COMPUESTO:
        
        ing_puntos.config(state='normal')

        
    elif oper == TipoOperacion.SIMPLE:
        ing_puntos.config(state='disabled')
        
    else:
        print(oper)


def select_operation(operacion: TipoOperacion, metodo: Metodo, a: int, b: int, func: str, puntos: int) -> (str, float):
    oper: way = None
    if(operacion == TipoOperacion.SIMPLE):
        oper = simple()
    elif(operacion == TipoOperacion.COMPUESTO):
        oper = compuesto()

    if(metodo == Metodo.SIMPSON):
        return oper.simpson(func, a, b, puntos)
    elif(metodo == Metodo.TRAPECIO):
        return oper.trapecio(func, a, b, puntos)
    elif(metodo == Metodo.BOOLE_O_GAUSSIANA):
        return oper.boole(func, a, b, puntos)

def titulo_operacion():
    global oper
    if (oper == TipoOperacion.SIMPLE):
        return "Metodos Compuestos"
    elif (oper == TipoOperacion.COMPUESTO):
        return "Metodos Simples"

funcion = ""
inter_a = 0
inter_b = 0
oper = TipoOperacion.COMPUESTO
metodo = Metodo.SIMPSON
puntos = 0


def obtener_metodo(met):
    global metodo
    # met = lista_desplegable.get()


    if met == "Trapecio" or met == "Trapecio Compuesto" :
        metodo = Metodo.TRAPECIO
    elif met == "Simpson" or met == "Simpson Compuesto":
        metodo = Metodo.SIMPSON
    elif met == "Regla de Boole" or met == "Cuadraturas Gaussianas":
        metodo = Metodo.BOOLE_O_GAUSSIANA
    
    else:
        popupmsg(Error.NOT_METHOD)
    
def cambiar_operacion():
    global oper

    if(oper == TipoOperacion.COMPUESTO):
        oper = TipoOperacion.SIMPLE
        lista_desplegable['values'] = metodos_simples
    elif(oper == TipoOperacion.SIMPLE):
        oper = TipoOperacion.COMPUESTO
        lista_desplegable['values'] = metodos_compuestos

    b_compuesto['text'] = titulo_operacion()
    
    interfaz_operacion()


def prueba():
    global funcion
    global inter_a
    global inter_b
    global oper
    global metodo 
    global puntos

    funcion = ing_fun.get()
    met = lista_desplegable.get()

    obtener_metodo(met)

    try:
        inter_a = int(ing_a.get())
        inter_b = int(ing_b.get())
    except:
        popupmsg(Error.NUM)

    try:
        if(ing_puntos['state'] != 'disabled'):
            puntos = int(ing_puntos.get())

    except:
        print("ERROR DE PUNTOS")

    try:
        f = lambdify(x, funcion)
        r = f(inter_b - inter_a)
    except:
        popupmsg(Error.DIG_FUNC)

    if isinstance(inter_a, int):
        if isinstance(inter_b, int):
            if(continua(funcion, inter_a, inter_b)):
                integral, err = select_operation(
                    oper, metodo, inter_a, inter_b, funcion, puntos)
                # QUITAR ESTOS PRINTS
                print("a:",inter_a)
                print("b:",inter_b)
                print(oper)
                print(metodo)
                # DEBE MOSTRAR ESTOS VALORES

                result_label['text'] = "Aproximación :" + str(integral)
                error_label['text'] = "Error :" + str(err)

                print(integral, err)

        else:
            print("Error en b")
    else:
        print("Error en a")


# crear la ventana Tk
ventana = tkinter.Tk()

# Gets the requested values of the height and widht.
windowWidth = ventana.winfo_reqwidth()
windowHeight = ventana.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(ventana.winfo_screenwidth()/2 - windowWidth/2) - 250
positionDown = int(ventana.winfo_screenheight()/2 - windowHeight/2) - 400

# Positions the window in the center of the page.
ventana.geometry("+{}+{}".format(positionRight, positionDown))

ventana.geometry("500x800")
ventana.title("Calculadora de Integrales Definidas")
imagen_funcion = PhotoImage(file="fun.png")
Label(ventana, image=imagen_funcion).place(x=190, y=20)

# Escribir f(x) en la ventana
etiqueta_fun = tkinter.Label(ventana, text="f ( x ) = ", font="40")
etiqueta_fun.place(x=85, y=110)

# Escribir intervalo a
etiqueta_a = tkinter.Label(ventana, text="a = ", font="40")
etiqueta_a.place(x=150, y=155)

# Escribir intervalo b
etiqueta_b = tkinter.Label(ventana, text="b = ", font="40")
etiqueta_b.place(x=290, y=155)



# Escribir puntos
etiqueta_cant = tkinter.Label(ventana, text="Cantidad de Puntos = ", font="40")



b_compuesto = tkinter.Button(
    ventana, text=titulo_operacion(), padx=10, pady=5, command=cambiar_operacion)
b_compuesto.place(x=195, y=220)


# Escribir selecionar método
etiqueta_método = tkinter.Label(ventana, text="Método = ", font="40")
etiqueta_método.place(x=130, y=290)

# Lista desplegable y selección
lista_desplegable = ttk.Combobox(ventana, width=17)
lista_desplegable.place(x=208, y=295)

metodos_simples = ["Trapecio", "Simpson", "Regla de Boole"]
metodos_compuestos = ["Trapecio Compuesto",
                      "Simpson Compuesto", "Cuadraturas Gaussianas"]


# colocar una entrada de texto en la ventana
ing_fun = tkinter.Entry(ventana, font="Arial 20")
ing_fun.place(x=140, y=105)

ing_a = tkinter.Entry(ventana, font="Arial 20", width=5)
ing_a.place(x=180, y=150)

ing_b = tkinter.Entry(ventana, font="Arial 20", width=5)
ing_b.place(x=330, y=150)

ing_puntos = tkinter.Entry(ventana, font="Arial 20", width=5)
ing_puntos.place(x=250, y=350)
etiqueta_cant.place(x=80, y=355)

cambiar_operacion()

# colocar el botón calcular en la ventana
bcalcular = tkinter.Button(ventana, text="Calcular",
                           padx=30, pady=10, command=prueba)
bcalcular.place(x=200, y=700)

result_label = Label(ventana, text = "Aproximación :" + str(0.0), font = "40")
result_label.place(x = 135, y = 450)
error_label =Label(ventana, text = "Error :" + str(0.0), font = "40")
error_label.place(x = 210, y = 500)


ventana.mainloop()
