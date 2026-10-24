# Fundamentos de la estructura del programa:

1. **Enganche y "Quick Wins" (De la superficie a las tripas)**
   * **Empezar por Agentes (OpenCode, MCP, Specs, Skills):** El alumno aprende a interactuar inmediatamente con el estado del arte. Puede construir flujos útiles, conectar herramientas vía MCP y entender cómo se orquesta un sistema autónomo sin necesidad de saber cómo funciona una matriz internamente.
   * **Bajar a los Fundamentos (Anatomía del LLM):** Una vez que el alumno entiende qué hace un agente cuando llama a una Tool o procesa un contexto, se le abre la caja negra ("open the box"): ¿Cómo tokeniza? ¿Cómo calcula la atención? ¿Por qué alucina?

2. **MCP y Specs como arquitectura; RAG como una simple herramienta**
   * Como hablábamos antes, el mayor error de los cursos tradicionales es enseñar RAG como si fuera "la definición de un Agente".
   * Al enseñar primero MCP y Specs, tus alumnos entienden que un Agente es un sistema de toma de decisiones autónomo gobernado por reglas y herramientas.
   * Cuando en la segunda parte les enseñas a construir un RAG, ellos no lo ven como "un Agente", sino como una Skill/Tool más que el Agente invoca vía MCP para consultar documentación cuando la necesita.

3. **Progresión pedagógica real:**

$$\text{Agente (Comportamiento y MCP)} \longrightarrow \text{LLM a mano (Mapeo de Tokens y Matrices)} \longrightarrow \text{Modelos locales/APIs} \longrightarrow \text{RAG (Infraestructura de Datos)}$$

* **Parte 1 (Macro):** Cómo piensa y actúa un Agente (OpenCode, CLI, MCP, Specs, Skills).
* **Parte 2A (Micro):** Cómo funciona por dentro el motor probabilístico (Anatomía LLM, numpy, embeddings, atención Q/K/V).
* **Parte 2B (Infraestructura):** Cómo conectar datos externos (RAG, Vector DBs, FastAPI, LangChain).

### Conclusión
Tu planteo es totalmente coherente. No tienes que cambiar el orden:
* La **Parte 1** prepara al estudiante para trabajar como un desarrollador moderno de IA (usando CLI, OpenCode, Specs y MCP).
* La **Parte 2** le da el conocimiento técnico profundo (*under the hood*) para entender la matemática, los límites de tokens, la latencia y la infraestructura de datos (RAG).

# Curso de IA Agentic en la nube

* **Become an Oracle Agentic AI Foundations Associate**
  * **Duración:** 6h 46m
  * **Por qué empezar por esta:** Cubre exactamente lo que necesitas desde cero: fundamentos de IA Generativa, RAG (Retrieval-Augmented Generation), Agentes de IA y flujos de trabajo con frameworks como LangChain.
  * Haz clic en esa tarjeta para abrir el curso y presiona el botón de *Enroll / Register*.

* **Become an OCI Enterprise AI Professional**
  * **Duración:** 9h 17m
  * **Por qué seguir con esta:** Es el paso de especialización para llevar a producción arquitecturas avanzadas de RAG, bases de datos vectoriales y ajuste fino (*fine-tuning*) de Grandes Modelos de Lenguaje (LLMs).

* **Become an Agentic AI for Oracle AI Database Professional**
  * Te enseñará a implementar Select AI y búsquedas de similitud vectorial (*Vector Search*) dentro de bases de datos relacionales.

# Cursos de RAG Gratuitos con Certificación Gratuita

Guía de cursos sobre **RAG (Retrieval-Augmented Generation)** adaptados para ejecutarse en **equipos de escasos recursos**, priorizando plataformas que no requieren carga de cómputo local.

---

## Tabla Comparativa

| Curso | Plataforma | Tipo de Cómputo | Duración | Idioma | Certificado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Sistemas RAG para Conocimiento Privado** | Formencia | 100% Navegador (Teórico) | ~12 horas | Español | Gratuito |
| **2. Free RAG Course for Beginners** | Simplilearn (SkillUp) | 100% Navegador (Teórico) | 2 a 4 horas | Inglés | Gratuito |
| **3. Advanced RAG Certification** | LlamaIndex / Activeloop | Nube (Google Colab / Cloud) | 10 a 15 horas | Inglés | Gratuito |

---

## Detalle de la Ruta de Aprendizaje Recomendada

### 1. Implementación de Sistemas RAG
* **Plataforma:** Formencia
* **Por qué conviene para PC de bajos recursos:** Es un curso conceptual y de evaluación técnica. Todo el contenido se consume desde la web sin necesidad de instalar bases de datos vectoriales, entornos de Python ni modelos locales.
* **Duración:** ~12 horas (12 unidades temáticas de 1 hora + Examen de 20 preguntas).
* **Idioma:** Español.
* **Requisito de Certificación:** Aprobar el examen final con al menos un 70%.

---

### 2. Free RAG Course for Beginners
* **Plataforma:** Simplilearn (SkillUp)
* **Por qué conviene para PC de bajos recursos:** Enfocado en explicaciones teóricas y demostrativas de los componentes clave de RAG (chunking, embeddings, prompt engineering) sin requerir configuración de infraestructura local.
* **Duración:** 2 a 4 horas.
* **Idioma:** Inglés.
* **Requisito de Certificación:** Completar la totalidad de las lecciones del módulo.

---

### 3. Advanced RAG Certification
* **Plataforma:** LlamaIndex + Activeloop
* **Por qué conviene para PC de bajos recursos:** Aunque incluye más de 40 lecciones y 7 proyectos prácticos en código, toda la práctica está diseñada para ejecutarse en **Google Colab** o en servicios en la nube de Activeloop. La PC solo funciona como cliente web.
* **Duración:** 10 a 15 horas (2 horas de video + laboratorios interactivos).
* **Idioma:** Inglés.
* **Requisito de Certificación:** Completar los módulos y las evaluaciones de los proyectos.

---

## Recomendaciones Técnicas para Optimizar tu PC

Para evitar saturar la memoria RAM o la CPU al realizar prácticas en código:

1. **Entorno de Ejecución:** Utiliza siempre **Google Colab** en lugar de ejecutar Jupyter Notebooks locales con modelos pesados.
2. **Bases de Datos Vectoriales en la Nube:** Utiliza los niveles gratuitos (*Free Tiers*) de plataformas administradas como **Pinecone**, **Qdrant Cloud** o **Chroma Cloud** para almacenar tus vectores sin consumir recursos locales.
3. **Modelos vía API:** Consume los *embeddings* y LLMs a través de llamadas HTTP/API (OpenAI, Cohere, Gemini) en lugar de descargar o ejecutar modelos HuggingFace locales.

## Una vez terminado el curso:

```

[ Oracle Agentic AI Foundations ] (Conceptos, LangChain, MCP, Tools)
               │
               ▼
[ OCI Generative AI Professional ] (LLMs en OCI, RAG Avanzado, Clusters)
               │
               ▼
[ Oracle AI Vector Search / Database 23ai ] (Vectores + SQL relacional)
               │
               ▼
[ OCI Enterprise AI Agents / Fusion Agent Studio ] (Agentes en producción)
```