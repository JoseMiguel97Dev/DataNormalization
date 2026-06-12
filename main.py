import os
import pandas as pd
import openai as OpenAI

#AI client configuration
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_data(file_path):
   
    try:
        df = pd.read_csv(file_path)
        print("[INFO] Datos extraídos correctamente.")
        return df
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")
        return None
    
datos_cargados = extract_data("datos_clientes.csv")

# Si el archivo tiene datos, mostramos los primeros 5 en la pantalla
if datos_cargados is not None:
    print("\n--- Mostrando las primeras filas del archivo ---")
    print(datos_cargados.head())

