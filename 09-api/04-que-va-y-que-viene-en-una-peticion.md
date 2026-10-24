# 04 - ¿Qué va y qué viene en una petición?

## Objetivo

Diferenciar entre request y response: qué envía el cliente y qué devuelve el servidor.

## Petición (Request) vs Respuesta (Response)

| Elemento | Request | Response |
|---|---|---|
| **Quién** | Cliente | Servidor |
| **Cuándo** | Siempre primero | Siempre después de la petición |
| **Contenido** | Método, URL, headers, body (opcional) | Código de estado, headers, body (suele tener datos) |

## Partes de una petición

1. **Método HTTP** - qué acción querés hacer (GET, POST, PUT, DELETE...)
2. **URL/Endpoint** - a dónde ir
3. **Headers** - información extra (autenticación, tipo de dato)
4. **Body** - datos que enviás (solo en algunos métodos como POST/PUT)

## Partes de una respuesta

1. **Código de estado** - resultado de la operación (200, 404, 500...)
2. **Headers** - metadatos sobre la respuesta
3. **Body** - los datos que pediste (JSON, texto, etc.)

## Ejemplo práctico: pedir clima

**Petición (cliente):**
```http
GET https://api.ejemplo.com/v1/clima?ciudad=cordoba
Accept: application/json
```

**Respuesta (servidor):**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "ciudad": "Cordoba",
  "temperatura": 22,
  "estado": "soleado"
}
```

## ¿Por qué importa?

- En un agente con herramientas, el agente **arma** la petición.
- Al llamar a un LLM por API, enviás un body con tu prompt en JSON.
- Al recibir la respuesta, extraés los datos que necesitás.

## Recapitulación

- Request = lo que pedís. Response = lo que te devuelven.
- Headers dan contexto; body lleva datos.
- El formato más común hoy es **JSON**.

[← Anterior: Cliente-Servidor](./03-flujo-cliente-servidor.md) | [Índice](./README.md) | [Siguiente: Tipos de peticiones HTTP →](./05-tipos-de-peticiones-http.md)
