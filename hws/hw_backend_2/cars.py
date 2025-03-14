from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Car(BaseModel):
    id: int
    name: str
    subclass: str
    year: int

cars = [
        Car(id=1, name='Toyota', subclass='Camry 70', year=2019),
        Car(id=2, name='Toyota', subclass='Camry 55', year=2012),
        Car(id=3, name='Toyota', subclass='Camry 80', year=2022),
        Car(id=4, name='Toyota', subclass='Prado 150', year=2008),
        Car(id=5, name='Lexus', subclass='LX 570', year=2015)
    ]

@app.get("/cars/", response_model=List[Car])
async def cars_pagination(page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    return cars[offset : offset + limit]


@app.get("/cars/{id}", response_model=Car)
async def get_car_id(id: int):
    car = next((car for car in cars if car.id == id), None)

    if car is None:
        raise HTTPException(status_code=404, detail="Not found")

    return car