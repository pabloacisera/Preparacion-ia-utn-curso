# Programa Curricular

## Nombre comercial y nombre académico

- **Nombre comercial:** *Asistente IA a medida*
- **Frase de venta:** *Tus documentos, tus reglas.*
- **Nombre académico:** *Agentes de IA con LangChain y RAG: construí tu herramienta*
- **Subtítulo:** *Del prototipo no-code al agente con documentos privados, herramientas propias y despliegue*

El nombre comercial está pensado para personas que no vienen del rubro IT: dice qué se llevan (un asistente), para qué (a medida) y a quién le sirve (a cualquiera que quiera usar IA en su actividad diaria).

### Alternativas de nombre comercial

| Nombre | Frase de venta | Cuándo conviene |
| :-- | :-- | :-- |
| **Asistente IA a medida** | Tus documentos, tus reglas. | Opción principal: claro, beneficioso y no técnico. |
| **Tu Asistente IA** | Conocé tus documentos, automatizá tu trabajo. | Más personal y directo, pero más genérico. |
| **IA en tus documentos** | De archivos a respuestas. | Muy descriptivo para el público administrativo. |
| **IA a medida** | Sin programar, con tus datos. | Corto y llamativo; requiere explicar más el alcance. |
| **Copiloto de documentos** | Tu copiloto para trabajar con archivos. | Bueno para marketing; "copiloto" ya es un término conocido. |

## Datos generales

| Campo | Detalle |
| :-- | :-- |
| **Modalidad** | Curso de Extensión Universitaria, presencial o híbrido |
| **Duración** | 3 meses / 12 semanas |
| **Clases** | 24 clases de 2 horas, dos veces por semana |
| **Carga horaria** | 48 horas teórico-prácticas + 48 horas de autoestudio |
| **Inicio** | Marzo de 2027 |
| **Público destinatario** | Profesionales, docentes, técnicos, emprendedores, administrativos y estudiantes avanzados |
| **Requisitos** | Manejo básico de computadora. No requiere experiencia previa en IA. Python y SQL se nivelan en las primeras clases |
| **Cupo sugerido** | 15 alumnos |
| **Certificación** | UTN-FRD e Instituto Linux |
| **Evaluación** | Ejercicios semanales, parcial integrador y proyecto final |

## Fundamentación

La universidad ya tiene machine learning dentro de su oferta. Ese espacio enseña a **entrenar modelos**. Este curso no compite con eso: cubre el espacio que queda entre el modelo entrenado y el uso real en una organización.

Las empresas y los profesionales necesitan usar IA con **sus propios documentos**, **sus propias reglas** y **sus propias herramientas**, sin reentrenar modelos, sin costos altos y sin subir información sensible a cualquier servicio. RAG (Retrieval Augmented Generation) y los agentes de IA resuelven ese problema hoy.

La ventaja del curso está en tres puntos:

1. **Velocidad de desarrollo:** con LangChain y la vía no-code, el alumno pasa de la idea al prototipo en horas, no en semanas.
2. **Baja curva de aprendizaje:** no se enseña a programar desde cero ni a entrenar modelos. Se enseña lo justo del ecosistema para que el alumno entienda lo que hace y pueda construir.
3. **Resultado concreto:** el alumno termina con un agente funcional, con un contexto bien determinado y con herramientas personalizadas: lectura de PDF, DOCX y XLSX, OCR, voz, APIs y servidores MCP propios.

## Objetivo general

Al finalizar el curso, el alumno será capaz de **diseñar, construir y desplegar un agente de IA** que responde con documentos privados, usa herramientas personalizadas y se integra mediante MCP, tanto con código como por la vía no-code.

## Resultados de aprendizaje

Al finalizar el curso, el alumno podrá:

1. Entender el ecosistema LLM: tokens, ventana de contexto, embeddings, costo y latencia.
2. Consumir modelos por API y controlar prompts, roles, parámetros y errores.
3. Preparar documentos reales (PDF, DOCX, XLSX, imágenes) y construir un pipeline RAG.
4. Operar bases de datos vectoriales y aplicar búsqueda vectorial e híbrida.
5. Crear agentes con LangChain, tools propias y guardrails de seguridad.
6. Crear servidores MCP y conectarlos a un agente.
7. Prototipar agentes no-code con especificaciones, skills y opencode.
8. Desplegar un servicio básico con FastAPI, Docker, variables de entorno y control de costos.

## Perfil del egresado

Persona capaz de **resolver un problema real con IA**: tomar los documentos de su trabajo, convertirlos en una base de conocimiento consultable, crear un agente que los use y dejarlo funcionando con reglas claras. No sale como investigador de machine learning ni como desarrollador senior: sale como alguien que puede **construir, explicar y mantener** una herramienta de IA aplicada.

## Metodología

