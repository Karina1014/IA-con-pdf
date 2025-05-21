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

def preguntar_sobre_pdf(contenido_pdf, pregunta_usuario):
    prompt = f"""Basándote estrictamente en el siguiente contenido del PDF, responde de forma clara:

Contenido del PDF:
\"\"\"
{contenido_pdf}
\"\"\"

Pregunta:
{pregunta_usuario}
"""
    response = model.generate_content(prompt)
    return response.text

ruta_pdf = "C:/Users/Karina/Downloads/Factura.pdf"
contenido_pdf = leer_pdf(ruta_pdf)

print("¡PDF cargado exitosamente! Puedes hacer preguntas sobre su contenido.")
print("Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("¿Qué quieres preguntarle al PDF? ")
    
    if pregunta.lower() == "salir":
        print("👋 Saliendo del chatbot. ¡Hasta luego!")
        break

    respuesta = preguntar_sobre_pdf(contenido_pdf, pregunta)
    print(f"\nRespuesta:\n{respuesta}\n")
