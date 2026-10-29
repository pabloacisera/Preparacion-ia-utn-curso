import tiktoken
from langchain_text_splitter import RecursiveCharacterTextSplitter

# =====================================================================
# MODULO 0: CARGAR EL DOCUMENTO DE PRUEBA
# =====================================================================
with open("documento_prueba.txt", "r", encoding="utf-8") as f:
    lineas_documento = [linea.rstrip() for linea in f if linea.strip()]


# =====================================================================
# MODULO 1: SEGMENTACIÓN POR CLASE (Reglas Simples)
# =====================================================================
def segmentar_por_clase(lineas):
    """
    Agrupa las líneas según su tipo de contenido (Clase).
    """
    bloques = []
    for linea in lineas:
        if "|" in linea:
            bloques.append({"clase": "tabla", "texto": linea})
        elif linea.startswith("def ") or linea.startswith("    print"):
            bloques.append({"clase": "codigo", "texto": linea})
        else:
            bloques.append({"clase": "texto", "texto": linea})
    return bloques


# =====================================================================
# MODULO 2: SEGMENTACIÓN SEMÁNTICA SIMPLIFICADA (Concepto de Embeddings)
# =====================================================================
def segmentar_semantica_manual(bloques):
    """
    Agrupa el texto plano por significado usando palabras clave.
    Las tablas y códigos pasan de largo sin tocarse.
    """
    chunks_logicos = []
    acumulador_texto = []
    conectores_cambio_tema = ["Por otro lado,", "En cuanto a"]

    for b in bloques:
        if b["clase"] == "texto":
            cambio_tema = any(b["texto"].startswith(c) for c in conectores_cambio_tema)
            if cambio_tema and acumulador_texto:
                chunks_logicos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})
                acumulador_texto = [b["texto"]]
            else:
                acumulador_texto.append(b["texto"])
        else:
            if acumulador_texto:
                chunks_logicos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})
                acumulador_texto = []
            chunks_logicos.append({"tipo": b["clase"], "contenido": b["texto"]})

    if acumulador_texto:
        chunks_logicos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})
    return chunks_logicos


# =====================================================================
# MODULO 3: UTILERÍA DE TOKENS (Con tiktoken)
# =====================================================================
def contar_tokens(texto: str) -> int:
    """
    Cuenta cuántos tokens tiene un texto usando el tokenizador de OpenAI.
    """
    encoder = tiktoken.get_encoding("cl100k_base")
    return len(encoder.encode(texto))


# =====================================================================
# MODULO 4: SEGMENTACIÓN FIJA RECURSIVA POR TOKENS (Con LangChain)
# =====================================================================
def aplicar_splitter_langchain(chunks_previos, max_tokens=30):
    """
    Usa el RecursiveCharacterTextSplitter medido en TOKENS reales.
    Solo fragmenta los bloques de texto que se pasen del límite de tokens.
    """
    chunks_finales = []
    
    # Configuramos el splitter de LangChain usando nuestra función de conteo de tokens
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_tokens,
        chunk_overlap=5,
        length_function=contar_tokens,
        separators=["\n\n", "\n", " ", ""]
    )

    for chunk in chunks_previos:
        tipo = chunk["tipo"]
        texto = chunk["contenido"]

        # Si el texto procesado por semántica sigue siendo muy largo en tokens, lo refinamos
        if tipo == "texto_semantico" and contar_tokens(texto) > max_tokens:
            sub_chunks = text_splitter.split_text(texto)
            for sub in sub_chunks:
                chunks_finales.append(f"CHUNK [TEXTO - RECURSIVE TOKENS]:\n{sub}")
        else:
            # Las tablas y códigos preservan su estructura íntegra tal como entraron
            chunks_finales.append(f"CHUNK [{tipo.upper()} INTEGRAL]:\n{texto}")

    return chunks_finales


# =====================================================================
# EJECUCIÓN DEL PIPELINE FUSIONADO
# =====================================================================

# 1. Separar por clases básicas
bloques_clase = segmentar_por_clase(lineas_documento)

# 2. Agrupar semánticamente (Mantenemos la simulación conceptual de embeddings)
bloques_semanticos = segmentar_semantica_manual(bloques_clase)

# 3. Aplicar control estricto de tamaño usando LangChain + Tiktoken
# Bajamos el límite a 20 tokens para obligar al splitter de LangChain a trabajar
resultado = aplicar_splitter_langchain(bloques_semanticos, max_tokens=20)

# Mostrar los fragmentos limpios en pantalla
print(f"=== PIPELINE COMPLETADO: {len(resultado)} CHUNKS ===")
for idx, chunk in enumerate(resultado):
    print(f"Fragmento {idx + 1}:\n{chunk}")
    print("-" * 50)
