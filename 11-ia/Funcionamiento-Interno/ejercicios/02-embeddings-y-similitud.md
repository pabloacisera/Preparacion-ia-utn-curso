# Ejercicio 02 — Embeddings y similitud

**Objetivo:** convertir oraciones en vectores y medir cuánto se parecen. Es la base del RAG: comparar la pregunta del usuario con los documentos.

## Requisitos

```bash
pip install fastembed numpy
```

> La primera ejecución descarga un modelo de ~0.22 GB en `./cache_modelos`.

## Código

```python
import numpy as np
from fastembed import TextEmbedding

# Modelo multilingüe y liviano (0.22 GB, 384 dimensiones)
modelo = TextEmbedding("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                       cache_dir="./cache_modelos")

frases = [
    "El gato come pescado.",
    "Un felino se alimenta de peces.",        # mismo sentido, casi sin palabras en común
    "El perro duerme en el jardín.",
    "El banco cerró por la tarde.",
    "Nos sentamos en el banco del parque.",    # 'banco' con otro sentido
]

V = np.array(list(modelo.embed(frases)))       # matriz (frases, dimensiones)
print("Forma:", V.shape)

# Normalizamos: con vectores de largo 1, coseno = producto punto
V = V / np.linalg.norm(V, axis=1, keepdims=True)
S = V @ V.T                                    # similitud de todas contra todas

np.set_printoptions(precision=2, suppress=True)
print("Matriz de similitud:\n", S)
```

## Qué deberías observar

- La matriz `S` es **simétrica** y su diagonal vale 1 (cada frase es idéntica a sí misma).
- La similitud entre las frases **0 y 1** (mismo sentido, otras palabras) debería ser **alta**.
- Las frases **3 y 4** usan `banco` con sentidos distintos: observá si el modelo las acerca o las separa.

## Experimentos

1. Agregá pares de frases con el mismo sentido pero palabras distintas y contá cuántos acierta.
2. Probá una frase muy larga (600 palabras). ¿Qué pasa? (pista: hay un límite de tokens).
3. Medí `du -sm cache_modelos` y comprobá cuánto ocupa el modelo en disco.

[Volver al módulo](../readme.md)
