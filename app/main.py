"""
    Hola esta es una descripcion del modulo sin empezar :)
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Root Endpoint"""
    return "hello world"


def start():
    """Start app function for poetry script"""
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=2,
    )


if __name__ == "__main__":
    start()
