# Ejercicio 03 — Cómo predice el modelo

**Objetivo:** entender, con números, el paso que va de **puntajes (logits)** a **probabilidades (softmax)** y cómo la **temperatura** cambia la elección. No hace falta ningún modelo: usamos valores de ejemplo.

## Requisitos

```bash
pip install numpy
```

## Código

```python
import numpy as np

def softmax(x):
    x = x - x.max()          # estabilidad numérica
    e = np.exp(x)
    return e / e.sum()

# Puntajes crudos que "devolvería" el modelo para el siguiente token.
# Imaginemos el vocabulario [" pescado", " carne", " pan", " auto"]
logits = np.array([3.0, 2.0, 1.0, -1.0])
vocab = [" pescado", " carne", " pan", " auto"]

for temp in (0.0, 0.5, 1.0, 2.0):
    if temp == 0.0:
        elegido = int(np.argmax(logits))            # greedy
        print(f"temp={temp}: greedy → {vocab[elegido]!r}")
        continue
    p = softmax(logits / temp)
    elegido = int(np.argmax(p))
    print(f"temp={temp}: probs={np.round(p, 2)} → más probable: {vocab[elegido]!r}")
```

## Qué deberías observar

- Con `temp=0` (greedy) siempre gana el más probable: `" pescado"`.
- Temperaturas **bajas** concentran la probabilidad en los primeros; temperaturas **altas** la reparten y todo se vuelve más "plano" (más variado).
- El softmax **siempre** da probabilidades que suman 1.

## Experimentos

1. Cambiá `logits` para que los dos primeros queden casi iguales (`[2.0, 1.9, ...]`) y observá cómo la temperatura decide entre ellos.
2. Implementá **top-k**: poné en cero todo lo que no esté entre los `k` más probables y renormalizá. ¿Cómo cambia la elección?
3. Repetí la elección con `np.random.choice(len(p), p=p)` varias veces con `temp=1.0` y comprobá que el resultado varía.

[Volver al módulo](../readme.md)
