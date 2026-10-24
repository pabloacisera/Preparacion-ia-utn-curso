# 10 - Errores comunes al trabajar con APIs

## Objetivo

Aprender a identificar y solucionar los errores más frecuentes.

## Tabla de errores comunes

| Error | Causa | Solución |
|tag: Error | Causa | Solución |
|---|---|---|
| **404 Not Found** | URL o endpoint incorrecto | Revisá la ruta. Fijate en la documentación. |
| **401 Unauthorized** | Falta API key o está mal | Verificá el header `Authorization: Bearer ...` o `x-api-key`. |
| **400 Bad Request** | JSON mal armado, faltan campos | Validá el JSON. Revisá `required` en la docs. |
| **415 Unsupported Media Type** | Falta `Content-Type: application/json` | Agregá el header correcto. |
| **429 Too Many Requests** | Excediste el límite (rate limit) | Esperá un momento. Revisá límites del proveedor. |
| **500 Internal Server Error**| Fallo del servidor API | Reintentá más tarde. Generalmente no es tu culpa. |
| **SSL/TLS errors** | Problema de HTTPS/certificado | Usá `https://`. En curl raro, pero puede pasar. |

## Errores típicos en APIs de LLM

| Error | Explicación | Solución |
|---|---|---|
| **"model not found"** | Modelo mal escrito o no disponible | Revisá el nombre exacto en la documentación. |
| **"Invalid API key"** | Clave incorrecta o expirada | Generá una nueva key. Revisá que no tenga espacios. |
| **"messages must be non-empty"** | Falta el array `messages` o está vacío | Asegurate de enviar `messages: [{role: "user", content: "..."}]` |
| **"max_tokens exceeded"** | Demasiado largo para ese modelo | Acortá el prompt o subí límite si aplica. |
| **JSON decode error** | Respuesta no es JSON | A veces el proveedor devuelve error HTML. Mirá la respuesta completa. |

## Trucos para debuggear

1. **Usá `curl -v`** - te muestra todo: petición + respuesta.
2. **Imprimí la respuesta completa** - no solo el error, mirá el body.
3. **Probá primero con curl** - antes de pasar a Python, confirmá que funciona.
4. **Fijate en el body del error** - casi siempre explica qué falta.

```bash
curl -v -X POST https://httpbin.org/status/400
```

## Mentalidad

Los errores HTTP son **normales** cuando aprendés APIs. Leer el mensaje de error te dice el 90% de la solución. No adivines: **leé la respuesta**.

## Recapitulación

- 4xx = error tuyo (petición mal armada).
- 5xx = error del servidor.
- Con LLMs, el body del error suele decir qué campo falta.
- Debuggear = leer headers + body.

[← Anterior: Ejercicios con curl](./09-ejercicios-con-curl.md) | [Índice](./README.md) | [Siguiente: Practicas/API →](../../Practicas/API/README.md)
