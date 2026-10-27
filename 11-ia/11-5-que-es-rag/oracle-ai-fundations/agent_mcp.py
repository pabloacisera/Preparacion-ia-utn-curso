import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv(find_dotenv())
groq_model = os.getenv("GROQ_MODEL")

model = init_chat_model(groq_model, model_provider="groq")  # type: ignore


async def main():
    base = Path("/home/kscod/Practicas/Preparacion-ia-utn-curso")
    server_path = (
        base / "11-ia" / "11-5-que-es-rag" / "oracle-ai-fundations" / "server.py"
    )
    server_dir = base / "11-ia" / "11-5-que-es-rag" / "oracle-ai-fundations"
    venv_python = base / "venv" / "bin" / "python3"

    client = MultiServerMCPClient(
        {  # type: ignore
            "database_methods": {
                "command": str(venv_python),
                "args": [str(server_path)],
                "transport": "stdio",
                "cwd": str(server_dir),
            },
            "github_mcp": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "transport": "stdio",
                "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")},
            },
        }
    )

    # Obtenemos y listamos las herramientas de ambos servidores MCP con éxito
    tools = await client.get_tools()
    print(f"\n¡Éxito! Total de herramientas mapeadas: {len(tools)}")
    for t in tools:
        print(f"-> [{t.name}] {t.description[:50]}...")

    agent = create_agent(  # type: ignore
        model=model,
        tools=tools,
        system_prompt=(
            "You are a versatile assistant with access to the user's local database and GitHub tools through MCP. "
            "Help the user by combining both sources of information if needed. "
            "Respond clearly and concisely in plain text, without using mathematical notation."
        ),
    )

    # 1. Definimos la función como async para usar await agent.ainvoke
    async def run_agent(question: str):
        print("=" * 50)
        print(f"Pregunta: {question}")
        print("=" * 50)

        # 2. Usamos ainvoke en lugar de invoke para soportar herramientas async de MCP
        results = await agent.ainvoke({"messages": [("human", question)]})

        # 3. Iteramos sobre results["messages"] en lugar de results directamente
        for msg in results["messages"]:
            if msg.type == "human":
                continue
            elif msg.type == "ai" and getattr(msg, "tool_calls", None):
                for call in msg.tool_calls:
                    print(f"[RAZONAMIENTO]: usa {call['name']} con {call['args']}")
            elif msg.type == "tool":
                print(f"[OBSERVA] - resultado: {msg.content} ")
            elif msg.type == "ai" and msg.content:
                print(f"[RESPONDE]: {msg.content}")

    # 4. Llamamos a las funciones con await
    await run_agent(
        "Listame los usuarios que hay en la base de datos. Si no encuentras datos, vas a crear un usuario y luego mostrarlo. El nuevo usuario será Pablo Cisera, con email pablo@example.com y telefono 3482278591. Si el usuario ya existe inventa uno"
    )
    print("")
    print("*" * 50)
    print("")
    await run_agent(
        "Listame los repositorio que tengo publicos en mi plataforma de github, y cuenta los repositorios que tengo como privado."
    )


if __name__ == "__main__":
    asyncio.run(main())
