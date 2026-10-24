# 03 - Clave primaria, clave foránea y relaciones

## Objetivo

Entender cómo se vinculan las tablas usando claves.

## ¿Qué es una clave primaria (Primary Key)?

Una **clave primaria (PK)** identifica **únicamente** cada fila de una tabla. No puede repetirse y generalmente no puede ser nula.

Suele llamarse `id` y muchas veces es auto-incremental.

Tabla `clientes`:
| id (PK) | nombre | email |
|---|---|---|
| 1 | Ana | ana@mail.com |
| 2 | Carlos | carlos@mail.com |

Ningún cliente puede tener el mismo `id`.

## ¿Qué es una clave foránea (Foreign Key)?

Una **clave foránea (FK)** es una columna que hace referencia a la **clave primaria** de otra tabla. Sirve para crear una **relación**.

Tabla `pedidos`:
| id_pedido (PK) | fecha | id_cliente (FK) |
|---|---|---|
| 101 | 2025-10-01 | 1 |
| 102 | 2025-10-02 | 1 |
| 103 | 2025-10-03 | 2 |

- `id_cliente = 1` apunta al cliente **Ana** (id 1 en `clientes`).
- Un cliente puede tener **muchos** pedidos.
- Un pedido pertenece a **un solo** cliente.

## Tipos de relaciones

| Relación | Explicación | Ejemplo |
|---|---|---|
| **1:1** | Un registro se relaciona con uno y solo uno | `usuarios` - `perfiles` |
| **1:N** | Uno se relaciona con muchos | `clientes` - `pedidos` |
| **N:M** | Muchos con muchos (necesita tabla intermedia) | `estudiantes` - `cursos` (tabla `inscripciones`) |

## ¿Por qué es importante?

Sin relaciones evitaríamos repetir datos. Gracias a ellas guardamos la información una sola vez y la vinculamos cuando la necesitamos.

## Para LLM/Agentes

Un agente que consulta SQL puede unir tablas (`JOIN`) para responder: *"¿Qué pedidos hizo Ana?"* sin que vos copies datos, preguntando directamente a la base.

## Recapitulación

- **PK** identifica la fila.
- **FK** apunta a otra tabla.
- Las relaciones evitan duplicados y mantienen la integridad.

[← Anterior: Tablas, filas y columnas](./02-tablas-filas-columnas.md) | [Índice](./README.md) | [Siguiente: Tipos de datos básicos →](./04-tipos-de-datos-basicos.md)
