# Fundamentos de Python

**Filosofía y Legibilidad**: 

Python prioriza la legibilidad humana por encima de la optimización extrema del ordenador. "El codigo se lee mucho mas de lo que se escribe". Bajo esta premisa, no se usan simbolos complejos como {} o ; que si estan presentes y son obligtorios en la mayoria de los lenguajes, por el contrario se basa en la estructuración de la sintaxis.

**Tipado Dinamico y "Duck Typing"**:

- Tipado dinámico: Las variables no tiene un tipo de dato fijo, una variable que originalmente contiene una cadena de caráteres, en la siguiente linea puede ser utilizada para guardar un número.

- Duck Typing: "Si camina como pato...". A python no le importa la etiqueta, sino los métodos y atributos que poseé.

**Naturleza Interpretada y el motor(CPython)**:

Python es un lenguaje interpretado, lo que quiere decir que no se compila a binario(como el caso de c, c++, go, java) sino que primero se traduce y un formato intermedio llamado bytecode, y una maquina virtual(cpython) lee y ejecuta ese codigo.

**Todo es un objeto**:

Numeros, strings o funciones, son objetos. Esto hace que todas la sintaxis se pueda mezclar y fusionar para obtener datos mas complejos, se puede pasar una funcion dentro de una variable sin problemas.

**Gestion automatica de memoria**:

En lenguajes como c el programador tiene que preocuparse por liberar la memoria una vez que esta ya no sea utilizada, python rastrea automaticamente objetos que ya no son utilizados.

**Baterias Incluidas**:

Python viene con una gran cantidad de libreria nativa, que permite obtener información del dispositivo, comunicarse con otros dispositivos, ejecutar opearciones matematicas, manipular documentos, etc.

[Menu Principal](../../README.md)
[Siguiente Lección: Basicos](../Basicos/basicos.python.readme.md)