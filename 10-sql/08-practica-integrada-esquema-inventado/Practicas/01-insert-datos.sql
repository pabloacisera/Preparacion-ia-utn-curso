-- 01-insert-datos.sql
-- Inserción de datos en TODAS las tablas
-- Ejecutar después de 00-crear-esquema.sql

-- 1. Categorías
INSERT INTO categorias (nombre) VALUES 
('Bebidas'),
('Snacks'),
('Limpieza'),
('Panadería');

-- 2. Productos
INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES
('Agua mineral 500ml', 850.00, 100, 1),
('Gaseosa cola 1L', 1500.00, 80, 1),
('Jugo naranja 1L', 1650.00, 60, 1),
('Papas fritas clásicas', 1200.00, 150, 2),
('Galletitas dulces', 950.00, 120, 2),
('Maní salado', 800.00, 90, 2),
('Detergente líquido', 2450.00, 40, 3),
('Lavandina', 1100.00, 35, 3),
('Pan francés', 650.00, 200, 4),
('Facturas surtidas', 1400.00, 75, 4);

-- 3. Clientes
INSERT INTO clientes (nombre, email, telefono) VALUES
('Ana García', 'ana.garcia@mail.com', '111-234-5678'),
('Carlos López', 'carlos.lopez@mail.com', '112-345-6789'),
('María Fernández', 'maria.fernandez@mail.com', '113-456-7890'),
('Pedro Martínez', 'pedro.martinez@mail.com', '114-567-8901'),
('Lucía Rodríguez', 'lucia.rodriguez@mail.com', '115-678-9012');

-- 4. Pedidos
INSERT INTO pedidos (id_cliente, fecha, estado) VALUES
(1, '2025-10-01', 'entregado'),
(2, '2025-10-05', 'entregado'),
(1, '2025-10-12', 'enviado'),
(3, '2025-10-15', 'pendiente'),
(4, '2025-10-18', 'pendiente'),
(5, '2025-10-20', 'entregado');

-- 5. Detalle de pedido (varias líneas por pedido)
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
-- Pedido 1 (Ana)
(1, 1, 2, 850.00),
(1, 4, 1, 1200.00),
(1, 9, 3, 650.00),
-- Pedido 2 (Carlos)
(2, 2, 2, 1500.00),
(2, 5, 2, 950.00),
-- Pedido 3 (Ana)
(3, 3, 1, 1650.00),
(3, 6, 1, 800.00),
(3, 10, 2, 1400.00),
-- Pedido 4 (María)
(4, 7, 1, 2450.00),
(4, 8, 1, 1100.00),
-- Pedido 5 (Pedro)
(5, 1, 5, 850.00),
(5, 4, 3, 1200.00),
(5, 9, 2, 650.00),
-- Pedido 6 (Lucía)
(6, 3, 2, 1650.00),
(6, 10, 3, 1400.00);
