import sqlite3
from contextlib import contextmanager

DB_NAME = "mcp-test-db.db"

@contextmanager
def get_db():
    """Módulo que abre la conexión y entrega el cursor. 
    Maneja el commit y el cierre de forma automática."""
    conn = sqlite3.connect(DB_NAME)
    # Habilitamos Row para acceder a las columnas por nombre (como en read_users)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    try:
        # Entrega el cursor a la función que lo llamó
        yield cursor 
        # Si no hubo errores en la herramienta, hace el commit automático
        conn.commit() 
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

"""
from database import get_db

@my_mcp.tool()
def create_user(user: UserCreate) -> str:
    
    try:
        # Usás tu propio módulo simplificado
        with get_db() as cursor:
            cursor.execute(
                "INSERT INTO users(name, email, phone) VALUES(?, ?, ?)",
                (user.name, user.email, user.phone)
            )
            return f"User successfully created. Assigned ID: {cursor.lastrowid}"
    except Exception as e:
        return f"Error creating user: {str(e)}"

"""
