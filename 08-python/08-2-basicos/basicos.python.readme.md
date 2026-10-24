### Ejecución de código
*Actividad Práctica Preparatoria*

1. Aprovechando el contenido aprendido anteriormente, debemos automatizar las siguientes tareas en un solo comando de Bash:
   1. Creamos una carpeta.
   2. Ingresamos a la carpeta creada.
   3. Creamos un entorno virtual con el módulo de Python.
   4. Activamos el entorno de trabajo.
   5. Verificamos si dicho entorno está activo.
   6. Si es correcto el paso anterior, creamos un archivo con extensión `.py`.
   7. Inicializamos el repositorio de Git en la rama principal (`main`).
   8. Informamos el proceso de apertura del editor de código.
   9. Le indicamos a VS Code que queremos abrir la carpeta del proyecto y ver el archivo en pantalla.

```bash
mkdir curso_ia && cd curso_ia && python3 -m venv entorno-utn && source entorno-utn/bin/activate && [[ "$(which pip)" == *"entorno-utn"* ]] && echo "Entorno verificado. Continuamos..." && touch basic.py && sleep 0.5 && git init -b main && echo "Abriendo entorno en Visual Studio Code, por favor aguarde..." && code . basic.py
```

> Si quisiéramos reutilizar el comando solo cambiamos: nombre de carpeta, nombre de archivo, nombre de entorno de trabajo.

Una vez creado el archivo basta ejecutar:
```bash
python3 basic.py # o el nombre correspondiente
```

---

## Tipos de datos

**Strings o cadenas de caracteres**
- Se refieren a todo el texto: letras, números y símbolos. Cada elemento ocupa el espacio de 1 carácter, *siempre que estén enmarcados entre comillas dobles (`""`) o simples (`''`)*.
- **Métodos comunes de manipulación:** 
  Al ser **inmutables**, no se pueden modificar de forma directa, sino que devuelven un nuevo texto resultante.
  - `.upper()`: Pasa todo el texto a mayúsculas.
  - `.lower()`: Pasa todo el texto a minúsculas.
  - `.replace(viejo, nuevo)`: Busca un fragmento de texto y lo reemplaza por otro.

```python
texto = "hola utn"
print(texto.upper())  # Salida: "HOLA UTN"
```

**Números**
En Python, los números nativos son de **3 tipos principales**:
- `int` (Enteros): Números sin decimales, ya sean positivos o negativos (ej. `10`, `-5`). En Python tienen precisión infinita.
- `float` (Flotantes): Números con punto decimal (ej. `3.14`, `-0.5`). Representan números reales.
- `complex` (Complejos): Números matemáticos que poseen una parte real y una parte imaginaria (ej. `2 + 3j`, donde la `j` representa la raíz cuadrada de -1). Se utilizan para cálculos científicos, físicos y algebraicos avanzados.

*(Nota: Si necesitás alta precisión financiera para evitar errores de redondeo, Python incluye un módulo especial llamado `decimal`, pero se debe importar aparte).*

**Booleanos (Booleans)**
- Representan valores de lógica binaria: verdadero o falso. En Python se definen con el tipo `bool`.
- **Regla estricta:** La primera letra **siempre** va en mayúscula: `True` o `False` (escribir `true` en minúscula dará un error de sintaxis).

---

## Datos Compuestos (Colecciones)
Estructuras de datos que permiten almacenar múltiples valores en una sola variable. Python ofrece 4 tipos principales incorporados:

| Colección | Sintaxis | ¿Es Ordenada? | ¿Permite Duplicados? | ¿Es Modificable (Mutable)? |
| :--- | :--- | :--- | :--- | :--- |
| **`list` (Lista)** | Corchetes `[ ]` | Sí (Basada en índice `0`) | Sí | Sí |
| **`tuple` (Tupla)** | Paréntesis `( )` | Sí (Basada en índice `0`) | Sí | **No (Inmutable)** |
| **`set` (Conjunto)** | Llaves `{ }` | No (Desordenada) | **No** | Sí (Pero sus elementos individuales deben ser inmutables) |
| **`dict` (Diccionarios)** | Llaves y pares `{clave: valor}` | Sí (Desde Python 3.7) | No (Claves únicas) | Sí |

