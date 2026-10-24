-- 03 - Consultas condicionales
-- Objetivo: Practicar WHERE, AND, OR, IN, BETWEEN, LIKE

-- 1. Clientes de Córdoba
SELECT * FROM clientes WHERE ciudad = 'Cordoba';

-- 2. Clientes de Córdoba O Rosario
SELECT * FROM clientes WHERE ciudad = 'Cordoba' OR ciudad = 'Rosario';

-- 3. Usando IN (equivalente al anterior)
SELECT * FROM clientes WHERE ciudad IN ('Cordoba', 'Rosario');

-- 4. Productos con precio entre 10000 y 15000
SELECT * FROM productos WHERE precio BETWEEN 10000 AND 15000;

-- 5. Productos cuyo título empiece con 'P'
SELECT * FROM productos WHERE titulo LIKE 'P%';

-- 6. Productos cuyo autor contenga 'Martin'
SELECT * FROM productos WHERE autor LIKE '%Martin%';

-- 7. Clientes cuyo email termine con 'mail.com'
SELECT * FROM clientes WHERE email LIKE '%mail.com';

-- 8. Pedidos entre dos fechas
SELECT * FROM pedidos WHERE fecha BETWEEN '2025-10-01' AND '2025-10-02';

-- 9. Clientes activos (si existe campo activo)
-- SELECT * FROM clientes WHERE activo = 1;

-- 10. Combinar condiciones: productos con stock > 0 y precio < 13000
SELECT * FROM productos WHERE stock > 0 AND precio < 13000;
