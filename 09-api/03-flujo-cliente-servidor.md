# 03 - Flujo básico: cliente y servidor

## Objetivo

Entender quién pide, quién responde y cuál es el camino de una petición.

## Los dos roles

| Rol | Qué hace | Ejemplo |
|---|---|---|
| **Cliente** | Inicia la petición y espera la respuesta | Tu navegador, tu script de Python, `curl` |
| **Servidor** | Recibe la petición, la procesa y responde | La máquina donde corre la API del clima |

El cliente **siempre inicia** la conversación. El servidor **responde**.

## El camino de una petición

```
Cliente                         Servidor
   |                               |
   |--- 1. Petición (request) ---->|
   |                               | 2. Procesa
   |<-- 3. Respuesta (response) ---|
   |                               |
```

1. El cliente arma una petición con una **dirección** (URL), un **método** y, a veces, **datos**.
2. El servidor la recibe, valida y procesa.
3. El servidor devuelve una respuesta con un **código de estado** y, normalmente, **datos**.

## La URL: la dirección del recurso

```
https://api.ejemplo.com/v1/clima?ciudad=cordoba
 \___/   \_____________/ \__/ \________/ \_____________/
  http       dominio      ver.  recurso     parámetros
```

- **`https://`**: protocolo seguro.
- **`api.ejemplo.com`**: dónde está el servidor.
- **`/v1/`**: versión de la API.
- **`/clima`**: recurso que querés.
- **`?ciudad=cordoba`**: parámetros que modifican la consulta.

## ¿Qué es un endpoint?

Un **endpoint** es una dirección concreta de la API que hace una cosa. Por ejemplo:
- `GET /v1/clima` → obtener el clima.
- `POST /v1/pedidos` → crear un pedido.

## ¿Por qué importa para el curso?

Cuando llamás a un LLM, sos el **cliente** y el proveedor (Groq, Gemini) es el **servidor**. El flujo es exactamente este: armás una petición con tu mensaje, el servidor la procesa y te devuelve la respuesta del modelo.

## Recapitulación

- Cliente pide, servidor responde.
- La URL indica dónde y qué recurso.
- Un endpoint es una dirección que hace una acción concreta.

[← Anterior: Contexto y uso](./02-contexto-donde-cuando-se-usa.md) | [Índice](./README.md) | [Siguiente: ¿Qué va y qué viene? →](./04-que-va-y-que-viene-en-una-peticion.md)
