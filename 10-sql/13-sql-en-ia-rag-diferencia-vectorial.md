# 13 - SQL en IA, RAG y diferencia con búsqueda vectorial

## Objective
Conocer cómo se usa SQL en el mundo de LLMs, agentes, RAG and la diferencia con las bases vectoriales.

## ¿Cuándo usar SQL vs Búsqueda Vectorial?

Ambos sirven para buscar información, pero **de formas distintas**.

| Aspecto | **SQL (Relacional)** | **Búsqueda Vectorial (RAG)** | 
|---|---|---|
| **Tipo de búsqueda** | Exacta o por filtros (`WHERE`, `LIKE`) | Semántica (por significado) |
| **Datos** | Estructurados (tablas, filas, columnas) | No estructurados (texto, PDFs, documentos) |
| **Pregunta típica** | *"¿Cuántos pedidos hizo Ana?"* | *"¿Qué dice el manual sobre garantías?"* |
| **Resultado** | Datos exactos y calculados | Fragmentos de texto con mayor similitud |
| **Precisión** | Muy precisa | Aproximada, basada en similitud |
| **Ejemplo** | SQLite, PostgreSQL | Chroma, Qdrant, Weaviate |

## ¿Cómo se usa SQL en IA?

Los agentes usan **herramientas SQL** para responder con datos reales:

1. **Text-to-SQL**: El usuario pregunta en lenguaje natural → el LLM genera SQL → se ejecuta en la base → se devuelve la respuesta.
2. **Agentes con herramientas**: El agente decide cuándo usar `SQLTool` vs otras herramientas.
3. **Consultas híbridas**: Combinar datos SQL + contexto del RAG para respuestas más completas.

## ¿Cómo se usa en RAG?

En un sistema RAG tradicional:
- Los documentos se dividen en trozos (chunks).
- Se convierten a **vectores** con una API de embeddings.
- Se guardan en una **base vectorial**.
- Al preguntar, se busca por **similitud semántica** los chunks más cercanos.

Ahí **no** se usa SQL para buscar por significado, se usa **búsqueda vectorial**.

## ¿Cuándo conviene combinar ambos?

| Caso | Recomendado |
|---|---|
| **Inventario, ventas, facturación** | **SQL** - datos exactos, contados, filtrados |
| **Manual de usuario, FAQ, políticas** | **Vectorial/RAG** - buscar por significado |
| **"¿Cuántos productos hay bajo stock?"** | **SQL** - respuesta directa, exacta |
| **"¿Cómo configuro la VPN?"** | **RAG** - busca en manuales, documentos |
| **Agente empresarial** | **Híbrido** - SQL + RAG (lo mejor de ambos) |

## La clave para recordar

- **SQL** = *"Dime qué hay"* (filtros, conteos, joins)
- **Vectorial** = *"Dime qué dice"* (significado, contexto, documentos)

## Recapitulación

- SQL busca por **campos/valores**. Vectorial busca por **similitud semántica**.
- Los agentes pueden generar SQL desde lenguaje natural (**Text-to-SQL**).
- En proyectos reales **SQL + RAG** se complementan, no compiten.

[← Anterior: Migraciones](./12-migraciones.md) | [Índice](./README.md) | [Siguiente: Práctica integrada →](./14-practica-integrada-esquema-inventado.md)
