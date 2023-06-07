import uvicorn
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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)