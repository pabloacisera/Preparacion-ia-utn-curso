# sqlite3: lightweight local database module
import sqlite3

# typing: native python library to establish complex types
# List: expected variable or output type is a list
# Optional: helps define an implicit None value
from typing import List, Optional

# pydantic: external library for data validation and settings management
from pydantic import BaseModel, Field

# fastmcp: allows creating a python server for our MCP
from fastmcp import FastMCP


# Initialize application and assign a name
my_mcp = FastMCP("mcp:sqlite-user-crud")

# Set the database file name
db_name = "mcp-test-db.db"

# Create a function to initialize the database if it doesn't exist
def init_db():
    """Create database if it does not exist when the server initializes."""
    # Start context manager
    with sqlite3.connect(db_name) as conn:
        # connect returns the connection object to create the intermediary (cursor)
        cursor = conn.cursor()

        # Execute table creation
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            phone TEXT
                        )
                       """)
        conn.commit()

# Run database initialization
init_db()


# Schema validation (data structures)

class UserCreate(BaseModel):
    name: str = Field(..., description="The user's full name")
    email: str = Field(..., description="The user's email address")
    phone: Optional[str] = Field(None, description="The user's phone number")

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The user's full name")
    email: Optional[str] = Field(None, description="The user's email address")
    phone: Optional[str] = Field(None, description="The user's phone number")


# MCP Tool Creation

@my_mcp.tool()
def create_user(user: UserCreate) -> str:
    """Create a new user in the users table."""
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            # Pass the values securely as a tuple in the second argument of execute()
            cursor.execute(
                "INSERT INTO users(name, email, phone) VALUES(?, ?, ?)",
                (user.name, user.email, user.phone)
            )
            conn.commit()
            return f"User successfully created. Assigned ID: {cursor.lastrowid}"
    except sqlite3.IntegrityError as e:
        return f"Error creating user: {str(e)}"


@my_mcp.tool()
def read_users() -> str:
    """Read all users from the database."""
    # Change presentation settings; by default, connection returns tuples like ("john", 25)
    # Using row_factory converts it into a dict-like object to access columns by name
    # This prevents us from needing to know the exact index position
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")

        rows = cursor.fetchall()

        if not rows:
            return "No users found in the database."

        results: List[str] = []
        for row in rows:
            results.append(f"ID: {row['id']} | Name: {row['name']} | Email: {row['email']} | Phone: {row['phone']}")
        return "\n".join(results)


@my_mcp.tool()
def update_user(user_id: int, new_data: UserUpdate) -> str:
    """Update fields of an existing user found by their ID."""
    # model_dump converts the Pydantic object into a dictionary
    # exclude_unset=True ignores fields that were not sent for update
    row_to_update = new_data.model_dump(exclude_unset=True)

    if not row_to_update:
        return "No fields were provided for update."

    # Added a trailing space to prevent SQL syntax errors
    query = "UPDATE users SET " + ", ".join([f"{k} = ?" for k in row_to_update.keys()]) + " WHERE id = ?"

    # Critical fix: Appended the user_id to the values list to match the WHERE clause placeholder
    values = list(row_to_update.values()) + [user_id]

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return f"No user found with ID: {user_id}"

    return f"User with ID = {user_id} successfully updated."


@my_mcp.tool()
def delete_user(user_id: int) -> str:
    """Permanently delete a user from the database by their ID."""
    # Fixed the table name from 'usuarios' to 'users'
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return f"No user found with ID {user_id}."
        return f"User with ID {user_id} successfully deleted."


if __name__ == "__main__":
    my_mcp.run()
