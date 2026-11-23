### 3 capas de prompting

- Capa 1: reformulación de consultas. Transorma la consulta del usuario, en una estructura mas efectiva para la busqueda vectorial.
- Capa 2: prompt de sistema para paréntesis. Define la personalidad del modelo, su rol, reglas de anclaje, formato de citas, comportamiento ante información faltante, etc.
- Capa 3: prompt de ensamblaje y sintesis. Maneja como se combinan los fragmentos recuperados, la deduplicación y el razonamiento multi-salto. Usualmente la capa 2 y 3 se encriben juntas, pero se deben analizar su implementación cuando la informacion es conflictiva y dispersa.

Prompt de sistema vs prompt de usuario:

El prompt de sistema establece las reglas bases para cada solicitud, el prompt de usuario contiene la consulta actual e instrucciones especificas para esta consulta.

La separación entre ambos es crucial: cuando las instrucciones se mezclan entre las dos capas, el modelo puede ignorar reglas importantes, priorizar instrucciones de corto plazo sobre las de largo plazo y perder consistencia entre consultas.

*Lost in the middle* y la colocación.

La posición de los fragmentos recuperados dentro del prompt afecta drásticamente si el modelo los utiliza o no. Los LLMs muestran una curva de rendimiento en forma de U: prestan más atención al principio y al final del contexto, mientras que la información en el medio tiende a ser ignorada. Este fenómeno, conocido como lost-in-the-middle, fue formalizado por Liu et al. (2023) y se ha convertido en uno de los hallazgos más influyentes en la literatura de RAG.

Incluso con ventanas de 4K tokens, la precisión puede caer del 70-75% al 55-60% cuando se colocan 20 documentos recuperados en el medio. La solución práctica es colocar los fragmentos más relevantes al principio o al final del bloque de contexto, y estructurar el prompt con el mensaje de sistema al inicio, los fragmentos en el medio (ordenados por relevancia), y la consulta del usuario y las restricciones al final, aprovechando el efecto de recencia.

*Gestión de Contexto y consumo de tokens*

El costo escala linealmente con cada iteración de inferencia. Podemos aplicar ciertas técnicas para optimizar calidad/consumo.

- Ventana Deslizante: descartar mensajes antiguos;
- Sumarización Recursiva: resumir periodicamente las conversaciones;
- Estado Estructurado: crear un json con metas, hechos o registros
- Contexto efimero via RAG: recuperar solo eventos relevantes
- enrutamiento dinamico: usar mas de 1 tipo de modelo(livianos + razonamiento profundo)


