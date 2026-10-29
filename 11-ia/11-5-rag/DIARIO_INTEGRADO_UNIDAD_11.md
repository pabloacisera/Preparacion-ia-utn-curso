# DIARIO INTEGRADO UNIDAD 11 - RAG + AGENTES

> **ÚNICA UNIDAD.** Todo va en `11-5-rag/`, organizado por concepto: `01-info/`, `02-formencia/` y `03-oracle/mcp/`. **Se enlaza, no se duplica.**

## ¿Por dónde empezar?
Este archivo es el **hilo único**. Vas a ir leyendo por concepto, mezclando teoría + práctica de ambos cursos (Formencia y Oracle) tal como los vas viendo.

## 1. Fundamentos base
- [11-1 - Introducción a los LLMs](../11-1-introduccion-llms/readme.md)
- [11-1 - Ejercicios](../11-1-introduccion-llms/ejercicios/01-primera-llamada-api.md)
- [11-2 - Funcionamiento interno](../11-2-funcionamiento-interno/readme.md)
- [11-2 - Ejercicios](../11-2-funcionamiento-interno/ejercicios/)

## 2. Preparación e ingesta de documentos
- [Formencia - Preparación de documentos](./02-formencia/0_preparacion_documentos.md)
- [Práctica - Extraer textos](./02-formencia/exercises/0_extraction_text.py)
- [Documentos de prueba](./02-formencia/exercises/_Documentos/)

## 3. Chunking, segmentación y lógica manual
- [Formencia - Segmentación](./02-formencia/1_segementation.md)
- [Práctica - Segmentación completa (sin LangChain)](./02-formencia/exercises/2_segmentartion.py)

## 4. Embeddings, vectores y búsqueda vectorial
- [11-2 - Embeddings y similitud](../11-2-funcionamiento-interno/ejercicios/02-embeddings-y-similitud.md)
- [Formencia - Embeddings](./02-formencia/2_embeddings.md)
- [Práctica - Integrador: lectura, segmentación por capas y embeddings](./02-formencia/exercises/4_segment_and_embedding.py)
- [11-5 - ¿Qué es RAG?](./readme.md)
- [11-5 - Ejercicios](./01-info/)

## 5. RAG with LangChain
- [11-4 - LangChain](../11-4-langchain/readme.md)
- [11-4 - Ejercicios](../11-4-langchain/exercises/)
- [Práctica - Segmentación con LangChain](./02-formencia/exercises/3_segmentation_with_langchain.py)
- [Práctica - Estrategias de segmentación](./02-formencia/exercises/1_strategies_segmentation.py)

## 6. Agentes, herramientas y orquestación
- [11-3 - Teoría de agentes](../11-3-teoria-agentes/readme.md)
- [Oracle - LangChain integration](../11-4-langchain/into_langchain.md)
- [11-4 - Agentes con tools](../11-4-langchain/exercises/01-primer-agente-tools.md)

## 7. MCP + Agente RAG
- [Oracle - MCP](./03-oracle/mcp/into_mcp.md)
- [Oracle - local_server.py](./03-oracle/mcp/local_server.py)
- [Oracle - client.py: cliente MCP local](./03-oracle/mcp/client.py)
- [Oracle - external_api.py: conexión a un MCP externo (GitHub)](./03-oracle/mcp/external_api.py)
- [Oracle - agent_mcp.py: agente con tools de MCP local + GitHub](./03-oracle/mcp/agent_mcp.py)

## 8. Pendientes / Sin clasificar
Se irán agregando los archivos nuevos de Formencia y Oracle conforme avances. **Sin duplicarlos.** Solo se enlazan.
