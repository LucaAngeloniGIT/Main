#Funcion Para llamar al inicio del programa
def inicio():
    Menu()
    Ramificacion()

#Menu principal, lo primero que se muestra en pantalla
def Menu():
    print("1: Leer lista de tareas", "\n")
    print("2: Editar Lista de Tareas", "\n")
    print("3: Borrar y Crear Lista", "\n")
    global Lectura 
    Lectura = int(input())
    print("\n")

#Llave de seleccion del Menu principal
def Ramificacion():
    if Lectura == 1:
        Muestreo()
            
    if Lectura == 2:
        Edicion()

    if Lectura == 3:
        global ListaTareas
        ListaTareas.clear()
        Crear()

    

#Editar la lista
def Edicion():
    global ListaTareas
    LecturaLista()
    print("Editando la Lista de Tareas...","\n","\n")
    
    for x in ListaTareas:
        print("Elemento de la lista", ListaTareas.index(x),":",x,)
    print("\n")
    print("+: Agregar un nuevo elemento")
    print("x: Salir al Menu principal")
    LecturaMenu = str(input())
    if LecturaMenu == "+":
        NuevoElemento()
        Edicion()
    elif LecturaMenu == "x":
        inicio()
    else:
        LecturaMenuEntero = int(LecturaMenu)
        print("Editando el Elemento:",ListaTareas[LecturaMenuEntero],"\n")
        print("1: Eliminar Elemento","\n")
        print("2: Modificar Elemento","\n")
        print("3: Agregar un nuevo elemento","\n")
        print("x: Volver al Menu principal","\n")
        LecturaEdicion = str(input())
        if LecturaEdicion == "x":
            inicio()
        LecturaEdicionEntero = int(LecturaEdicion)
        if LecturaEdicionEntero == 1:
            linea=ListaTareas[LecturaMenuEntero]
            ListaTareas.remove(linea)
            Guardar()
            Edicion()
        if LecturaEdicionEntero == 2:
            print("Escriba el nuevo cambio de elemento","\n")
            CambioVariable = str(input())
            ListaTareas[LecturaMenuEntero] = CambioVariable
            Guardar()
            inicio()
        if LecturaEdicionEntero == 3:
            NuevoElemento()
        if LecturaEdicionEntero == 4:
            inicio()

#Agregar un nuevo elemento a la lista
def NuevoElemento():
        print("Escriba El nuevo elemento que desea agregar")
        AgregarElemento = str(input())
        LecturaLista()
        ListaTareas.append(AgregarElemento)
        Guardar()

#Leer la base de datos y copiar los datos a la lista, para manejarlos en el programa
def LecturaLista():
    global ListaTareas
    f = open('LecturaFicheroDesafio4.dat', 'r')
    ListaTareas = [linea.strip() for linea in f]
    f.close()

#Mostrar Contenido de la lista
def Muestreo():
    global ListaTareas
    LecturaLista()
    for i in ListaTareas:
        print(i)
    print("Lista de Tareas:","\n")
    for i in ListaTareas:
        print("Tarea", ListaTareas.index(i),":",i,"\n")
    print("x: Volver al Menu Principal", "\n")
    LecturaMuestreo = str(input())
    if LecturaMuestreo == "x":
        inicio()

#Agregar Elementos a una lista borrada 
def Crear():
    global ListaTareas
    global Elementos
    print("+: Agregar un Elemento a la lista","\n")
    print("x: Volver al menu","\n")
    LecturaCreacion = str(input())
    if LecturaCreacion == "+":
        NuevoElemento = str(input())
        ListaTareas.append(NuevoElemento)
        Guardar()
        Crear()
    if LecturaCreacion == "x":
        inicio()
    
#Guardar los datos de la lista en la base de datos
def Guardar():
    f = open('LecturaFicheroDesafio4.dat', 'w')
    for i in ListaTareas:
        f.write(i)
        f.write("\n")
    f.close()

#Inicio del programa  
#Se crean las variables globales
ListaTareas = [""]
#Se da inicio al programa
inicio()
