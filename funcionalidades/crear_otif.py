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
        plantilla = pd.read_excel("plantilla/otif.xlsx")
        print(plantilla)


        print("Llenando datos...")
        for index, row in datos_a_llenar.iterrows():
            plantilla.loc[index, "Documento compras"] = row["Documento compras"]
            plantilla.loc[index, "Proveedor/Centro suministrador"] = row["Proveedor/Centro suministrador"]
            plantilla.loc[index, "fecha entrega CKD"] = row["Fecha documento"]
            plantilla.loc[index, "Material"] = row["Material"]
            plantilla.loc[index, "Texto breve"] = row["Texto breve"]
            plantilla.loc[index, "Precio neto"] = row["Precio neto"]
            plantilla.loc[index, "Cantidad de pedido"] = row["Cantidad de pedido"]
        #    plantilla.loc[index, "Cantidad de reparto"] = row["Cantidad de reparto"]  

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            print("No se ha seleccionado una ubicación para guardar el archivo.")
            return    
            
        print("Guardando archivo en:", file_path)
        plantilla.to_excel(file_path, index=False)
        print("Archivo guardado correctamente.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

