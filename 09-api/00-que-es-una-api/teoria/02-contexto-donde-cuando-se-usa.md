# Contexto, dónde y cuándo se usa

## Objetivo

Profundizar en el contexto de uso de las APIs para entender su utilidad en la vida diaria y en el mundo de IA.

## ¿En qué contexto aparecen?

Cuando una aplicación necesita **información o una acción** que no tiene por sí misma, recurre a una API.

**Ejemplos cotidianos:**

| Situación | ¿Cómo usa API? |
|---|---|
| **Consultar el clima** | La app pide el pronóstico a una API meteorológica |
| **Iniciar sesión con Google** | Usa la API de autenticación de Google |
| **Comprar online** | Se conecta con la API de la pasarela de pago |
| **Traducir texto** | Usa la API de un servicio de traducción |
| **Hablar con un LLM** | Usa la API del modelo (Groq, OpenAI, Gemini) |

## ¿Cuándo usar una API?

- **Cuando no quieres replicar datos**: Mejor pedirlos que copiarlos.
- **Cuando necesitas funcionalidad externa**: Pagos, mapas, IA, etc.
- **Cuando varios sistemas deben compartir información**: Web + app móvil + terceros.
- **Cuando quieres automatizar**: Desde scripts con `curl` hasta agentes de IA.

## ¿Cuándo NO es necesario crear una API?

- **Todo es interno y muy simple**: Si solo una app usa los datos directamente, a veces no hace falta.
- **Sin necesidad de compartir**: Si no hay otro cliente que lo consuma.

## Relación con IA y Agentes

En el mundo de **agentes de IA**, las APIs son fundamentales:

- **Herramientas (Tools)**: Un agente puede llamar a una API para buscar información, enviar correos, consultar una base de datos, etc.
- **Modelos LLM**: Se accede a ellos principalmente vía API.
- **MCP**: Usa APIs/funciones para dar capacidades al agente.

**Idea clave:** Las APIs permiten que los agentes **actúen** fuera de sí mismos, no solo **respondan**.

[← Anterior: ¿Qué es una API?](./01-que-es-una-api.md) | [Índice de API](../README.md) | [Siguiente: Analogías y cliente-servidor →](./03-analogias-y-cliente-servidor.md)
