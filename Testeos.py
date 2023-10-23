Posicion = 0
posicionNum = 0
Orden = []
operacion = ""
Numeros = []
def Limpiar():
    global Posicion
    Orden.clear()
    Posicion = 0
def ConsolidarNum():
    global Posicion
    global Orden
    NumeroSTR = ''.join(Orden)
    UltimoNum = int(NumeroSTR)

def Boton0():
    global Posicion
    Orden[Posicion] = 0
    Posicion += 1
def Boton7():
    global Posicion
    Orden[Posicion] = 7
    Posicion += 1
       
def Boton8():
    global Posicion
    Orden[Posicion] = 8
    Posicion += 1

def Boton9():
    global Posicion
    Orden[Posicion] = 9
    Posicion += 1

def Boton4():
    global Posicion
    Orden[Posicion] = 4
    Posicion += 1

def Boton5():
    global Posicion
    global Orden
    Orden[Posicion] = 5
    Posicion += 1

def Boton6():
    global Posicion
    Orden[Posicion] = 6
    Posicion += 1

def Boton1():
    global Posicion
    Orden[Posicion] = 1
    Posicion += 1

def Boton2():
    global Posicion
    Orden[Posicion] = 2
    Posicion += 1

def Boton3():
    global Posicion
    Orden[Posicion] = 3
    Posicion += 1

def BotonBorrar():
    global Posicion
    Orden.remove[Posicion]
    Posicion-1

def Botonmas():
    global Posicion
    operacion = suma
    ConsolidarNum()
    Numeros[posicionNum] = UltimoNum
    posicionNum += 1
    Limpiar()
    
def Botonmenos():
    global Posicion
    operacion = resta
    Numeros[posicionNum]
    posicionNum += 1
    

def Botonmultiplicar():
    global Posicion
    Orden[Posicion] = "*"

def Botondividir():
    global Posicion
    Orden[Posicion] = "/"

def Botonresultado():
    if operacion == suma:
        Resultado = Numers[0] + Numeros[1]
        
    print(Resultado)
    
print("Elegir primer numero")
Primer = int(input())
if Primer == 0:
    Boton0()
if Primer == 1:
    Boton1()
if Primer == 3:
    Boton3()
if Primer == 4:
    Boton4()
if Primer == 5:
    Boton5()
if Primer == 6:
    Boton6()
if Primer == 7:
    Boton7()
if Primer == 8:
    Boton8()
if Primer == 9:
    Boton9()
print("Elegir la operacion")
Segundo = str(input())
if Segundo == "+":
    Botonmas()
if Segundo == "-":
    Botonmenos()
print("Elegir segundo numero")
Tercero = int(input())
if Tercero == 0:
    Boton0()
if Tercero == 1:
    Boton1()
if Tercero == 3:
    Boton3()
if Tercero == 4:
    Boton4()
if Tercero == 5:
    Boton5()
if Tercero == 6:
    Boton6()
if Tercero == 7:
    Boton7()
if Tercero == 8:
    Boton8()
if Tercero == 9:
    Boton9()