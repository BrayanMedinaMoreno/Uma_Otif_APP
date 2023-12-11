import pandas as pd
from tkinter import filedialog, messagebox

def creacion_otif(otif_create_file):
    if not otif_create_file:
        messagebox.showwarning("Advertencia", "Debe seleccionar el archivo mb51 para continuar")
        return
    try:
        print("Letendo datos del archivo de entrada...")
        datos_a_llenar = pd.read_excel(otif_create_file)
        print(datos_a_llenar.head())

        print("Leyendo plantilla...")
        


    
    except Exception as e:
        messagebox.showerror("Error", str(e))