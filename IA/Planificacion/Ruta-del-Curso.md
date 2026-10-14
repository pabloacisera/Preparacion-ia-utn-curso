# Ruta del curso: de una frase a una aplicación con IA

> Documento de orientación. Registra **qué está hecho, qué falta y qué decisiones siguen abiertas**. Se actualiza a medida que avanzas.

## La escalera

| # | Módulo | Qué enseña | Herramientas | Estado |
|---|--------|------------|--------------|--------|
| 01 | Anatomía de un LLM (a mano) | Frase → números → tokens → predicción → elección → bucle → embeddings → atención → entrenamiento → chat | Python puro, numpy | **Hecho y ejecutado** (E01–E11) |
| 02A | Librerías livianas: tokens y embeddings | `tokenizers`, `fastembed`, abrir la caja con `onnxruntime` | tokenizers, fastembed, onnxruntime | **Redactado**; L01, L02, L03a, L05 ejecutados; L03b y L04 real pendientes de tu ejecución |
| 02B | Generación local liviana | Logits reales, bucle, chat con un modelo de ~0.11 GB | llama-cpp-python | **Redactado; sin ejecutar contra el modelo real** |
| 03 | APIs (Groq y Gemini) | El mismo recorrido por API: costo, límites, latencia, streaming | Groq, Gemini | **Pendiente** |
| 04 | RAG | Documentos, chunking, embeddings, base vectorial, recuperación, armado del prompt, evaluación | por definir (p. ej. PostgreSQL + pgvector) | **Pendiente** |

## Principios acordados

1. **De lo menos a lo más**: se empieza por una frase, no por un chat ni por un RAG.
2. **Primero a mano, luego librerías, luego API, luego sistema completo.**
3. **Nada pesado hasta que haga falta**: se mide el peso de cada dependencia y se justifica cada elección.
4. **Cada pieza nueva nace de un fallo de la anterior** que el alumno ya vio.
5. **Nada se afirma sin verificarlo**; lo que no se pudo ejecutar queda marcado.

## Lo que queda por hacer antes de escribir el Módulo 03

- Ejecutar tú L03b, L04 y G01–G05 y anotar qué falló (versiones, rutas, memoria, tiempos).
- Decidir qué se mide en el Módulo 03: latencia por token, costo por consulta, límites del plan gratuito (hay que **consultarlos en la documentación vigente**: cambian).
- Definir el criterio con el que Groq y Gemini se comparan con el modelo local.

## Decisiones abiertas del programa (de tu borrador)

| Decisión | Por qué importa |
|----------|-----------------|
| ¿A quién va dirigido: cero programación o base mínima? | Define ritmo y orden de los módulos |
| ¿Quién construye el proyecto: el docente en vivo o el alumno? | El borrador dice ambas cosas en secciones distintas |
| ¿Cuándo se enseña Python mínimo? | Si dirigir a un agente de código va antes, el alumno no puede leer lo que produce |
| ¿Dónde se despliega? | Falta para el módulo final |
| Versiones y cifras citadas en el borrador | No se verificaron; re-verificar antes de enviar (cambian) |

## Fechas de la convocatoria (según el texto que pasaste)

Fecha límite de recepción: **30 de octubre**. Respuesta en 14 días. Inicio de clases: marzo de 2027. Correo único de recepción: el indicado en la convocatoria. Adjuntos: solo certificaciones; además, enlaces a redes y un minivideo.
