# Estado del trabajo (traspaso)

> Leer esto primero al retomar el trabajo. Última actualización: 14 de octubre de 2026.

## Objetivo

Consolidar el material de `curso-utn-privado` dentro de `Preparacion-ia-utn-curso`, creando la sección de IA del curso (módulos 10 a 15).

- `curso-utn-privado` es **solo una fuente de consulta**. No se modifica ni se borra nada de ahí.
- El curso real es `Preparacion-ia-utn-curso`. La migración ya está hecha.

## Hecho

- **Módulos 10 a 15 completos**, cada uno con su `readme.md` (teoría) y subcarpeta `ejercicios/` (cada ejercicio es un `.md` con la consigna y el código en un bloque):
  - 10 Introducción a los LLMs
  - 11 Funcionamiento interno
  - 12 RAG
  - 13 LangChain y su ecosistema
  - 14 Agentes
  - 15 Agentes no-code
- Recursos de RAG copiados a `IA/RAG/recursos/` (`RAG-flow.png`, `rag_vs_fine_tuning.png`).
- `IA/Planificacion/` con `readme.md`, `Ruta-del-Curso.md`, `Schedule.md` y `Topics.md`.
- `Glosario.md` unificado (conceptos generales + vocabulario de IA).
- `IA/readme.md` (portada de la sección) e `IA/requirements.txt`.
- `README.md` raíz actualizado con el ítem 10 (IA) y el 11 (Glosario).
- Enlaces internos verificados: todos resuelven.
- **Corrección de orden:** se quitó LangChain de los módulos anteriores al 13:
  - Módulo 10, ejercicio 01: usa el SDK crudo de Groq (`groq`), no `init_chat_model`.
  - Módulo 12, ejercicio 02: chunking 100% a mano (con solapamiento), sin `langchain_text_splitters`.
  - Módulo 12, `readme.md`: referencia a LangChain suavizada (queda como "se ve después").
- Sin emojis decorativos. Sin `commit` ni `push`.
- **Revisión de solapamientos (hecha):** `Configuracion_Inicial` cubre la instalación de terminal, VS Code, Debian y Android; **no** trata `.env` ni API keys. Por lo tanto el setup del Módulo 10 no duplica nada. No hay solapamiento en el curso.

## Próximo

1. Revisión del material migrado por parte del usuario.
2. Cierre: repaso final de enlaces y consistencia.

## Decisiones clave

- **Orden:** de lo menos a lo más. Primero se llama a la API "a mano", después aparecen las librerías (LangChain en el Módulo 13) y cada pieza nueva nace de un fallo de la anterior.
- **6 módulos:** 10 Intro LLMs, 11 Funcionamiento interno, 12 RAG, 13 LangChain, 14 Agentes, 15 Agentes no-code.
- **Escalera** (a mano → librerías → local → API → RAG) dentro del Módulo 11.
- **Alcance:** solo lo necesario. Sin fine-tuning, sin ML, sin DL. El ONNX se conserva.
- **Cada ejercicio** = un `.md` con código en bloque, dentro de `ejercicios/`.
- Sin emojis. No hacer `commit`/`push` salvo pedido explícito.

## Mapa de fuentes (solo referencia; la cantera no se toca)

| Origen en `curso-utn-privado` | Destino en `Preparacion` |
|-------------------------------|--------------------------|
| `preparatories-bonus/modulo_anatomia_llm_v3.md`, `Modulo_02A...`, `Modulo_02B...`, `LLM/optimization/apuntes_ia_bajos_recursos.md` | `IA/Funcionamiento-Interno` |
| `RAG-formencia/README.md` + `resources/*.png` | `IA/RAG` |
| `cert-oracle-ai/langchain_module.md`, `reasoning_patterns.md`, `01-demo`, notebooks `01-demo` y `02-basic` | `IA/LangChain` |
| `cert-oracle-ai/introduction.md`, `03-into-langchain/agent_one.ipynb` | `IA/Agentes` |
| `Schedule.md`, `Topics.md`, `preparatories-bonus/Ruta_del_curso.md` | `IA/Planificacion` |

## Pendientes / decisiones abiertas

- Revisar si el Módulo 11 necesita un ejercicio "a mano" antes de los de librerías, o si alcanza con `profundizacion.md`.
- El Módulo 15 (Agentes no-code) no tiene material de origen: está redactado de cero. Revisar que el nivel y los ejemplos estén alineados con el resto.
