# Cronograma de Preparación e Implementación del Curso de IA

**Período:** 5 al 30 de octubre de 2026
**Dedicación:** 8 horas diarias (Full-time)
**Meta de Finalización de Formación:** 27 de octubre (3 días antes de la fecha límite)

---

## PARTE 1: Cronograma de Estudio y Certificación Personal
*(Del 5 al 27 de Octubre - 8h diarias)*

### Estrategia Diaria de Trabajo
* **Bloque Mañana (4h):** Formación teórica, cursos conceptuales y certificaciones oficiales.
* **Bloque Tarde (4h):** Práctica en código, laboratorios (en Google Colab / Nube) y desarrollo de proyectos propios.

---

### Semana 1: Días 1 a 7 (5 al 11 de Octubre)
**Enfoque:** Fundamentos de Agentes, RAG Inicial y Primeras Certificaciones.

* **Mañana (4h):**
  * **Oracle Agentic AI Foundations Associate** (~7h total | *Días 1 y 2*).
  * **Free RAG Course for Beginners - Simplilearn** (~3h total | *Día 3*).
  * **Advanced RAG Certification - LlamaIndex / Activeloop** (Inicio de teoría | *Días 4 a 7*).
* **Tarde (4h):**
  * **Sistemas RAG para Conocimiento Privado - Formencia** (~12h total | *Días 1 a 3*).
  * **Práctica Propia - Parte 1 (Macro):** Configuración de Agentes CLI, OpenCode, Specs, Skills y protocolo MCP (*Días 4 a 7*).

---

### Semana 2: Días 8 a 14 (12 al 18 de Octubre)
**Enfoque:** Especialización RAG, Infraestructura Cloud y Anatomía Interna.

* **Mañana (4h):**
  * **Advanced RAG Certification - LlamaIndex / Activeloop** (Laboratorios en Google Colab | *Días 8 a 10*).
  * **Become an OCI Enterprise AI Professional** (~9h total | *Días 11 a 14*).
* **Tarde (4h):**
  * **Práctica Propia - Parte 2A (Micro):** Anatomía del LLM a mano con Python puro y `numpy` (tokens, embeddings, matrices y atención Q/K/V) (*Días 8 a 14*).

---

### Semana 3: Días 15 a 21 (19 al 25 de Octubre)
**Enfoque:** Bases de Datos Vectoriales, Select AI e Infraestructura RAG.

* **Mañana (4h):**
  * **Become an Agentic AI for Oracle AI Database Professional** (Select AI y Vector Search) (*Días 15 a 18*).
  * Repaso e integración de certificaciones Oracle (*Días 19 a 21*).
* **Tarde (4h):**
  * **Práctica Propia - Parte 2B (Infraestructura):** Construcción de RAG desde cero, FastAPI, Vector DBs (Chroma/pgvector) y LangChain/LangGraph (*Días 15 a 21*).

---

### Cierre de Formación: Días 22 y 23 (26 y 27 de Octubre)
* Rendición de exámenes finales o certificaciones pendientes.
* Consolidación del entorno de trabajo e infraestructura local.

---

## PARTE 2: Planificación de Entregables para la Universidad
*(Del 28 al 30 de Octubre - 3 Días de Trabajo Enfocado)*

Al finalizar tu formación con 3 días de margen, este es el plan paso a paso para elaborar la propuesta académica y la presentación institucional.

---

### Día 28 de Octubre: Elaboración del Programa de Estudio (Syllabus)

**Objetivo:** Diseñar la estructura curricular del curso para los alumnos.

#### Estructura del Documento `Programa_Curricular.md`:
1. **Datos Generales:**
   * Nombre del curso: *Desarrollo de Software Asistido por Agentes y Aplicaciones con RAG*.
   * Duración total en horas, modalidad (Teórico-Práctico) y prerrequisitos (Python básico, SQL básico).
2. **Fundamentos y Filosofía Pedagógica:**
   * Declaración del enfoque *"De la superficie a las tripas"* (Agentes y MCP primero, matemática del LLM después, RAG como Tool).
3. **Módulos del Programa:**
   * **Módulo 1: Arquitectura de Agentes y Entorno CLI.** OpenCode, Specs, Skills, contratos JSON y servidor MCP.
   * **Módulo 2: Anatomía de un LLM a Mano.** Tokenización, BPE, Embeddings, Mecanismo de Atención (Q, K, V) con `numpy`.
   * **Módulo 3: Modelos Locales y consumo de APIs.** Ollama/llama.cpp, Groq, Gemini API, estructuración de outputs.
   * **Módulo 4: Sistemas RAG y Bases de Datos Vectoriales.** Chunking, embeddings, Chroma, pgvector, FastAPI y orquestación con LangChain/LangGraph.
4. **Metodología de Evaluación y Proyecto Final:**
   * Criterios de aprobación, evaluaciones parciales y proyecto integrador de fin de curso.

---

### Día 29 de Octubre: Construcción del Material Técnico y Repositorio

**Objetivo:** Dejar listo el repositorio de referencia con el código, laboratorios y documentación para la clase.

#### Estructura del Repositorio (`GitHub / GitLab`):
```text
curso-agentic-ai-rag/
 README.md                   # Presentación del curso y guía de inicio rápido
 docs/
    01_Syllabus.md          # Programa de estudio
    02_Decisiones_Tecnicas.md # Justificación del stack (Python 3.12, FastAPI, etc.)
 modulo_01_agentes_mcp/     # Ejemplos de Specs, Skills y servidores MCP
 modulo_02_llm_a_mano/       # Notebooks de Python puro y numpy (E01-E11)
 modulo_03_apis_locales/     # Integración con Groq, Gemini y llama-cpp
 modulo_04_rag_fastapi/      # Proyecto base: Ingesta, Vector DB y API RAG
 templates/                  # Plantillas base para los proyectos de los alumnos
```

## Tareas Cumplidas

Dia 0:

[x]- Conceptos Básicos, Loop, Componentes y propiedades de un agente;

Día 1:
