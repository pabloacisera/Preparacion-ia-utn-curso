# Propuesta para la aprobación del curso

## Datos Generales

- **Nombre comercial:** *Asistente IA a medida*
- **Frase de venta:** *Tus documentos, tus reglas*
- **Nombre académico:** *Agentes de IA con LangChain y RAG: construí tu herramienta*
- **Subtítulo:** *Del prototipo no-code al agente con documentos privados, herramientas propias y despliegue*
- **Modalidad:** Curso de Extensión Universitaria (presencial o híbrido)
- **Duración:** 3 meses / 12 semanas
- **Total de clases:** 24 clases
- **Carga horaria:** 48 horas teórico-prácticas + 48 horas de autoestudio
- **Frecuencia:** 2 clases por semana, de 2 horas cada una
- **Inicio de clases:** marzo de 2027
- **Público destinatario:** profesionales, docentes, técnicos, administrativos, emprendedores y estudiantes avanzados. No requiere experiencia previa en IA. Python y SQL se nivelan en las primeras clases.
- **Cupo sugerido:** 15 alumnos
- **Certificación:** UTN-FRD e Instituto Linux

## Idea Central

El objetivo del curso **no** es enseñar Python, Linux, Git o APIs a fondo. Es **enseñar ese ecosistema justo lo necesario para entenderlo y utilizarlo con un único fin: crear un agente de IA con RAG, herramientas propias y MCP, tanto con código como por la vía no-code**.

Todo lo que se vea desde el módulo `00` hasta el `11` se da con esa mirada: *"¿Para qué me sirve esto para armar mi agente, darle el contexto correcto, crear mis herramientas, integrar mis MCPs y dejarlo funcionando?"*

## Justificación

Las empresas necesitan aprovechar sus propios documentos, manuales, procedimientos o bases internas con IA, sin reentrenar modelos, sin altos costos y manteniendo el control sobre sus propios datos.

El **RAG (Retrieval Augmented Generation)** es hoy la solución más viable, económica, segura y aplicable para lograrlo. Para poder armarlo correctamente, entender sus límites, su fiabilidad y su seguridad, es necesario conocer lo justo del ecosistema que lo rodea.

Este curso integra ese ecosistema completo para formar personas capaces de **diseñar, construir, validar y asegurar un agente con RAG confiable, crear sus propias herramientas, integrar servidores MCP y convertirlo en una herramienta funcional**, todo por API y entendiendo qué hay bajo el capó.

La ventaja del curso está en tres puntos:

1. **Velocidad de desarrollo:** con LangChain y la vía no-code, el alumno pasa de la idea al prototipo en horas, no en semanas.
2. **Baja curva de aprendizaje:** no se enseña a programar desde cero ni a entrenar modelos. Se enseña lo justo para entender y construir.
3. **Resultado concreto:** el alumno termina con un agente funcional, con un contexto bien determinado y con herramientas personalizadas: PDF, DOCX, XLSX, OCR, voz y APIs.

## Diferenciación con otros talleres

| Taller Existente | Qué cubre | Diferenciación con este curso |
| :-- | :-- | :-- |
| **Oracle** | LangChain, agentes a nivel código y bases de datos vectoriales en profundidad. | Complementario. Oracle va por la implementación a nivel código con LangChain. Este curso integra el ecosistema completo y suma la vía no-code, MCP y despliegue. |
| **Python / Terminal / Linux / Servidores** | Base técnica por separado. | Se integran con un propósito único. No se enseña en profundidad, se enseña lo justo para moverse por CLI, entender archivos, leer JSON, consumir APIs y trabajar con agentes. |
| **Machine Learning / Deep Learning** | Entrenamiento de modelos. | Fuera del alcance. Este curso es netamente de **consumo, construcción, configuración y aplicación práctica**. No hay reentrenamiento ni fine-tuning. |
| **Agentes no-code** | Herramientas visuales o de terminal. | Este curso combina no-code con comprensión del funcionamiento interno y código cuando hace falta. |

## Objetivo General

Al finalizar el curso, el alumno será capaz de **crear su propia herramienta con RAG + agente**, entendiendo lo justo del ecosistema necesario para hacerlo: configurar su entorno, consumir modelos por API, construir un RAG confiable con conocimiento privado, vincularlo al agente, crear e integrar sus propios MCPs y dejarlo funcional con una configuración clara.

## Resultados de Aprendizaje

Al finalizar, el alumno podrá:

1. Entender el ecosistema LLM: tokens, contexto, embeddings, costo y latencia.
2. Consumir modelos por API y controlar prompts, roles, parámetros y errores.
3. Preparar documentos reales (PDF, DOCX, XLSX, imágenes) y construir un pipeline RAG.
4. Operar bases vectoriales y aplicar búsqueda vectorial e híbrida.
5. Crear agentes con LangChain, tools propias y guardrails.
6. Crear servidores MCP y conectarlos a un agente.
7. Prototipar agentes no-code con specs, skills y opencode.
8. Desplegar un servicio básico con FastAPI, Docker y control de costos.

