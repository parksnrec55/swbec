import uvicorn
import socket
from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
def read_root():
    return "./src/index.html"

@app.get("/{file}", response_class=FileResponse)
def read_root(file: str):
    return "./src/" + file

@app.get("/data/on_seconds")
def serve_on_seconds():
    return 5

@app.get("/data/off_seconds")
def serve_off_seconds():
    return 5

@app.post("/data/on_seconds")
def set_on_seconds():
    return 5

@app.post("/data/on_seconds")
def set_off_seconds():
    return 5


if __name__ == "__main__":
   uvicorn.run("main:app", host="129.123.134.198", port=8000, reload=True)