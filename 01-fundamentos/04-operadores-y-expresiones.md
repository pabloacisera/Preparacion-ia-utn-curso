# 04 - Operadores y expresiones

## Objetivo

Entender cómo combinar datos para calcular o comparar cosas.

## ¿Qué es un operador?

Un **operador** es un símbolo que hace una operación entre dos valores. El resultado es una **expresión**.

```python
precio = 100 + 50      # suma: da 150
```

## Operadores matemáticos

| Operador | Significado | Ejemplo |
|---|---|---|
| `+` | Suma | `10 + 5` → `15` |
| `-` | Resta | `10 - 5` → `5` |
| `*` | Multiplicación | `10 * 5` → `50` |
| `/` | División | `10 / 5` → `2.0` |

## Operadores de comparación

Devuelven `True` o `False`:

| Operador | Significado | Ejemplo |
|---|---|---|
| `==` | Igual a | `5 == 5` → `True` |
| `!=` | Distinto de | `5 != 3` → `True` |
| `>` | Mayor que | `5 > 3` → `True` |
| `<` | Menor que | `5 < 3` → `False` |

> **Cuidado:** `=` asigna un valor a una variable; `==` compara. Son distintos.

## Operadores lógicos

| Operador | Significado |
|---|---|
| `and` | Se cumplen las dos condiciones |
| `or` | Se cumple al menos una |
| `not` | Niega una condición |

```python
edad = 20
tiene_entrada = True
puede_entrar = edad >= 18 and tiene_entrada   # True
```

## ¿Por qué importa para el curso?

- Para filtrar datos: `stock > 0`.
- Para decidir en un agente: `si el usuario pidió un dato exacto → usar SQL`.
- Para armar condiciones de búsqueda en un RAG.

## Recapitulación

- Los operadores combinan o comparan datos.
- Las comparaciones devuelven `True` o `False`.
- `and`, `or` y `not` combinan condiciones.

[← Anterior: Datos, tipos y variables](./03-datos-tipos-y-variables.md) | [Índice](./fundamento.readme.md) | [Siguiente: Control de flujo →](./05-control-de-flujo.md)
