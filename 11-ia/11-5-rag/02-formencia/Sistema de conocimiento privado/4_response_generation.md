## Ultima etapa de recuperación

Imagina que has construido un sistema de recuperación impecable: los documentos más relevantes están en tus manos. Pero al pasárselos al modelo de lenguaje, la respuesta que obtienes es genérica, imprecisa o, peor aún, inventada. ¿Qué ha fallado? La clave no está solo en qué información le das al modelo, sino en cómo se la presentas.

Un estudio sobre fundamentación en generaciones largas reveló que incluso modelos masivos como Falcon 180B producen alrededor de un 25% de respuestas correctas pero no fundamentadas en los documentos proporcionados. Esto demuestra que la mera presencia del contexto no garantiza que el LLM lo utilice.

En esta lección, aprenderás a tender el puente entre la recuperación y la generación: técnicas de inyección de contexto que obligan al modelo a basarse en la evidencia, y estrategias para detectar y frenar las alucinaciones antes de que lleguen al usuario.

La inyección de contexto es el mecanismo que añade al prompt los datos recuperados o el conocimiento situacional relevante. Aunque la forma más directa es concatenar el texto recuperado antes o después de la pregunta del usuario, esta aproximación carece de control y puede llevar al modelo a ignorar la información o a mezclarla con su conocimiento preentrenado.

La inyección por plantillas (templated injection) resuelve este problema utilizando una cadena de prompt predefinida con marcadores de posición para el contexto y la pregunta. Herramientas como f-strings de Python o Jinja2 permiten construir prompts donde se insertan los pasajes recuperados en ubicaciones estratégicas, acompañados de instrucciones explícitas como «Responde basándote únicamente en el contexto proporcionado». Este método ofrece un control preciso sobre la estructura, facilita la depuración y el versionado, y asegura que el modelo preste atención prioritaria a la información recuperada.

Una de las técnicas más sencillas y efectivas para reducir las alucinaciones es incluir en el prompt una instrucción clara que obligue al LLM a utilizar exclusivamente la información de los documentos recuperados. Por ejemplo: «Solo debes responder a la pregunta del usuario utilizando la información proporcionada en los documentos siguientes».

Esta práctica, recomendada tanto en guías de desarrolladores como en estudios sobre RAG, evita que el modelo recurra a su conocimiento de preentrenamiento, una fuente habitual de contenido no fundamentado. La inyección por plantillas facilita la incorporación sistemática de este tipo de directrices, ya que el texto de la instrucción forma parte fija del molde del prompt.

Además, la colocación del contexto dentro del prompt es relevante: algunos modelos muestran un sesgo de recencia, prestando más atención a la información que aparece al final. Por ello, situar el contexto justo antes de la pregunta puede mejorar la adherencia a los documentos.

Por qué sube tanto el costo cuando sumás todo
En la mayoría de las APIs, pagás los tokens de entrada en cada petición, incluyendo lo que ya se había enviado en turnos anteriores. Si tenés:

System prompt largo +

6 o 10 turnos de historial +

8 o 10 chunks recuperados (cada uno de 500–800 tokens) +

La pregunta actual

Podés estar enviando fácilmente 4.000 a 10.000 tokens de entrada por cada repregunta de un solo usuario. Multiplicado por decenas o cientos de usuarios activos, el volumen crece rápido.

Palancas concretas para bajar el consumo de tokens
Ajustar el tamaño de chunk y el top_k:
No necesitás llenar la ventana de contexto. Muchas veces 3 a 5 chunks bien rankeados (de ~300 a 500 tokens cada uno) dan mejor respuesta y menos ruido que 12 chunks largos. Menos contexto irrelevante también reduce alucinaciones.

Ventana deslizante corta + resumen selectivo:
En lugar de enviar toda la conversación, quedate con los últimos 2 a 4 turnos (user / assistant). Solo cuando la conversación supere un umbral (por ejemplo, 8 o 10 turnos), generá un resumen breve de los turnos viejos y reemplazá la historia antigua por ese resumen.

Query Rewrite condicional y con modelo barato:
No reescribas todas las preguntas. Si es el Turno 1 o la consulta ya es explícita (contiene el sustantivo o la materia), salteá el paso. Si hace falta reescribir, usá un modelo pequeño y económico (no el mismo modelo que redacta la respuesta final).

Model Routing (modelo liviano vs. modelo principal):
Usá un modelo económico para tareas auxiliares (clasificar materia, reescribir consulta, resumir historial) y dejá el modelo más capaz para responder cuando realmente se necesita razonamiento o síntesis fina.

Prompt Caching y caché de consultas:

Prompt caching: si el system prompt (y el orden fijo del prompt) se mantiene igual entre llamadas, varios proveedores cobran mucho menos por esos tokens repetidos.

Caché de recuperación / respuestas: si varios alumnos o usuarios consultan sobre el mismo tema o documento en el mismo período, cachear el resultado de búsqueda (o respuestas frecuentes) evita repetir cómputo y tokens.

Filtrado previo por metadata:
Si sabés la materia o el tema (por filtro explícito o clasificación previa), reducís el espacio de búsqueda y evitás traer chunks de otras materias que compiten por espacio en el contexto.

Regla práctica para dimensionar
Antes de optimizar a ciegas, medí dos números en tu flujo real:

Tokens promedio por turno (desglosados en: system + historial + chunks + respuesta).

Porcentaje de turnos que son repreguntas ambiguas vs. preguntas nuevas.
