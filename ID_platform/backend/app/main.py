from fastapi import FastAPI
from app.api.auth.register import router as register_router

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Bytewatchers API running"}
app.include_router(register_router, prefix="/auth")
