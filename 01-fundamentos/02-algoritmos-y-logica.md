# 02 - Algoritmos y lógica

## Objetivo

Entender qué es un algoritmo y cómo se piensa la lógica para resolver un problema.

## ¿Qué es un algoritmo?

Un **algoritmo** es una secuencia de pasos finitos que resuelve un problema. No es código todavía: es la idea, el procedimiento.

Ejemplo: cómo encontrar el número mayor de una lista.
1. Tomar el primer número como el mayor.
2. Mirar el siguiente número.
3. Si es más grande, guardarlo como el nuevo mayor.
4. Repetir hasta terminar la lista.
5. El mayor es el último guardado.

## Lógica: las tres estructuras básicas

Casi todos los programas se arman con tres ideas:

| Estructura | Para qué sirve | Ejemplo cotidiano |
|---|---|---|
| **Secuencia** | Hacer una cosa después de otra | Ponerse medias y después zapatos |
| **Decisión** | Elegir un camino según una condición | Si llueve, llevar paraguas |
| **Repetición** | Hacer algo varias veces | Revolver la sopa hasta que hierva |

## Pensar antes de programar

Un buen hábito: escribir los pasos en lenguaje normal (seudocódigo) antes de pasar a Python.

```
pedir un número
si el número es par:
    mostrar "es par"
si no:
    mostrar "es impar"
```

Después ese seudocódigo se transforma en código.

## Descomponer un problema

Los problemas grandes se parten en partes chicas:
- "Hacer un chatbot" →
  - Leer la pregunta.
  - Enviarla al modelo.
  - Mostrar la respuesta.

Cada parte es un problema más simple de resolver.

## ¿Por qué importa para el curso?

- Un **agente** es un algoritmo que decide en un bucle.
- Un **RAG** tiene una secuencia: buscar → filtrar → armar prompt → responder.
- Si no entendés la lógica, el código de IA parece magia.

## Recapitulación

- Algoritmo = pasos ordenados para resolver algo.
- Se construyen con secuencia, decisión y repetición.
- Primero se piensa en pasos; después se escribe código.

[← Anterior: ¿Qué es programar?](./01-que-es-programar.md) | [Índice](./fundamento.readme.md) | [Siguiente: Datos, tipos y variables →](./03-datos-tipos-y-variables.md)
