-- 04-inner-joins.sql
-- Práctica INNER JOIN con el esquema tienda online

-- 1. Productos con su categoría
SELECT p.nombre AS producto, c.nombre AS categoria, p.precio, p.stock
FROM productos p
INNER JOIN categorias c ON p.id_categoria = c.id_categoria
ORDER BY c.nombre, p.nombre;

-- 2. Pedidos con datos del cliente
SELECT ped.id_pedido, cli.nombre AS cliente, cli.email, ped.fecha, ped.estado
FROM pedidos ped
INNER JOIN clientes cli ON ped.id_cliente = cli.id_cliente
ORDER BY ped.fecha;

-- 3. Detalle completo de pedidos (3+ tablas)
SELECT 
    ped.id_pedido,
    cli.nombre AS cliente,
    p.nombre AS producto,
    c.nombre AS categoria,
    dp.cantidad,
    dp.precio_unitario,
    (dp.cantidad * dp.precio_unitario) AS subtotal
FROM detalle_pedido dp
INNER JOIN pedidos ped ON dp.id_pedido = ped.id_pedido
INNER JOIN clientes cli ON ped.id_cliente = cli.id_cliente
INNER JOIN productos p ON dp.id_producto = p.id_producto
INNER JOIN categorias c ON p.id_categoria = c.id_categoria
ORDER BY ped.id_pedido, p.nombre;

-- 4. Total por pedido
SELECT 
    ped.id_pedido,
    cli.nombre AS cliente,
    SUM(dp.cantidad * dp.precio_unitario) AS total_pedido
FROM detalle_pedido dp
INNER JOIN pedidos ped ON dp.id_pedido = ped.id_pedido
INNER JOIN clientes cli ON ped.id_cliente = cli.id_cliente
GROUP BY ped.id_pedido, cli.nombre
ORDER BY total_pedido DESC;
