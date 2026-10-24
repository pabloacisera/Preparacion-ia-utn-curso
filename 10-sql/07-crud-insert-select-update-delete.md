# 07 - CRUD: INSERT, SELECT, UPDATE, DELETE

## Objetivo

Aprender las operaciones fundamentales para manejar datos: crear, leer, actualizar y eliminar.

## ¿Qué es CRUD?

**CRUD** = Crear, Leer, Actualizar, Eliminar (*Create, Read, Update, Delete*). Son las 4 operaciones básicas con datos.

| Operación | Comando SQL | Acción |
|---|---|---|
| **Create** | `INSERT` | Agregar nuevos registros |
| **Read** | `SELECT` | Consultar/ver registros |
| **Update** | `UPDATE` | Modificar registros existentes |
| **Delete** | `DELETE` | Eliminar registros |

## 1. INSERT - Crear datos

```sql
INSERT INTO clientes (nombre, apellido, email)
VALUES ('Ana', 'Pérez', 'ana@mail.com');
```

Podés insertar varios a la vez:

```sql
INSERT INTO clientes (nombre, apellido, email)
VALUES 
  ('Carlos', 'López', 'carlos@mail.com'),
  ('Lucía', 'Gómez', 'lucia@mail.com');
```

## 2. SELECT - Leer datos

```sql
-- Ver todos los campos y todos los registros
SELECT * FROM clientes;

-- Ver solo algunos campos
SELECT nombre, email FROM clientes;

-- Ver con alias
SELECT nombre AS cliente, email AS correo FROM clientes;
```

`*` significa **todos los campos**. En consultas grandes conviene evitarlo y pedir solo lo necesario.

## 3. UPDATE - Actualizar datos

**Siempre usar `WHERE` con UPDATE.** Si te olvidás, actualizás **todos** los registros.

```sql
UPDATE clientes
SET email = 'ana.nuevo@mail.com'
WHERE id = 1;
```

Podés actualizar varios campos:

```sql
UPDATE clientes
SET nombre = 'Ana María', email = 'anamaria@mail.com'
WHERE id = 1;
```

## 4. DELETE - Eliminar datos

**Siempre usar `WHERE` con DELETE.** Si te olvidás, borrás **todos** los registros.

```sql
DELETE FROM clientes
WHERE id = 3;
```

## Regla de oro

> **Antes de hacer UPDATE o DELETE: hacé un SELECT con el mismo WHERE para verificar qué registros van a afectar.**

```sql
-- Verificar primero
SELECT * FROM clientes WHERE id = 3;

-- Después borrar
DELETE FROM clientes WHERE id = 3;
```

## Recapitulación

- CRUD cubre todo lo necesario para manejar datos.
- `INSERT` crea, `SELECT` lee, `UPDATE` modifica, `DELETE` borra.
- **`WHERE` es obligatorio en UPDATE/DELETE** para no afectar todo.

[← Anterior: Obtener estructura](./06-obtener-estructura-columnas.md) | [Índice](./README.md) | [Siguiente: Consultas condicionales →](./08-consultas-condicionales-where.md)
