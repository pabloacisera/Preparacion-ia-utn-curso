## Comandos básicos de Bash

| Comando | Acción |
| :--- | :--- |
| `ls` | Lista los directorios y archivos donde estamos parados. |
| `ls -a` | Lista todos los elementos, incluyendo los archivos ocultos. |
| `cd <ruta>` | **Change Directory**: Nos mueve a la ruta especificada. Si se usa `cd` solo, te lleva a tu carpeta de usuario. |
| `cd ..` | Retrocede un nivel (una carpeta hacia atrás). |
| `mkdir <nombre>` | Crea un nuevo directorio o carpeta. |
| `mkdir -p a/b` | Crea una ruta completa de carpetas anidadas de forma recursiva. |
| `touch <archivo>` | Crea un archivo vacío con la extensión indicada. |
| `rm <archivo>` | Borra un archivo de forma permanente. |
| `rm -rf <carpeta>` | Borra una carpeta y todo su contenido de forma recursiva y forzada. |
| `nano <archivo>` | Abre un editor de texto sencillo dentro de la misma terminal. |
| `clear` | Limpia la pantalla de la terminal. |
| `cat <archivo>` | Muestra en pantalla el contenido completo de un archivo. |
| `less <archivo>` | Muestra el contenido de un archivo de forma paginada (ideal para archivos largos). |

---

## Herramientas avanzadas para Scripts

Un script siempre suele escribirse en un archivo porque es una operación que queremos automatizar y reutilizar varias veces. Suelen utilizar las siguientes herramientas:

| Comando / Operador | Acción |
| :--- | :--- |
| `&&` | Concatena comandos. El segundo se ejecuta solo si el primero tiene éxito (ej: `sudo apt update && sudo apt upgrade`). |
| `\|` | **Pipeline o Tubería**: Pasa la salida de un comando como entrada del siguiente. |
| `read -p "<mensaje>" <variable>` | Muestra un mensaje y guarda lo que escriba el usuario en la `<variable>`. |
| `date +"<formato>"` | Muestra la fecha/hora. El formato va pegado al `+`. Ejemplo: `date +"%H-%M-%S"` (Hora-Minuto-Segundo). |
| `>` | Redirecciona la salida de un comando y **sobrescribe** un archivo (ej: `echo "hola" > notas.txt`). |

> ⚠️ **Importante:** Bash requiere que los scripts usen la extensión `.sh`. Además, para poder ser ejecutados, debemos darles permisos de ejecución en la terminal con el comando: `chmod +x <archivo.sh>`. Luego, podemos invocarlo usando `./<archivo.sh>`.

[Siguiente Lección: SSH](../../Ssh/ssh.readme.md)