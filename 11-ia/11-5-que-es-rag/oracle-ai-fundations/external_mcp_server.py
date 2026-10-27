import os
import asyncio
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
github_token = os.getenv("GITHUB_TOKEN")


async def main():
    # 1. Inicializamos el cliente apuntando al binario interno del venv
    client = MultiServerMCPClient(
        {  # type: ignore
            "github": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "transport": "stdio",
                "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")},
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
