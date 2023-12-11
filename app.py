from tkinter import *
import pandas as pd 

### Variables globales ###

export_file = ""
otif_file = ""
otif_create_file = ""
otiftime_file = ""
mb51 = ""
otif_entradas = ""

### Manejo // Ventanas // FunOcultar ###

def abrir_principal():
        home.withdraw()


### Interfaz // Inicio ###

home = Tk()
home.title("OTIF APP")
home.geometry("800x600")
home.resizable(False,False)

canvas = Canvas(home,width=800, height=600)
canvas.pack()


canvas.create_rectangle(0,0,800,90, fill="black")


home.mainloop()
