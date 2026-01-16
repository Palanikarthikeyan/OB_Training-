from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="FastAPI + SQLite Example")

DB_NAME = "users.db"

# ---------- Database helper ----------
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- Create table on startup ----------
@app.on_event("startup")
def startup():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- Pydantic model ----------
class User(BaseModel):
    name: str
    age: int

# ---------- POST: Create user ----------
@app.post("/users")
def create_user(user: User):
    if user.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be positive")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        (user.name, user.age)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return {"id": user_id, "name": user.name, "age": user.age}

# ---------- GET: All users ----------
@app.get("/users")
def get_users():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return [dict(row) for row in rows]

# ---------- GET: User by ID ----------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(row)
