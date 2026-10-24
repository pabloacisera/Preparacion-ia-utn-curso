# 10 - INNER JOIN: función, utilidad e importancia

## Objetivo

Entender por qué usamos `JOIN` para combinar datos de varias tablas relacionadas.

## El problema

Tenemos dos tablas relacionadas:
- `clientes(id, nombre, email)`
- `pedidos(id_pedido, fecha, id_cliente)`

Si queremos saber **"¿Quién hizo el pedido 101?"**, no alcanza con mirar solo `pedidos`. Necesitamos el nombre del cliente desde `clientes`.

## ¿Qué es INNER JOIN?

**INNER JOIN** devuelve solo los registros que **tienen coincidencia** en **ambas tablas**. Es decir, pedidos que sí tienen un cliente asociado (y viceversa).

## Sintaxis básica

```sql
SELECT columnas
FROM tabla1
INNER JOIN tabla2 ON tabla1.clave = tabla2.clave_foranea;
```

## Ejemplo práctico

```sql
SELECT clientes.nombre, clientes.email, pedidos.id_pedido, pedidos.fecha
FROM pedidos
INNER JOIN clientes ON pedidos.id_cliente = clientes.id;
```

Resultado: vemos el **nombre y email del cliente** junto a cada **pedido**.

## Con alias para escribir menos

```sql
SELECT c.nombre, p.id_pedido, p.fecha
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id;
```

- `p` = alias de `pedidos`
- `c` = alias de `clientes`
- Más corto y legible

## ¿Cuándo usar INNER JOIN?

- Cuando querés información **completa** cruzando datos.
- Cuando ambas tablas tienen el dato necesario.
- Cuando **no** querés mostrar registros huérfanos (pedidos sin cliente válido).

## Importancia para agentes y RAG

Un agente que responde *"Dame los pedidos de Ana con su fecha"* necesita hacer un `JOIN`. Si entendés esto, podés guiarlo correctamente y revisar si la consulta es coherente.

## Recapitulación

- `JOIN` une tablas usando claves.
- `INNER JOIN` trae solo coincidencias.
- Usar alias hace las consultas más legibles.

[← Anterior: LIKE/BETWEEN/IN/ORDER BY/LIMIT](./09-like-between-in-orderby-limit.md) | [Índice](./README.md) | [Siguiente: INNER JOIN con múltiples tablas →](./11-inner-join-multiples-tablas.md)
