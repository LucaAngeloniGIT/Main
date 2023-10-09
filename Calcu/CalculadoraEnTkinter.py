import tkinter


vent = tkinter.Tk()
vent.title("Main")
vent.geometry("300x400")

LabelResultado = tkinter.Label(vent, text="Esto es el resultado",width=30,height=4)
LabelResultado.grid(row=0,column=0,columnspan=4)
px = 3
py = 3
tw = 8
th = 4

Orden = list= ""
Posicion = 0


def Boton0():
    Orden[Posicion] = 0
def Boton7():
    Orden[Posicion] = 7

def Boton8():
    Orden[Posicion] = 8

def Boton9():
    Orden[Posicion] = 9

def Boton4():
    Orden[Posicion] = 4

def Boton5():
    Orden[Posicion] = 5

def Boton6():
    Orden[Posicion] = 6

def Boton1():
    Orden[Posicion] = 1

def Boton2():
    Orden[Posicion] = 2

def Boton3():
    Orden[Posicion] = 3

def BotonBorrar():
    Orden.remove[Posicion]
    Posicion-1

def Botonmas():
    Orden[Posicion] = "+"

def Botonmenos():
    Orden[Posicion] = "-"

def Botonmultiplicar():
    Orden[Posicion] = "*"

def Botondividir():
    Orden[Posicion] = "/"



Boton7 = tkinter.Button(vent, text="7",width=tw,height=th)
Boton7.grid(padx=px, pady=py,row=1,column=0)

Boton8 = tkinter.Button(vent, text="8",width=tw,height=th)
Boton8.grid(padx=px, pady=py,row=1,column=1)

Boton9 = tkinter.Button(vent, text="9",width=tw,height=th)
Boton9.grid(padx=px, pady=py,row=1,column=2)

BotonBorrar = tkinter.Button(vent, text="<=",width=tw,height=th)
BotonBorrar.grid(padx=px, pady=py,row=1,column=3)

Boton4 = tkinter.Button(vent, text="4",width=tw,height=th)
Boton4.grid(padx=px, pady=py,row=2,column=0)

Boton5 = tkinter.Button(vent, text="5",width=tw,height=th)
Boton5.grid(padx=px, pady=py,row=2,column=1)

Boton6 = tkinter.Button(vent, text="6",width=tw,height=th)
Boton6.grid(padx=px, pady=py,row=2,column=2)

Botonmas = tkinter.Button(vent, text="+",width=tw,height=th)
Botonmas.grid(padx=px, pady=py,row=2,column=3)

Boton1 = tkinter.Button(vent, text="1",width=tw,height=th)
Boton1.grid(padx=px, pady=py,row=3,column=0)

Boton2 = tkinter.Button(vent, text="2",width=tw,height=th)
Boton2.grid(padx=px, pady=py,row=3,column=1)

Boton3 = tkinter.Button(vent, text="3",width=tw,height=th)
Boton3.grid(padx=px, pady=py,row=3,column=2)

Botonmenos = tkinter.Button(vent, text="-",width=tw,height=th)
Botonmenos.grid(padx=px, pady=py,row=3,column=3)

Boton0 = tkinter.Button(vent, text="0",width=tw,height=th)
Boton0.grid(padx=px, pady=py,row=4,column=0)

Botonmultiplicar = tkinter.Button(vent, text="x",width=tw,height=th)
Botonmultiplicar.grid(padx=px, pady=py,row=4,column=1)

Botondividir = tkinter.Button(vent, text="%",width=tw,height=th)
Botondividir.grid(padx=px, pady=py,row=4,column=2)

Botonresultado = tkinter.Button(vent, text="=",width=tw,height=th)
Botonresultado.grid(padx=px, pady=py,row=4,column=3)

vent.mainloop()