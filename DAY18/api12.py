from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="FastAPI SQLite CRUD")

DB_NAME = "users.db"

# ---------- Database connection ----------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- Create table ----------
@app.on_event("startup")
def startup():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    db.commit()
    db.close()

# ---------- Pydantic Models ----------
class User(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

# ==================================================
# CREATE (POST)
# ==================================================
@app.post("/users")
def create_user(user: User):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        (user.name, user.age)
    )
    db.commit()
    user_id = cursor.lastrowid
    db.close()

    return {"id": user_id, **user.model_dump()}

# ==================================================
# READ ALL (GET)
# ==================================================
@app.get("/users")
def get_users():
    db = get_db()
    rows = db.execute("SELECT * FROM users").fetchall()
    db.close()

    return [dict(row) for row in rows]

# ==================================================
# READ ONE (GET)
# ==================================================
@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = get_db()
    row = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    db.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(row)

# ==================================================
# UPDATE (PUT)
# ==================================================
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    db = get_db()
    existing = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    if existing is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    new_name = user.name if user.name is not None else existing["name"]
    new_age = user.age if user.age is not None else existing["age"]

    db.execute(
        "UPDATE users SET name = ?, age = ? WHERE id = ?",
        (new_name, new_age, user_id)
    )
    db.commit()
    db.close()

    return {"id": user_id, "name": new_name, "age": new_age}

# ==================================================
# DELETE (DELETE)
# ==================================================
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = get_db()
    cursor = db.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    db.commit()
    db.close()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
