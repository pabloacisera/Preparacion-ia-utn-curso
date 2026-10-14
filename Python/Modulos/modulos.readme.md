### Modularización y Módulos en Python

La modularización es una práctica fundamental en programación que consiste en dividir un programa grande y complejo en partes más pequeñas, independientes y reutilizables llamadas **módulos**.

---

## 1. ¿Qué es un Módulo?
En Python, un módulo es simplemente un archivo con extensión `.py` que contiene código ejecutable, funciones, clases o variables. Al separar el código en varios archivos, evitamos scripts gigantescos difíciles de mantener.

### Formas de importar módulos:
- **`import modulo`:** Importa el módulo completo. Para usar sus funciones debemos anteponer el nombre del módulo (`modulo.funcion()`).
- **`from modulo import funcion`:** Importa únicamente una función o elemento específico, permitiendo usarlo directamente por su nombre.
- **`import modulo as alias`:** Permite asignar un apodo o nombre corto al módulo para agilizar su llamado en el código.

```python
# Ejemplo de importación y uso
import math

resultado = math.sqrt(25)
print(resultado)  # Salida: 5.0
```

---

## 2. ¿Cómo funciona internamente la búsqueda de Módulos?
Cuando ejecutamos la instrucción `import`, Python busca el archivo siguiendo un orden estricto de rutas definido en la variable `sys.path`:
1. El directorio actual desde donde se está ejecutando el script principal.
2. Las rutas configuradas en las variables de entorno del sistema (`PYTHONPATH`).
3. El directorio de la biblioteca estándar de Python instalada en el equipo.

---

## 3. Paquetes (Packages)
Un paquete es una carpeta que contiene múltiples módulos organizados jerárquicamente. 
- Para que Python reconozca una carpeta como un paquete, tradicionalmente incluye un archivo especial llamado `__init__.py` (que puede estar vacío o contener código de inicialización del paquete).
- Esto nos permite organizar proyectos grandes con estructuras como: `mi_proyecto/paquete/modulo.py`.