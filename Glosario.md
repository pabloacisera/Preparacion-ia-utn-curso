# Glosario

## Conceptos generales

| Termino | Significado |
| :---    | :---        |
| `Programación` |  |
| `Repositorio`| |
| `Paquete` | |
| `Script` | |

## Inteligencia Artificial

| Término | Significado |
| :---    | :---        |
| `LLM` | Modelo de lenguaje grande; un "autocompletar" muy entrenado que predice el token siguiente. |
| `Prompt` | Texto de entrada que se le da al modelo. |
| `Token` | Pieza de texto que el modelo trata como unidad (por ejemplo, `" gato"`, `"."`). |
| `ID` | Número de un token dentro del vocabulario. |
| `Vocabulario (V)` | Lista de todos los tokens que el modelo conoce. |
| `Contexto` | Lo que el modelo tiene a la vista para predecir. |
| `Ventana de contexto` | Cantidad máxima de tokens que el modelo puede tener a la vista a la vez. |
| `Vector` | Lista ordenada de números. |
| `Dimensión (D)` | Cuántos números tiene cada vector. |
| `Embedding` | Vector que representa el significado de un texto o token. |
| `Similitud coseno` | Medida de qué tan parecidos son dos vectores (1 = misma dirección). |
| `Parámetros / pesos` | Los números que el modelo ajusta al entrenarse. |
| `Query / Key / Value` | En atención: "qué busco" / "qué ofrezco" / "qué contenido aporto". |
| `Codificación posicional` | Marca el lugar que ocupa cada token en la secuencia. |
| `Máscara causal` | Regla que impide mirar tokens futuros. |
| `Atención` | Mecanismo donde cada token decide a cuáles otros "escuchar". |
| `Transformer` | Arquitectura basada en capas de atención; el motor de los LLM actuales. |
| `Logit` | Puntaje crudo por token, antes de softmax. |
| `Softmax` | Convierte puntajes en probabilidades que suman 1. |
| `Greedy` | Estrategia de elegir siempre el token más probable. |
| `Temperatura` | Control del azar al elegir: menor = más conservador, mayor = más variado. |
| `Top-k` | Sortear solo entre los k tokens más probables. |
| `Autorregresión` | Usar la propia salida como parte de la siguiente entrada. |
| `Token de fin` | Marca con la que el modelo señala que terminó. |
| `Pérdida (loss)` | Mide qué tan mal predice el modelo; entrenar es bajarla. |
| `Gradiente` | Dirección en la que mover cada parámetro para bajar la pérdida. |
| `Chat template` | Formato con roles que convierte una conversación en un solo texto. |
| `Alucinación` | Respuesta inventada que el modelo presenta como cierta. |
| `API` | Interfaz para usar un modelo alojado en un servidor (por ejemplo, Groq, Gemini). |
| `ONNX` | Formato estándar para guardar un modelo y ejecutarlo en distintos entornos. |
| `ONNX Runtime` | Motor que ejecuta un modelo en formato ONNX. |
| `RAG` | *Retrieval-Augmented Generation*: arquitectura que recupera fragmentos relevantes y se los pasa al LLM. |
| `Chunking` | Partir los documentos en fragmentos (chunks) antes de indexarlos. |
| `Base de datos vectorial` | Almacén que guarda embeddings y hace búsquedas por similitud. |
| `ANN` | Búsqueda aproximada de vecinos cercanos; rápida sobre millones de vectores. |
| `Búsqueda híbrida` | Combinar búsqueda semántica (vectores) con búsqueda por palabra clave (BM25). |
| `BM25` | Algoritmo clásico de búsqueda por palabra clave. |
| `Metadatos` | Datos que acompañan a un fragmento (título, autor, fecha). |
| `LangChain` | Framework para orquestar modelos, prompts, memoria y herramientas. |
| `LangGraph` | Extensión de LangChain para flujos como grafos de estados. |
| `LangSmith` | Herramienta de observabilidad y depuración de aplicaciones con LLM. |
| `Prompt template` | Texto con huecos (variables) que se rellenan en tiempo de ejecución. |
| `ChatPromptTemplate` | Secuencia de mensajes con roles (system, user, assistant). |
| `Few-shot` | Incluir ejemplos dentro del prompt para guiar el formato o el estilo. |
| `Chain` | Proceso paso a paso donde la salida de un paso alimenta al siguiente. |
| `Parser` | Componente que extrae el texto limpio de la respuesta del modelo. |
| `Agente` | Sistema que decide qué hacer y actúa en un bucle hasta cumplir un objetivo. |
| `Tool` (herramienta) | Función que el agente puede invocar para actuar sobre el mundo. |
| `Tool calling` | El LLM emite una llamada estructurada (qué tool y con qué argumentos); el agente la ejecuta. |
| `Bucle agéntico` | Ciclo percibir → razonar → actuar → observar. |
| `Orquestación` | El "pegamento" que maneja el bucle, la memoria y las rutas de las herramientas. |
| `CoT` | *Chain of Thought*: pedirle al modelo que piense paso a paso. |
| `ReAct` | Patrón que entrelaza razonar y actuar. |
| `ToT` | *Tree of Thoughts*: explorar varios caminos de razonamiento y compararlos. |
| `Guardrails` | Reglas y filtros que limitan el comportamiento permitido de un agente. |
| `Prompt injection` | Ataque que intenta secuestrar las instrucciones del sistema. |
| `Human-in-the-loop` | Que una persona valide una acción antes de ejecutarla. |
| `Sandboxing` | Ejecutar en un entorno aislado para limitar daños. |
| `MCP` | *Model Context Protocol*: estándar para conectar agentes con herramientas y datos externos. |
| `Skill` | Paquete de instrucciones y recursos que enseña al agente cómo hacer una tarea. |
| `Spec` (especificación) | Descripción clara de objetivo, entradas, salidas y criterios de éxito de una tarea. |
