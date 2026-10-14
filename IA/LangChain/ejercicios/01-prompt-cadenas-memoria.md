# Ejercicio 01 — Prompt templates, cadenas y memoria

**Objetivo:** recorrer las piezas base de LangChain: un template simple, un template de chat con roles, una cadena con `|` y memoria de conversación.

## Requisitos

```bash
pip install langchain langchain-groq python-dotenv
```

`.env`:

```env
GROQ_API_KEY=tu_clave
GROQ_MODEL=llama-3.3-70b-versatile
```

## Configuración común

```python
import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(find_dotenv())
model = init_chat_model(os.getenv("GROQ_MODEL"), model_provider="groq")
print(model)
```

## 1. Prompt template simple

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Sos ingeniero de software y explicás el concepto a un principiante: {tema}"
)
respuesta = model.invoke(prompt.format(tema="el bucle de razonamiento de un agente"))
print(respuesta.content)
```

## 2. Chat prompt template (con roles y datos)

```python
from langchain_core.prompts import ChatPromptTemplate

mock_db = {
    "tabla": "users_payroll_2026",
    "columnas": ["user_id", "first_name", "last_name", "yearly_compensation_usd"],
    "motor": "PostgreSQL",
}

chat_template = ChatPromptTemplate.from_messages([
    ("system", "Sos un analista de datos. Escribí SQL para {motor}. Devolvé SOLO el SQL."),
    ("human", "Tabla: {tabla}\nColumnas: {columnas}\n\nTarea: los 5 empleados mejor pagos."),
])

mensajes = chat_template.format_messages(
    motor=mock_db["motor"],
    tabla=mock_db["tabla"],
    columnas=", ".join(mock_db["columnas"]),
)
print(model.invoke(mensajes).content)
```

## 3. Cadena con pipe y parser

```python
from langchain_core.output_parsers import StrOutputParser

chat_template = ChatPromptTemplate.from_messages([
    ("system", "Traducí del español al inglés. Respondé SOLO con la palabra traducida."),
    ("human", "Traducí: {palabra}"),
])

chain = chat_template | model | StrOutputParser()
resultado = chain.invoke({"palabra": "Perro"})
print(resultado, type(resultado))   # ahora es un string, no un objeto con .content
```

## 4. Memoria de conversación

```python
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

historial = InMemoryChatMessageHistory()
historial.add_message(HumanMessage(content="Me llamo Pablo."))
historial.add_message(HumanMessage(content="Vivo en Reconquista, Santa Fe."))

chat_con_memoria = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente útil."),
    ("placeholder", "{historial}"),
    ("human", "{pregunta}"),
])
chain_mem = chat_con_memoria | model | StrOutputParser()

print(chain_mem.invoke({"historial": historial.messages,
                        "pregunta": "¿Dónde vivo?"}))
```

## Qué deberías observar

- El template simple y el de chat producen resultados distintos: los **roles** cambian el comportamiento.
- La cadena con `|` devuelve un **string limpio** gracias a `StrOutputParser`.
- El modelo "recuerda" porque le **reenviamos el historial** en el prompt, no porque tenga memoria propia.

## Experimentos

1. Quitá el `StrOutputParser()` de la cadena e imprimí el resultado. ¿Qué tipo de objeto es?
2. Agregá un segundo turno al historial y volvé a preguntar: ¿recuerda más cosas?
3. Cambiá el `system` y observá cómo cambia el tono de todas las respuestas.

[Volver al módulo](../readme.md)
