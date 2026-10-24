# 08 - APIs en IA: LLMs, embeddings y más

## Objetivo

Identificar qué APIs se usan para construir agentes y sistemas RAG.

## Principales APIs que vas a encontrar

| Servicio | Para qué | Ejemplo |
|---|---|---|
| **Chat Completions API** | Preguntar al LLM y obtener respuesta | Groq, OpenRouter, Google Gemini |
| **Embeddings API** | Convertir texto a vectores numéricos | `text-embedding-3-small`, `mxbai-embed` |
| **Vector DB API** | Guardar/buscar vectores (búsqueda semántica) | Chroma, Qdrant, Upstash Vector |
| **Tools / Function Calling** | Permitir que el modelo llame funciones | OpenAI-compatible |
| **File Upload / Retrieval** | Subir documentos para usar en RAG | Algunos proveedores |

## ¿Por qué embeddings?

Un **embedding** es una representación numérica del significado de un texto. Dos textos con significado parecido tienen vectores cercanos.

Gracias a eso, en RAG podés buscar **por significado**, no solo por palabras exactas.

```python
# Idea simplificada
"gato" y "felino" → vectores cercanos
"gato" y "avión"  → vectores lejanos
```

## Flujo típico de un RAG con APIs

```
1. Documento (PDF/TXT) → Embeddings API → Vectores
2. Vectores → Guardar en Vector DB (API/SDK)
3. Pregunta usuario → Embeddings API → Vector de pregunta
4. Buscar similares en Vector DB → Fragmentos relevantes
5. Armar prompt con fragmentos + pregunta → Chat Completions API → Respuesta
```

## Flujo típico de un agente con APIs

```
1. Usuario pregunta
2. Agente decide: ¿necesita herramienta?
3. Si sí → llama API (buscar, calcular, enviar)
4. Recibe resultado de esa API
5. Pasa resultado al LLM → genera respuesta final
```

## ¿OpenAI-compatible?

Muchos proveedores usan el **mismo formato** que OpenAI:
- Mismo endpoint `/chat/completions`
- Mismos campos `messages`, `model`, `temperature`

Eso te permite cambiar de proveedor (Groq → OpenRouter) con **cambiar solo la URL y la API key**. Muy útil para aprender.

## Recapitulación

- **Chat Completions** = hablar con el LLM.
- **Embeddings** = entender significado numéricamente.
- **Vector DB** = buscar por similitud.
- **Agentes** = combinan todo esto llamando APIs como herramientas.

[← Anterior: Versionado en IA](./07-versionado-en-ia.md) | [Índice](./README.md) | [Siguiente: Ejercicios con curl →](./09-ejercicios-con-curl.md)
