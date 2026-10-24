# Propuesta para la aprobación del curso

## Datos Generales

- **Nombre del curso:** *Agentes de IA y RAG: de la teoría a la práctica*
- **Subtítulo:** *Aprende a darle el contexto correcto a un agente de IA con tus propios documentos, usando opencode*
- **Modalidad:** Curso de Extensión Universitaria (Presencial)
- **Día y horario:** Sábados - 3 horas por clase
- **Duración:** 5 meses
- **Total de clases:** 20 clases
- **Carga horaria total:** 60 horas presenciales
- **Práctica entre semana:** Recomendado (1 - 2 horas)
- **Público destinatario:** Todo público. Se integra con lo ya visto en talleres de Python, Terminal/Linux, pero no los repite en profundidad.


## Idea Central

El objetivo del curso **no** es enseñar Python, Linux, Git o APIs a fondo. Es **enseñar ese ecosistema justo lo necesario para entenderlo y utilizarlo con un único fin: crear una herramienta con RAG + agente utilizando opencode**.

Todo lo que se vea desde el módulo `00` hasta el `11` se da con esa mirada: *"¿Para qué me sirve esto para armar mi RAG, vincularlo a mi agente, crear e integrar mis MCPs y configurarlo con opencode?"*


## Justificación

Las empresas necesitan aprovechar sus propios documentos, manuales, procedimientos o bases internas con IA, sin reentrenar modelos, sin altos costos y manteniendo el control sobre sus propios datos.

El **RAG (Retrieval Augmented Generation)** es hoy la solución más viable, económica, segura y aplicable para lograrlo. Para poder armarlo correctamente, entender sus límites, su fiabilidad y su seguridad, es necesario conocer lo justo del ecosistema que lo rodea.

Este curso integra ese ecosistema completo para formar personas capaces de **diseñar, construir, validar y asegurar un sistema RAG confiable, vincularlo a un agente, crear sus propios MCPs y convertirlo en una herramienta funcional con opencode CLI**, todo por API y entendiendo qué hay bajo el capó.


## Diferenciación con otros talleres

| Taller Existente | Qué cubre | Diferenciación con este curso |
| :-- | :-- | :-- |
| **Oracle** | LangChain, agentes a nivel código y bases de datos vectoriales en profundidad. | Complementario. Oracle va por la implementación a nivel código con LangChain. Este curso va por la **construcción de un RAG confiable, su vinculación al agente, creación e integración de MCPs propios y aplicación práctica con opencode CLI**. |
| **Python / Terminal / Linux / Servidores** | Base técnica por separado. | Se integran con un propósito único. No se enseña en profundidad, se enseña lo justo para moverse por CLI, entender archivos, leer JSON, consumir APIs y trabajar con `opencode`. |
| **Machine Learning / Deep Learning** | Entrenamiento de modelos. | Fuera del alcance. Este curso es netamente de **consumo, construcción, configuración y aplicación práctica**. No hay reentrenamiento ni fine-tuning. |


## Objetivo General

Al finalizar el curso, el alumno será capaz de **crear su propia herramienta con RAG + agente utilizando opencode**, entendiendo lo justo del ecosistema necesario para hacerlo: configurar su entorno, consumir modelos por API, construir un RAG confiable con conocimiento privado, vincularlo al agente, crear e integrar sus propios MCPs y dejarlo funcional con una configuración clara.


## Estructura por Bloques

| Bloque | Módulos del repositorio | Propósito |
| :-- | :-- | :-- |
| **Bloque 1: Entorno, CLI y Versionado** | `00 - Configuración Inicial`, `02 - Terminal`, `03 - PowerShell`, `04 - Bash`, `05 - SSH`, `06 - Git`, `07 - GitHub` | Lo justo para configurar el entorno, moverse por CLI, conectarse por SSH, versionar y preparar todo para trabajar con `opencode`. |
| **Bloque 2: Lógica, Python y Fundamentos** | `01 - Fundamentos de Programación`, `08 - Python` | Bases mínimas para entender lógica, leer código, archivos y estructuras. Enfoque: saber para entender, no para volverse desarrollador. |
| **Bloque 3: APIs y SQL** | `09 - API`, `10 - SQL` | Entender APIs, JSON, consumo por API (clave para modelos), headers, body y lo comprensivo de SQL. |
| **Bloque 4: Agentes, RAG y Aplicación con opencode** | `11 - IA` (11-1 a 11-6) | Núcleo del curso. Fundamentos sólidos de LLM, RAG confiable, agentes, vinculación RAG-agente, MCPs, configuración y aplicación con `opencode`. |


