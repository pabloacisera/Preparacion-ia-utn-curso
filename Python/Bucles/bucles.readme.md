### Bucles `for` en Python

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de texto) o cualquier objeto iterable, ejecutando un bloque de código para cada elemento.

---

## 1. Conceptos Básicos

### A. Iterar sobre secuencias
Permite recorrer elemento por elemento de forma directa sin necesidad de manejar índices manuales.

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

### B. La función `range()`
Se utiliza frecuentemente con bucles `for` cuando queremos repetir una acción un número determinado de veces.
- `range(stop)`: Va de 0 hasta stop - 1.
- `range(start, stop)`: Desde start hasta stop - 1.
- `range(start, stop, step)`: Añade un salto o paso.

```python
for i in range(1, 6):
    print(f"Número: {i}")
```

---

## 2. Nivel Intermedio y Patrones Avanzados

### A. Función `enumerate()`
Permite obtener tanto el índice como el valor de cada elemento de forma simultánea mientras iteramos.

```python
colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")
```

### B. Función `zip()`
Permite recorrer múltiples secuencias o listas en paralelo al mismo tiempo.

```python
nombres = ["Ana", "Carlos", "Lucia"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")
```

### C. Control de bucles (`break`, `continue`, `else`)
- **`break`:** Rompe y finaliza el bucle por completo antes de que termine.
- **`continue`:** Salta la iteración actual y pasa directamente a la siguiente.
- **`else` en bucles:** Se ejecuta cuando el bucle termina de recorrer todo el iterable de forma normal (sin ser interrumpido por un `break`).

```python
for numero in range(1, 6):
    if numero == 3:
        continue  # Salta el número 3
    if numero == 5:
        break     # Sale del bucle al llegar al 5
    print(numero)
```

### D. Comprensión de listas (List Comprehensions)
Una forma elegante, compacta y moderna en Python de crear una nueva lista aplicando una operación o filtro con un `for` en una sola línea.

```python
# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x ** 2 for x in range(1, 6)]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
```

[Menu Principal](../../README.md)
[Siguiente Lección: Basicos](../funciones/funciones.readme.md)