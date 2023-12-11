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

# Parte superior negra #
canvas.create_rectangle(0,0,800,90, fill="black")

# logo # 
img = PhotoImage(file="Logos/uma-logo.png")
ibi_img = Label(home,image=img, bg="black")
ibi_img.place(relx=0.5, rely=0.04, anchor="n")

etiquita_logo = Label(home, text="G    R    U    P    O", bg="black", fg="white")
etiquita_logo.place(relx=0.5, rely=0.02, anchor="n")


home.mainloop()
