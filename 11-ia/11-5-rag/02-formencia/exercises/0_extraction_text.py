# %%
from pypdf import PdfReader
from pathlib import Path

# Creamos un error personalizado
class InvalidDocPathError(Exception):
    """Exception raised when a directory or file path does not exist."""
    pass

# Definimos el nombre de la función y el parametro que requiere
def read_pdf(route: str)->str:

    # Verificar si la ruta existe
    path_file = Path(route)

    if not path_file.exists():
        raise InvalidDocPathError("Directory or file does not exist.")

    # Bloque try-except para capturar errores del proceso
    try:
        pdf_document = PdfReader(path_file)
        complete_document:list = []

        for page in pdf_document.pages:
            text = page.extract_text()
            if text:
                complete_document.append(text)
        # Cuando termine de recorrer podemos mostrar lo que extrajo
        return "\n".join(complete_document)
    except Exception as e:
        return f"Error in process {str(e)}"

read_pdf("_Documentos/prueba_lectura.pdf")

# %%
from PIL import Image
from pytesseract import pytesseract

def extract_and_read_image(route: str)-> str:

    # Verificar si la ruta existe
    path_file = Path(route)
    print(path_file)

    if not path_file.exists():
        raise InvalidDocPathError("Directory or file does not exist.")

    try:
        # Abrimos la imagen
        image = Image.open(route)

        # Extraemos el texto de la imagen
        text = pytesseract.image_to_string(image, lang="spa") # configuramos el lenguaje de la imagen

        return text
    except Exception as e:
        return f"Error en OCR: {str(e)}"

extract_and_read_image("_Documentos/prueba_ocr.png")

# %%
%pip install pandas openpyxl tabulate

# %%
import pandas as pd
from IPython.display import display, Markdown

def extract_text_to_excel(route: str)-> str:

    path_file = Path(route)
    print(path_file.exists()) # Devolverá True o False

    if not path_file.exists():
        raise InvalidDocPathError("Directory or file does not exist.")

    try:
        # Obtenemos el archivo y lo abrimos
        df = pd.read_excel(path_file)
        return df.to_markdown(index=False)
    except Exception as e:
        return f"Error to extract: {str(e)}"

display(Markdown(extract_text_to_excel("_Documentos/prueba_datos.xlsx")))


# %%
import docx

def read_doc(route):

    path_file = Path(route)
    print(path_file.exists())

    if not path_file.exists():
        raise InvalidDocPathError("Directory or file does not exist.")

    try:
        # Cargamos el archivo
        doc = docx.Document(path_file)
        text_document = []

        for line in doc.paragraphs:
            text_document.append(line.text)

        return "\n".join(text_document)
    except Exception as e:
        return f"Error to read file: {str(e)}"

read_doc("_Documentos/prueba_documento.docx")

# %%
import time


def get_route_file():
    while True:
        path_file = input("Introduzca ruta o nombre del archivo: ").strip()
        if not path_file:
            print("Ruta o directorio inválido. Intente de nuevo.")
            continue
        return path_file


def select_option():
    while True:
        print("\n=== Panel de Control (Opciones) ===")
        print("1. docx")
        print("2. pdf")
        print("3. xlsx")
        print("4. png/jpg/jpeg")

        option = input("Seleccione una opción (escriba 'exit' para salir): ").strip()

        # Validación de salida limpia antes de convertir a entero
        if option.lower() == "exit":
            print("Saliendo del programa...")
            time.sleep(0.5)
            return None

        # Validación segura de rango numérico
        if option in ["1", "2", "3", "4"]:
            print(f"Opción seleccionada correctamente: {option}\n")
            return option  # Retorna y rompe el bucle automáticamente

        print("La opción seleccionada no es válida. Elija un número del 1 al 4.")

option = select_option()

if option:
    path_file = get_route_file()

    match option:
        case "1":
            print("\n--- Contenido extraído del archivo Word ---")
            print(read_doc(path_file))
        case "2":
            print("\n--- Contenido extraído del archivo PDF ---")
            print(read_pdf(path_file))
        case "3":
            print("\n--- Contenido estructurado de la tabla Excel ---")
            # Usamos display y Markdown para que en .ipynb se renderice visualmente
            tabla_md = extract_text_to_excel(path_file)
            if not tabla_md.startswith("Error"):
                display(Markdown(tabla_md))
            else:
                print(tabla_md)
        case "4":
            print("\n--- Texto procesado por el motor OCR ---")
            print(extract_and_read_image(path_file))