- **60 % práctica, 40 % teoría.** Cada clase tiene un bloque conceptual corto y un laboratorio guiado.
- **Cada clase termina con algo que funciona.** No se acumula teoría sin ejecución.
- **Progresión de lo simple a lo complejo:** primero se usa la herramienta, después se abre la caja negra.
- **Autoestudio guiado:** 4 horas por semana con ejercicios y lecturas del repositorio.
- **Repositorio del curso:** material, ejercicios y proyectos de referencia.
- **Proyecto transversal:** el alumno construye su agente a lo largo de las clases, no al final.

## Carga horaria y cronograma

| Semana | Clases | Bloque | Autoestudio (4 h) |
| :--: | :--: | :-- | :-- |
| 1 | 1–2 | Entorno, terminal y Git | Configuración del entorno y práctica de CLI |
| 2 | 3–4 | Python esencial | Ejercicios de lógica, archivos y JSON |
| 3 | 5–6 | APIs | Consumo de APIs con `curl` y Python |
| 4 | 7–8 | SQL y datos | CRUD, consultas y esquema integrador |
| 5 | 9–10 | LLMs y funcionamiento interno | Tokens, embeddings y similitud |
| 6 | 11–12 | Agentes y LangChain I | Teoría de agentes y cadenas |
| 7 | 13–14 | LangChain II y RAG | Agentes con tools y flujo RAG |
| 8 | 15–16 | Documentos y chunking | Extracción, OCR y segmentación |
| 9 | 17–18 | Bases vectoriales | Indexación, búsqueda y persistencia |
| 10 | 19–20 | RAG con LangChain y tools propias | Evaluación y herramientas de archivo |
| 11 | 21–22 | MCP e integración | Servidor MCP y agente integrado |
| 12 | 23–24 | No-code, infraestructura y cierre | Proyecto final y demo |

**Total:** 24 clases × 2 h = 48 h de cursada + 48 h de autoestudio = 96 h.

## Estructura por bloques

| Bloque | Clases | Horas | Foco |
| :-- | :--: | :--: | :-- |
| 1. Entorno, CLI y Python esencial | 1–4 | 8 h | Poder ejecutar, versionar y leer código |
| 2. APIs, SQL y datos | 5–8 | 8 h | Entender el ida y vuelta de los datos |
| 3. LLMs, agentes y LangChain | 9–13 | 10 h | Pasar del modelo al agente |
| 4. RAG, documentos y bases vectoriales | 14–19 | 12 h | Dar contexto privado confiable |
| 5. Herramientas, MCP, no-code e infraestructura | 20–24 | 10 h | Convertirlo en una herramienta real |
| **Total** | **24** | **48 h** | |

## Temario clase por clase

| Clase | Bloque | Tema | Contenido y práctica | Estado del material |
| :--: | :-- | :-- | :-- | :-- |
| 1 | 1 | Entorno y primer contacto | Linux/WSL, VS Code, terminal, opencode, `.env`, API keys, Git | Hecho |
| 2 | 1 | Terminal, archivos y SSH | Navegación, permisos, Git y GitHub | Hecho |
| 3 | 1 | Python I | Lógica, variables, condicionales, bucles y funciones | Hecho |
| 4 | 1 | Python II | `venv`, JSON, archivos, `pypdf`, `python-docx`, `openpyxl` | Hecho |
| 5 | 2 | APIs | HTTP, JSON, headers, body, métodos, `curl`, errores y versionado | Hecho |
| 6 | 2 | APIs con Python | `requests`/`httpx`, rate limits, streaming y costos | Hecho/parcial |
| 7 | 2 | SQL | Tablas, PK/FK, tipos, CRUD, `WHERE` y `JOIN` | Hecho |
| 8 | 2 | SQL aplicado | Migraciones, esquema integrador, SQL relacional vs vectorial | Hecho |
| 9 | 3 | LLMs | Tokens, contexto, prompts, roles, parámetros y alucinaciones | Hecho |
| 10 | 3 | Funcionamiento interno | Tokenización, embeddings, similitud, predicción y ONNX | Hecho |
| 11 | 3 | Agentes | Chatbot vs workflow vs agente, bucle, tools, tool calling, ReAct, guardrails y seguridad | Hecho |
| 12 | 3 | LangChain I | Prompts, chains, memoria y parsers | Hecho |
| 13 | 3 | LangChain II | Agentes con tools, múltiples herramientas, trazas y manejo de errores | Hecho |
| 14 | 4 | RAG | Arquitectura, indexación vs consulta, RAG vs fine-tuning y cuándo aplicarlo | Hecho |
| 15 | 4 | Documentos | PDF, DOCX, XLSX, OCR, limpieza, metadatos, extracción híbrida y privacidad | Hecho |
| 16 | 4 | Chunking | Estrategias fija, recursiva y semántica; overlap, tamaño y errores | Hecho |
| 17 | 4 | Bases vectoriales I | Embeddings, dimensiones, ANN, top-k, Chroma y FAISS | Parcial |
| 18 | 4 | Bases vectoriales II | pgvector/Postgres, búsqueda híbrida (BM25), reranking, persistencia y actualización | Pendiente |
| 19 | 4 | RAG con LangChain | Pipeline completo, retrievers, prompt aumentado, evaluación y seguridad | Parcial |
| 20 | 5 | Tools propias | Herramientas de PDF/DOCX/XLSX, OCR, voz (STT/TTS), APIs, esquemas y docstrings | Parcial |
| 21 | 5 | MCP | Host/client/server, primitivas, JSON-RPC, transporte, servidor propio con FastMCP y SQLite | Hecho |
| 22 | 5 | Integración | Agente + MCP + RAG, `MultiServerMCPClient`, tools locales y externas (GitHub) | Hecho |
| 23 | 5 | No-code | Specs, skills (`SKILL.md`), opencode, `AGENTS.md`, subagentes y permisos | Parcial |
| 24 | 5 | Infraestructura y cierre | FastAPI, Docker, auth, logs, observabilidad, costos y presentación del proyecto final | Pendiente |

