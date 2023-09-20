import tkinter

vent = tkinter.Tk()
vent.title("Aula")
vent.attributes()
vent.geometry("500x300")
vent['bg'] = 'sky blue'

NumAulas = 0

NumeroDeAulas = tkinter.Label(vent, background='sky blue', font='calibri')
NumeroDeAulas.place(x=100, y=50)
NumeroDeAulas.pack()

NombreAula = tkinter.Entry(text="nombre del aula ")

def NuevaAula():
    global NumAulas
    NumAulas = NumAulas + 1
    NumeroDeAulas.config(text = NumAulas)

    
    
MenuPrincipal = tkinter.Menu(vent, background='purple', fg='white')
archivo = tkinter.Menu(MenuPrincipal, tearoff=False)

archivo.add_command(label="Nueva Aula", command=NuevaAula, background='sky blue')
archivo.add_separator()
archivo.add_command(label="Salir", command=vent.quit, background='red')

MenuPrincipal.add_cascade(menu=archivo, label="Archivo")
vent.config(menu=MenuPrincipal)
vent.mainloop()
