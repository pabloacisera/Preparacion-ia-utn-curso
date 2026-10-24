# Ejercicio 01 — Tu primer agente con tools

**Objetivo:** crear un agente mínimo: definir **herramientas**, entregárselas al agente y ver cómo **decide** cuál usar en un bucle.

## Requisitos

```bash
pip install langchain langchain-groq python-dotenv
```

`.env`:

```env
GROQ_API_KEY=tu_clave
GROQ_MODEL=llama-3.3-70b-versatile
```

## Código

```python
import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv(find_dotenv())
model = init_chat_model(os.getenv("GROQ_MODEL"), model_provider="groq")

# ---- 1) Definimos las herramientas ----
# El decorador @tool convierte una función de Python en una herramienta.
# El docstring es lo que el LLM lee para entender cuándo usarla.
@tool
def add(a: float, b: float) -> float:
    """Suma dos números. Usar para operaciones de suma."""
    return a + b

@tool
def rest(a: float, b: float) -> float:
    """Resta dos números. Usar para operaciones de resta."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiplica dos números. Usar para operaciones de multiplicación."""
    return a * b

# Podemos inspeccionar el esquema JSON que se le envía al modelo
print(add.args_schema.model_json_schema())

# ---- 2) Creamos el agente ----
tools = [add, rest, multiply]
agent = create_agent(model=model, tools=tools)

# ---- 3) Lo invocamos ----
respuesta = agent.invoke({"messages": [("user", "¿Cuánto es 15 multiplicado por 3?")]})
print(respuesta["messages"][-1].content)

# ---- 4) Vemos la ruta completa de mensajes ----
for msg in respuesta["messages"]:
    print(msg)
```

## Qué deberías observar

- El agente **no** calcula solo: detecta la intención, elige `multiply`, la ejecuta y redacta la respuesta.
- En el bucle de mensajes vas a ver: el mensaje del usuario, una **llamada a herramienta** (qué tool y con qué argumentos), el **resultado** de la tool y la respuesta final.
- El `docstring` importa: es la descripción que el modelo lee para decidir.

## Experimentos

1. Preguntá algo que **no** requiera herramientas (por ejemplo, *"¿quién sos?"*). ¿Llama a alguna tool?
2. Preguntá una operación **combinada**: *"sumá 4 y 6 y luego multiplicá por 2"*. Observá cuántos pasos da.
3. Renombrá un docstring a algo ambiguo y mirá si el agente elige la herramienta correcta.

[Volver al módulo](../readme.md)
