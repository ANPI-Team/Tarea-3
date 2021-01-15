from tkinter import *
from tkinter import ttk
from enum import Enum
from parte1_p2 import compuesto, simple, way

class TipoOperacion(Enum):
    SIMPLE = 1
    COMPUESTO = 2

class Metodo(Enum):
    SIMPSON = 1
    TRAPECIO = 2
    BOOLE = 3

def select_operation(operacion: TipoOperacion, metodo: Metodo, a: int, b: int, func: str) -> (str, float):
    oper: way = None
    if(operacion == TipoOperacion.SIMPLE):
        oper = simple()
    elif(operacion == TipoOperacion.COMPUESTO):
        oper = compuesto()
    
    if(metodo == Metodo.SIMPSON):
        return oper.simpson(func, a, b)
    elif(metodo == Metodo.TRAPECIO):
        return oper.trapecio(func, a, b)
    elif(metodo == Metodo.BOOLE):
        return oper.boole(func, a, b)

def popupmsg(msg):
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

i, err = select_operation(TipoOperacion.SIMPLE, Metodo.TRAPECIO,0,0,'func')
print("i = " + i)
print("err = " + str(err))

root = Tk() 
root.config(width=300, height=200)
a = Label(root, text ="Calculadora de Integrales Definidas")
a.pack() 
  
root.mainloop()