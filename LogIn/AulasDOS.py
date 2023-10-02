Seleccion = 0

def MenuSeleccion():
    print("\n", "1: Iniciar sesion","\n","2: Crear cuenta", "\n")
    global Seleccion 
    Seleccion = int(input())

MenuSeleccion()

if Seleccion != 1 and Seleccion != 2:
    print("La respuesta de seleccion no es valida, por favor indique con un numero que menu quiere ingresar.")
    MenuSeleccion()



if Seleccion == 1:
    f = open ('Aulas.dat','r')
    print("\n", "Escriba su nombre de usuario", "\n")
    IntentoUser = str(input())
    DatoUser = f.readline()
    DatoUser.replace("\n","")
    print("\n", "Escriba su contraseña", "\n")
    IntentoPassword = str(input())
    DatoPassword = f.readline()
    DatoPassword.replace("\n","")
    if IntentoUser == DatoUser and IntentoPassword == DatoPassword:
        print("\n","Contraseña y Usuario correcto","\n")
    else:
        print("Contraseña o Usuario incorrecto")
        MenuSeleccion()
    f.close()
    
    


if Seleccion == 2:
    f = open ('Aulas.dat','w')
    print("\n","Crear nombre de usuario","\n")
    User = str(input())
    f.write(User)
    f.write("\n")
    print("\n","Crear contraseña","\n")
    Password = str(input())
    f.write(Password)
    print("\n")
    f.close()