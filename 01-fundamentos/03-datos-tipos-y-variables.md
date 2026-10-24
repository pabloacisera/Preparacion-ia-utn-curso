# 03 - Datos, tipos y variables

## Objetivo

Entender qué es un dato, qué tipos básicos existen y qué es una variable.

## ¿Qué es un dato?

Un **dato** es una pieza de información: un número, un texto, una respuesta sí/no.

## Tipos de datos básicos

| Tipo | Qué guarda | Ejemplos |
|---|---|---|
| **Número entero** | Números sin decimales | `5`, `-3`, `100` |
| **Número decimal** | Números con coma | `3.14`, `0.5` |
| **Texto (string)** | Letras, palabras, símbolos | `"hola"`, `"UTN"` |
| **Booleano** | Verdadero o falso | `True`, `False` |
| **Lista** | Varios valores en orden | `["ana", "carlos"]` |

Cada tipo se usa para algo distinto. No es lo mismo el número `5` que el texto `"5"`.

## ¿Qué es una variable?

Una **variable** es un nombre que guarda un dato para usarlo después.

Pensala como una caja con etiqueta:
- La etiqueta es el nombre (`edad`).
- El contenido es el dato (`25`).

```python
edad = 25
nombre = "Ana"
activo = True
```

- `edad` guarda el número `25`.
- `nombre` guarda el texto `"Ana"`.
- `activo` guarda un booleano.

## ¿Por qué importa?

Sin variables no podrías guardar la pregunta del usuario, la respuesta del modelo ni los documentos recuperados. Todo eso se guarda en variables.

## Regla de oro

Una variable tiene un **nombre claro**. `edad` es mejor que `x`. En un agente vas a tener muchas variables y los nombres claros evitan errores.

## Recapitulación

- Un dato es información; tiene un tipo.
- Una variable es un nombre que guarda un dato.
- Elegir buenos nombres hace el código más entendible.

[← Anterior: Algoritmos y lógica](./02-algoritmos-y-logica.md) | [Índice](./fundamento.readme.md) | [Siguiente: Operadores y expresiones →](./04-operadores-y-expresiones.md)
