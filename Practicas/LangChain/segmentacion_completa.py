# =====================================================================
# MODULO 0: CARGAR EL DOCUMENTO DE PRUEBA
# =====================================================================

# Leemos el archivo línea por línea eliminando saltos de página colgados
with open("documento_prueba.txt", "r", encoding="utf-8") as f:
    lineas_documento = [linea.rstrip() for linea in f if linea.strip()]


# =====================================================================
# MODULO 1: SEGMENTACIÓN POR CLASE (Estructura Básica)
# =====================================================================
def segmentar_por_clase(lineas):
    """
    Identifica el tipo de contenido (Clase) de cada línea.
    Separa las tablas y bloques de código del texto plano.
    """
    bloques_clasificados = []
    
    for linea in lineas:
        # REGLA CLASE TABLA: Si contiene el cañito '|', es una tabla
        if "|" in linea:
            bloques_clasificados.append({"clase": "tabla", "texto": linea})
            
        # REGLA CLASE CÓDIGO: Si empieza con def o print, es código python
        elif linea.startswith("def ") or linea.startswith("    print"):
            bloques_clasificados.append({"clase": "codigo", "texto": linea})
            
        # REGLA CLASE TEXTO: Cualquier otra cosa es texto plano
        else:
            bloques_clasificados.append({"clase": "texto", "texto": linea})
            
    return bloques_clasificados


# =====================================================================
# MODULO 2: SEGMENTACIÓN SEMÁNTICA SIMPLIFICADA (Y Concepto de Embedding)
# =====================================================================
def segmentar_semantica_y_embeddings(bloques):
    """
    Toma los bloques. Si son texto plano, busca conectores de cambio de tema
    (Semántica). Aquí es donde a futuro los Embeddings calcularán la similitud
    numérica para decidir si se corta o no el fragmento.
    """
    chunks_semanticos = []
    acumulador_texto = []
    
    # Conectores manuales para simular el cambio de idea (Semántica sin embeddings)
    conectores_cambio_tema = ["Por otro lado,", "En cuanto a"]

    for bloque in bloques:
        clase = bloque["clase"]
        contenido = bloque["texto"]

        if clase == "texto":
            # REGLA SEMÁNTICA: ¿La línea actual empieza con un cambio de tema?
            cambio_de_tema_detectado = any(contenido.startswith(c) for c in conectores_cambio_tema)
            
            # --- SIMPLIFICACIÓN CONCEPTUAL DE EMBEDDINGS ---
            # En la próxima unidad, en lugar de usar la lista 'conectores_cambio_tema', harás esto:
            # vector_oracion_1 = modelo.generar_embedding(acumulador_texto)
            # vector_oracion_2 = modelo.generar_embedding(contenido)
            # si_distancia_numerica_es_grande = True -> Cortar Chunk
            # -----------------------------------------------

            if cambio_de_tema_detectado and acumulador_texto:
                # Guardamos la idea anterior acumulada antes de empezar la nueva
                chunks_semanticos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})
                acumulador_texto = [contenido]
            else:
                acumulador_texto.append(contenido)
        else:
            # Si veníamos guardando texto y aparece una tabla o código, cerramos el texto pendiente
            if acumulador_texto:
                chunks_semanticos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})
                acumulador_texto = []
            
            # Las tablas y códigos pasan directo para no romper su estructura interna
            chunks_semanticos.append({"tipo": clase, "contenido": contenido})

    # No olvidar guardar el último texto que quedó en el acumulador
    if acumulador_texto:
        chunks_semanticos.append({"tipo": "texto_semantico", "contenido": " ".join(acumulador_texto)})

    return chunks_semanticos


# =====================================================================
# MODULO 3: SEGMENTACIÓN FIJA RECURSIVA (Fase Final de Control)
# =====================================================================
def aplicar_segmentacion_fija_recursiva(chunks_previos, max_caracteres=100):
    """
    Recibe los chunks lógicos anteriores. Como última capa de seguridad,
    si un chunk de texto quedó demasiado largo, aplica una división fija 
    recursiva (por caracteres o palabras) para garantizar que el tamaño sea manejable.
    """
    chunks_finales_limpios = []

    for chunk in chunks_previos:
        tipo = chunk["tipo"]
        texto = chunk["contenido"]

        # Si el fragmento es de texto y supera el tamaño máximo permitido
        if tipo == "texto_semantico" and len(texto) > max_caracteres:
            # Segmentación fija recursiva simple: cortamos en partes del tamaño máximo
            for i in range(0, len(texto), max_caracteres):
                sub_texto = texto[i:i + max_caracteres]
                chunks_finales_limpios.append(f"CHUNK [TEXTO FIJO RECURSIVO]:\n{sub_texto}")
        else:
            # Las tablas, códigos o textos cortos se mantienen intactos
            chunks_finales_limpios.append(f"CHUNK [{tipo.upper()} INTEGRAL]:\n{texto}")

    return chunks_finales_limpios


# =====================================================================
# PIPELINE PRINCIPAL: EJECUCIÓN UNITARIA PASO A PASO
# =====================================================================

print("--- PASO 1: Ejecutando Segmentación por Clase ---")
bloques_clase = segmentar_por_clase(lineas_documento)
print(f"Líneas procesadas y clasificadas en estructuras lógicas.\n")

print("--- PASO 2: Aplicando Lógica Semántica (Simulada) ---")
bloques_semanticos = segmentar_semantica_y_embeddings(bloques_clase)
print(f"Ideas separadas por temática y tipos aislados.\n")

print("--- PASO 3: Control Final con Segmentación Fija ---")
# Limitamos a 100 caracteres para forzar que el texto largo se divida de forma fija
resultado_chunks = aplicar_segmentacion_fija_recursiva(bloques_semanticos, max_caracteres=100)

print(f"=== RESULTADO FINAL: {len(resultado_chunks)} CHUNKS GENERADOS ===")
for idx, chunk_final in enumerate(resultado_chunks):
    print(f"Fragmento {idx + 1}:")
    print(chunk_final)
    print("-" * 50)
