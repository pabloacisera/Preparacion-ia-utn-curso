# %%
from langchain_text_splitters import CharacterTextSplitter

# Obtenemos el texto
document = ""

with open("_Documentos/doc_for_chunk.txt") as f:
    document = f.read()

# Dividimos el texto en chunks
# CharacterTextSplitter por defecto corta en salto de linea \n\n
basic_splitter = CharacterTextSplitter(
    separator="\n\n", chunk_size=400, chunk_overlap=80
)

basic_segments = basic_splitter.create_documents([document])

print(f"Total de fragmentos: {len(basic_segments)}")

for i, chunk in enumerate(basic_segments[:3]):  # develve la poscion 0 y 1
    print(f"Fragmento {i}: \n{chunk.page_content}\n")

# Resultado: En lugar de romper la oración por la mitad de forma brusca en el carácter 400, el método prioriza el separador \n\n

# %%
from langchain_text_splitters import RecursiveCharacterTextSplitter

document = ""

with open("_Documentos/doc_for_chunk.txt") as f:
    document = f.read()

recursive_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=80)

segments = recursive_splitter.create_documents([document])

print(f"Segmentos totales: {len(segments)}")

for i, c in enumerate(segments[:4]):
    print(f"Segmentos {i}: \n{c.page_content}\n")

# %%
from langchain_text_splitters import MarkdownTextSplitter

document = ""

with open("_Documentos/doc_for_chunk.txt") as f:
    document = f.read()

md_splitter = MarkdownTextSplitter(chunk_size=400, chunk_overlap=80)

md_segments = md_splitter.create_documents([document])

print(f"Segmentos: {len(md_segments)}")

for i, c in enumerate(md_segments[:4]):
    print(f"Segmento {i}: \n{c.page_content}\n")

# Toma los simbolos como # o ## y los utiliza como factor de corte ademas del tamaño del chunk(chunk=caracteres)

# %%
from langchain_text_splitters import TokenTextSplitter

document = ""

with open("_Documentos/doc_for_chunk.txt") as f:
    document = f.read()

ts = TokenTextSplitter(chunk_size=5, chunk_overlap=1)

segments = ts.create_documents([document])

print(f"Segmentos: {len(segments)}")

# Tokens puros, cortes matematicos
for i, c in enumerate(segments[:4]):
    print(f"Segmento {i}: \n{c.page_content}\n")

# Casi nunca se usa para PDFs o texto libre. Se utiliza únicamente cuando el formato original no importa en absoluto y necesitas un control matemático destructivo del espacio. Por ejemplo, al pasarle a la IA listas masivas de números de serie, logs de servidores muy largos, datos crudos de sensores, o código de programación donde necesitas garantizar que entre exactamente una cantidad fija de tokens en la ventana de contexto sin importar dónde corte.

# %%
# Este es el estándar para el 95% de los casos reales (PDFs, Word, imágenes OCR, páginas web). Aquí se mezcla lo mejor de ambos mundos: el algoritmo analiza el texto buscando puntos, comas y espacios (para no romper el lenguaje humano), pero mide el tamaño del fragmento usando el tokenizador de la IA en lugar de contar letras.

from langchain_text_splitters import RecursiveCharacterTextSplitter

document = ""

with open("_Documentos/doc_for_chunk.txt") as f:
    document = f.read()

# La Combinación Perfecta:
# Corta de forma inteligente (párrafos, puntos, espacios)
# pero el tamaño se calcula en TOKENS nativos de la IA
splitter_hibrido = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",  # Le dice qué "idioma" de tokens habla tu IA
    chunk_size=100,  # 100 TOKENS de capacidad máxima por fragmento
    chunk_overlap=20,  # 20 TOKENS de solapamiento
)

chunks_hibridos = splitter_hibrido.create_documents([document])

print("--- MÉTODO HÍBRIDO (El estándar de la industria) ---")
print(f"Total de fragmentos logrados: {len(chunks_hibridos)}")
for i, chunk in enumerate(chunks_hibridos[:5]):
    print(f"\nChunk {i} (Cortado en un espacio/punto limpio, pero midiendo tokens):")
    print(chunk.page_content)

# %%
