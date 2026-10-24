# Prácticas - curl desde cero

## Objetivo

Practicar peticiones HTTP con `curl` usando endpoints públicos seguros.

## Prerrequisitos

Tener `curl` instalado. En WSL/Linux normalmente ya viene instalado.

Para verificar:
```bash
curl --version
```

## Práctica 1: GET simple

Abre tu terminal y ejecuta:

```bash
curl https://httpbin.org/get
```

**Observar:** Verás JSON con información sobre tu petición (headers, origen, etc.)

## Práctica 2: GET con parámetros

Los parámetros van en la URL con `?clave=valor&otra=valor`

```bash
curl "https://httpbin.org/get?nombre=ana&curso=agentes-ia"
```

**Observar:** httpbin.org muestra los `args` que le enviaste.

## Práctica 3: POST con JSON

Enviar datos al servidor:

```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"usuario": "estudiante", "tema": "apis"}'
```

**Observar:** Verás que httpbin.org devuelve el `json` que enviaste.

## Práctica 4: Ver headers de respuesta

```bash
curl -i https://httpbin.org/get
```

**Observar:** Verás las cabeceras HTTP primero, luego el body.

## Práctica 5: Modo verbose

Para entender TODO el intercambio:

```bash
curl -v https://httpbin.org/get
```

**Observar:** Verás lo que envía curl y lo que recibe (útil para debug).

## Ejercicios para practicar

1. **Ejercicio 1**: Haz un GET a `https://httpbin.org/status/200`. ¿Qué código devuelve?
2. **Ejercicio 2**: Haz un GET a `https://httpbin.org/status/404`. ¿Qué ocurre?
3. **Ejercicio 3**: Envía un POST con tus propios datos en JSON
4. **Ejercicio 4**: Usa `-H` para añadir un header personalizado, por ejemplo `-H "X-Mi-Header: prueba"`

## Archivos de práctica

También tienes archivos listos para ejecutar:
- [`01-curl-get.sh`](./01-curl-get.sh)
- [`02-curl-con-headers.sh`](./02-curl-con-headers.sh)
- [`03-curl-post-json.sh`](./03-curl-post-json.sh)

[← Volver a teoría](../teoria/01-curl-desde-cero.md) | [Índice de API](../../README.md) | [Siguiente sección: Errores comunes y debug →](../../06-errores-comunes-y-debug/teoria/01-como-leer-una-respuesta-y-depurar.md)
