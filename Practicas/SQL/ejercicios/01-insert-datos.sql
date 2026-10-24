-- 01-insert-datos.sql
-- Insertar datos en TODAS las tablas

INSERT INTO categorias (nombre) VALUES ('Bebidas'), ('Snacks'), ('Limpieza'), ('Panadería');

INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES
('Agua mineral 500ml', 850.00, 100, 1),
('Gaseosa cola 1L', 1500.00, 80, 1),
('Jugo naranja 1L', 1650.00, 60, 1),
('Papas fritas clásicas', 1200.00, 150, 2),
('Galletitas dulces', 950.00, 120, 2),
('Detergente líquido', 2450.00, 40, 3),
('Pan francés', 650.00, 200, 4),
('Facturas surtidas', 1400.00, 75, 4);

INSERT INTO clientes (nombre, email, telefono) VALUES
('Ana García', 'ana@mail.com', '111-111'),
('Carlos López', 'carlos@mail.com', '222-222'),
('María Fernández', 'maria@mail.com', '333-333');

INSERT INTO pedidos (id_cliente, fecha, estado) VALUES
(1, '2025-10-01', 'entregado'),
(2, '2025-10-05', 'entregado'),
(1, '2025-10-12', 'enviado'),
(3, '2025-10-15', 'pendiente');

INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 850.00),
(1, 4, 1, 1200.00),
(1, 7, 3, 650.00),
(2, 2, 2, 1500.00),
(2, 5, 2, 950.00),
(3, 3, 1, 1650.00),
(3, 8, 2, 1400.00),
(4, 6, 1, 2450.00);
