# Fundamentos de Programación

### ¿Que es un sistema operativo?

### Virtual Environment(Entorno Virtual o venv)

Es igual a decir Labortaorio personal, o entorno aislado, o entorno de prueba. Un conjunto de herramientas, almacenadas o empaquetadas en lugar, que viene a conformar el ecosistema de un proyecto.

Imagina que tu computadora es un gran edificio. Si instalas todas tus librerías de Python de forma global, es como si todos tus proyectos compartieran una única mesa de trabajo gigante. Si un proyecto ensucia la mesa o cambia las herramientas, arruina los proyectos de los demás.
Crear un venv es como construir una habitación separada con su propia mesa y sus propias herramientas exclusivas para un proyecto específico. Nada de lo que pase ahí dentro afectará al resto del edificio (tu computadora).

*Contenido Básico de un venv*

1. Una copia (o enlace) del ejecutable de Python: Así, ese entorno usa una versión fija de Python.
2. Su propio gestor de paquetes (pip): Todas las librerías que descargues (como pandas, flask o scikit-learn) se guardarán estrictamente dentro de esa carpeta.
3. Scripts de activación: Archivos especiales que le dicen a tu terminal: "Oye, a partir de ahora, cuando use Python, búscalo dentro de esta carpeta y no en el sistema global".

