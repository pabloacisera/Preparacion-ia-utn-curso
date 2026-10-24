## Powershell

Es el intreprete de comandos de la terminal de windows. La ultima versión de shell es la 7 o superior. 

Vamos a ejecutar <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="#0078D4" style="height: 1.2em; vertical-align: middle;"><!--!Font Awesome Free v7.3.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2026 Fonticons, Inc.--><path d="M96 157.7L279.6 132.4L279.6 309.8L96 309.8L96 157.7zM96 482.3L279.6 507.6L279.6 332.4L96 332.4L96 482.3zM299.8 510.3L544 544L544 332.4L299.8 332.4L299.8 510.3zM299.8 129.7L299.8 309.8L544 309.8L544 96L299.8 129.7z"/></svg> Windows y escribimos `Powershell`

Si el icono es celeste, tenemos un version vieja. Vamos a abrir la `Microsoft Store` y buscamos `Microsoft Powershell`

Si no podemos acceder a la tienda podemos usar el gestor de paquetes de windows: `winget install --id Microsoft.PowerShell --source winget
`

Si sucede que el sistema de descarga de paquetes esta desactivado primero debemos ejecutar:

```Powershell
# Comprobar el estado del servicio
Get-Service AppXSvc

# Si está detenido o deshabilitado, forzar su inicio en modo automático
Set-Service AppXSvc -StartupType Automatic
Start-Service AppXSvc

```

[Siguiente Lección: Configuracion incial de dispositivo(laptop)](../00-configuracion-inicial/00-1-laptop/install.md)

[Siguiente Lección: Configuracion incial de dispositivo(smartphone)](../00-configuracion-inicial/00-2-android/install.md)