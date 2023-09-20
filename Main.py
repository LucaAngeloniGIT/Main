import tkinter

vent = tkinter.Tk()
vent.title("Aula")
vent.attributes('-fullscreen', True)

menu_archivo = tk.Menu(vent, tearoff=0)
menu_editar = tk.Menu(vent, tearoff=0)
menu_ayuda = tk.Menu(vent, tearoff=0)

box1 = tkinter.Entry(vent)
box1.pack()
vent.mainloop()
