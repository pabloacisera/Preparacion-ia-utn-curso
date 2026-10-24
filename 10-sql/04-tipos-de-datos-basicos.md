# 04 - Tipos de datos básicos en SQL

## Objetivo

Conocer los tipos de datos más usados para crear tablas correctamente.

## Tipos principales

| Tipo | Uso | Ejemplo |
|---|---|---|
| **INTEGER / INT** | Números enteros | `edad INT`, `cantidad INT` |
| **REAL / FLOAT / DECIMAL** | Números con decimales | `precio DECIMAL(10,2)`, `peso REAL` |
| **TEXT / VARCHAR(n)** | Texto de longitud variable | `nombre VARCHAR(50)`, `email TEXT` |
| **CHAR(n)** | Texto de longitud fija | `codigo CHAR(3)` |
| **DATE** | Fecha (año-mes-día) | `fecha_nacimiento DATE` |
| **DATETIME / TIMESTAMP** | Fecha y hora | `creado_en DATETIME` |
| **BOOLEAN** | Verdadero/Falso | `activo BOOLEAN` |

> **Nota:** Los nombres varían según el motor (SQLite, PostgreSQL, MySQL). Los de arriba son los más comunes para aprender.

## Ejemplo: crear una tabla

```sql
CREATE TABLE productos (
  id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  stock INTEGER DEFAULT 0,
  activo BOOLEAN DEFAULT TRUE
);
```

- `PRIMARY KEY` - clave primaria
- `NOT NULL` - no puede quedar vacío
- `DEFAULT` - valor por defecto si no se indica

## ¿Por qué elegir el tipo correcto?

- **Menor espacio**: usar `INT` para edades, no `TEXT`.
- **Menos errores**: `DECIMAL` para precios (evita errores con decimales).
- **Consultas más claras**: el tipo define qué operaciones son válidas.

## ¿Por qué importa para agentes?

Cuando un agente genera SQL con herramientas, necesita saber los tipos para armar consultas correctas. Entenderlos te ayuda a revisar y corregir lo que genere.

## Recapitulación

- Cada columna tiene un tipo de dato.
- Elegir bien el tipo evita errores y guarda mejor la información.
- `TEXT`, `INTEGER`, `DECIMAL`, `DATE` son los que más vas a usar.

[← Anterior: Clave primaria/foránea](./03-clave-primaria-foranea-relaciones.md) | [Índice](./README.md) | [Siguiente: Crear, borrar bases y tablas →](./05-crear-borrar-bases-tablas.md)
