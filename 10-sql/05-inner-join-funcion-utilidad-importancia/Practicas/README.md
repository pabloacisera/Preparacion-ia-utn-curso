# Prácticas - INNER JOIN

## Objetivo

Practicar `INNER JOIN` con el esquema relacional.

## Esquema mental

Recuerda nuestras tablas:
- `categorias(id_categoria, nombre)`
- `productos(id_producto, nombre, precio, stock, id_categoria)`  → FK a categorias
- `clientes(id_cliente, nombre, email, telefono)`
- `pedidos(id_pedido, id_cliente, fecha, estado)`  → FK a clientes
- `detalle_pedido(id_detalle, id_pedido, id_producto, cantidad, precio_unitario)`  → FK a pedidos y productos

## Práctica 1: Productos con su categoría

**Objetivo:** Mostrar el nombre del producto junto al nombre de su categoría.

```sql
SELECT productos.nombre, categorias.nombre AS categoria
FROM productos
INNER JOIN categorias ON productos.id_categoria = categorias.id_categoria;
```

**Pregunta:** ¿Por qué usamos `AS` para renombrar la columna?

## Práctica 2: Pedidos con datos del cliente

**Objetivo:** Ver qué cliente hizo cada pedido.

```sql
SELECT pedidos.id_pedido, clientes.nombre, pedidos.fecha, pedidos.estado
FROM pedidos
INNER JOIN clientes ON pedidos.id_cliente = clientes.id_cliente
ORDER BY pedidos.fecha;
```

## Práctica 3: INNER JOIN entre 3 tablas

**Objetivo:** Ver productos incluidos en cada pedido con sus datos.

```sql
SELECT pedidos.id_pedido, clientes.nombre, productos.nombre AS producto, 
       detalle_pedido.cantidad, detalle_pedido.precio_unitario
FROM detalle_pedido
INNER JOIN pedidos ON detalle_pedido.id_pedido = pedidos.id_pedido
INNER JOIN clientes ON pedidos.id_cliente = clientes.id_cliente
INNER JOIN productos ON detalle_pedido.id_producto = productos.id_producto
ORDER BY pedidos.id_pedido;
```

## Desafío

Usando el esquema, intenta responder mentalmente:
1. ¿Qué productos pertenecen a la categoría "Bebidas"?
2. ¿Qué pedidos ha hecho un cliente específico?
3. ¿Cuál es el total por pedido? (Pista: `cantidad * precio_unitario`)

[← Volver a teoría](../teoria/02-inner-join-funcion-utilidad-e-importancia.md) | [Índice de SQL](../../README.md) | [Siguiente sección: Migraciones →](../../06-migraciones/teoria/01-que-son-las-migraciones.md)
