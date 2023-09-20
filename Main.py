import tkinter

vent = tkinter.Tk()
vent.title("Aula")
vent.attributes()
vent.geometry("500x300")
vent['bg'] = 'sky blue'

NumAulas = 0

NumeroDeAulas = tkinter.Label(vent, background='sky blue', font='calibri')
NumeroDeAulas.place()

BandejaNombre = tkinter.Entry(text="nombre del aula ")
BandejaNombre.place_forget()



def NuevaAula():
    global NumAulas
    NumAulas = NumAulas + 1
    Texto = f"Numero de Aulas: {NumAulas}"
    NumeroDeAulas.config(text=Texto) 
    NumeroDeAulas.place(x=1, y=280)
    BandejaNombre.place(x=200, y=30)

    
   
MenuPrincipal = tkinter.Menu(vent, background='purple')
archivo = tkinter.Menu(MenuPrincipal, tearoff=False)

archivo.add_command(label="Nueva Aula", command=NuevaAula, background='sky blue')
archivo.add_separator()
archivo.add_command(label="Salir", command=vent.quit)

MenuPrincipal.add_cascade(menu=archivo, label="Archivo")
vent.config(menu=MenuPrincipal)
vent.mainloop()
