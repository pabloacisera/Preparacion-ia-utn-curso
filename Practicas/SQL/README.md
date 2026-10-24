# Prácticas SQL

Los ejercicios se basan en un **esquema inventado** con varias tablas para practicar CRUD, consultas condicionales e `INNER JOIN`.

## Esquema

- `categorias(id_categoria, nombre)`
- `productos(id_producto, nombre, precio, stock, id_categoria)`
- `clientes(id_cliente, nombre, email, telefono)`
- `pedidos(id_pedido, id_cliente, fecha, estado)`
- `detalle_pedido(id_detalle, id_pedido, id_producto, cantidad, precio_unitario)`

## Orden de ejercicios

1. [00 - Crear esquema](./ejercicios/00-crear-esquema.sql)
2. [01 - Insertar datos en todas las tablas](./ejercicios/01-insert-datos.sql)
3. [02 - CRUD](./ejercicios/02-crud.sql)
4. [03 - Consultas condicionales](./ejercicios/03-consultas-condicionales.sql)
5. [04 - INNER JOIN](./ejercicios/04-inner-join.sql)
6. [05 - Desafíos](./ejercicios/05-desafios.sql)

[← Volver a 10-SQL](../../10-sql/README.md)
