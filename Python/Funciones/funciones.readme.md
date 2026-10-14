### Funciones en Python

Una función es un bloque de código reutilizable diseñado para realizar una tarea específica. Ayudan a organizar el código, evitar la repetición (principio DRY - *Don't Repeat Yourself*) y modularizar los programas.

---

## 1. Conceptos Básicos (`def`)

Se definen utilizando la palabra reservada `def`, seguida del nombre de la función, paréntesis y dos puntos (`:`).

- **Parámetros:** Variables locales que la función espera recibir al ser invocada.
- **Argumentos:** Los valores reales que se le envían a la función cuando se la llama.
- **`return`:** Permite que la función devuelva un resultado hacia afuera y finalice su ejecución.

```python
# Definición básica con retorno
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función
suma_total = sumar(5, 3)
print(suma_total)  # Salida: 8
```

---

## 2. Nivel Intermedio

### A. Argumentos por defecto y nombrados
Podemos establecer valores predeterminados para los parámetros, de modo que si el usuario no los pasa, la función use ese valor por defecto. También se pueden pasar argumentos indicando explícitamente el nombre del parámetro.

```python
def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}!"

print(saludar("Carlos"))                     # Usa el valor por defecto: "Hola, Carlos!"
print(saludar(nombre="Ana", mensaje="Buen día")) # Argumentos nombrados
```

### B. Argumentos arbitrarios (`*args` y `**kwargs`)
Permiten recibir una cantidad indefinida de argumentos sin necesidad de definir un límite estricto de parámetros.

- **`*args`:** Recibe múltiples argumentos posicionales en forma de **tupla**.
- **`**kwargs`:** Recibe múltiples argumentos con clave-valor en forma de **diccionario**.

```python
# Usando *args para sumar múltiples números
def sumar_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3, 4, 10))  # Salida: 20


# Usando **kwargs para datos de perfil
def mostrar_perfil(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_perfil(nombre="Lucia", rol="Developer", edad=28)
```

### C. Ámbito de las variables (Scope)
- **Variables locales:** Creadas dentro de una función; solo existen y pueden usarse dentro de ella.
- **Variables globales:** Definidas fuera de cualquier función; pueden ser leídas en todo el script.

### D. Funciones Lambda (Anónimas)
Funciones pequeñas de una sola línea que não necesitan la palabra `def`. Se usan frecuentemente para operaciones rápidas u ordenamientos.

```python
# Función lambda que multiplica por 2 un número
multiplicar_por_dos = lambda x: x * 2
print(multiplicar_por_dos(5))  # Salida: 10
```