import os
import fitz
import google.generativeai as genai

API_KEY = "AIzaSyCyk08TLRfsamf8ePvW0fElhFfy8z2NNIU"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

def leer_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def extraer_datos_factura(contenido_pdf):
    prompt = f"""
Extrae de esta factura lo siguiente:

- Nombre del proveedor
- RUC / NIT
- Razón Social / Nombres y Apellidos:
- Número de factura
- Fecha de emisión
- Monto total
- Moneda
- IGV / IVA (si aplica)
- Detalles de productos o servicios

Devuélvelo como una lista clara. No expliques nada más.

Contenido:
\"\"\"{contenido_pdf}\"\"\"
"""
    response = model.generate_content(prompt)
    return response.text

carpeta_pdfs = "C:/Users/Karina/Downloads/Facturas"
archivos_pdf = [f for f in os.listdir(carpeta_pdfs) if f.lower().endswith(".pdf")]

for archivo in archivos_pdf:
    ruta = os.path.join(carpeta_pdfs, archivo)
    print(f"\n📄 Procesando: {archivo}")
    texto = leer_pdf(ruta)
    datos = extraer_datos_factura(texto)
    print(f"✅ Datos encontrados:\n{datos}")
    print("-" * 50)
