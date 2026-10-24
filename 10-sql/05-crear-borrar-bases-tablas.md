# 05 - Crear y borrar bases de datos y tablas

## Objetivo

Aprender los comandos DDL más básicos: `CREATE`, `DROP`.

## ¿Qué es DDL?

**DDL** (*Data Definition Language*) son comandos que **definen la estructura**: crear, modificar o borrar bases, tablas, etc.

Principales: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.

## Crear una base de datos

```sql
CREATE DATABASE tienda;
```

> En SQLite no se usa `CREATE DATABASE` igual: cada archivo `.db` es una base de datos. Ahí vas a ver `sqlite3 tienda.db` directamente.

## Usar una base de datos

```sql
USE tienda;
```

> En SQLite se omite `USE`; abrís el archivo directamente.

## Crear una tabla

```sql
CREATE TABLE clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  fecha_registro DATE DEFAULT (DATE('now'))
);
```

- `AUTOINCREMENT` (SQLite) / `AUTO_INCREMENT` (MySQL): genera el `id` solo.
- `UNIQUE`: no permite emails duplicados.
- `DEFAULT (DATE('now'))`: pone la fecha actual si no se indica.

## Borrar una tabla

```sql
DROP TABLE clientes;
```

**Cuidado:** Esto borra **toda** la tabla con sus datos. No se puede deshacer fácilmente.

## Borrar una base de datos

```sql
DROP DATABASE tienda;
```

También **irreversible**. Usalo con mucho cuidado.

## Buenas prácticas

- Creá nombres claros y en plural o singular coherentes (`clientes`, `productos`).
- Usá `NOT NULL` cuando el campo es obligatorio.
- Pensá las relaciones antes de crear todas las tablas.
- **Nunca** uses `DROP` sin estar seguro.

## Recapitulación

- `CREATE` crea estructura.
- `DROP` elimina estructura (con datos).
- `UNIQUE`, `NOT NULL`, `DEFAULT` ayudan a mantener datos válidos.

[← Anterior: Tipos de datos](./04-tipos-de-datos-basicos.md) | [Índice](./README.md) | [Siguiente: Obtener estructura de columnas →](./06-obtener-estructura-columnas.md)
