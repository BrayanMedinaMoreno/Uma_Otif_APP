import pandas as pd
from tkinter import filedialog, messagebox

def fun_crear_otif(export_data):
    if not export_data:
        messagebox.showwarning("Advertencia", "Debe seleccionar el archivo mb51 para continuar")
        return
    try:
        print("Leyendo datos del archivo de entrada...")
        datos_a_llenar = pd.read_excel(export_data)
        print(datos_a_llenar.head())

        print("Leyendo plantilla...")
        plantilla = pd.read_excel("plantilla/otif.xlsx")
        print(plantilla)

        print("Llenando datos...")
        # Definir una función para aplicar a cada fila de datos_a_llenar
        def fill_template(row):
            index = row.name  # Obtener el índice de la fila
            plantilla.loc[index, "Documento compras"] = row["Documento compras"]
            plantilla.loc[index, "Proveedor/Centro suministrador"] = row["Proveedor/Centro suministrador"]
            plantilla.loc[index, "fecha entrega CKD"] = row["Fecha documento"]
            plantilla.loc[index, "Material"] = row["Material"]
            plantilla.loc[index, "Texto breve"] = row["Texto breve"]
            plantilla.loc[index, "Precio neto"] = row["Precio neto"]
            plantilla.loc[index, "Cantidad de pedido"] = row["Cantidad de pedido"]
            # plantilla.loc[index, "Cantidad de reparto"] = row["Cantidad de reparto"]

        # Aplicar la función fill_template a cada fila de datos_a_llenar
        datos_a_llenar.apply(fill_template, axis=1)

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            print("No se ha seleccionado una ubicación para guardar el archivo.")
            return

        print("Guardando archivo en:", file_path)
        plantilla.to_excel(file_path, index=False)
        print("Archivo guardado correctamente.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
