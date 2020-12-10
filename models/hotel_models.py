# Estefany: definir parámetros de entrada y salida de los hoteles en hotel_models.py
from pydantic import BaseModel


class HotelIn(BaseModel):
    name: str
    n_rooms: int
    operation_cost: float
    l_days: int
    h_days: int


class HotelOut(BaseModel):
    name: str
    n_rooms: int
    operation_cost: float
    l_days: int
    h_days: int
