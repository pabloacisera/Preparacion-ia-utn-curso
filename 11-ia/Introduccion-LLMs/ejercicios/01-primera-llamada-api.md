# Ejercicio 01 — Primera llamada a la API

**Objetivo:** configurar la credencial y hacer nuestra primera consulta a un LLM vía API, usando directamente el SDK del proveedor (sin frameworks intermediarios).

## Requisitos

```bash
pip install groq python-dotenv
```

Obtené una API key gratuita en la consola de Groq y guardala en un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_clave
MODEL=llama-3.3-70b-versatile
```

> No compartas el `.env`. Agregá `.env` al `.gitignore` para que nunca se suba al repositorio.

## Código

```python
import os
from dotenv import load_dotenv, find_dotenv
from groq import Groq

load_dotenv(find_dotenv())                              # carga el .env

client = Groq(api_key=os.getenv("GROQ_API_KEY"))        # cliente del proveedor

respuesta = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": "¿Qué es una API en una frase?"}],
)

print(respuesta.choices[0].message.content)
```

## Qué deberías observar

- La llamada funciona **sin tener ningún modelo instalado localmente**: el cálculo ocurre en los servidores del proveedor.
- La respuesta es un objeto; el texto está en `respuesta.choices[0].message.content`.
- Todo es una **petición HTTP** que la librería `groq` arma por nosotros. En el Módulo 13 veremos que un framework puede envolver esto mismo, pero primero conviene verlo "a mano".

## Experimentos

1. Agregá `temperature=0` y luego `temperature=1.5` a la llamada `create(...)` con la misma pregunta. ¿Cuándo cambia la respuesta?
2. Enviá varios mensajes con **roles** (`system` y `user`) dentro de `messages` y observá cómo cambia el tono.
3. Pedile algo que probablemente no sepa, por ejemplo *"¿Cuál fue el resultado del partido de ayer de mi equipo?"*, y comprobá si **inventa** o admite que no lo sabe. Anotá el resultado.

[Volver al módulo](../readme.md)
