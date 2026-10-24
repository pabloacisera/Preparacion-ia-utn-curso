# ¿Qué es curl?

## Objetivo

Aprender a usar `curl` desde cero para hacer peticiones HTTP y ver qué va y qué viene.

## ¿Qué es curl?

**curl** (*Client URL*) es una herramienta de línea de comandos que permite **enviar peticiones HTTP/HTTPS** desde la terminal y ver la respuesta del servidor.

Es perfecto para aprender APIs porque:
- **Simple**: No necesita interfaz gráfica
- **Directo**: Ves exactamente request y response
- **Universal**: Viene en Linux, macOS y Windows (WSL)
- **Muy usado**: Es estándar en desarrollo e IA

## ¿Por qué usar curl para aprender?

Cuando trabajes con APIs de IA (Groq, OpenAI, etc.), muchas veces verás ejemplos con `curl`. Entenderlo te ayudará a:
- Debuggear peticiones
- Probar endpoints rápidamente
- Entender headers, body, método HTTP
- Aprender sin depender de herramientas visuales

## Sintaxis básica

```bash
curl [opciones] [URL]
```

**Opciones más comunes:**

| Opción | Significado |
|---|---|
| `-X` o `--request` | Especifica el método HTTP (GET, POST, PUT, DELETE) |
| `-H` o `--header` | Añade cabeceras (headers) |
| `-d` o `--data` | Envía datos en el body (para POST/PUT) |
| `-i` | Muestra headers de respuesta |
| `-v` | Modo verbose (muestra todo el intercambio) |
| `-L` | Sigue redirecciones |

## GET vs POST con curl

**GET (por defecto):**
```bash
curl https://httpbin.org/get
```

**POST con JSON:**
```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"nombre": "test", "mensaje": "hola"}'
```

## ¿Qué vamos a practicar?

Usaremos [httpbin.org](https://httpbin.org) - un servicio público seguro para practicar sin afectar nada real.

**Nota:** httpbin.org devuelve lo que le enviamos, perfecto para aprender.

[← Volver al índice de API](../README.md) | [Índice de API](../README.md) | [Ir a prácticas con curl →](../Practicas/README.md)
