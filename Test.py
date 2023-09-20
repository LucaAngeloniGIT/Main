import tkinter
from tkinter import PhotoImage

ventana = tkinter.Tk()
ventana.geometry("600x600+150+50")
ventana.config(bg="whitesmoke")
ventana.title("Ventana con imagen")

img = PhotoImage(file="C:\Users\lucaa\Temp\Bash\Main\Colegio.jpeg")
Label = tkinter.Label(image=img).pack()

ventana.mainloop()