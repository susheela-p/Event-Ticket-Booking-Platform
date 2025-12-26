from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.schemas import Signup, Login
from app.auth import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/signup")
def signup(user: Signup):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "INSERT INTO users (email, password, role) VALUES (%s, %s, %s)",
        (user.email, hash_password(user.password), user.role)
    )

    db.commit()
    cur.close()
    db.close()
    return {"message": "Signup successful"}

@router.post("/login")
def login(data: Login):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM users WHERE email=%s", (data.email,))
    user = cur.fetchone()

    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"id": user["id"], "role": user["role"]})
    return {"access_token": token}
