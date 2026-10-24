# 12 - Migraciones en SQL

## Objetivo

Entender qué son las migraciones, para qué sirven and cómo aplicarlas correctamente.

## ¿Qué es una migración?

Una **migración** es un archivo con instrucciones SQL que **cambia la estructura** de la base de datos de forma controlada, ordenada y reproducible.

Es como un **historial de cambios** de tu base de datos.

## ¿Por qué usar migraciones?

Sin migraciones, es fácil:
- Olvidar qué cambios se hicieron
- Crear tablas distintas en diferentes entornos (local, producción)
- Romper la base sin saber por qué
- Perder tiempo reconstruyendo el esquema

Con migraciones:
- **Reproducible**: cualquiera puede recrear la base con los mismos pasos
- **Ordenado**: los cambios van uno detrás de otro
- **Versionado**: sabés qué se agregó, cuándo y por qué
- **Seguro**: se pueden revertir o seguir paso a paso

## Ejemplo práctico

Vamos a crear una migración para agregar una columna:

**Archivo: `001_agregar_telefono_a_clientes.sql`**

```sql
-- Migración: agregar campo telefono a tabla clientes
ALTER TABLE clientes ADD COLUMN telefono TEXT;
```

Otro ejemplo: crear tabla:

**Archivo: `002_crear_tabla_categorias.sql`**

```sql
CREATE TABLE categorias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL UNIQUE
);
```

## Comandos comunes en migraciones

| Comando | Uso |
|---|---|
| `CREATE TABLE` | Crear tabla |
| `ALTER TABLE ... ADD COLUMN` | Agregar columna |
| `ALTER TABLE ... DROP COLUMN` | Borrar columna (no siempre soportado) |
| `DROP TABLE` | Eliminar tabla |
| `CREATE INDEX` | Crear índice para acelerar búsquedas |

## Buenas prácticas

- **Numeralas**: `001_`, `002_`, `003_...` para mantener orden.
- **Descriptivas**: `001_crear_tabla_clientes.sql` mejor que `migracion1.sql`.
- **Una acción lógica por migración**: más fácil de entender y revertir.
- **Nunca modifiques migraciones ya aplicadas**: crea una nueva migración.
- **Guardalas en el repositorio**: forman parte del proyecto.

## ¿Dónde las vemos en este curso?

En `Practicas/SQL/` vas a encontrar esquemas e inserciones. Ahí podés empezar a pensar en migraciones: primero crear estructura, después cargar datos.

## Recapitulación

- Migración = cambio controlado de la estructura.
- Permite versionar y reproducir la base de datos.
- Usá nombres numerados y descriptivos.
- Creá una nueva migración, no edites las viejas.

[← Anterior: INNER JOIN múltiples tablas](./11-inner-join-multiples-tablas.md) | [Índice](./README.md) | [Siguiente: SQL en IA, RAG y diferencia vectorial →](./13-sql-en-ia-rag-diferencia-vectorial.md)
