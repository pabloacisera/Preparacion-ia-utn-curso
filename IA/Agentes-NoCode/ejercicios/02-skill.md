# Ejercicio 02 — Diseñar una skill

**Objetivo:** empaquetar un procedimiento reutilizable en una **skill**, al estilo de un archivo `SKILL.md`.

## Consigna

Tomá la spec del Ejercicio 01 y convertila en una skill. Escribí el archivo con esta estructura:

```markdown
---
name: resumen-semanal
description: Use when the user asks to summarize weekly course notes into a PDF.
---

# Resumen semanal de apuntes

## Cuándo usar esta skill
Cuando el usuario pide resumir los apuntes de la semana y generar un PDF.

## Procedimiento
1. Leer los archivos de la carpeta de apuntes.
2. Agrupar por tema.
3. Escribir un resumen de cada tema (máximo N líneas).
4. Generar un PDF con el resultado.

## Recursos
- Plantilla de portada (plantilla.md)
- Script de generación de PDF (generar_pdf.py)

## Errores comunes
- Si no hay apuntes, avisar en lugar de inventar.
```

## Qué deberías observar

- La **descripción** (arriba) es lo que el agente lee para decidir **cuándo** cargar la skill; equivale a la descripción de una tool.
- El **procedimiento** son las instrucciones que guían el trabajo.
- Los **recursos** son archivos de apoyo: la skill no está sola, trae sus materiales.

## Experimentos

1. ¿Qué diferencia hay entre una skill muy genérica (*"ayudar con documentos"*) y una específica (*"resumir apuntes semanales a PDF"*)? ¿Cuál elegiría mejor un agente?
2. Pensá qué skill te serviría a vos y escribila. ¿Qué recursos necesitaría?
3. Relacioná: ¿en qué se parece una skill a una **tool** del Módulo 14 y en qué se diferencia?

[Volver al módulo](../readme.md)
