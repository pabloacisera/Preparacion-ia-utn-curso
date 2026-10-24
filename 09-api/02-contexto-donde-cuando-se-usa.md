# 02 - Contexto: dónde y cuándo se usa una API

## Objetivo

Reconocer en qué situaciones reales aparece una API y por qué es la forma estándar de conectar sistemas.

## La idea

Una API existe cuando **dos programas necesitan intercambiar información o acciones** sin conocerse por dentro. Uno pide (cliente) y otro responde (servidor).

## Ejemplos cotidianos

| Situación | Qué hace la API |
|---|---|
| Abrís la app del clima | Le pide el pronóstico a un servicio meteorológico |
| "Iniciar sesión con Google" | Verifica tu identidad con Google |
| Pagás una compra online | Envía los datos del pago a la pasarela de pago |
| Pedís un viaje en una app | Consulta conductores y calcula el precio |
| Hablás con un chatbot | Envía tu mensaje al modelo de lenguaje |

En todos los casos, tu dispositivo **no tiene** esos datos ni esa capacidad: los pide a otra máquina mediante una API.

## ¿Cuándo conviene usar una API?

- **Cuando el dato lo tiene otro**: clima, mapas, cotizaciones.
- **Cuando la acción la hace otro**: pagos, envíos de correo, autenticación.
- **Cuando varios clientes comparten el mismo servicio**: web, app móvil, agentes.
- **Cuando querés automatizar**: scripts, agentes, integraciones.

## ¿Cuándo NO conviene?

- Si el dato es local y nadie más lo necesita, a veces alcanza con un archivo o una base de datos.
- Si el servicio es muy simple y no va a crecer, una API puede ser complejidad innecesaria.

## ¿Por qué importa para LLM, agentes y RAG?

- **LLM**: casi todos se usan por API (Groq, Gemini, OpenAI). No ejecutás el modelo en tu computadora.
- **Agentes**: cada herramienta que usa un agente suele ser una API (buscar, enviar, consultar).
- **RAG**: las bases de datos vectoriales y los servicios de embeddings también se consumen por API.

> Sin entender APIs no podés entender cómo un agente "actúa" sobre el mundo.

## Recapitulación

- Una API conecta dos programas que no se conocen por dentro.
- Se usa cuando el dato o la acción están en otro lugar.
- Es la base de la IA moderna: modelos, herramientas y bases vectoriales son APIs.

[← Anterior: ¿Qué es una API?](./01-que-es-una-api.md) | [Índice](./README.md) | [Siguiente: Flujo cliente-servidor →](./03-flujo-cliente-servidor.md)
