from tkinter import *
import pandas as pd 
from funcionalidades.botones import carga_archivo_export,combinar_archivos


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
logo = PhotoImage(file="Logos/uma-logo.png")
color_logo = Label(home,image=logo, bg="black")
color_logo.place(relx=0.5, rely=0.04, anchor="n")

# texto sobre el logo #
etiquita_texto_logo = Label(home, text="G    R    U    P    O", bg="black", fg="white")
etiquita_texto_logo.place(relx=0.5, rely=0.02, anchor="n")

boton_mb51 = Button(home, text="Seleccionar archivo export", bg="#fafafc", command=carga_archivo_export)
boton_generar_otif = Button(home, text="Generar", bg="#fafafc", command=combinar_archivos)

boton_mb51.place(relx=0.15, rely=0.23, anchor="center")
boton_generar_otif.place(relx=0.15, rely=0.29, anchor="center")
home.mainloop()
