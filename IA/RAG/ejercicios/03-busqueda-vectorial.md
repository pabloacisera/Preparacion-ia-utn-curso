# Ejercicio 03 — De fragmentos a vectores y búsqueda

**Objetivo:** completar la segunda y tercera etapa de la indexación (embeddings + base vectorial) y la recuperación (**top-k**), todo de forma mínima con numpy. Es el corazón del RAG.

## Requisitos

```bash
pip install fastembed numpy
```

## Código

```python
import numpy as np
from fastembed import TextEmbedding

modelo = TextEmbedding("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                       cache_dir="./cache_modelos")

# (Simulamos los "fragmentos" de la etapa de chunking)
fragmentos = [
    "El gato come pescado.",
    "Los perros duermen en el jardín.",
    "El banco cerró por la tarde.",
    "La capital de Francia es París.",
    "Los felinos se alimentan de peces.",
]

# --- Tubería de indexación: fragmentos -> vectores ---
V = np.array(list(modelo.embed(fragmentos)))
V = V / np.linalg.norm(V, axis=1, keepdims=True)   # normalizamos (coseno = producto punto)

def recuperar(pregunta, k=2):
    q = np.array(list(modelo.embed([pregunta])))[0]
    q = q / np.linalg.norm(q)
    similitudes = V @ q                             # similitud contra cada fragmento
    orden = np.argsort(-similitudes)[:k]            # top-k
    return [(fragmentos[i], float(similitudes[i])) for i in orden]

# --- Tubería de consulta ---
for pregunta in ["¿De qué se alimenta el gato?", "¿Dónde está París?"]:
    print(f"\nPregunta: {pregunta}")
    for texto, score in recuperar(pregunta):
        print(f"  {score:.3f}  {texto}")
```

## Qué deberías observar

- Para *"¿De qué se alimenta el gato?"* deberían aparecer los fragmentos sobre **gatos/felinos**, aunque no compartan palabras exactas.
- Las puntuaciones más altas corresponden a los fragmentos más parecidos (top-k).
- Esta recuperación es la que **alimentaría el prompt** del LLM.

## Experimentos

1. Agregá fragmentos que hablen de temas distintos y hacé preguntas "trampa".
2. Subí `k` a 3 y 4: ¿entra ruido?
3. ¿Qué pasa si buscás algo que **no está** en la lista? ¿La mejor puntuación es alta o baja?

## Para pensar

Esta base vectorial es "de juguete" (está en memoria). Una base real (Chroma, pgvector, faiss) agrega persistencia, escala y búsqueda ANN. La lógica, sin embargo, es la misma.

[Volver al módulo](../readme.md)
