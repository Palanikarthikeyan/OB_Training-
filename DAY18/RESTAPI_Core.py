from fastapi import FastAPI, HTTPException
from database import get_db, create_table
from models import UserCreate, UserUpdate

app = FastAPI(title="User Management API")

# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def startup():
    create_table()

# -----------------------------
# CREATE User
# -----------------------------
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (user.name, user.email, user.age)
        )
        db.commit()
    except Exception:
        raise HTTPException(status_code=400, detail="Email already exists")
    finally:
        db.close()

    return {"message": "User created successfully"}

# -----------------------------
# READ All Users
# -----------------------------
@app.get("/users")
def get_users():
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    db.close()
    return [dict(u) for u in users]

# -----------------------------
# READ Single User
# -----------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(user)

# -----------------------------
# UPDATE User
# -----------------------------
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    db = get_db()
    existing = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    if not existing:
        raise HTTPException(status_code=404, detail="User not found")

    name = user.name or existing["name"]
    age = user.age or existing["age"]

    db.execute(
        "UPDATE users SET name = ?, age = ? WHERE id = ?",
        (name, age, user_id)
    )
    db.commit()
    db.close()

    return {"message": "User updated successfully"}

# -----------------------------
# DELETE User
# -----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = get_db()
    cur = db.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    db.commit()
    db.close()

    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
