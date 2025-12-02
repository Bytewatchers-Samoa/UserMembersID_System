from fastapi import FastAPI
from app.api.auth.register import router as register_router
from app.api.auth.login import router as login_router

app = FastAPI()

app.include_router(register_router, prefix="/auth") #POST /auth/register
app.include_router(login_router, prefix="/auth")    #POST /auth/login

@app.get("/")
def home():
    return {"message": "Bytewatchers API running"}
