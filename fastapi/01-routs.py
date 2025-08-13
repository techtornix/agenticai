from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    id:int
    name:str
    price:float


app = FastAPI()

@app.get('/')
def read_root():
    return {
        "Hello": "World"
            
            }
@app.get('/user/{id}/{name}/{age}/{city}')
def read_root(id,name,age,city):
    return {
        "id": id,
        "name":name,
        "age":age,
        "city":city
            
            }
@app.get('/data')
def read_root(id:int,name:str,age:int,city:str):
    return {
        "id": id,
        "name":name,
        "age":age,
        "city":city
            
            }

@app.get('/student')
def read_root(item:item):
    return {
        "id" :item.id,
        "name":item.name,
        "price":item.price
    }

