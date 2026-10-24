# Practicas/API

## Objetivo

Practicar el consumo de APIs con `curl` paso a paso. Estos ejercicios complementan la teoría del módulo [09-api](../09-api/README.md).

## Estructura

- `curl/` - Scripts bash con ejemplos prácticos

## Ruta

1. [01-curl-get.sh](./curl/01-curl-get.sh) - Petición GET básica
2. [02-curl-parametros.sh](./curl/02-curl-parametros.sh) - GET con query params
3. [03-curl-post-json.sh](./curl/03-curl-post-json.sh) - POST con JSON
4. [04-curl-headers.sh](./curl/04-curl-headers.sh) - Headers personalizados
5. [05-curl-headers-verbose.sh](./curl/05-curl-headers-verbose.sh) - Inspeccionar petición/respuesta con `-v`

## Cómo usar

Dale permisos de ejecución y corré el script:

```bash
chmod +x curl/01-curl-get.sh
./curl/01-curl-get.sh
```

O ejecutalo directamente con bash:

```bash
bash curl/01-curl-get.sh
```

## Notas

- Usamos [httpbin.org](https://httpbin.org) para practicar sin API keys.
- Leé la salida: te muestra qué enviaste y qué devolvió el servidor.
- Ideal para entender el flujo cliente-servidor antes de llamar APIs de LLM.

[← Volver a 09-API](../09-api/README.md) | [Índice principal](../README.md)
