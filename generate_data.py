
import random
import pandas as pd

# Listas base para combinar datos al azar
nombres = [" jOSe mIGUel ", "maria elena", "Carlos R.", " ana gomez ", "LUIS perez", "Sofia m.", " dIego "]
apellidos = ["Ramirez", " Lopez", "Martinez ", "Gomez", " rOdRiGuEz", " Sanchez"]
telefonos = ["555-123-456", "  +52 555 987 654 ", "N/A", "1234567", "+57 300 111 222", "  "]
paises = ["mexico", "MEXICO", "colombia", "COLOMBIA", "argentina", "ARGENTINA", "chile"]

print("[INFO] Generando 10,000 registros sucios...")

# Crear la lista de 10k datos usando un bucle
raw_data = []
for i in range(1, 10001):
    fila = {
        "id": i,
        "name": random.choice(nombres) + random.choice(apellidos),
        "phone": random.choice(telefonos),
        "country": random.choice(paises)
    }
    raw_data.append(fila)

# Convertir a DataFrame y guardar en un archivo CSV
df = pd.DataFrame(raw_data)
df.to_csv("clients_raw_data.csv", index=False)

print("[CORRECTO] Archivo 'clients_raw_data.csv' creado con 10,000 filas.")