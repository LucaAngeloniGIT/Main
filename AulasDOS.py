



print("\n", "1: Iniciar sesion","\n","2: Crear cuenta", "\n")
Seleccion = int(input())

if Seleccion == 1:
    f = open ('Aulas.dat','r')
    print("\n", "Escriba su nombre de usuario", "\n")
    IntentoUser = str(input())
    DatoUser = f.readline()
    if IntentoUser == DatoUser:
        print("\n","Usuario correcto")

    print("\n", "Escriba su contraseña", "\n")
    IntentoPassword = str(input())
    DatoPassword = f.readline()
    if IntentoPassword == DatoPassword:
        print("\n","Contraseña correcta","\n")
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