## Autoestudio

El autoestudio se organiza en entregables cortos, alineados con la clase de la semana:

- **Semanas 1–2:** entorno, terminal y Python.
- **Semanas 3–4:** APIs y SQL.
- **Semanas 5–6:** LLM, embeddings y agentes.
- **Semanas 7–8:** documentos, chunking y RAG.
- **Semanas 9–10:** bases vectoriales y evaluación.
- **Semanas 11–12:** tools, MCP, no-code, infraestructura y proyecto final.

## Proyecto final

**Nombre:** *Agente de conocimiento privado con herramientas propias.*

El alumno debe entregar:

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

## Herramientas y tecnologías

| Herramienta | Uso |
| :-- | :-- |
| Python 3.12 | Lenguaje base del curso |
| opencode CLI | Agente de terminal, specs, skills, subagentes y MCP |
| LangChain / LangGraph | Orquestación de prompts, chains, agentes y tools |
| Groq / Gemini | Modelos por API con plan gratuito |
| Chroma / FAISS / pgvector | Bases de datos vectoriales |
| FastAPI | Exposición del agente como servicio |
| Docker | Empaquetado y despliegue básico |
| FastMCP | Creación de servidores MCP propios |
| pypdf, python-docx, openpyxl | Lectura de PDF, DOCX y XLSX |
| pytesseract | OCR para documentos escaneados |
| Whisper (STT/TTS) | Herramientas de voz |
| Git / GitHub | Versionado y portfolio |
| SQLite / PostgreSQL | Bases relacionales |

## Estado del material

| Tema | Estado | Qué falta |
| :-- | :-- | :-- |
| Entorno, terminal, Git y Python | Hecho | Revisión final de ejercicios |
| APIs y SQL | Hecho | Ejercicio integrador de cierre |
| LLMs, embeddings y agentes | Hecho | Nada crítico |
| LangChain | Hecho | Ejercicio integrador con varias tools |
| RAG y documentos | Hecho | Métricas de evaluación |
| Bases vectoriales | Parcial | Laboratorio de pgvector, búsqueda híbrida, reranking y persistencia |
| Tools propias | Parcial | Tool de voz (STT/TTS) y ejemplos de PDF/DOCX/XLSX integrados |
| MCP | Hecho | Servidor MCP de ejemplo con RAG |
| No-code | Parcial | Integración guiada con opencode, `AGENTS.md` y subagentes |
| Infraestructura | Pendiente | FastAPI, Docker, auth, logs, observabilidad y costos |
| Proyecto final | Pendiente | Rúbrica y plantilla de repositorio |

## Diferenciación con otros espacios

| Espacio existente | Qué cubre | Diferencia con este curso |
| :-- | :-- | :-- |
| Machine Learning / Deep Learning | Entrenamiento de modelos | Este curso usa modelos ya entrenados y se enfoca en aplicarlos con datos y herramientas propias |
| Oracle / LangChain | Implementación a nivel código y bases vectoriales en profundidad | Este curso integra el ecosistema completo y suma la vía no-code, MCP y despliegue |
| Python / Terminal / Linux | Base técnica por separado | Se enseña lo justo y con un propósito: construir el agente |
| Agentes no-code | Herramientas visuales o de terminal | Este curso combina no-code con comprensión del funcionamiento interno y código cuando hace falta |

## Cumplimiento de la convocatoria

| Requisito | Cumplimiento |
| :-- | :-- |
| Máximo 48 horas de teoría | Sí: 24 clases × 2 h = 48 h |
| 48 horas de autoestudio | Sí: 4 h por semana × 12 semanas |
| Inicio marzo 2027 | Sí |
| Formato de 2 h por clase, dos veces por semana | Sí: 12 semanas = 3 meses |
| Propuesta por correo electrónico | Pendiente de envío |
| Asunto exacto y adjuntos solo de certificaciones | Pendiente de armado |
| Redes sociales y minivideo | Pendiente de grabación y enlaces |

## Próximos pasos

1. Completar el laboratorio de bases vectoriales (Chroma/FAISS y pgvector).
2. Completar el módulo de infraestructura (FastAPI, Docker, auth, logs y costos).
3. Agregar la tool de voz y los ejemplos integrados de PDF/DOCX/XLSX.
4. Definir la rúbrica del proyecto final.
5. Grabar el minivideo y enviar la propuesta.
