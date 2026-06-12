import os
import pandas as pd
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    # Initialize the real OpenAI client if the key is present
    client = OpenAI(api_key=api_key)
    print("[INFO] Successfully connected to OpenAI service.")
else:
    # Fallback to simulation mode if no key is found
    client = None
    print("[WARNING] No OPENAI_API_KEY detected. Running in 'Simulation Mode' (Free).")

def extract_data(file_path):
   
    try:
        df = pd.read_csv(file_path)
        print("[INFO] Datos extraídos correctamente.")
        return df
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")
        return None

def normalize_row_with_ai(name, phone, country):
    """
    Sends dirty row data to OpenAI for normalization.
    Falls back to a local simulation if no API key is provided.
    """
    
    # Structured prompt to guide the AI model's behavior
    prompt = f"""
    Act as an expert data cleansing assistant. Normalize the following customer record:
    Name: {name} -> Must have correct initial capitals and no extra whitespace.
    Phone: {phone} -> If invalid or empty, set to 'N/A'. If valid, use international format.
    Country: {country} -> Standardize capitalization (e.g., 'Mexico', 'Colombia').
    
    Strictly respond with a valid JSON object matching this schema:
    {{"name": "Cleaned Name", "phone": "Cleaned Phone", "country": "Cleaned Country"}}
    """

    # If the OpenAI client is initialized, attempt the API call
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return response.choices[0].message.content
        except Exception:
            # If the API call fails (e.g., billing issues), pass to local simulation
            pass
            
    # LOCAL SIMULATION
    clean_name = str(name).strip().title()
    clean_country = str(country).strip().capitalize()
    clean_phone = str(phone).strip()
    
    if clean_phone == "" or "N/A" in clean_phone or clean_phone == "nan":
        clean_phone = "N/A"
        
    return f'{{"name": "{clean_name}", "phone": "{clean_phone}", "country": "{clean_country}"}}'

dirty_df = extract_data("datos_clientes.csv")

if dirty_df is not None:
    print("\n[PROCESS] Starting data normalization...")
    
    # Take the first 5 rows for local testing to get instant results
    test_df = dirty_df.head(5).copy()
    
    normalization_results = []
    for idx, row in test_df.iterrows():
        print(f"-> Processing row ID {row['id']}...")
        
        # Call the AI/Fallback normalization function
        json_result = normalize_row_with_ai(row['nombre'], row['telefono'], row['pais'])
        normalization_results.append(json_result)
        
    print("\n Process Finished Successfully! ")
    print("Structured JSON results ready for database insertion:")
    for result in normalization_results:
        print(result)

