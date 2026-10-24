# INNER JOIN: Función, utilidad e importancia

## Objetivo

Entender qué es `INNER JOIN`, para qué sirve, por qué es importante y cómo usarlo correctamente.

## ¿Qué es un JOIN?

Un **JOIN** nos permite **combinar filas de dos o más tablas** basándonos en una relación entre ellas (generalmente una clave primaria con una clave foránea).

## ¿Qué es INNER JOIN?

`INNER JOIN` devuelve **únicamente las filas que tienen coincidencia en ambas tablas**. Si no hay coincidencia, esa fila **no aparece** en el resultado.

## Analogía

Imagina que tienes dos listas:
- **Lista A**: Clientes que hicieron pedidos
- **Lista B**: Pedidos registrados

Si quieres ver **"qué cliente hizo qué pedido"**, solo te interesan los casos donde **existe relación en ambas listas**. Ahí es donde entra `INNER JOIN`.

## Función

**Función principal:** Relacionar información distribuida en varias tablas para obtener una vista completa sin duplicar datos.

## Utilidad

- **Evitar duplicación**: Guardamos datos en su tabla correcta (normalización)
- **Consultas significativas**: Ver nombres de clientes junto a sus pedidos, productos con sus categorías, etc.
- **Integridad**: Trabajamos con datos relacionados correctamente
- **Eficiencia**: Mejor organización y mantenimiento

## Importancia

`INNER JOIN` es **fundamental** porque:

- **Es la base de las consultas relacionales**: La mayoría de reportes usan joins
- **Permite aprovechar el diseño relacional**: Sin joins, las tablas relacionales perderían gran parte de su valor
- **Esencial para aplicaciones reales**: Casi toda app con usuarios + pedidos + productos usa joins
- **Clave para entender datos**: Te permite ver el "panorama completo" uniendo piezas

## Sintaxis básica

```sql
SELECT tabla1.columna, tabla2.columna
FROM tabla1
INNER JOIN tabla2 ON tabla1.clave = tabla2.clave_foranea;
```

**Partes:**
- `SELECT`: Qué columnas queremos ver
- `FROM tabla1`: Tabla principal
- `INNER JOIN tabla2`: Tabla a unir
- `ON`: Condición de unión (cómo se relacionan)

## Diferencia con otras uniones (conceptual)

- **INNER JOIN**: Solo coincidencias en ambas tablas
- **LEFT JOIN**: Todas las filas de la tabla izquierda + coincidencias de la derecha (veremos más adelante, pero lo importante ahora es INNER)
- **RIGHT JOIN / FULL OUTER JOIN**: Otros casos menos frecuentes

**Por ahora nos enfocamos en INNER JOIN**, ya que es el que pide el ejercicio.

[← Volver al índice de SQL](../README.md) | [Índice de SQL](../README.md) | [Siguiente: Relaciones 1 a muchos →](./03-relaciones-1-a-muchos.md)
