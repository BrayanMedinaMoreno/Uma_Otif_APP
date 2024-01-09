from tkinter import filedialog, messagebox
from funcionalidades.crear_otif import fun_crear_otif
from funcionalidades.calculofechas import calculo_tiempo

# Creación otif #
def carga_archivo_export():
    global export_data
    export_data = filedialog.askopenfilename()
    if export_data:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {export_data}")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def combinar_archivos():
    if not export_data:
        messagebox.showwarning("Advertencia", "si.")
        return
    else:
        fun_crear_otif(export_data)

# Update otif #

def cargar_archivo_mb51():
    global mb51_data
    mb51_data = filedialog.askopenfilename()
    if mb51_data:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {mb51_data}")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def cargar_archivo_otif():
    global otif_data
    otif_data = filedialog.askopenfilename()
    if otif_data:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {otif_data}")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

# fechas #

def abrir_otiftime():
    global otiftime_file
    otiftime_file = filedialog.askopenfilename()
    if otiftime_file:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {otiftime_file}")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def combinar_otiftime():
    if not otiftime_file:
        messagebox.showwarning("Advertencia", "Debes seleccionar el archivo")
        return
    else: 
        calculo_tiempo(otiftime_file)
