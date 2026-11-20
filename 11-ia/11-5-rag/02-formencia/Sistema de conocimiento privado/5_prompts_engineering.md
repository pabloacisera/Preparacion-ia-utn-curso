## Ingeniería de Prompts

> “En un sistema RAG, el orden en que se presentan los documentos recuperados en el prompt puede cambiar la respuesta del modelo, incluso si todos son relevantes.”

<img src="../../../../assets/imagenes/11-ia/rag/prompts_structure.webp" width="650"/>

### 1. Concepto y función de un prompt

Un **prompt** es la entrada estructurada (instrucciones, reglas, contexto y consulta) que se le envía a un modelo de lenguaje (LLM) para acotar su comportamiento y obtener una salida útil y verificable.

* **No reemplaza al código:** el prompt define *cómo* interpretar el texto que recibe y *qué* formato o límites respetar, pero no busca en bases de datos por sí solo ni ejecuta programas externos.
* **Controla el foco y reduce invenciones:** al establecer reglas explícitas (como responder solo con los fragmentos provistos o indicar cuándo falta información), vuelve más predecible la respuesta.

### 2. Tipos de prompt

En una arquitectura real, los prompts cumplen distintos roles según el momento del flujo:

* **Prompt de sistema (*system prompt*):** define el rol, las reglas generales, los límites y qué hacer ante información faltante.
* **Prompt de usuario / tarea:** contiene la pregunta o instrucción del turno actual y, cuando aplica, el contexto recuperado.
* **Prompt de síntesis / multi-fuente:** reúne varios fragmentos o fuentes etiquetadas para cruzar datos, comparar o resumir sin mezclar contextos distintos.
* **Prompt de decisión / ruteo o extracción:** se emplea en pasos intermedios (clasificar intención, reformular consulta o extraer datos estructurados) antes de armar la respuesta final.

### 3. Cómo se escribe un prompt

Un buen prompt técnico es **claro, específico, delimitado y fácil de parsear**:

1. **Definí la tarea y el límite de información:** indicá qué debe hacer el modelo y qué fuente de verdad debe utilizar.
2. **Separá claramente las partes:** distinguí instrucciones, fuentes/contexto y pregunta del usuario con etiquetas o delimitadores claros.
3. **Indicá qué hacer si falta información:** habilitá explícitamente una respuesta honesta cuando el contexto no alcanza.
4. **Ordená y acotá el contexto:** priorizá los fragmentos más relevantes, evitá ruido innecesario y pedí un formato de salida concreto.

#### Plantilla de síntesis con múltiples documentos

Pregunta del usuario: [PREGUNTA_USUARIO]

Información relevante:

Fuente 1 (archivo: manual_laboral.pdf | sección: Licencias | pág. 12):
[texto del fragmento 1]

Fuente 2 (archivo: convenio_docente.pdf | sección: Suplencias | pág. 8):
[texto del fragmento 2]

Combina la información relevante de los documentos para proporcionar una respuesta completa.

### 4. Cómo ayuda el prompt a la recuperación (RAG) y al agente (*tools*)

El prompt guía las decisiones en cada etapa de la recuperación y generación de respuestas, trabajando en conjunto con la lógica del sistema:

* **En RAG (recuperación y síntesis):**
  * **Antes de buscar:** ayuda a reformular consultas ambiguas para mejorar la búsqueda, mientras que el código aplica los filtros duros (`file_id`, `session_id`, metadatos reales).
  * **Al generar:** organiza los fragmentos recuperados con sus metadatos reales, respeta el orden de relevancia y guía cómo combinar fuentes o citar respaldos.
* **En un agente / flujo con *tools*:**
  * **Selección y argumentos de herramientas:** junto con las descripciones de las *tools*, orienta cuándo conviene invocar una herramienta (por ejemplo, consultar datos o generar un archivo) y con qué parámetros.
  * **Cierre y verificación:** tras recibir el resultado de una *tool*, ayuda a evaluar si la información ya es suficiente o si hace falta otro paso antes de responder.
