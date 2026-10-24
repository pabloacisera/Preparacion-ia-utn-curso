# Ejercicio 02 — Chunking: fragmentar un documento

**Objetivo:** implementar la **primera etapa** de la tubería de indexación: partir un texto en fragmentos (chunks) con distintas estrategias y comparar resultados. Todo a mano, sin librerías.

## Requisitos

Ninguno. Solo Python.

## Código

```python
TEXTO = """Un RAG combina recuperación y generación. Primero se fragmentan los documentos.
El chunking decide cuánto contexto entra en cada fragmento. Fragmentos muy chicos pierden contexto.
Fragmentos muy grandes meten ruido y consumen más tokens.

La búsqueda vectorial recupera los fragmentos más parecidos a la pregunta.
El resultado se agrega al prompt como contexto."""

def por_tamano(texto, tam=120):
    return [texto[i:i + tam] for i in range(0, len(texto), tam)]

def por_parrafo(texto):
    return [p.strip() for p in texto.split("\n\n") if p.strip()]

def con_solapamiento(texto, tam=120, overlap=20):
    # Avanza de a (tam - overlap): cada fragmento repite el final del anterior.
    paso = tam - overlap
    return [texto[i:i + tam] for i in range(0, len(texto), paso)]

print("--- Por tamaño (120) ---")
for i, c in enumerate(por_tamano(TEXTO)):
    print(f"[{i}] {c!r}\n")

print("--- Por párrafo ---")
for i, c in enumerate(por_parrafo(TEXTO)):
    print(f"[{i}] {c!r}\n")

print("--- Con solapamiento (120, overlap 20) ---")
for i, c in enumerate(con_solapamiento(TEXTO)):
    print(f"[{i}] {c!r}\n")
```

## Qué deberías observar

- El corte **por tamaño fijo** puede partir una palabra al medio.
- El corte **por párrafo** respeta las ideas, pero los fragmentos tienen largos muy distintos.
- El **solapamiento** repite un poco de contexto entre fragmentos vecinos para no perder la continuidad en los bordes.

> Un splitter "recursivo" (corta primero por párrafo, luego por oración y, si hace falta, por carácter) es una versión más elaborada de esto. En el **Módulo 13** veremos que un framework lo trae resuelto, pero acá conviene construirlo a mano para entender qué hace.

## Experimentos

1. Cambiá `tam` a 60 y a 400. ¿Cómo cambia la cantidad de fragmentos?
2. Probá `overlap=0`. ¿Qué problema puede aparecer en los bordes de los fragmentos?
3. Descargá o copiá un documento real (un apunte en texto) y fragmentalo con estas funciones. ¿Qué estrategia funciona mejor para tu caso?

[Volver al módulo](../readme.md)
