# Prácticas RAG (Manual -> Framework -> Agente)

> **Regla:** Separar código manual del código con framework. Siempre ir por progresión.

## Estructura

| Carpeta | Uso | Notas |
| --- | --- | --- |
| **[01-manual/](01-manual/)** | **SIN LangChain** | Lógica pura en Python. Aquí van `segmentacion_completa.py`, `extraer_texts.ipynb` y todo lo hecho a mano para entender la mecánica. |
| **[02-con-langchain/](02-con-langchain/)** | **CON LangChain** | Mismo flujo que `01-manual/` pero con `langchain`, `langchain_text_splitters`, etc. Comparar con el manual es la clave. |
| **[_documentos/](./_documentos/)** | **Documentos compartidos** | PDFs, TXT, DOCX, XLSX, imágenes para usar en ambas etapas. |

## Cómo usarlo
1. **Primero:** Trabajá en `01-manual/`. Entendé chunking, tokens, similitud a mano.
2. **Segundo:** Pasá a `02-con-langchain/` y **repetí** lo mismo. Compará archivo por archivo.
3. **Tercero:** Llevá lo aprendido a `11-ia/11-5-rag/03-agente-rag/` para convertirlo en herramienta para un agente.

## Importante
- **No mezclar imports.** Si un archivo en `01-manual/` importa `langchain`, está mal ubicado.
- **Los originales siguen ahí.** Los archivos en `Practicas/LangChain/` se mantienen tal como están. Acá tenés una **vista organizada por progresión** para aprender mejor.