## Estructura por Bloques

| Bloque | Clases | Horas | Propósito |
| :-- | :--: | :--: | :-- |
| **Bloque 1: Entorno, CLI y Python esencial** | 1–4 | 8 h | Configurar el entorno, moverse por CLI, versionar y leer código |
| **Bloque 2: APIs, SQL y datos** | 5–8 | 8 h | Entender APIs, JSON, consumo por API y SQL comprensivo |
| **Bloque 3: LLMs, agentes y LangChain** | 9–13 | 10 h | Pasar del modelo al agente y orquestar con LangChain |
| **Bloque 4: RAG, documentos y bases vectoriales** | 14–19 | 12 h | Construir un RAG confiable con conocimiento privado |
| **Bloque 5: Herramientas, MCP, no-code e infraestructura** | 20–24 | 10 h | Convertirlo en una herramienta real y desplegable |
| **Total** | **24** | **48 h** | |

## Temario General Clase por Clase

| Clase | Bloque | Tema | Objetivo |
| :--: | :-- | :-- | :-- |
| **Clase 1** | Bloque 1 | *Entorno y primer contacto* | Configurar Linux/WSL, VS Code, terminal, opencode, `.env`, API keys y Git. |
| **Clase 2** | Bloque 1 | *Terminal, archivos y SSH* | Navegación, carpetas, archivos, permisos, Git y GitHub. |
| **Clase 3** | Bloque 1 | *Python I* | Lógica, variables, condicionales, bucles y funciones. |
| **Clase 4** | Bloque 1 | *Python II* | `venv`, JSON, archivos, `pypdf`, `python-docx` y `openpyxl`. |
| **Clase 5** | Bloque 2 | *APIs* | HTTP, JSON, headers, body, métodos, `curl`, errores y versionado. |
| **Clase 6** | Bloque 2 | *APIs con Python* | `requests`/`httpx`, rate limits, streaming y costos. |
| **Clase 7** | Bloque 2 | *SQL* | Tablas, PK/FK, tipos, CRUD, `WHERE` y `JOIN`. |
| **Clase 8** | Bloque 2 | *SQL aplicado* | Migraciones, esquema integrador y diferencia con bases vectoriales. |
| **Clase 9** | Bloque 3 | *Introducción a los LLMs* | Tokens, contexto, prompts, roles, parámetros y alucinaciones. |
| **Clase 10** | Bloque 3 | *Funcionamiento interno* | Tokenización, embeddings, similitud, predicción y ONNX. |
| **Clase 11** | Bloque 3 | *Teoría de agentes* | Chatbot vs workflow vs agente, bucle, tools, tool calling, ReAct, guardrails y seguridad. |
| **Clase 12** | Bloque 3 | *LangChain I* | Prompts, chains, memoria y parsers. |
| **Clase 13** | Bloque 3 | *LangChain II* | Agentes con tools, múltiples herramientas, trazas y manejo de errores. |
| **Clase 14** | Bloque 4 | *Fundamentos de RAG* | Arquitectura, indexación vs consulta, RAG vs fine-tuning y cuándo aplicarlo. |
| **Clase 15** | Bloque 4 | *Preparación de documentos* | PDF, DOCX, XLSX, OCR, limpieza, metadatos, extracción híbrida y privacidad. |
| **Clase 16** | Bloque 4 | *Chunking* | Estrategias fija, recursiva y semántica; overlap, tamaño y errores. |
| **Clase 17** | Bloque 4 | *Bases vectoriales I* | Embeddings, dimensiones, ANN, top-k, Chroma y FAISS. |
| **Clase 18** | Bloque 4 | *Bases vectoriales II* | pgvector/Postgres, búsqueda híbrida (BM25), reranking, persistencia y actualización. |
| **Clase 19** | Bloque 4 | *RAG con LangChain* | Pipeline completo, retrievers, prompt aumentado, evaluación y seguridad. |
| **Clase 20** | Bloque 5 | *Herramientas propias* | Tools de PDF/DOCX/XLSX, OCR, voz (STT/TTS), APIs, esquemas y docstrings. |
| **Clase 21** | Bloque 5 | *MCP* | Host/client/server, primitivas, JSON-RPC, transporte, servidor propio con FastMCP y SQLite. |
| **Clase 22** | Bloque 5 | *Integración* | Agente + MCP + RAG, `MultiServerMCPClient`, tools locales y externas (GitHub). |
| **Clase 23** | Bloque 5 | *No-code* | Specs, skills (`SKILL.md`), opencode, `AGENTS.md`, subagentes y permisos. |
| **Clase 24** | Bloque 5 | *Infraestructura y cierre* | FastAPI, Docker, auth, logs, observabilidad, costos y presentación del proyecto final. |

## Proyecto Final

