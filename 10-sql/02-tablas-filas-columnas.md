# 02 - Tablas, filas y columnas

## Objetivo

Entender la estructura básica de una base de datos relacional: tablas, filas, columnas y registros.

## ¿Qué es una tabla?

Una **tabla** es como una hoja de cálculo. Organiza información en **filas** y **columnas**. Cada tabla guarda un tipo de entidad: `usuarios`, `productos`, `pedidos`, etc.

## Filas, columnas y registros

- **Columna (campo)**: Define el tipo de dato. Ej: `nombre`, `edad`, `email`.
- **Fila (registro/tupla)**: Representa un elemento completo. Ej: un usuario en particular.
- **Tabla (relación)**: Conjunto de filas con la misma estructura.

## Ejemplo práctico

Tabla `clientes`:

| id | nombre | apellido | email |
|---|---|---|---|
| 1 | Ana | Pérez | ana@mail.com |
| 2 | Carlos | López | carlos@mail.com |
| 3 | Lucía | Gómez | lucia@mail.com |

- **Columnas**: `id`, `nombre`, `apellido`, `email`
- **Filas**: cada una es un cliente distinto
- **Dato**: `Ana` es un valor dentro de la columna `nombre`

## ¿Por qué se llama "relacional"?

Porque las tablas **se relacionan entre sí** usando claves. Más adelante veremos claves primarias y foráneas.

## Analogía

Pensalo como fichas en un archivo. Cada ficha (fila) tiene campos (columnas). Todas las fichas de ese tipo siguen el mismo formato.

## ¿Por qué importa para LLM, agentes y RAG?

- Muchos sistemas guardan información en SQL: usuarios, productos, historial, etc.
- Un **agente** puede consultar una base SQL con herramientas (`SQLTool`) para responder con datos reales.
- Aunque RAG suele usar bases vectoriales, **combinar SQL + RAG** es muy común en proyectos reales.

## Recapitulación

- Tabla = estructura que guarda datos relacionados.
- Columna = campo. Fila = registro.
- SQL trabaja con tablas para organizar y consultar información.

[← Anterior: ¿Qué es SQL y base de datos?](./01-que-es-sql-y-base-de-datos.md) | [Índice](./README.md) | [Siguiente: Clave primaria, foránea y relaciones →](./03-clave-primaria-foranea-relaciones.md)
