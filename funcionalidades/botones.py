from tkinter import filedialog, messagebox
from funcionalidades.crear_otif import fun_crear_otif

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