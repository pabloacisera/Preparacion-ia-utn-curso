# 09 - LIKE, BETWEEN, IN, ORDER BY, LIMIT

## Objetivo

Aprender filtros más prácticos y ordenar/limitar resultados.

## LIKE - Búsqueda por patrón

`LIKE` busca coincidencias parciales con `%` y `_`.

| Símbolo | Significado | Ejemplo |
|---|---|---|
| `%` | Cualquier cantidad de caracteres | `%gmail%` encuentra cualquier mail con gmail |
| `_` | Un solo carácter | `ana_` encuentra `anar`, `anas` (un carácter más) |

```sql
-- Nombres que empiecen con 'A'
SELECT * FROM clientes WHERE nombre LIKE 'A%';

-- Emails que contengan 'gmail'
SELECT * FROM clientes WHERE email LIKE '%gmail%';

-- Nombres que terminen con 'a'
SELECT * FROM clientes WHERE nombre LIKE '%a';
```

> En algunos motores `LIKE` no distingue mayúsculas/minúsculas. En SQLite sí distingue por defecto.

## IN - Lista de valores

Más limpio que varios `OR`.

```sql
-- Clientes de Córdoba, Rosario o Mendoza
SELECT * FROM clientes WHERE ciudad IN ('Cordoba', 'Rosario', 'Mendoza');

-- Equivale a:
-- WHERE ciudad = 'Cordoba' OR ciudad = 'Rosario' OR ciudad = 'Mendoza'
```

## BETWEEN - Rango de valores

Funciona con números, fechas y textos.

```sql
-- Precios entre 1000 y 5000
SELECT * FROM productos WHERE precio BETWEEN 1000 AND 5000;

-- Pedidos entre dos fechas
SELECT * FROM pedidos WHERE fecha BETWEEN '2025-10-01' AND '2025-10-07';
```

> `BETWEEN` es **inclusivo**: incluye los límites.

## ORDER BY - Ordenar resultados

```sql
-- Ordenar por precio ascendente (menor a mayor)
SELECT * FROM productos ORDER BY precio ASC;

-- Ordenar por precio descendente (mayor a menor)
SELECT * FROM productos ORDER BY precio DESC;

-- Ordenar por varios campos
SELECT * FROM clientes ORDER BY ciudad ASC, apellido ASC;
```

`ASC` es por defecto, no hace falta escribirlo.

## LIMIT - Limitar cantidad

Útil para ver pocos resultados o paginar.

```sql
-- Ver solo los 5 productos más caros
SELECT * FROM productos ORDER BY precio DESC LIMIT 5;

-- Primer registro
SELECT * FROM clientes ORDER BY id ASC LIMIT 1;
```

## Combinando todo

```sql
SELECT nombre, email, ciudad
FROM clientes
WHERE ciudad IN ('Cordoba', 'Rosario') AND activo = 1
ORDER BY apellido ASC
LIMIT 10;
```

## Recapitulación

- `LIKE` para búsquedas parciales.
- `IN` para listas, `BETWEEN` para rangos.
- `ORDER BY` ordena, `LIMIT` limita.

[← Anterior: WHERE](./08-consultas-condicionales-where.md) | [Índice](./README.md) | [Siguiente: INNER JOIN →](./10-inner-join-funcion-utilidad-importancia.md)
