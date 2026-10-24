# 09 - Ejercicios con curl

## Objetivo

Practicar peticiones HTTP reales con `curl` desde la terminal.

## ¿Qué es curl?

`curl` (Client URL) es una herramienta de línea de comandos para hacer peticiones HTTP/HTTPS. Viene en Linux, macOS y WSL.

## Antes de empezar

Usaremos **httpbin.org**: un servicio público para practicar. No requiere autenticación y devuelve lo que le envíes.

## Ejercicio 1: GET simple

Obtener información con GET.

```bash
curl https://httpbin.org/get
```

Verás un JSON con tu IP, headers, etc.

## Ejercicio 2: GET con parámetros

```bash
curl "https://httpbin.org/get?curso=ia&modulo=api"
```

Fijate cómo `args` muestra los parámetros que enviaste.

## Ejercicio 3: POST con JSON

Enviar datos en formato JSON al servidor.

```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Ana", "curso": "UTN"}'
```

- `-X POST`: método
- `-H`: header (le decimos que es JSON)
- `-d`: datos a enviar

## Ejercicio 4: Ver headers y código de estado

```bash
curl -i https://httpbin.org/get
```

`-i` muestra headers de respuesta + body. Vas a ver `HTTP/1.1 200 OK`.

## Ejercicio 5: Ver solo el código de estado

```bash
curl -o /dev/null -s -w "Código: %{http_code}\n" https://httpbin.org/get
```

## Práctica guiada

Los ejercicios prácticos centralizados están en:
[Practicas/API/curl/](../Practicas/API/curl/)

Ahí vas a encontrar los scripts `.sh` para ejecutar paso a paso.

## Consejos

- Usá comillas dobles en la URL si tiene `?` y `&`.
- Siempre poné `Content-Type: application/json` al enviar JSON.
- Leé la respuesta JSON: te enseña lo que realmente se envía/recibe.

## Recapitulación

- `curl` te permite ver el flujo HTTP sin navegador.
- Practicar GET/POST con JSON es la base para llamar APIs de LLM.
- httpbin es ideal para aprender sin riesgo.

[← Anterior: APIs en IA](./08-apis-en-ia.md) | [Índice](./README.md) | [Siguiente: Errores comunes →](./10-errores-comunes.md)
