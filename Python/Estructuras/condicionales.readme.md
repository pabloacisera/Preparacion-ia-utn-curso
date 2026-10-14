### Estructuras Condicionales en Python

Las estructuras condicionales permiten que nuestro programa tome decisiones y ejecute bloques de código específicos según se cumplan o no determinadas condiciones lógicas.

---

## 1. Conceptos Básicos (`if`, `elif`, `else`)

Permiten evaluar expresiones booleanas (`True` o `False`).

- **`if` (Si):** Evalúa una condición. Si es verdadera, ejecuta el código interno.
- **`elif` (Si no, si):** Evalúa otra condición adicional si la anterior fue falsa.
- **`else` (Si no):** Captura cualquier caso que no haya cumplido las condiciones anteriores.

### Operadores relacionales comunes:
- `==` (Igual a)
- `!=` (Diferente de)
- `>` / `<` (Mayor / Menor que)
- `>=` / `<=` (Mayor o igual / Menor o igual que)

```python
edad = 18

if edad < 12:
    print("Es un niño.")
elif edad < 18:
    print("Es un adolescente.")
else:
    print("Es un adulto.")
```

---

## 2. Nivel Intermedio

### A. Operadores lógicos (`and`, `or`, `not`)
Permiten combinar múltiples condiciones en una sola línea.

- **`and`:** Da verdadero solo si **todas** las condiciones son verdaderas.
- **`or`:** Da verdadero si **al menos una** condición es verdadera.
- **`not`:** Niega o invierte el valor de la condición.

```python
tiene_entrada = True
es_mayor_de_edad = True

if es_mayor_de_edad and tiene_entrada:
    print("Puede ingresar al evento.")
else:
    print("Acceso denegado.")
```

### B. Condicionales anidados
Consiste en colocar un bloque condicional dentro de otro para evaluar casos más específicos de forma jerárquica.

```python
usuario = "admin"
activo = True

if usuario == "admin":
    if activo:
        print("Panel de administración habilitado.")
    else:
        print("Cuenta de administrador inactiva.")
else:
    print("Acceso restringido para usuarios estándar.")
```

### C. Operador ternario (If en una línea)
Una forma abreviada de escribir una estructura simple de `if-else` cuando necesitamos asignar un valor según una condición.

```python
calificacion = 85
resultado = "Aprobado" if calificacion >= 60 else "Reprobado"
print(resultado)  # Salida: Aprobado
```

[Menu Principal](../../README.md)
[Siguiente Lección: Basicos](../bucles/bucles.readme.md)