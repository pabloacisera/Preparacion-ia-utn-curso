# 11 - INNER JOIN con múltiples tablas

## Objetivo

Aprender a unir tres o más tablas para obtener información completa.

## Escenario real

Queremos responder: *"¿Qué productos compró Ana en cada pedido?"*

Tenemos 4 tablas relacionadas:

- `clientes(id, nombre)`
- `pedidos(id_pedido, fecha, id_cliente)`
- `detalle_pedido(id_detalle, id_pedido, id_producto, cantidad)`
- `productos(id_producto, nombre, precio)`

## Camino para unirlas

1. `pedidos` → une con `clientes` (quién hizo el pedido)
2. `detalle_pedido` → une con `pedidos` (qué pedido)
3. `productos` → une con `detalle_pedido` (qué producto)

## Consulta completa

```sql
SELECT 
  c.nombre AS cliente,
  p.id_pedido,
  pr.nombre AS producto,
  dp.cantidad,
  pr.precio,
  (dp.cantidad * pr.precio) AS total_linea
FROM clientes c
INNER JOIN pedidos p ON c.id = p.id_cliente
INNER JOIN detalle_pedido dp ON p.id_pedido = dp.id_pedido
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
ORDER BY p.id_pedido;
```

## ¿Qué estamos viendo?

- **cliente**: quién compró
- **producto**: qué compró
- **cantidad**: cuántos
- **precio**: precio unitario
- **total_linea**: cálculo directo en la consulta

## Tips prácticos

- **Uní en orden lógico**: desde lo más general (cliente) hasta el detalle (productos).
- **Usá alias siempre** con múltiples tablas.
- **Pedí solo las columnas que necesitás** (`SELECT *` confunde con muchas tablas).
- **Podés calcular** con expresiones matemáticas.

## ¿Por qué es importante?

Este patrón es **exactamente** el que usaría un agente con una herramienta SQL para responder preguntas de negocio con datos reales.

## Recapitulación

- Con varios `INNER JOIN` conectás todo el esquema.
- Las tablas intermedias (`detalle_pedido`) permiten la relación **N:M**.
- Podés combinar datos + cálculos en una sola consulta.

[← Anterior: INNER JOIN](./10-inner-join-funcion-utilidad-importancia.md) | [Índice](./README.md) | [Siguiente: Migraciones →](./12-migraciones.md)
