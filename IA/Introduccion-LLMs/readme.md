# 10. Introducción a los LLMs

> **Objetivo:** entender qué es un modelo de lenguaje, cómo se lo usa desde el código (vía API) y qué esperar de él: aciertos, prompts y alucinaciones.

## ¿Qué es un LLM?

Un **LLM** (*Large Language Model*, modelo grande de lenguaje) es un programa entrenado con enormes cantidades de texto cuya única tarea es **predecir la siguiente pieza de texto** (el siguiente *token*) dada la secuencia anterior. Repite esa predicción una y otra vez, y así "escribe".

No consulta una base de datos ni "sabe" cosas: calcula probabilidades. Cuando le pedimos una respuesta, en realidad le pedimos que **continúe** un texto de la forma más probable.

> Los detalles internos (tokens, embeddings, cómo calcula esas probabilidades) se ven en el [Módulo 11](../Funcionamiento-Interno/readme.md). Por ahora alcanza con la idea de "autocompletar muy entrenado".

## Cómo se usa: la API

No ejecutamos el modelo en nuestra computadora: se lo pedimos a un proveedor a través de una **API**. Los proveedores que usamos en el curso son **Groq** y **Gemini** (tienen plan gratuito). El flujo es siempre el mismo:

1. Nos registramos y obtenemos una **API key** (una credencial secreta).
2. Guardamos la key en un archivo `.env` (nunca en el código ni en el repositorio).
3. Desde Python enviamos una **petición** con el mensaje y recibimos una **respuesta**.

### La API key y el archivo `.env`

```bash
# En la raíz del proyecto
touch .env && nano .env
```

```env
# .env  (NO se sube al repositorio: agregar .env al .gitignore)
GROQ_API_KEY=tu_clave_secreta
MODEL=llama-3.3-70b-versatile
```

```python
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())                       # carga el .env a las variables de entorno
api_key = os.getenv("GROQ_API_KEY")
modelo = os.getenv("MODEL")
```

### Parámetros que conviene conocer

| Parámetro | Qué controla |
|-----------|--------------|
| `temperature` | Cuán "creativo" es. `0` = siempre la opción más probable (predecible); valores altos = más variado. |
| `max_tokens` | Largo máximo de la respuesta. |
| `top_p` | Alternativa a la temperatura para limitar entre qué candidatos elige. |
| `stream` | Si es `True`, la respuesta llega **de a poco** (streaming) en lugar de esperar el texto completo. |

> **Costo y latencia:** cada llamada consume *tokens* (se cobra por token) y tarda un tiempo. El plan gratuito tiene **límites de uso** que cambian con el tiempo: conviene consultar la documentación vigente del proveedor.

## El poder de los prompts

Todo lo que enviamos al modelo es un **prompt**. La forma en que lo escribimos cambia el resultado. En una conversación el prompt se arma con **roles**:

- **system:** las instrucciones generales (quién es el asistente, cómo debe responder).
- **user:** el mensaje de la persona.
- **assistant:** las respuestas previas del modelo.

```python
mensajes = [
    {"role": "system", "content": "Sos un asistente breve y claro. Respondé en español."},
    {"role": "user", "content": "¿Qué es una API en una frase?"},
]
```

Buenas prácticas:

- Ser **específico** con lo que se pide (formato, extensión, idioma).
- Dar **contexto** cuando la pregunta lo necesita.
- Usar **ejemplos** dentro del prompt (*few-shot*) cuando el formato importa.

## Alucinaciones

Un LLM **inventa** cuando no tiene la información o el contexto para responder bien. Eso es una **alucinación**: una respuesta que suena correcta pero es falsa. Ocurre porque el modelo no busca la verdad, sino que continúa texto probable.

Formas de reducirla:

1. **Dar contexto** en el mismo prompt (por ejemplo, el documento relevante).
2. **Permitir la herramienta** adecuada (buscar en una base, consultar una API).
3. **Pedir que admita el desconocimiento**: *"Responde únicamente con la información proporcionada. Si no encuentras la respuesta, indica que no dispones de esa información."*

> Esta limitación es la que motiva el **RAG** (Módulo 12): en lugar de reentrenar el modelo, le damos los datos correctos en el momento de la consulta.

## Ejercicios

- [Primera llamada a la API](./ejercicios/01-primera-llamada-api.md)

## Cierre

Ya sabemos **qué** es un LLM y **cómo** se lo invoca. La pregunta que queda abierta es *qué pasa por dentro* cuando calcula esa respuesta. Eso es el [Módulo 11](../Funcionamiento-Interno/readme.md).

[Menu Principal](../../README.md) | [Siguiente: Funcionamiento interno](../Funcionamiento-Interno/readme.md)
