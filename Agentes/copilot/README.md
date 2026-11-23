# Guía de Instalación y Uso: VS Code Agents Window y VS Code CLI en Linux

Esta guía documenta cómo instalar la **VS Code CLI independiente** sin pisar el comando `code` del editor gráfico tradicional, y cómo utilizar tanto la interfaz visual de agentes (estilo Cursor) como los servicios de agentes en terminal.

---

## 1. Descarga de la CLI Standalone

1. Ingresa a la página oficial de descargas de Visual Studio Code: [://visualstudio.com](https://://visualstudio.com)
2. En la sección de **CLI**, descarga el paquete correspondiente a tu arquitectura de Linux (por ejemplo, `x64` o `ARM64` en formato `.tar.gz`).
   * *Nota:* Si usas Ubuntu, Debian, Mint o Fedora, elige la versión estándar de Linux (**x64**). La versión *Alpine* está pensada para contenedores minimalistas, aunque funciona en varios sistemas.

---

## 2. Extracción e Instalación sin Conflictos

Por defecto, tanto el editor gráfico como la CLI independiente usan el nombre `code`. Para evitar que la CLI sobrescriba tu comando `code` habitual, la instalaremos como `code-cli`.

1. **Abre la terminal y ve a la carpeta de descargas:**
   ```bash
   cd ~/Descargas
   ```

2. **Extrae el archivo descargado:**
   *(Reemplaza el nombre del archivo por el que hayas descargado)*
   ```bash
   tar -xzf vscode_cli_*.tar.gz
   ```
   Esto extraerá un único archivo binario ejecutable llamado `code`.

3. **Mueve el binario a una ruta global del sistema renombrándolo a `code-cli`:**
   ```bash
   sudo mv ~/Descargas/code /usr/local/bin/code-cli
   ```

4. **Asigna permisos de ejecución y actualiza la caché de comandos:**
   ```bash
   sudo chmod +x /usr/local/bin/code-cli
   hash -r
   ```

---

## 3. Verificación de la Instalación

Comprueba que ambos comandos apuntan a herramientas distintas y funcionan correctamente:

* **Verificar el editor gráfico tradicional:**
  ```bash
  code --version
  ```
* **Verificar la CLI independiente:**
  ```bash
  code-cli --version
  ```

---

## 4. Configuración y Primeros Pasos

### A. Configurar proveedores y modelos de IA
1. Abre la ventana de agentes:
   ```bash
   code --agents
   ```
2. Inicia sesión con tu cuenta de **GitHub** (para usar GitHub Copilot) o ve al icono de **Configuración / Modelos** dentro de la ventana para conectar cuentas externas o claves API (BYOK) como **Claude (Anthropic)** o **Codex / ChatGPT (OpenAI)**.
3. *(Opcional)* Crea un archivo de instrucciones en la raíz de tu proyecto (por ejemplo, `.github/copilot-instructions.md` o archivos `.agent.md`) para definir reglas de estilo, arquitectura y comandos de prueba que los agentes deban respetar.

### B. Configurar la CLI para sesiones remotas (Opcional)
Si vas a usar la CLI en un servidor remoto o contenedor sin interfaz gráfica:
1. Vincula tu cuenta ejecutando:
   ```bash
   code-cli tunnel user login
   ```
2. Sigue el enlace en pantalla e introduce el código de verificación en tu navegador.

---

## 5. Chuleta de Comandos Principales

| Comando | Herramienta | Qué hace |
| :--- | :--- | :--- |
| `code .` | Editor Gráfico | Abre VS Code tradicional en la carpeta actual. |
| `code --agents` | Agents Window | Abre la interfaz visual de agentes (estilo Cursor) para gestionar múltiples tareas en paralelo y revisar *diffs*. |
| `code --agents .` | Agents Window | Abre la ventana de agentes directamente en el proyecto actual. |
| `code-cli agent` | CLI Standalone | Gestiona sesiones y servidores host de agentes en segundo plano desde la terminal. |
| `code-cli tunnel` | CLI Standalone | Crea un túnel seguro para conectarte a tu máquina desde `vscode.dev` o desde otro VS Code. |
| `code-cli serve-web` | CLI Standalone | Levanta una versión web local de VS Code accesible desde el navegador. |
| `code-cli update` | CLI Standalone | Actualiza el binario de la CLI a la última versión disponible. |
