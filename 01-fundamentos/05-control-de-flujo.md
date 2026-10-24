# 05 - Control de flujo: decisiones y repeticiones

## Objetivo

Entender cómo un programa elige caminos y cómo repite tareas.

## Decisiones: `if`, `elif`, `else`

Permiten ejecutar un bloque solo si se cumple una condición.

```python
edad = 20

if edad >= 18:
    print("puede entrar")
else:
    print("no puede entrar")
```

- `if` evalúa una condición.
- `elif` evalúa otra si la anterior fue falsa.
- `else` se ejecuta si nada se cumplió.

## Repeticiones: bucles

Sirven para hacer lo mismo varias veces sin repetir código.

```python
for numero in [1, 2, 3]:
    print(numero)
```

Ese código imprime `1`, `2` y `3`.

También existe `while`, que repite **mientras** se cumpla una condición.

## ¿Por qué importan para el curso?

- Un **agente** funciona en un bucle: piensa → actúa → observa → repite.
- Al procesar documentos para un RAG, recorrés una lista de fragmentos y los convertís en vectores uno por uno.
- Al recorrer los resultados de una base de datos, usás bucles.

Sin decisiones y repeticiones no existirían los agentes.

## Recapitulación

- `if/elif/else` eligen entre caminos.
- `for` recorre una colección; `while` repite mientras se cumpla una condición.
- Los agentes y los RAG se apoyan en estas estructuras.

[← Anterior: Operadores y expresiones](./04-operadores-y-expresiones.md) | [Índice](./fundamento.readme.md) | [Siguiente: Python →](../08-python/08-1-fundamentos/fundamento.python.readme.md)
