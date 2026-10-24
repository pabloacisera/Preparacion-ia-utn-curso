# 06 - Obtener la estructura de una tabla

## Objetivo

Saber cómo ver qué columnas tiene una tabla, sus tipos y restricciones.

## ¿Por qué es útil?

Antes de consultar o insertar, conviene saber:
- Qué campos existen
- Qué tipo tiene cada uno
- Cuáles son obligatorios
- Si hay claves

## Comandos según el motor

| Motor | Comando | Notas |
|---|---|---|
| **SQLite** | `.schema nombre_tabla` | Muestra el `CREATE TABLE` completo |
| **SQLite** | `PRAGMA table_info(nombre_tabla);` | Muestra columnas, tipos, null, PK, default |
| **MySQL** | `DESCRIBE nombre_tabla;` o `DESC nombre_tabla;` | Rápido y claro |
| **PostgreSQL** | `\d nombre_tabla` (psql) o `INFORMATION_SCHEMA` | En psql es el más usado |

## Ejemplo con SQLite

```sql
PRAGMA table_info(clientes);
```

Resultado aproximado:

| cid | name | type | notnull | dflt_value | pk |
|---|---|---|---|---|---|
| 0 | id | INTEGER | 0 | NULL | 1 |
| 1 | nombre | TEXT | 1 | NULL | 0 |
| 2 | email | TEXT | 1 | NULL | 0 |

- `name` = nombre de columna
- `type` = tipo de dato
- `notnull` = 1 significa `NOT NULL`
- `pk` = 1 significa clave primaria

## Ejemplo con MySQL

```sql
DESCRIBE productos;
```

Muestra: `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`.

## ¿Por qué importa para agentes?

Cuando un agente genera consultas SQL, muchas veces necesita **conocer el esquema** primero. Si entendés esto, podés pedirle al agente que inspeccione la estructura o revisar lo que hace.

## Recapitulación

- `.schema` / `DESCRIBE` / `PRAGMA` te muestran la estructura.
- Es un paso fundamental antes de hacer `INSERT`, `SELECT`, `UPDATE`.
- Saber esto te permite debuggear consultas rápidamente.

[← Anterior: Crear/borrar tablas](./05-crear-borrar-bases-tablas.md) | [Índice](./README.md) | [Siguiente: CRUD →](./07-crud-insert-select-update-delete.md)
