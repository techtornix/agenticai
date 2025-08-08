from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}
@app.get("/about")
def root():
    return "this is about root"

@app.get("/about/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/about")
def root():
    return {"data": "this is post method about page"}