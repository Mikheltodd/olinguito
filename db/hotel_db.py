# Luis: completar el módulo hotel_db
from typing import Dict
from pydantic import BaseModel


class HotelInDB(BaseModel):
    # Atributos del Hotel


database_hotels = Dict[str, HotelInDB]
database_hotels = {
    # Hotel de prueba: olinguito
    "olinguito": HotelInDB(**{}),
}


def get_hotel_info(hotel_name: str):
    # retornar datos del hotel
    return hotel_name


def update_hotel(hotel_in_db: HotelInDB):
    # actualizar datos del hotel
    return hotel_in_db
