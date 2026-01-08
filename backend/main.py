from fastapi import FastAPI
from api.routes import chat

app = FastAPI()

app.include_router(chat.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Fruit API is running"}