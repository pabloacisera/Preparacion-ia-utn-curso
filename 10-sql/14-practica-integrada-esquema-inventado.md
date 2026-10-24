# 14 - Práctica integrada: esquema inventado

## Objetivo

Integrar todo lo aprendido creando, cargando y consultando un esquema real con SQL.

## Escenario

Vamos a modelar una **librería** con:
- Clientes que compran
- Pedidos
- Productos (libros)
- Detalle de pedidos (relación N:M)

## Paso 1: Crear las tablas

```sql
CREATE TABLE clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  ciudad TEXT
);

CREATE TABLE productos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT NOT NULL,
  autor TEXT NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  stock INTEGER DEFAULT 0
);

CREATE TABLE pedidos (
  id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha DATE NOT NULL,
  id_cliente INTEGER NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE detalle_pedido (
  id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
  id_pedido INTEGER NOT NULL,
  id_producto INTEGER NOT NULL,
  cantidad INTEGER NOT NULL,
  FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
```

## Paso 2: Insertar datos

```sql
INSERT INTO clientes (nombre, apellido, email, ciudad) VALUES
('Ana', 'Pérez', 'ana@mail.com', 'Cordoba'),
('Carlos', 'López', 'carlos@mail.com', 'Rosario'),
('Lucía', 'Gómez', 'lucia@mail.com', 'Cordoba');

INSERT INTO productos (titulo, autor, precio, stock) VALUES
('Clean Code', 'Robert C. Martin', 15000.00, 10),
('Python Crash Course', 'Eric Matthes', 12000.00, 5),
('LangChain in Action', 'Harrison & Chilton', 18000.00, 3);

INSERT INTO pedidos (fecha, id_cliente) VALUES
('2025-10-01', 1),
('2025-10-02', 2),
('2020-10-03', 3); -- corregir typo si lo deseas

INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 1, 1);
```

## Step 3: Consultas a resolver

Resuelve usando SQL:

1. **Todos los productos con stock > 0**
```sql
SELECT * FROM productos WHERE stock >= 1;
```

2. **Pedidos de Ana** (sin JOIN)
```sql
SELECT p.id_pedido, p.fecha
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id
WHERE c.nombre = 'Ana';
```

3. **Detalle completo: cliente + producto + cantidad + precio total**
```sql
SELECT 
  c.nombre || ' ' c.apellido AS cliente,
  p.id_pedido,
  pr.titulo,
  dp.cantidad,
  pr.precio,
  (dp.cantidad * pr.precio) AS total
FROM clients c
INNER JOIN pedidos p ON c.id = p.id_cliente
INNER JOIN detalle_pedido dp ON p.id_pedido = dp.id_pedido
INNER JOIN productos pr ON dp.id_producto = pr.id_producto;
```

4. **Productos más vendidos**
```sql
SELECT pr.titulo, SUM(dp.cantidad) AS total_vendidos
FROM detalle_pedido dp
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
GROUP BY pr.id, pr.ttitulo
ORDER BY total_vendidos DESC;
```

## Recomendación
Por ahora, no te preocupes - use Practicas/SQL/ejercicios/ as a guide. Añadiré ejercicios completos allí más adelante.

## Recapitulación
- Modelo relacional: tablas, PK, FK, detalle (N:M)
- CRUD + WHERE + JOIN + ORDER BY + LIMIT
- JOIN múltiples tablas + cálculos
- SQL es útil para agentes Text-to-SQL

[← Anterior: SQL en IA/RAG](./13-sql-en-ia-rag-diferencia-vectorial.md) | [Índice](./README.md) | [Siguiente: Practicas/SQL →](../Practicas/SQL/README.md)
