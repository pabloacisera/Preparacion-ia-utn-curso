-- 04-inner-join.sql
-- Práctica INNER JOIN

-- 1. Productos con su categoría
SELECT p.nombre, c.nombre AS categoria, p.precio
FROM productos p
INNER JOIN categorias c ON p.id_categoria = c.id_categoria;

-- 2. Pedidos con cliente
SELECT ped.id_pedido, cli.nombre, ped.fecha, ped.estado
FROM pedidos ped
INNER JOIN clientes cli ON ped.id_cliente = cli.id_cliente;

-- 3. Detalle completo con INNER JOIN entre varias tablas
SELECT ped.id_pedido, cli.nombre AS cliente, p.nombre AS producto, 
       dp.cantidad, dp.precio_unitario, (dp.cantidad * dp.precio_unitario) AS subtotal
FROM detalle_pedido dp
INNER JOIN pedidos ped ON dp.id_pedido = ped.id_pedido
INNER JOIN clientes cli ON ped.id_cliente = cli.id_cliente
INNER JOIN productos p ON dp.id_producto = p.id_producto
ORDER BY ped.id_pedido;
