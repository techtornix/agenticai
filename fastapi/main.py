from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}
# @app.get("/about")
# def root():
#     return "this is about root"

# @app.get("/about/{a}")
# def read_item(a: int):
#     return {"item_id": a}

@app.get("/about")
def root():
    try:
        return {
            "data":"jadyahskd",
            "status":200,
            "message":"success"
        }
    except Exception as e:
        return {"error": str(e)}

