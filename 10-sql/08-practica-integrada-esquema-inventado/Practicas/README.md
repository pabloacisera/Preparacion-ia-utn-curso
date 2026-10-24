# Prácticas integradas - Esquema tienda online

## Objetivo

Practicar con un esquema realista usando múltiples tablas e `INSERTs`.

## Orden de ejecución

Ejecuta los archivos `.sql` en este orden con tu cliente SQLite.

### 1. Crear esquema
[`00-crear-esquema.sql`](./00-crear-esquema.sql) - Crea todas las tablas con sus relaciones

### 2. Insertar datos
[`01-insert-datos.sql`](./01-insert-datos.sql) - Inserta datos en **todas** las tablas (categorías, productos, clientes, pedidos, detalle_pedido)

### 3. CRUD básico
[`02-crud.sql`](./02-crud.sql) - Practica `INSERT`, `SELECT`, `UPDATE`, `DELETE`

### 4. Consultas condicionales
[`03-consultas-condicionales.sql`](./03-consultas-condicionales.sql) - `WHERE`, `AND/OR`, `ORDER BY`, `LIMIT`

### 5. INNER JOIN
[`04-inner-joins.sql`](./04-inner-joins.sql) - Uniones entre 2 y 3+ tablas

### 6. Desafíos
[`05-desafios.sql`](./05-desafios.sql) - Ejercicios para resolver por tu cuenta

## Consejos

- **Lee los comentarios**: Cada archivo tiene comentarios explicando qué hace
- **Ejecuta paso a paso**: No copies todo de golpe, entiende cada consulta
- **Experimenta**: Cambia valores, añade filtros, prueba cosas nuevas
- **Usa `.schema`**: En SQLite `sqlite> .schema` te muestra todas las tablas creadas

## Recomendado: Ver estructura

Después de crear el esquema, comprueba:
```sql
.tables
.schema
```

[← Volver a teoría](../teoria/01-enunciado-del-caso-practico.md) | [Índice de SQL](../../README.md)
