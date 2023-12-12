from tkinter import *
from tkinter import filedialog, messagebox
import pandas as pd 
from funcionalidades.crear_otif import creacion_otif

### Variables globales ###

export_file = ""
otif_file = ""
otif_create_file = ""
otiftime_file = ""
mb51 = ""
otif_entradas = ""

def abrir_archivo_export():
    global otif_create_file
    otif_create_file = filedialog.askopenfilename()
    if otif_create_file:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {otif_create_file}")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def combinar_archivos_export():
    if not otif_create_file:
        messagebox.showwarning("Advertencia", "si.")
        return
    else:
        creacion_otif(otif_create_file)

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

# texto sobre el logo #
etiquita_logo = Label(home, text="G    R    U    P    O", bg="black", fg="white")
etiquita_logo.place(relx=0.5, rely=0.02, anchor="n")

boton_mb51 = Button(home, text="Seleccionar archivo export", bg="#fafafc", command=abrir_archivo_export)
boton_generar_otif = Button(home, text="Generar", bg="#fafafc", command=combinar_archivos_export)

home.mainloop()
