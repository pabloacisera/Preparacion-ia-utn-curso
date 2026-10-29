# GUIA DE ORDENAMIENTO FUTURO: RAG + AGENTES

> **ÚNICA UNIDAD:** Todo va en `11-ia/11-5-rag/`. Ahí está el `DIARIO_INTEGRADO_UNIDAD_11.md`.
> **SOLO SE PUEDE TOCAR:** `11-ia/`
> **REGLA ABSOLUTA:** **ENLAZAR, NO DUPLICAR.**

## Estructura actual

```text
11-ia/
├── 11-4-langchain/
│   ├── exercises/          # Ejercicios de LangChain
│   ├── into_langchain.md   # Integración con LangChain
│   └── readme.md
├── 11-5-rag/
│   ├── 01-info/            # Teoría y ejercicios base de RAG
│   ├── 02-formencia/       # Preparación, segmentación y embeddings
│   │   └── exercises/      # Prácticas y documentos de prueba
│   ├── 03-oracle/mcp/      # MCP: teoría y prácticas
│   ├── DIARIO_INTEGRADO_UNIDAD_11.md
│   └── readme.md
└── 11-6-agentes-nocode/
    └── info/               # Especificaciones y skills
```

Las prácticas de RAG y LangChain ya no viven en `Practicas/`: todo el contenido no duplicado se consolidó en `11-ia/`.

## Principio

La unidad `11-5-rag/` está ordenada por **concepto**, no por curso:

- `01-info/`: fundamentos y ejercicios de RAG.
- `02-formencia/`: material del curso Formencia (documentos, chunking, embeddings), con sus prácticas en `02-formencia/exercises/`.
- `03-oracle/mcp/`: material de Oracle (MCP).

El **diario integrado** es el hilo único que mezcla teoría y práctica.

## A dónde van los archivos nuevos

Cuando agregues archivos nuevos de Formencia u Oracle:

1. **Identificá el concepto:** fundamentos, preparación/ingesta, chunking, embeddings/vectores, búsqueda, LangChain, agentes/tools, MCP, integración.
2. **Ubicalo en la carpeta que corresponda:** `01-info/`, `02-formencia/` (prácticas en `02-formencia/exercises/`), `03-oracle/mcp/` o `11-4-langchain/`.
3. **Agregá un enlace** en `11-ia/11-5-rag/DIARIO_INTEGRADO_UNIDAD_11.md` dentro de la sección correcta, mezclando teoría + práctica.
4. **Si no encaja aún**, dejalo en **Pendientes / Sin clasificar**.

## Reglas

- **UNA SOLA UNIDAD:** Usar `11-5-rag/`. NO crear carpetas paralelas.
- **SIN DUPLICADOS:** Si ya existe, se enlaza, no se copia.
- **ENLAZAR, NO MOVER:** Mantener las ubicaciones actuales.
- **PRÁCTICA SEPARADA DE TEORÍA, PERO UNIDAS:** El diario une ambos.
- **SEGUIR EL HILO:** Aprender mezclado tal como viene, ordenando por concepto en el diario.

## Estado

- Formencia ~25% (hoy embeddings) -> enlazar en la sección correspondiente.
- Oracle ~25% (MCPs) -> enlazar en la sección 7.
