# 08 - Consultas condicionales: WHERE

## Objetivo

Filtrar registros para obtener solo lo que necesitamos.

## ¿Qué es WHERE?

`WHERE` filtra las filas que cumplen una **condición**. Solo devuelve los registros donde la condición es `TRUE`.

## Operadores básicos

| Operador | Significado | Ejemplo |
|---|---|---|
| `=` | Igual | `WHERE id = 1` |
| `<>` o `!=` | Distinto | `WHERE nombre <> 'Ana'` |
| `<`, `>`, `<=`, `>=` | Comparación | `WHERE edad >= 18` |
| `AND` | Ambas condiciones | `WHERE edad >= 18 AND activo = 1` |
| `OR` | Al menos una | `WHERE ciudad = 'CBA' OR ciudad = 'ROS'` |
| `NOT` | Niega la condición | `WHERE NOT activo = 1` |

## Ejemplos prácticos

```sql
-- Clientes mayores de 18
SELECT * FROM clientes WHERE edad >= 18;

-- Clientes activos de Córdoba
SELECT * FROM clientes WHERE activo = 1 AND ciudad = 'Cordoba';

-- Clientes de Córdoba o Rosario
SELECT * FROM clientes WHERE ciudad = 'Cordoba' OR ciudad = 'Rosario';
```

## Combinar con paréntesis

Cuando mezclamos `AND` y `OR`, los paréntesis evitan confusiones.

```sql
-- (Córdoba o Rosario) Y activos
SELECT * FROM clientes 
WHERE (ciudad = 'Cordoba' OR ciudad = 'Rosario') AND activo = 1;
```

Sin paréntesis el resultado puede ser distinto.

## ¿Por qué importa?

- Filtrás datos relevantes, no traés toda la tabla.
- Esencial para agentes: *"buscá pedidos de este cliente"* = `WHERE id_cliente = ...`
- Menor cantidad de datos = respuestas más rápidas y claras.

## Recapitulación

- `WHERE` filtra filas.
- `AND/OR/NOT` combinan condiciones.
- Usá paréntesis al mezclar `AND` y `OR`.

[← Anterior: CRUD](./07-crud-insert-select-update-delete.md) | [Índice](./README.md) | [Siguiente: LIKE, BETWEEN, IN, ORDER BY, LIMIT →](./09-like-between-in-orderby-limit.md)
