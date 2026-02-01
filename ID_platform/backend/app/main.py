from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.register import router as register_router
from app.api.auth.login import router as login_router
from app.api.users.me import router as users_router
from app.api.users import router as users_router
from app.db.init_db import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite frontend
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(register_router, prefix="/auth")
app.include_router(login_router, prefix="/auth")
app.include_router(users_router, prefix="/users", tags=["Users"])

app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def home():
    return {"message": "Testing if API is running"}