**Agente de conocimiento privado con herramientas propias.** Debe incluir:

- Ingesta de al menos 3 documentos (PDF, DOCX, XLSX o escaneados con OCR).
- Pipeline RAG con chunking, embeddings y base vectorial.
- Agente LangChain con al menos 2 herramientas propias (archivos, SQL, voz o API).
- Un servidor MCP propio conectado al agente.
- Interfaz mínima: CLI o API con FastAPI.
- `README`, `.env.example` y demo de 3 minutos.
- Evaluación con 5 preguntas de prueba, revisión de respuestas y análisis de seguridad.

## Evaluación

| Instancia | Peso | Qué se evalúa |
| :-- | :--: | :-- |
| Ejercicios semanales | 20 % | Ejecución y comprensión de cada bloque |
| Parcial integrador | 30 % | RAG funcionando con documentos reales |
| Proyecto final + defensa | 50 % | Agente completo, herramientas, MCP, despliegue y explicación |
| **Aprobación** | **70 %** | |

## Herramientas y Tecnologías a Enseñar

| Herramienta/Tecnología | Uso |
| :-- | :-- |
| **opencode (CLI)** | Agente de terminal, configuración, `AGENTS.md`, specs, skills, subagentes y MCPs. |
| **LLMs por API** | Consumo exclusivo por API (Groq y Gemini). |
| **Terminal (Bash/PowerShell)** | Navegación, archivos, ejecución y trabajo con agentes. |
| **Git & GitHub** | Versionado del proyecto final y portfolio. |
| **SSH** | Autenticación y conexión básica. |
| **Python** | Lo necesario para entender y construir el RAG. |
| **APIs / JSON** | Consumo, headers, body, respuestas y errores. |
| **LangChain / LangGraph** | Orquestación de prompts, chains, agentes y tools. |
| **Embeddings & Bases de Datos Vectoriales** | Indexación, almacenamiento, búsqueda vectorial, híbrida y reranking. |
| **Chunking** | Segmentación, solapamiento y criterios de recuperación confiable. |
| **MCPs (creación e integración)** | Servidores propios con FastMCP e integración al agente. |
| **FastAPI / Docker** | Exposición y despliegue básico del agente. |
| **Herramientas de archivos y voz** | PDF, DOCX, XLSX, OCR, speech-to-text y text-to-speech. |
| **Evaluación / Seguridad / Privacidad** | Métricas, validación, guardrails y datos sensibles. |

## Duración, Modalidad y Precio

- **Duración:** 3 meses / 12 semanas
- **Clases:** 24 clases de 2 horas, dos veces por semana (48 horas de cursada)
- **Autoestudio:** 48 horas (4 horas por semana)
- **Modalidad:** Curso de Extensión Universitaria
- **Cupo sugerido:** 15 alumnos
- **Promedio objetivo:** 10 alumnos

**Cálculo económico de referencia:**

| Concepto | Cálculo | Total |
| :-- | :-- | :-- |
| **Precio por alumno / mes** | $35.000 ARS | $35.000 ARS |
| **Promedio de alumnos** | 10 | 10 |
| **Recaudación mensual** | $35.000 × 10 | $350.000 ARS |
| **Recaudación total (3 meses)** | $350.000 × 3 | $1.050.000 ARS |
| **50% para la Institución** | $1.050.000 × 50% | $525.000 ARS |
| **50% para el docente** | $1.050.000 × 50% | **$525.000 ARS** (ganancia bruta) |

> Los valores son de referencia y quedan sujetos a la definición de la institución.

## Cumplimiento de la Convocatoria

| Requisito | Cumplimiento |
| :-- | :-- |
| Máximo 48 horas de teoría | Sí: 24 clases × 2 h = 48 h |
| 48 horas de autoestudio | Sí: 4 h por semana × 12 semanas |
| Inicio marzo 2027 | Sí |
| Formato de 2 h por clase, dos veces por semana | Sí: 12 semanas = 3 meses |
| Propuesta por correo electrónico | Pendiente de envío |
| Asunto exacto y adjuntos solo de certificaciones | Pendiente de armado |
| Redes sociales y minivideo | Pendiente de grabación y enlaces |

## Conclusión

La fortaleza del curso es **integrar lo justo y necesario**.

Los módulos `00` a `10` son **parte del curso**. No se enseñan por separado, se enseñan con el propósito de armar, entender y configurar la herramienta final.

El alumno sale **con una herramienta funcional**: un agente con RAG confiable de conocimiento privado, herramientas propias, servidores MCP y configuración clara. Entiende lo justo del ecosistema, pero con la suficiente solidez para explicar el "por qué" detrás de cada paso.

Este curso **complementa** los talleres existentes, aprovecha la malla ya cursada, responde a una demanda real de pymes y profesionales, es entendible para todo público y sostiene el objetivo: *"Aprendé a darle el contexto correcto a un agente de IA con tus propios documentos, usando herramientas propias y opencode"*.
