import asyncio
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    # 1. Definimos la ruta base de tu proyecto actual
    base_path = Path("/home/kscod/Practicas/Preparacion-ia-utn-curso")

    # 2. Construimos de forma limpia las rutas del servidor y del ejecutable de Python
    server_path = (
        base_path / "11-ia" / "11-5-rag" / "03-oracle" / "mcp" / "local_server.py"
    )
    venv_python = base_path / "venv" / "bin" / "python3"
    server_dir = base_path / "11-ia" / "11-5-rag" / "03-oracle"

    print(f"Usando Python del entorno: {venv_python}")
    print(f"Cargando servidor desde: {server_path}")

    # 3. Inicializamos el cliente apuntando al binario interno del venv
    client = MultiServerMCPClient(
        {
            "db_queries": {
                "command": str(
                    venv_python
                ),  # <--- Ahora sí ejecutará con tus librerías instaladas
                "args": [str(server_path)],
                "transport": "stdio",
                # ACLARACIÓN: Le indicamos dónde correr para que SQLite cree el .db en la carpeta correcta
                "cwd": str(server_dir),
            }
        }
    )

    # Cargar las herramientas
    tools = await client.get_tools()

    # Revisar que se hayan mapeado correctamente
    print(f"\n¡Éxito! Herramientas encontradas: {len(tools)}")
    for t in tools:
        print(f"-> {t.name}: {t.description[:40]}...")


if __name__ == "__main__":
    asyncio.run(main())
