# 15. Agentes no-code

> **Objetivo:** entender la otra vía: construir agentes **sin programar**, describiendo lo que querés en lenguaje natural (**specs**), dándole **capacidades** reutilizables y conectándolo a herramientas externas. Es el mismo concepto del Módulo 14, con otra forma de armarlo.

## La idea

En el Módulo 14 armamos un agente **con código**: definimos tools en Python, lo creamos y lo ejecutamos. En la vía no-code, en lugar de escribir el programa, **describimos** qué queremos que haga. La herramienta (un asistente tipo OpenCode, un builder visual, etc.) se encarga de la parte técnica.

En los dos casos hay lo mismo debajo: un LLM (cerebro), capacidades (manos) y un bucle (orquestación). Cambia **quién escribe el código**: vos o la herramienta.

## De código a especificación

| Con código (Módulo 14) | No-code |
|------------------------|---------|
| Escribís funciones en Python | Describís la tarea en lenguaje natural |
| Definís tools con `@tool` | Instalás **skills** ya hechas |
| Configurás el loop a mano | La herramienta maneja el loop |
| Conectás APIs programando | Conectás servicios vía **MCP** |

El paso clave es aprender a escribir **buenas especificaciones**: descripciones claras del objetivo, las entradas, las salidas y los criterios de éxito. Una buena spec es, para una herramienta no-code, lo que un buen `docstring` es para una tool.

## Skills (capacidades empaquetadas)

Una **skill** es un paquete de instrucciones y recursos que le enseña al agente **cómo** hacer una tarea concreta. Se describe en un archivo de texto (por ejemplo, `SKILL.md`) con:

- **Nombre y descripción:** cuándo debe usarse.
- **Instrucciones:** el procedimiento paso a paso.
- **Recursos:** scripts, plantillas o referencias que la skill necesita.

Las skills son **reutilizables** y se cargan solo cuando hacen falta, igual que un humano consulta una guía antes de una tarea específica.

## MCP (Model Context Protocol)

**MCP** es un **estándar** para conectar agentes con herramientas y datos externos sin programar la integración cada vez. Funciona como un "puerto universal": hay **servidores MCP** que exponen capacidades (leer archivos, consultar una base, usar un buscador) y el agente se **conecta** a ellos.

- Reemplaza el trabajo de escribir un conector a medida por **configurar** una conexión.
- El agente ve las opciones del servidor MCP como si fueran sus herramientas (Módulo 14).

## Herramientas del ecosistema

Asistentes como **OpenCode** (y otros agentes de terminal o builders visuales) permiten:

- Ejecutar tareas describiéndolas en lenguaje natural.
- Cargar **skills** para darles capacidades.
- Conectarse a **servidores MCP**.
- Definir **permisos** (qué puede tocar y qué no).

## Cuándo usar cada vía

- **No-code:** cuando existe una herramienta que ya resuelve bien el flujo, cuando no querés mantener código, o para prototipar rápido.
- **Con código (Módulos 13–14):** cuando necesitás control fino, lógica propia o integrarlo dentro de una aplicación.

> En la práctica se combinan: un agente no-code puede invocar una tool que escribiste a medida.

## Ejercicios

- [01 — Escribir una especificación](./ejercicios/01-especificacion.md)
- [02 — Diseñar una skill](./ejercicios/02-skill.md)

[Menu Principal](../../README.md) | [Índice IA](../readme.md) | [Anterior: ¿Qué es RAG? ←](../11-5-que-es-rag/readme.md) | [Siguiente: Índice principal →](../../README.md)
