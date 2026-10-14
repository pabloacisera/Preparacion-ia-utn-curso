# Ejercicio 01 — Diseccionar el flujo de un RAG

**Objetivo:** entender el flujo completo antes de programar nada. Este ejercicio es de lectura y análisis del readme del módulo.

## Consigna

1. Explicá con tus palabras la diferencia entre la **tubería de indexación** y la **tubería de consulta**. ¿Cuál corre una sola vez y cuál en cada pregunta?
2. Ordená estos pasos en la tubería que corresponda:

   - generar la respuesta con el LLM
   - fragmentar los documentos
   - buscar por similitud
   - convertir la pregunta a un vector
   - almacenar los vectores
   - convertir los fragmentos a vectores
   - aumentar el prompt con los fragmentos recuperados

3. ¿Por qué la **pregunta** y los **documentos** deben usar el **mismo** modelo de embeddings?
4. Con tus palabras: ¿cómo resuelve RAG el problema de la **memoria a largo plazo**?

## Desafío extra

Explicá, sin mirar el readme, por qué RAG reduce las alucinaciones y por qué es más barato que reentrenar el modelo.

[Volver al módulo](../readme.md)
