# Inteligencia Artificial

Esta sección es el núcleo del curso. Va **de lo general a lo interno y de vuelta a la práctica**: primero entendemos qué es un LLM y cómo se usa; después abrimos la caja para ver tokens, embeddings y vectores; con esa base construimos un RAG, lo orquestamos con LangChain y, al final, damos autonomía al modelo para convertirlo en un agente.

> **Filosofía:** solo lo necesario. El curso dura pocos meses y las horas semanales son limitadas, así que cada tema se enseña a la profundidad que hace falta para entender el sistema completo: **LLM, agentes, LangChain, chunking, embeddings, vectores, bases de datos vectoriales y streaming**. No es un curso de ingeniería de IA: no llegamos a machine learning ni a deep learning.

## Recorrido

| # | Módulo | Pregunta que responde |
|---|--------|-----------------------|
| 10 | [Introducción a los LLMs](./Introduccion-LLMs/readme.md) | ¿Qué es un LLM, cómo se usa por API y por qué alucina? |
| 11 | [Funcionamiento interno](./Funcionamiento-Interno/readme.md) | ¿Qué pasa por dentro: tokens, embeddings y vectores? |
| 12 | [RAG](./RAG/readme.md) | ¿Cómo le damos conocimiento privado y memoria a largo plazo? |
| 13 | [LangChain y su ecosistema](./LangChain/readme.md) | ¿Cómo se orquestan cadenas, conectores y memoria? |
| 14 | [Agentes](./Agentes/readme.md) | ¿Cómo le damos autonomía al modelo sobre todo lo anterior? |
| 15 | [Agentes no-code](./Agentes-NoCode/readme.md) | ¿Qué son specs, skills y MCP (sin programar)? |

## Cómo está organizado cada módulo

Cada carpeta tiene un `readme.md` con la teoría y una subcarpeta `ejercicios/` con la práctica. **Cada ejercicio es un archivo `.md`** que contiene la consigna, el código en un bloque y el resultado esperado.

## Instalación

Las dependencias de toda la sección están en [`requirements.txt`](../requirements.txt):

```bash
pip install -r requirements.txt
```

[Menu Principal](../README.md)
