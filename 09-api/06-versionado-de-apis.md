# 06 - Versionado de APIs

## Objetivo

Entender por qué las APIs se versionan y cómo identificar la versión.

## ¿Por qué versionar?

Una API puede cambiar con el tiempo:
- Agregar nuevos campos
- Cambiar nombres de campos
- Quitar funcionalidades
- Mejorar la respuesta

Si no se versiona, **esos cambios podrían romper** todos los scripts, apps y agentes que ya la usan.

El versionado permite **evolucionar sin romper lo existente**.

## Formas de versionar

| Forma | Ejemplo | Comentario |
|---|---|---|
| **En la URL** | `/v1/clima`, `/v2/clima` | La más común y clara. Fácil de ver. |
| **En el header** | `Accept: application/vnd.api+json; version=1` | Más limpia pero menos visible. |
| **En query params** | `?version=1` | Menos común hoy en día. |

## Ejemplo práctico

Imaginá una API que antes devolvía:
```json
{ "temp": 22 }
```

Y ahora quieren devolver más info. En `v2` devuelven:
```json
{ "temperatura": { "valor": 22, "unidad": "C" } }
```

Si el cliente sigue usando `/v1/`, sigue recibiendo el formato viejo. Si usa `/v2/`, recibe el nuevo.

## ¿Por qué importa?

- Muchos proveedores de LLM tienen versiones (`/v1/chat/completions`).
- Cuando actualizás una librería, podés seguir usando la misma versión de API sin romper todo.
- Te enseña a fijarte bien en la **URL** al leer documentación.

## Recapitulación

- Versionar = permitir cambios sin romper clientes existentes.
- Lo más habitual es poner `v1`, `v2` en la URL.
- Siempre fijate qué versión usa la documentación que seguís.

[← Anterior: Tipos de peticiones HTTP](./05-tipos-de-peticiones-http.md) | [Índice](./README.md) | [Siguiente: Versionado en IA →](./07-versionado-en-ia.md)
