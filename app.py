from tkinter import *
import pandas as pd 
from funcionalidades.botones import carga_archivo_export,combinar_archivos, abrir_otiftime, combinar_otiftime

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

## texto sobre los botones ##
# crear otif #
etiquita_texto_botones_crear_otif = Label(home, text="Crear Otif Primer Paso", fg="black")
etiquita_texto_botones_crear_otif.place(relx=0.20, rely=0.19, anchor="center")
# Texto sobre los botones fechas #
etiquita_texto_boton_fechas = Label(home, text="Calcular las fechas", fg="black" ) 
etiquita_texto_boton_fechas.place(relx=0.80, rely=0.19, anchor="center")
# texto sobre botones update otif #
etiquita_texto_boton_update = Label(home, text="Actualizar otif", fg="black" ) 
etiquita_texto_boton_update.place(relx=0.50, rely=0.40, anchor="center")

## botones ##
# crear otif #
boton_export = Button(home, text="Seleccionar archivo export", bg="#fafafc", command=carga_archivo_export)
boton_generar_otif = Button(home, text="Generar", bg="#fafafc", command=combinar_archivos)
boton_export.place(relx=0.20, rely=0.23, anchor="center")
boton_generar_otif.place(relx=0.20, rely=0.29, anchor="center")

# fechas #
boton_fechas = Button(home, text="Seleccionar archivo fechas", bg="#fafafc", command=abrir_otiftime)
boton_generar_fechas = Button(home, text="Calcular Fechas", bg="#fafafc", command=combinar_otiftime)
boton_fechas.place(relx=0.80, rely=0.23, anchor="center")
boton_generar_fechas.place(relx=0.80, rely=0.29, anchor="center")

# update otif #
boton_mb51 = Button(home, text="Seleccionar archivo mb51",bg="#fafafc")
boton_otif = Button(home, text="Seleccionar archivo otif",bg="#fafafc")
boton_entradas = Button(home, text="Generar otif", bg="#fafafc")
boton_mb51.place(relx=0.40, rely=0.46, anchor="center")
boton_otif.place(relx=0.60, rely=0.46, anchor="center")
boton_entradas.place(relx=0.50, rely=0.52, anchor="center")

home.mainloop()