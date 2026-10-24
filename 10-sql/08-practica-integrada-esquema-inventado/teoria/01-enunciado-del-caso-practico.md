# Enunciado del caso práctico: Tienda Online

## Objetivo

Aplicar todo lo aprendido: crear esquema, insertar datos en **varias tablas**, hacer `CRUD`, consultas con `WHERE` y `INNER JOIN`.

## Escenario

Vamos a modelar una **tienda online sencilla** con el siguiente negocio:
- Tenemos **categorías** de productos
- Tenemos **productos** que pertenecen a una categoría
- Tenemos **clientes** registrados
- Tenemos **pedidos** realizados por clientes
- Cada pedido tiene **detalles** con productos, cantidades y precios

## Esquema a implementar

| Tabla | Descripción |
|---|---|
| `categorias` | Clasificación de productos |
| `productos` | Catálogo de productos con precio y stock |
| `clientes` | Datos de clientes |
| `pedidos` | Cabecera del pedido (cliente, fecha, estado) |
| `detalle_pedido` | Líneas del pedido (productos, cantidad, precio unitario) |

## Relaciones

- `productos.id_categoria` → `categorias.id_categoria` (1:N)
- `pedidos.id_cliente` → `clientes.id_cliente` (1:N)
- `detalle_pedido.id_pedido` → `pedidos.id_pedido` (1:N)
- `detalle_pedido.id_producto` → `productos.id_producto` (1:N)

## Reglas para la práctica

1. **Crear esquema**: Usar `CREATE TABLE` con claves primarias y foráneas
2. **Insertar datos**: Cargar datos en **TODAS** las tablas (obligatorio para practicar `INNER JOIN`)
3. **CRUD**: Practicar `INSERT`, `SELECT`, `UPDATE`, `DELETE`
4. **Consultas condicionales**: Usar `WHERE`, `AND/OR`, `ORDER BY`, `LIMIT`
5. **INNER JOIN**: Unir varias tablas para obtener información completa
6. **Analizar**: Entender **qué** datos pides y **por qué** necesitas unir tablas

## Herramienta sugerida

Puedes usar **SQLite** (ligero, ideal para aprender). El archivo `sql/database.py` que existe en el repo te sirve como referencia para conectar con SQLite.

## Siguiente paso

Ve a la carpeta `Practicas/` y ejecuta los archivos en orden:
1. `00-crear-esquema.sql`
2. `01-insert-datos.sql`
3. `02-crud.sql`
4. `03-consultas-condicionales.sql`
5. `04-inner-joins.sql`
6. `05-desafios.sql`

[← Volver al índice de SQL](../README.md) | [Índice de SQL](../README.md) | [Ir a prácticas →](../Practicas/README.md)
