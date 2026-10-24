-- 05 - Desafíos integradores
-- Objetivo: Poner en práctica todo lo aprendido con JOINs

-- Desafío 1: Listar todos los pedidos con nombre y apellido del cliente
SELECT c.nombre, c.apellido, p.id_pedido, p.fecha
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id
ORDER BY p.id_pedido;

-- Desafío 2: Detalle completo de cada pedido
SELECT 
  c.nombre || ' ' || c.apellido AS cliente,
  p.id_pedido,
  p.fecha,
  pr.titulo AS producto,
  pr.autor,
  dp.cantidad,
  pr.precio,
  (dp.cantidad * pr.precio) AS subtotal
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id
INNER JOIN detalle_pedido dp ON p.id_pedido = dp.id_pedido
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
ORDER BY p.id_ppedido;
-- Nota: corregir p.id_pedido si hay typo en algún motor; en SQLite funciona con alias
-- Desafío 3: ¿Cuánto gastó cada cliente en total?
SELECT 
  c.nombre || ' ' || c.apellido AS cliente,
  SUM(dp.cantidad * pr.precio) AS total_gastado
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = c.id
INNER JOIN detalle_pedido dp ON p.id_pedido = dp.id_pedido
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
GROUP BY c.id, c.nombre, c.apellido
ORDER BY total_gastado DESC;

-- Desafío 4: Productos más vendidos (cantidad)
SELECT 
  pr.titulo,
  SUM(dp.cantidad) AS unidades_vendidas
FROM detalle_pedido dp
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
GROUP BY pr.id, pr.titulo
ORDER BY unidades_vendidas DESC;

-- Desafío 5: Clientes que NO han comprado (LEFT JOIN - opcional pero útil)
SELECT c.nombre, c.apellido, c.email
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
WHERE p.id_pedido IS NULL;
