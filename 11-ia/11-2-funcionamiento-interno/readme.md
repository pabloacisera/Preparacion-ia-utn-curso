# 11. Funcionamiento interno: tokens, embeddings y vectores

> **Objetivo:** abrir la caja del "autocompletar muy entrenado" del Módulo 10. Entender qué es un **token**, qué es un **embedding**, cómo el modelo **predice** y por qué todo eso nos lleva a los **vectores** y las **bases de datos vectoriales** que usa un RAG.
>
> **Alcance:** lo **necesario** para entender el sistema completo. No llegamos a machine learning ni a deep learning: no entrenamos modelos, no entramos en la matemática de las redes. Sí entendemos cómo se representa el texto y cómo se mide el parecido entre dos textos, que es la base de todo lo que viene.

## 1. Tokens

El modelo no "lee" letras ni palabras: trabaja con **tokens**, que son las piezas en que se corta el texto. Una palabra frecuente suele ser un token; una rara se arma con varios.

- Cada token tiene un **ID** (un número) dentro del **vocabulario** (la lista de todos los tokens que el modelo conoce).
- La **tokenización** es el proceso de cortar el texto y convertirlo en esos IDs.

Ejemplo (ilustrativo):

```
"el gato come"  →  ["el", " gato", " come"]  →  [11, 7, 6]
```

Puntos importantes:

- **El espacio cuenta**: fijate que `" gato"` lleva el espacio adelante; es parte de la pieza.
- **No todo cuesta igual**: un texto en un idioma poco representado en el entrenamiento suele usar **más tokens** que el mismo texto en inglés. Más tokens = más costo y más contexto consumido.
- Un texto muy técnico, un número largo o una URL se parten en muchas piezas.

> Profundizar: [ejercicio de tokenización](./ejercicios/01-tokenizar.md).

## 2. Embeddings: el significado como coordenadas

Un **embedding** es un **vector** (una lista de números) que representa el **significado** de un texto. Textos que significan cosas parecidas quedan **cerca** en ese espacio.

- La cantidad de números de cada vector es la **dimensión** (por ejemplo, 384 o 768).
- El vector **no** se arma a mano: lo produce un **modelo de embeddings**.
- La **similitud coseno** mide qué tan parecidos son dos vectores (1 = igual dirección). Con vectores normalizados (largo 1), comparar es simplemente multiplicar.

Lo importante para lo que sigue: **un embedding convierte texto en números comparables**, aunque las palabras no coincidan.

```
"El gato come pescado."      →  [0.12, -0.88, 0.03, ...]   (384 números)
"Un felino se alimenta..."   →  [0.10, -0.85, 0.05, ...]   ← cerca del anterior
```

> **Regla de oro:** la pregunta del usuario y los documentos deben convertirse con **el mismo** modelo de embeddings. Si se mezclan modelos distintos, las comparaciones no tienen sentido y la búsqueda falla.

> Profundizar: [ejercicio de embeddings y similitud](./ejercicios/02-embeddings-y-similitud.md).

## 3. Cómo predice el modelo

Ya con el texto en números, el modelo calcula la respuesta en tres pasos:

1. **Logits:** entrega un puntaje (crudo) por **cada token del vocabulario** para la siguiente posición.
2. **Softmax:** convierte esos puntajes en **probabilidades** que suman 1.
3. **Elección:** se elige un token según esas probabilidades.

Formas de elegir:

| Método | Qué hace |
|--------|----------|
| **Greedy** | Siempre el más probable (temperatura 0). Reproducible. |
| **Temperatura** | `0` = predecible; valores altos = más variado. |
| **Top-k / top-p** | Sortear solo entre los candidatos más probables. |

Luego el token elegido **se agrega** a la entrada y se repite el proceso. Eso es la **autorregresión**: el modelo se alimenta de lo que acaba de producir. Mostrar el texto a medida que sale es el **streaming** (no es un efecto visual: es cómo se genera).

> Profundizar: [ejercicio de predicción y temperatura](./ejercicios/03-como-predice-el-modelo.md).

## 4. Vectores y bases de datos vectoriales

Este punto conecta directamente con el RAG.

- Un **vector** es una lista ordenada de números. Un embedding es un vector que representa significado.
- Cuando guardamos **miles** de embeddings (por ejemplo, de miles de fragmentos de documentos), necesitamos buscarlos por **parecido**. Eso lo hace una **base de datos vectorial**.
- La búsqueda es **aproximada** (ANN, *approximate nearest neighbors*): en lugar de comparar contra todos, encuentra los **vecinos más cercanos** de forma veloz. A los mejores resultados se los llama **top-k**.
- Cuanto mayor sea la **dimensión**, más datos ocupa cada vector: 10 000 vectores de 384 números de 4 bytes ocupan unos **15 MB**.

Todo esto es lo que el RAG del Módulo 12 usa: convertir documentos y preguntas a vectores, guardarlos y recuperar los fragmentos más parecidos.

## 5. Ejecución eficiente: ONNX y ONNX Runtime

¿Cómo corren estos modelos en una computadora común? Dos piezas que conviene conocer:

- **ONNX** es un **formato de archivo universal** para modelos. No es un programa: es un archivo estándar que cualquier herramienta puede leer.
- **ONNX Runtime** es el **motor** que carga ese archivo y ejecuta las predicciones a máxima velocidad, usando la CPU o la placa de video disponible. Es liviano y no necesita librerías pesadas.

En el curso los vemos porque la librería de embeddings (`fastembed`) **usa ONNX por dentro**: cuando pedimos un embedding, en realidad corre un archivo `.onnx` con ONNX Runtime.

> **¿Por qué importa?** Porque separa dos mundos: el **entrenamiento** (pesado, con frameworks grandes) y la **ejecución** (liviana, con ONNX Runtime). Nosotros consumimos modelos ya entrenados; por eso nos alcanza con la parte liviana.

> Profundizar: [ejercicio con ONNX Runtime](./ejercicios/04-ejecutar-un-modelo-con-onnx.md).

## Material de profundización (opcional)

Para quien quiera ver **cómo se construye** un mini-modelo desde cero (atención, matrices, entrenamiento), hay un anexo que resume el recorrido, sin ser necesario para el resto del curso:

- [Profundización: el modelo por dentro](./profundizacion.md)

## Ejercicios

- [01 — Tokenizar texto](./ejercicios/01-tokenizar.md)
- [02 — Embeddings y similitud](./ejercicios/02-embeddings-y-similitud.md)
- [03 — Cómo predice el modelo](./ejercicios/03-como-predice-el-modelo.md)
- [04 — Ejecutar un modelo con ONNX Runtime](./ejercicios/04-ejecutar-un-modelo-con-onnx.md)

[Menu Principal](../../README.md) | [Índice IA](../readme.md) | [Anterior: Introducción a los LLMs ←](../11-1-introduccion-llms/readme.md) | [Siguiente: Teoría de agentes →](../11-3-teoria-agentes/readme.md)
