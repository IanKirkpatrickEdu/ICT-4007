from fastapi import FastAPI
from loguru import logger

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Hello, World!")
    return {"message": "Hello, World!"}

@app.get("/greet")
def read_greeting():
    logger.info("Hello, Replit!")
    return {"message": f"Hello, Replit!"}

@app.get("/greet/{name}")
def read_greeting_by_name(name: str):
    logger.info("Hello, Replit!")
    return {"message": f"Hello, {name}!"}