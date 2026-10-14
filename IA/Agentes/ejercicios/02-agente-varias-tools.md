# Ejercicio 02 — Agente con varias herramientas y traza

**Objetivo:** ampliar el agente a varias herramientas (incluyendo manejo de errores) y **trazar** paso a paso qué razona y hace, para entender el bucle agéntico.

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
import math
from typing import Union
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv(find_dotenv())
model = init_chat_model(os.getenv("GROQ_MODEL"), model_provider="groq")

# ---- Herramientas (con manejo de errores) ----
@tool
def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Resta el segundo número al primero."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

@tool
def divide(a: float, b: float) -> Union[float, str]:
    """Divide el primero por el segundo. Maneja la división por cero."""
    if b == 0:
        return "Error: división por cero."
    return a / b

@tool
def square_root(a: float) -> Union[float, str]:
    """Calcula la raíz cuadrada de un número no negativo."""
    if a < 0:
        return "Error: no se puede calcular la raíz de un número negativo."
    return math.sqrt(a)

tools = [add, subtract, multiply, divide, square_root]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=("Sos un asistente de matemática claro y conciso. "
                   "Respondé en texto plano, sin notación matemática."),
)

def run_agent(pregunta: str):
    print("=" * 60)
    print(f"Pregunta: {pregunta}")
    print("=" * 60)
    resultado = agent.invoke({"messages": [("human", pregunta)]})

    for msg in resultado["messages"]:
        if msg.type == "human":
            continue
        elif msg.type == "ai" and getattr(msg, "tool_calls", None):
            for call in msg.tool_calls:
                print(f"[RAZONA]  usa '{call['name']}' con {call['args']}")
        elif msg.type == "tool":
            print(f"[OBSERVA] resultado: {msg.content}")
        elif msg.type == "ai" and msg.content:
            print(f"\n[RESPONDE] {msg.content}\n")

if __name__ == "__main__":
    run_agent("¿Cuánto es 42 dividido 16?")
    run_agent("¿Cuánto es 15 por 8, y eso dividido 3?")
    run_agent("Tengo un rectángulo de 12 x 7. ¿Cuál es el área y su raíz cuadrada?")
```

## Qué deberías observar

- Para una operación simple hay **un** paso; para una **combinada**, varios (razonar → actuar → observar → razonar…).
- Las herramientas pueden **devolver errores como texto**: el agente los lee como observación y puede reaccionar.
- La traza muestra el patrón **ReAct**: alternancia de razonamiento y acción.

## Experimentos

1. Pedí *"dividí 10 por 0"*. ¿Cómo maneja el agente el mensaje de error?
2. Pedí la raíz cuadrada de un número negativo. ¿Qué responde?
3. Agregá una herramienta nueva (por ejemplo, `power`) y comprobá que el agente la usa sin cambiar el resto.

[Volver al módulo](../readme.md)
