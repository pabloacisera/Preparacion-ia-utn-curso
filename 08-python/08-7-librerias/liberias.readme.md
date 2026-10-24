### Librerías Nativas (Standard Library) más Usadas en Python

Python se destaca por su filosofía de *"batteries included"* (baterías incluidas), lo que significa que incluye una gran cantidad de módulos nativos listos para usar sin necesidad de instalar paquetes externos con `pip`.

---

## 1. Módulo `math` (Operaciones Matemáticas Avanzadas)
Permite realizar cálculos matemáticos complejos, trigonometría y manejo de constantes.

```python
import math

print(math.pi)                 # Salida: 3.141592653589793
print(math.factorial(5))       # Salida: 120 (5 * 4 * 3 * 2 * 1)
print(math.ceil(4.2))          # Redondeo hacia arriba: 5
```

---

## 2. Módulo `random` (Generación de Aleatoriedad)
Utilizado para simulaciones, juegos, selección aleatoria de elementos o contraseñas seguras.

```python
import random

# Número entero aleatorio entre un rango
numero_azar = random.randint(1, 10)

# Elegir un elemento al azar de una lista
colores = ["rojo", "verde", "azul"]
color_elegido = random.choice(colores)

print(color_elegido)
```

---

## 3. Módulo `datetime` (Manejo de Fechas y Horas)
Esencial para registrar logs, calcular tiempos de ejecución o gestionar fechas de bases de datos.

```python
from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()
print(ahora)

# Formatear fechas a texto legible
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_formateada)
```

---

## 4. Módulo `json` (Intercambio de Datos Estructurados)
Permite convertir diccionarios de Python a formato JSON (serialización) y viceversa (deserialización), ideal para APIs.

```python
import json

datos_dict = {"nombre": "Carlos", "edad": 30, "activo": True}

# Convertir diccionario a texto JSON (string)
json_string = json.dumps(datos_dict)
print(json_string)

# Convertir texto JSON de vuelta a diccionario
nuevo_dict = json.loads(json_string)
print(nuevo_dict["nombre"])  # Salida: Carlos
```

---

## 5. Módulo `os` (Interacción con el Sistema Operativo)
Permite interactuar con el sistema de archivos, leer variables de entorno y gestionar rutas del sistema.

```python
import os

# Ver el directorio de trabajo actual
directorio_actual = os.getcwd()
print(directorio_actual)

# Listar archivos de una carpeta
archivos = os.listdir(".")
print(archivos)
```