## Temario General Clase por Clase

| Clase | Bloque | Tema | Objetivo |
| :-- | :-- | :-- | :-- |
| **Clase 1** | Bloque 1 | *Configuración inicial y acercamiento al CLI* | Configurar entorno. Familiarización con terminal y primer contacto con `opencode`. |
| **Clase 2** | Bloque 1 | *Terminal, PowerShell y Bash (lo necesario)* | Navegación, carpetas, archivos, permisos básicos y uso práctico enfocado a `opencode`. |
| **Clase 3** | Bloque 1 | *SSH, Git y GitHub* | Versionado, clonado, commits. Aplicado al proyecto que irá creciendo clase a clase. |
| **Clase 4** | Bloque 2 | *Fundamentos de programación aplicados* | Lógica, variables, condicionales, bucles. Justo lo necesario para leer y entender. |
| **Clase 5** | Bloque 2 | *Python aplicado al ecosistema* | Lectura/escritura de archivos, estructuras, JSON. Enfoque 100% práctico para lo que se usará después. |
| **Clase 6** | Bloque 3 | *APIs, JSON y consumo por API* | ¿Qué es una API? Peticiones, headers, body, respuestas. Consumo por API (sin Ollama). |
| **Clase 7** | Bloque 3 | *SQL lo justo para entenderlo* | Comprensión de tablas, relaciones y consultas básicas. Enfoque comprensivo. |
| **Clase 8** | Bloque 4 - 11-1 | *Introducción a los LLMs* | ¿Qué es un LLM? ¿Cómo funciona a grandes rasgos? Consumo por API y visión general. |
| **Clase 9** | Bloque 4 - 11-2 | *Tokens, ventana de contexto, embeddings y similitud vectorial* | **Fundamental.** Base para entender chunking, recuperación y funcionamiento del RAG. |
| **Clase 10** | Bloque 4 - 11-5 | *Fundamentos de RAG, arquitectura y valor en entornos privados* | ¿Qué es RAG? Componentes, flujo de datos, por qué evita reentrenar y cuándo aplicarlo. |
| **Clase 11** | Bloque 4 - 11-5 | *Preparación de documentos y chunking* | Lectura de documentos reales, limpieza, segmentación (chunking), solapamiento y errores a evitar. |
| **Clase 12** | Bloque 4 - 11-5 | *Embeddings, bases de datos vectoriales, indexación y recuperación* | Representación vectorial, indexación, búsqueda vectorial, búsqueda híbrida y reranking. |
| **Clase 13** | Bloque 4 - 11-5 | *Generación, ingeniería de prompts para RAG* | Rol del LLM en RAG, prompts orientados a RAG, control de respuesta y reducción de alucinaciones. |
| **Clase 14** | Bloque 4 - 11-5 | *Evaluación, fiabilidad, seguridad y privacidad en RAG* | Métricas, validación, riesgos, datos sensibles y buenas prácticas para RAG confiable. |
| **Clase 15** | Bloque 4 - 11-3/11-4 | *Teoría de agentes + ejemplo ilustrativo mínimo* | ¿Qué necesita un agente para ser útil? Contexto + herramientas + reglas. Conexión RAG-Agente. Ejemplo mínimo (sin profundizar en LangChain). |
| **Clase 16** | Bloque 4 - 11-5 | *Construcción de un RAG confiable desde cero (por API)* | Práctica integrada: documentos, chunking, embeddings, base vectorial, recuperación, generación. Todo por API. |
| **Clase 17** | Bloque 4 - 11-6 | *Vinculando RAG al agente y creando MCPs propios* | **Clave.** Vincular el RAG construido al agente. Crear un MCP propio, integrarlo y probarlo. |
| **Clase 18** | Bloque 4 - 11-6 | *opencode CLI: AGENTS.md, specs, skills, subagentes* | Configuración por API, `AGENTS.md`, `specs`, `skills`, `subagentes`. Aplicado desde la documentación oficial de `opencode`. |
| **Clase 19** | Bloque 4 - 11-6 | *Integración completa: RAG + agente + MCP + opencode* | Integración total. Armar la herramienta funcional: RAG vinculado, MCP creado, agente configurado, reglas y contexto definidos. |
| **Clase 20** | Bloque 4 - Proyecto Final | *Proyecto integrador, presentación y cierre* | Presentación de la herramienta funcional creada por cada alumno (RAG + agente + MCP + opencode). Corrección, cierre y entrega. |


