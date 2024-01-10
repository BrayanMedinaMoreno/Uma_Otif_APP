import pandas as pd
from datetime import datetime, timedelta
from tkinter import messagebox, filedialog

def calculo_tiempo(fecha_propuesta):
    if not fecha_propuesta:
        messagebox.showwarning("Advertencia", "Debes seleccionar el archivo")
        return
    
    df = pd.read_excel(fecha_propuesta)
    print("Nombre columnas")
    print(df.columns)
    print("continuar.....")
    df["fecha entrega CKD"] = pd.to_datetime(df["fecha entrega CKD"], format="%d-%m-%y")
    df["Lead Time"] = pd.to_numeric(df["Lead Time"], errors="coerce")

    dias_no_habiles =[
        datetime(2024, 1, 1), datetime(2024, 1, 9),       # Enero 
        datetime(2024, 3, 20),                            # Marzo 
        datetime(2024, 4, 6), datetime(2024, 4, 7),       # Abril 
        datetime(2024, 5, 1), datetime(2024, 5, 22),      # Mayo  
        datetime(2024, 6, 12), datetime(2024, 6, 19),     # Junio
        datetime(2024, 7, 3), datetime(2024, 7, 20),      # Julio
        datetime(2024, 8, 7), datetime(2024, 8, 21),      # Agosto
        datetime(2024, 10, 16),                           # Octubre
        datetime(2024, 11, 6), datetime(2024, 11, 13),    # Noviembre
        datetime(2024, 12, 8), datetime(2024, 12, 25),    # Diciembre

        datetime(2025, 1, 1), datetime(2025, 1, 9),       # Enero 
        datetime(2025, 3, 20),                            # Marzo 
        datetime(2025, 4, 6), datetime(2025, 4, 7),       # Abril 
        datetime(2025, 5, 1), datetime(2025, 5, 22),      # Mayo  
        datetime(2025, 6, 12), datetime(2025, 6, 19),     # Junio
        datetime(2025, 7, 3), datetime(2025, 7, 20),      # Julio
        datetime(2025, 8, 7), datetime(2025, 8, 21),      # Agosto
        datetime(2025, 10, 16),                           # Octubre
        datetime(2025, 11, 6), datetime(2025, 11, 13),    # Noviembre
        datetime(2025, 12, 8), datetime(2025, 12, 25),    # Diciembre
    ]
    
    def no_dias_habiles(fecha):
        if fecha in dias_no_habiles:
            return True
        return False
    
    def calculo_de_fecha(row):
        fecha_actual = row["fecha entrega CKD"]
        lead_time = row["Lead Time"]
    
        for _ in range (int(lead_time)):
            fecha_actual += timedelta(days=1)
            while fecha_actual.weekday() >= 5 or no_dias_habiles(fecha_actual):
                fecha_actual += timedelta(days=1)

        return fecha_actual
    
    df["NuevaFecha"] = df.apply(calculo_de_fecha, axis=1)

    df["Fecha de entrega Propuesta"] = df["NuevaFecha"]

    df.drop("NuevaFecha", axis=1, inplace=True)

    archivo_output = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])
    if archivo_output:
        df.to_excel(archivo_output, index=False)
        messagebox.showinfo("Éxito", f"El archivo con las fechas actualizadas se ha guardado en: {archivo_output}")


        