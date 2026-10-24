-- 02 - CRUD: Practica
-- Objetivo: Practicar INSERT, SELECT, UPDATE, DELETE

-- 1. Insertar nuevos clientes
INSERT INTO clientes (nombre, apellido, email, ciudad) VALUES
('María', 'Fernández', 'maria@mail.com', 'Buenos Aires'),
('Jorge', 'Ruiz', 'jorge@mail.com', 'Mendoza');

-- 2. Ver todos los clientes
SELECT * FROM clientes;

-- 3. Ver solo nombre, apellido y email de todos los clientes
SELECT nombre, apellido, email FROM clientes;

-- 4. Actualizar la ciudad de María a 'La Plata'
-- Primero verificar
SELECT * FROM clientes WHERE nombre = 'María';

-- Luego actualizar
UPDATE clientes SET ciudad = 'La Plata' WHERE nombre = 'María' AND apellido = 'Fernández';

-- Verificar cambio
SELECT * FROM clientes WHERE nombre = 'María';

-- 5. Eliminar el cliente Jorge Ruiz
-- Primero verificar
SELECT * FROM clientes WHERE nombre = 'Jorge' AND apellido = 'Ruiz';

-- Luego eliminar
DELETE FROM clientes WHERE nombre = 'Jorge' AND apellido = 'Ruiz';

-- Verificar eliminación
SELECT * FROM clientes;