## Herramientas y Tecnologías a Enseñar

| Herramienta/Tecnología | Uso |
| :-- | :-- |
| **opencode (CLI)** | Herramienta principal. Configuración, `AGENTS.md`, `specs`, `skills`, `subagentes`, MCPs. |
| **LLMs por API** | Consumo exclusivo por API. Sin Ollama. |
| **Terminal (Bash/PowerShell)** | Lo justo: navegación, archivos, ejecución y trabajo con `opencode`. |
| **Git & GitHub** | Versionado del proyecto final. |
| **SSH** | Lo justo para entender autenticación y conexión. |
| **Python** | Aplicado únicamente lo necesario para entender el RAG. |
| **APIs / JSON** | Consumo, headers, body, respuestas. Fundamental. |
| **Embeddings & Bases de Datos Vectoriales** | Lo necesario: indexación, storage, búsqueda vectorial, híbrida, reranking. |
| **Chunking** | Segmentación, solapamiento, criterios para una recuperación confiable. |
| **MCPs (Creación e integración)** | Crear MCPs propios, integrar junto al RAG al agente. |
| **Evaluación / Seguridad / Privacidad** | Lo justo para construir a RAG confiable. |


## Duración, Modalidad y Precio

- **Duración:** 5 meses
- **Clases:** Sábados, 3 horas c/u (20 clases x 3 horas = 60 horas presenciales)
- **Modalidad:** Curso de Extensión Universitaria
- **Cupo sugerido:** 10 alumnos (seguimiento personalizado)
- **Promedio objetivo:** 10 alumnos

**Cálculo económico:**

| Concepto | Cálculo | Total |
| :-- | :-- | :-- |
| **Precio por alumno / mes** | $35.000 ARS | $35.000 ARS |
| **Promedio de alumnos** | 10 | 10 |
| **Recaudación mensual** | $35.000 x 10 | $350.000 ARS |
| **Recaudación total (5 meses)** | $350.000 x 5 | $1.750.000 ARS |
| **50% para la Institución** | $1.750.000 x 50% | $875.000 ARS |
| **50% para el docente** | $1.750.000 x 50% | **$875.000 ARS** (ganancia bruta) |


## Conclusión

La fortaleza del curso es **integrar lo justo y necesaria**.

Los módulos `00` - `10` son **parte del curso**. No se enseñan por separado, se enseñan con el propósito de armar, entender y configurar la herramienta final.

El alumno sale **con una herramienta funcional**: RAG confiable de conocimiento privado, vinculado al agente, con MCPs propios, configurado con `opencode` CLI, todo por API. Entendiendo lo justo del ecosistema, pero con la suficiente solidez to understand the "¿Por qué?" detrás de cada paso.

Este curso **complementa** los talleres existentes, aprovecha la malla ya cursada, responde a una demanda real de pymes, es entendible para todo público and upholds the objetivo: *"Aprende a darle the contexto correcto a un agente de AI with tus propios documents, usando opencode".*
