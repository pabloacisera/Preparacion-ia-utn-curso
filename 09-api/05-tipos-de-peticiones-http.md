# 05 - Tipos de peticiones HTTP

## Objetivo

Conocer los métodos HTTP más usados y cuándo aplicar cada uno.

## Métodos principales

| Método | Acción | Idempotente* | Tiene body | Uso típico |
|---|---|---|---|---|
| **GET** | Obtener datos | Sí | Raro (evitar) | Listar usuarios, ver clima |
| **POST** | Crear un recurso nuevo | No | Sí | Crear un pedido, enviar un mensaje al LLM |
| **PUT** | Reemplazar un recurso completo | Sí | Sí | Actualizar todo un perfil |
| **PATCH** | Actualizar solo parte | Depende | Sí | Cambiar solo el email |
| **DELETE** | Eliminar un recurso | Sí | Raro | Borrar una cuenta |

*\*Idempotente = hacer la misma petición varias veces da el mismo resultado.*

## Analogía con una caja

Pensalo como una oficina de pedidos:
- **GET**: "¿Qué hay en el archivo?" - solo mirás.
- **POST**: "Quiero abrir un expediente nuevo" - creás.
- **PUT/PATCH**: "Quiero modificar ese expediente" - actualizás.
- **DELETE**: "Quiero borrar ese expediente" - eliminás.

## Códigos de estado (los más importantes)

| Código | Significado | Cuándo aparece |
|---|---|---|
| **200 OK** | Todo bien | Petición exitosa (GET) |
| **201 Created** | Creado con éxito | POST exitoso |
| **400 Bad Request** | Petición mal armada | Faltan datos o están mal |
| **401 Unauthorized** | No autenticado | Falta token/API key |
| **403 Forbidden** | No autorizado | Tenés token pero no permiso |
| **404 Not Found** | No existe | URL o recurso incorrecto |
| **429 Too Many Requests** | Muchas peticiones | Límite de uso |
| **500 Internal Server Error** | Error del servidor | Fallo interno |

## ¿Cuándo usar qué con APIs de IA?

- **GET**: listar modelos disponibles.
- **POST**: **el más común**. Enviar prompt al LLM, crear conversación, buscar en RAG.
- **DELETE**: borrar historial/conversación.

## Recapitulación

- GET lee, POST crea, PUT/PATCH actualizan, DELETE borra.
- Los códigos de estado te dicen si salió bien o mal.
- Con LLMs vas a usar **POST** casi siempre.

[← Anterior: ¿Qué va y qué viene?](./04-que-va-y-que-viene-en-una-peticion.md) | [Índice](./README.md) | [Siguiente: Versionado de APIs →](./06-versionado-de-apis.md)
