# Profundización: el modelo por dentro (opcional)

> **No es obligatorio.** Este anexo resume, en una página, cómo se construye un mini-modelo paso a paso, para quien quiera ver la mecánica completa. El resto del curso no depende de esto.

## El viaje de una frase

```
"el gato come"
     │
     ▼  A. Números    → el texto se guarda como números (códigos de caracteres)
     ▼  B. Tokens     → se corta en piezas con un ID cada una
     ▼  C. Predicción → se calcula la probabilidad de cada siguiente token
     ▼  D. Elección   → se elige uno (el más probable o sorteando)
     ▼  E. Bucle      → se agrega y se repite hasta el final
```

Ese modelo mínimo ya "funciona", pero falla de dos formas:

1. **No entiende significado:** para él `gato` y `perro` no tienen relación → lo resuelven los **embeddings**.
2. **Olvida lo anterior:** solo mira lo último → lo resuelve la **atención**.

## Atención (Q, K, V)

La atención es el mecanismo donde cada palabra "decide a quién escuchar". Cada token genera tres vectores:

- **Query (Q):** qué estoy buscando.
- **Key (K):** qué ofrezco.
- **Value (V):** qué contenido aporto.

El parecido entre la Q de un token y las K de los demás (producto punto) da **cuánto peso** darle a cada uno; con esos pesos se combinan los V. Una **máscara causal** impide que un token "mire hacia adelante" (el futuro), porque solo puede usar lo que ya escribió.

## Un transformer, en una línea

Un **transformer** apila muchas capas de atención + pequeñas redes, con **codificación posicional** (marca el orden) y normalizaciones. Ese es el motor que hay dentro de cualquier LLM actual.

## Entrenamiento, en una línea

Entrenar es mostrar mucho texto y **ajustar los pesos** para bajar la **pérdida** (cuánto se equivoca al predecir el token siguiente). Nosotros no entrenamos: **consumimos modelos ya entrenados**, por eso llegamos hasta acá y no más.

## Si querés el recorrido completo

El material original de este curso (ejercicios E01–E11 "a mano" con Python puro y numpy, y la generación local con llama.cpp) es de otra etapa de formación y es mucho más extenso. Se mantiene aparte; este módulo se queda solo con lo **necesario** para entender el sistema.

[Volver al módulo](./readme.md)
