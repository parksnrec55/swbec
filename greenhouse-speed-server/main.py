import uvicorn
import socket
from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
def read_root():
    return "/home/parker/code/swbec/greenhouse-speed-server/src/index.html"

@app.get("/{file}", response_class=FileResponse)
def read_root(file: str):
    return "/home/parker/code/swbec/greenhouse-speed-server/src/" + file

@app.get("/data/on_seconds")
def serve_on_seconds():
    return 5

@app.get("/data/off_seconds")
def serve_off_seconds():
    return 10

@app.post("/data/set_on_seconds")
def set_on_seconds(seconds: int = 5):
    return {
        "status": "success",
        "on_seconds": seconds
    }

@app.post("/data/set_on_seconds")
def set_off_seconds(seconds: int = 10):
    return {
        "status": "success",
        "on_seconds": seconds
    }


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)