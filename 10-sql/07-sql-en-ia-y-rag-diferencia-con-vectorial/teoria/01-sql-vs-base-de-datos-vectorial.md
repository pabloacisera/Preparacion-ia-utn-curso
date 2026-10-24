# SQL vs Base de Datos Vectorial: Diferencias y uso en IA/RAG

## Objetivo

Entender las diferencias entre SQL relacional y bases de datos vectoriales, cuándo usar cada uno y cómo entran en IA/RAG.

## Diferencias principales

| Aspecto | **SQL (Relacional)** | **Base de datos vectorial** |
|---|---|---|
| **Tipo de datos** | Datos estructurados (tablas, filas, columnas) | Datos no estructurados convertidos a vectores (embeddings) |
| **Búsqueda** | Exacta o por filtros (`WHERE`, `=`, `LIKE`) | Por similitud semántica (coseno, euclidiana) |
| **Pregunta típica** | "¿Qué pedidos hizo Juan el mes pasado?" | "¿Qué documentos hablan sobre X tema?" |
| **Estructura** | Rigida con relaciones (`PK`/`FK`) | Flexible, enfocado a búsqueda por cercanía |
| **Casos de uso** | Usuarios, productos, pedidos, inventarios, reportes | Documentos, PDFs, FAQs, conocimiento privado, búsqueda semántica |
| **Precisión** | Muy precisa para datos exactos | Muy buena para "buscar por significado" |

## ¿Cuándo usar SQL?

Usa SQL cuando necesitas **datos exactos y con relaciones**:

- Listar usuarios registrados
- Obtener pedidos de un cliente
- Filtrar productos por categoría y precio
- Generar reportes con totales
- Validar información (IDs, estados)

## ¿Cuándo usar base de datos vectorial?

Usa una base vectorial cuando necesitas **buscar por significado**:

- Buscar en manuales, documentación o PDFs
- Responder con base en conocimiento privado
- Encontrar documentos similares
- Búsqueda semántica en chats/conversaciones
- Recuperar contexto relevante para un LLM

## ¿Cómo entran las bases de datos en IA y RAG?

**RAG** (*Retrieval-Augmented Generation*) = Aumentar la respuesta del LLM con información recuperada.

El flujo típico:

1. **Preparación**: Documentos → chunking → embeddings → guardar en **base vectorial**
2. **Consulta**: Pregunta del usuario → embedding → **búsqueda por similitud** en base vectorial
3. **Recuperación**: Se obtienen chunks relevantes
4. **Generación**: Se envían al LLM junto con la pregunta para generar respuesta fundamentada

## ¿SQL y vectorial son rivales o complementarios?

**Son complementarios**, no excluyentes.

**Ejemplo práctico:**

Imagina un agente de atención al cliente:
- **SQL**: "¿Cuál es el estado del pedido #123?" (dato exacto, necesita filtro preciso)
- **Vectorial**: "¿Cómo devuelvo un producto?" (buscar en política de devoluciones por significado)

Un **agente inteligente** puede usar **ambos**:
1. Usa SQL para obtener datos del pedido del usuario
2. Usa base vectorial para buscar en FAQs/políticas
3. Combina ambos contextos y responde con precisión

## Diferencia clave para recordar

- **SQL responde:** *"Dame lo que coincida exactamente con estas reglas"*
- **Vectorial responde:** *"Dame lo que se parezca más semánticamente a esta pregunta"*

**En resumen:** SQL = **datos estructurados + precisión**. Vectorial = **conocimiento no estructurado + búsqueda por significado**. En RAG moderno, **lo ideal es combinar ambos cuando tiene sentido**.

[← Volver al índice de SQL](../README.md) | [Índice de SQL](../README.md) | [Siguiente: Práctica integrada con esquema inventado →](../../08-practica-integrada-esquema-inventado/teoria/01-enunciado-del-caso-practico.md)
