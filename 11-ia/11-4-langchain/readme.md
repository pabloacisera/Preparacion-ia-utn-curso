# 13. LangChain y su ecosistema

> **Objetivo:** pasar de llamar al modelo "a mano" (Módulos 10–12) a **orquestar** todo con un framework: conectar modelos, prompts, datos externos, memoria y herramientas en una sola tubería, y encadenar varios pasos.

## Qué es LangChain

**LangChain** es un framework (marco de trabajo) para construir aplicaciones con modelos de lenguaje. Permite:

1. **Conectar** el LLM con APIs, herramientas y bases de datos.
2. **Orquestar** varios pasos en secuencia.
3. Construir **chatbots**, **RAG** y **agentes**.

Sin un framework, todo eso se puede hacer igual, pero a mano y repitiendo código. LangChain pone piezas estándar para cada parte.

> **Cuándo NO usarlo:** para cosas muy simples puede ser sobreingeniería. Por eso primero vimos cómo llamar a la API directamente (Módulo 10): así sabemos qué hace la librería por nosotros.

## El ecosistema

| Pieza | Para qué |
|-------|----------|
| **LangChain** | Las piezas base: prompts, cadenas, memoria, herramientas. |
| **LangGraph** | Flujos como **grafos de estados** (nodos y aristas): agentes cíclicos, ramificaciones, control humano en el medio (*human-in-the-loop*). |
| **LangSmith** | **Observabilidad**: trazas, logs y depuración de lo que pasa en cada paso. |
| **Integraciones** | Conectores a cientos de servicios externos (modelos, bases de datos, buscadores). |

## Prompt templates

Un **prompt template** es un texto con **huecos** (variables) que se rellenan en tiempo de ejecución. Es como una función: recibe entradas y devuelve un prompt listo.

- **`PromptTemplate`:** para una petición simple, de un solo turno.
- **`ChatPromptTemplate`:** una secuencia de mensajes con **roles** (system, user, assistant), para conversaciones.
- **Few-shot:** incluye **ejemplos** dentro del prompt para guiar el formato o el estilo.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Sos ingeniero de software y explicás el concepto a un principiante: {tema}"
)
prompt_listo = prompt.format(tema="el bucle de razonamiento de un agente")
```

## Chains (cadenas)

Una **cadena** es un proceso **paso a paso**: la salida de un paso es la entrada del siguiente. Se arma con el operador `|` (*pipe*).

```python
chain = prompt | model | StrOutputParser()
```

- `prompt` arma el texto.
- `model` genera la respuesta (objeto con `.content`).
- `StrOutputParser` extrae solo el **texto**, para que el resultado sea un string limpio.

Se invoca siempre igual: `chain.invoke({"tema": "..."})`.

## Memoria

El LLM **no recuerda** entre llamadas (Módulo 10). LangChain ofrece objetos de historial para **reenviar** la conversación:

```python
from langchain_core.chat_history import InMemoryChatMessageHistory

history = InMemoryChatMessageHistory()
# se agregan los mensajes y se inyectan en el prompt con un placeholder {history}
```

> Para memoria que **persiste** entre sesiones no alcanza con el historial en memoria: se combina con RAG (Módulo 12) guardando e indexando lo relevante.

## Otros frameworks del ecosistema

- **SDK de OpenAI para agentes:** threads (memoria), *code interpreter*, búsqueda documental y *function calling*.
- **CrewAI:** equipos **multi-agente** orientados a roles (varios agentes colaborando).
- **Hugging Face Smol Agents:** librería liviana donde el agente actúa escribiendo **código** en lugar de solo devolver texto o JSON.

Los mencionamos para ubicarnos; en el curso trabajamos con **LangChain**.

## Ejercicios

- [01 — Prompt templates, cadenas y memoria](./exercises/01-prompt-cadenas-memoria.md)

## Material complementario

- [Integración con LangChain](./into_langchain.md)

[Menu Principal](../../README.md) | [Índice IA](../readme.md) | [Anterior: Teoría de agentes ←](../11-3-teoria-agentes/readme.md) | [Siguiente: ¿Qué es RAG? →](../11-5-rag/readme.md)