### Explicación detallada y cuándo usar cada una:

#### 1. Listas (`list`)
- Son colecciones secuenciales de elementos donde importa el orden de llegada. Cada elemento tiene asignada una posición numérica o índice que arranca en `0`.
- **Cuándo usarla:** Cuando necesitás una lista de compras, un historial de logs ordenados cronológicamente o cualquier secuencia donde el orden sea clave, requieras modificar los datos constantemente y admitas duplicados.

#### 2. Tuplas (`tuple`)
- Estructuras idénticas a las listas en orden e índices, pero con una restricción absoluta: **son inmutables**. Una vez que la creás, la computadora te prohíbe agregar, quitar o alterar sus datos.
- **Cuándo usarla:** Para proteger datos que nunca deberían cambiar durante la ejecución del programa. Ejemplos perfectos: coordenadas geográficas `(latitud, longitud)`, los días de la semana, o configuraciones fijas de red de servidores.

#### 3. Conjuntos (`set`)
- Colecciones desordenadas de elementos únicos. No tienen índices (no podés pedirle el "primer" elemento) y si intentás agregar un elemento que ya existe, Python lo ignora en silencio.
- **Cuándo usarla:** Cuando necesitás eliminar duplicados de forma masiva de una base de datos o validar membresías rápidamente (saber si un ID de usuario existe o no dentro de un grupo sin importar el orden). Son ultra eficientes para operaciones matemáticas como uniones e intersecciones de datos.

#### 4. Diccionarios (`dict`)
- Colecciones que asocian una palabra clave única (`clave`) con un significado (`valor`). No se accede a los datos por su número de posición, sino llamando al nombre de su clave.
- **Cuándo usarla:** Para representar objetos reales mapeados con propiedades estructuradas. Por ejemplo, los datos de un usuario `{"id": 45, "nombre": "Pablo", "rol": "admin"}` o tablas de configuración de entornos IT.

---

## Métodos de manipulación para Datos Compuestos
Las colecciones mutables (`list`, `dict` y `set`) exigen el uso de métodos específicos para alterar su contenido.

### 1. En Listas (`list`)
**Agregar elementos:**
- `.append(valor)`: Agrega un elemento al **final** de la lista.
- `.insert(índice, valor)`: Inserta un elemento en una **posición específica** desplazando el resto hacia atrás.

**Modificar elementos:**
- Se realiza de forma directa seleccionando su posición por índice: `lista[índice] = nuevo_valor`.

**Eliminar elementos:**
- `.remove(valor)`: Busca y elimina la **primera aparición** de ese valor específico. Si no existe, da error.
- `.pop(índice)`: Elimina y te devuelve el elemento en esa posición. Si dejás los paréntesis vacíos `.pop()`, elimina el **último**.
- `del lista[índice]`: Palabra clave nativa para borrar un elemento por su posición en el arreglo.

```python
mi_lista = ["Python", "Git"]

# Agregar
mi_lista.append("Bash")          # ["Python", "Git", "Bash"]
mi_lista.insert(1, "Markdown")   # ["Python", "Markdown", "Git", "Bash"]

# Modificar
mi_lista[2] = "GitHub"           # ["Python", "Markdown", "GitHub", "Bash"]

# Eliminar
mi_lista.remove("Markdown")      # ["Python", "GitHub", "Bash"]
elemento_borrado = mi_lista.pop(0) # Borra "Python"
del mi_lista[0]                  # Borra lo que quedó en la posición 0 ("GitHub")
```

