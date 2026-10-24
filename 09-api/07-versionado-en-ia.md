# 07 - Versionado en el contexto de IA

## Objetivo

Entender por qué en APIs de LLMs el versionado es especialmente importante.

## ¿Por qué cambia tanto en IA?

Los modelos de lenguaje evolucionan rápido:
- Cambian el formato de respuesta
- Agregan o quitan funcionalidades
- Cambian parámetros (`max_tokens`, `temperature`, etc.)
- Modifican cómo se envían mensajes
- Mejoran costos, límites o capacidades

## Dónde se ve

La gran mayoría usa `/v1/`:

```
https://api.groq.com/openai/v1/chat/completions
https://generativelanguage.googleapis.com/v1beta/models/...
```

Algunas usan `v1beta` mientras están en prueba.

## Caso práctico: formato de mensajes

Antes podías enviar:
```json
{ "prompt": "Hola" }
```

Hoy es estándar el formato **OpenAI-compatible**:
```json
{
  "model": "llama-3.1-8b-instant",
  "messages": [
    { "role": "user", "content": "Hola" }
  ],
  "temperature": 0.7
}
```

Si la API cambiara ese formato sin versión, todos los agentes dejarían de funcionar.

## Versionado vs cambios de modelo

Hay dos cosas distintas:
- **Versión de API** (`v1`) - cambia el contrato (estructura de petición/respuesta).
- **Nombre de modelo** (`llama-3.1`, `gemini-2.5`) - cambia el modelo usado, pero suele mantener el mismo formato de API.

## ¿Por qué importa para agentes?

Los agentes usan herramientas para llamar APIs. Si la API cambia y no usás la versión correcta, el agente falla. Por eso siempre conviene:
- Leer la **documentación actual** del proveedor.
- Fijarte en `v1`/`v1beta` de la URL.
- Usar el formato que muestra esa documentación.

## Recapitulación

- Las APIs de IA cambian seguido, por eso se versionan.
- `/v1/` protege el formato para que siga funcionando.
- Modelo distinto ≠ versión de API distinta.

[← Anterior: Versionado de APIs](./06-versionado-de-apis.md) | [Índice](./README.md) | [Siguiente: APIs en IA →](./08-apis-en-ia.md)
