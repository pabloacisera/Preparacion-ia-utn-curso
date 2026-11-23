# GITHUB COPILOT

### FUNCIONES

1. AUTOCOMPLETADO

Usamos CTRL + SHIFT + P y activamos Enable Suggestions para que nos aparezcan sugerencias de código mientras escribimos.

Para probarlo podemos crear un archivo de python y escribir una función, por ejemplo:

```python
def suma(a, b):
    return a + b
```

2. CHAT EN LINEA

En vez de escribir a mano le podemos pedir a Copilot que nos genere el código, para eso usamos CTRL + SHIFT + P y activamos Enable Chat. En la conversacion podemos escribirle lo que queremos que haga, por ejemplo:

```
Genera una función que reciba dos números y devuelva su suma. Guardalá en un archivo llamado suma.py y por ultimo ejcuta el archivo para ver el resultado y verifica que el resultado sea correcto.
```

> Cuidar que el chat es en modo "ask" y no "agent". En modo agent levantara servidores mcp y cargara skills que no son necesarias en esta etapa.

> En "Configure tools" podemos activar o desactivar herramientas o mcp vinculados al agente.