### 2. En Diccionarios (`dict`)
**Agregar y Modificar elementos:**
- En diccionarios se usa la misma sintaxis para ambas tareas: `diccionario[clave] = valor`. Si la clave ya existe, pisa su contenido; si no existe, la crea al final de la colección.
- `.update({clave: valor})`: Permite agregar o modificar múltiples pares de datos en simultáneo.

**Eliminar elementos:**
- `.pop(clave)`: Elimina la clave indicada junto con su valor asignado de forma segura.
- `del diccionario[clave]`: Borra de forma directa la clave especificada de la estructura en memoria.
- `.clear()`: Vacía por completo el diccionario dejándolo vacío en `{}`.

```python
mi_dict = {"curso": "IA", "sede": "UTN"}

# Agregar
mi_dict["año"] = 2026            # {"curso": "IA", "sede": "UTN", "año": 2026}

# Modificar
mi_dict["sede"] = "UTN-FRBA"     # {"curso": "IA", "sede": "UTN-FRBA", "año": 2026}

# Eliminar
mi_dict.pop("curso")             # Elimina "curso" y su valor "IA"
del mi_dict["año"]               # Elimina la clave "año" de raíz
```

### 3. En Conjuntos (`set`)
**Agregar elementos:**
- `.add(valor)`: Agrega un elemento al conjunto. Si el elemento ya existía, no genera cambios ni da errores.

**Eliminar elementos:**
- `.remove(valor)`: Elimina el elemento especificado. Si el elemento no existe en el conjunto, lanza un error (`KeyError`).
- `.discard(valor)`: Elimina el elemento especificado de forma segura. Si el elemento no existe, el código continúa sin tirar error.

```python
mi_set = {"Linux", "Windows"}

# Agregar
mi_set.add("Debian")             # {"Linux", "Windows", "Debian"}
mi_set.add("Linux")              # No pasa nada, "Linux" ya existe en el set

# Eliminar
mi_set.remove("Windows")         # {"Linux", "Debian"}
mi_set.discard("MacOS")          # No hace nada y no da error, a diferencia de .remove()
```

---

## Funciones predeterminadas (Built-in Functions)
Python incluye funciones integradas listas para usar que nos permiten interactuar con los datos de forma nativa:

- **`print()`**: Muestra información por consola. Puede imprimir texto, variables o resultados de operaciones.
  ```python
  print("Hola Mundo")
  ```
- **`type()`**: Devuelve el tipo de dato exacto de la variable o valor que se le pase entre los paréntesis. Funciona como el inspector de tipos del lenguaje.
  ```python
  print(type(10))     # Salida: <class 'int'>
  print(type("UTN"))  # Salida: <class 'str'>
  ```

---

## Concatenación
La concatenación es la acción de **unir dos o más cadenas de caracteres (strings)** para formar un único bloque de texto. En Python existen dos formas principales de realizarla:

### 1. El operador tradicional (`+`)
Suma un string al lado del otro de forma secuencial.
- **Regla de oro:** Solo se pueden concatenar strings con strings. Si se intenta sumar un string con un número (`int` o `float`), Python lanzará un error de tipo (`TypeError`).
```python
nombre = "Andres"
saludo = "Hola " + nombre  # Resultado: "Hola Andres"
```
Para incluir un número, hay que transformarlo a texto primero usando `str()`:
```python
edad = 25
mensaje = "Tengo " + str(edad) + " años"
```

### 2. Cadenas formateadas o f-strings (Forma moderna y recomendada)
Se antepone una letra `f` inmediatamente antes de abrir las comillas. Permite incrustar variables o expresiones de código directo dentro del texto utilizando llaves `{}`.
- **Ventaja:** Python se encarga de convertir automáticamente cualquier tipo de dato (números, booleanos, etc.) a texto en segundo plano, evitando errores de tipado.
```python
curso = "IA"
alumnos = 40
info = f"En el curso de {curso} hay {alumnos} estudiantes inscritos."
```

[Menu Principal](../../README.md)

[Siguiente Lección: Basicos](../08-3-estructuras-condicionales/condicionales.readme.md)