# ¿Que es GIT?

Git es un sistema de control de versiones distribuido. Es una herramienta de trazabilidad, que registra cada cambio que ejecutas en un periodo de tiempo.

### Utilidad:
- Historial y auditoria: te permite saber que se cambio, cuando se cambio y quien lo hizo.
- Control de Errores: Si algo rompe tu codigo y trabajo, se puede volver al momento anterior al error, sin tener que empezar desde cero.
- Trabajo colaborativo: permite que multiples personas trabajen sobre el mismo proyecto sin pisarse.
- Experimentación seguro: Gracias al sistema de ramas, se pueden crear bifucarciones, para implementar cambios sin alterar el proyecto original.

## Comandos Básicos:

| Comando | Funcionalidad |
| :---    | :---          |
| Para repositorios locales: || 
| `git init` | Inicia el repositorio en un entorno determinado |
| `git status` | Muestra el estado actual del repositorio, si hay cambios pendientes |
| `git add` | Prepara el archivo para guardado(stage) |
| `git commit -m <descripción>` | Guarda los cambios y los asocia a un 
mensaje |
| `git branch` | Lista ramas de trabajo alterativa y donde estamos posicionados |
| `git branch -c [nombre nueva rama]` | Crea la nueva rama y se posiciona |
| `git merge [nombre rama]` | Fusiona a la rama especifica en la rama donde estamos posicionados |
| `git switch [nombre rama]` | Cambio entre ramas |
| `git restore --staged archivo.ext` | Saca el archivo del area de preparación |
| `git restore archivo.txt` | Borra los cambios en el archivo | 
| Para moverse en el tiempo: ||
| `git log --oneline` | Muestra una lista de los commits en orden cronologico inverso |
| `git checkout [hash del commit]` | Nos lleva el estado del proyecto en ese commit | 
| `git switch --detach [hash]` | HEAD desacoplado | 
| `git show [hash-antiguo]:archivo.ext` | Solo muestra ese archivo en ese momento |
| `git diff [hash-antiguo]` | Estando para en el main, podemos ver la diferencia del proyecto actual y de como era en el momento del commit |
| `git diff [hash-antiguo] -- archivo.ext` | Vemos como un solo archivo |
| Para repositorios remotos ||
| `git clone` | Descarga una copia de un repositorio remoto existente |
| `git push` | Empuja los cambios al remositorio remoto |
| `git pull` | Descarga cambios mas recientes del repositorio remoto |

> ⚠️ **RECOMENDACIÓN:** Si vas a ir atrás en el tiempo con intenciones de modificar algo, hacelo **siempre desde una rama nueva**. Si ejecutás cambios en modo *HEAD desacoplado* (detached HEAD), al salir de ese estado los cambios se pierden o es extremadamente difícil recuperarlos.
> 
> 🛠️ **Ejemplo práctico:** Descubrimos que hace dos semanas cometimos un error que arrastra a toda la configuración actual. El primer paso es aislar el problema creando la rama en ese punto del pasado:
> `git switch -c nombre-nueva-rama [hash-antiguo]`
> 
> 🛑 **El dilema de la fusión:** Una vez terminadas las modificaciones, es hora de traer esos cambios a la rama principal (`main`). Si mergeamos directamente con un `git merge` tradicional, probablemente tengamos conflictos de fusión porque estamos intentando acoplar código viejo al nuevo (sujeto a análisis del estado de los archivos).
> 
> ✨ **Posibles soluciones según lo que necesites lograr:**
> 
> 1. **Inyectar solo la solución quirúrgicamente:** Si queremos traer *únicamente* el parche de la rama creada al código actual, nos paramos en la rama principal y ejecutamos `git cherry-pick [hash-commit-de-reparacion]`. Esto copia exclusivamente el código que modificaste en ese commit específico sin arrastrar el resto de los archivos viejos de hace dos semanas.
> 
> 2. **Reescribir la historia (Rebase):** Ejecutar `git rebase main`. Literalmente mueve la base del tiempo. **Ojo:** esto no se hace parado desde `main` como en el caso anterior, sino que se ejecuta *desde la rama que creaste en el pasado*. Lo que hace es arrastrar tu commit de reparación hacia el presente, tomándolo como si lo hubieras programado hoy sobre el `main` o sobre tu rama de trabajo moderna.
> 
> 3. **Destruir el presente (Reset Hard):** Si te encontrás en otro supuesto donde **no te importa perder** todo lo que se hizo desde el error hasta el presente, te parás en main y tirás `git reset --hard [hash-antiguo]`. Esto hace que el proyecto viaje en el tiempo de forma destructiva hacia ese commit, eliminando las últimas dos semanas de trabajo por completo.

### Práctica:

> Los ejercicios incluyen la creacion del/los documento/s necesarios para emular los ejercicios.

- Ejercicio 1: Inspección y ramificación del pasado (Básico)
Viajarás a un commit viejo para ver cómo estaba el proyecto antes, experimentarás el estado desacoplado y crearás una rama desde ahí para dejar el código protegido.
- Ejercicio 2: El injerto de código con Cherry-Pick (Intermedio)
Simularás que encontraste un error en un archivo de hace dos semanas. Lo vas a solucionar creando una rama en el pasado y usarás cherry-pick desde main para traerte únicamente esa solución.
- Ejercicio 3: El descarte total con Reset y Rebase (Avanzado)
Simularás que todo lo que hiciste en las últimas dos semanas estuvo mal y querés borrarlo para arrancar de cero desde un commit viejo usando reset --hard. Luego, reordenarás tu rama de trabajo con rebase

[Siguiente Lección: Github](../07-github/github.readme.md)