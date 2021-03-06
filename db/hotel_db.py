# Luis: completar el módulo hotel_db
from typing import Dict
from pydantic import BaseModel


class HotelInDB(BaseModel):
    # Atributos del Hotel
    name: str
    n_rooms: int
    total_operation_cost: float
    l_days: int
    h_days: int
    h_price: float = 0
    m_price: float = 0
    l_price: float = 0


database_hotels = Dict[str, HotelInDB]
database_hotels = {
    # Hotel de prueba: olinguito
    "olinguito": HotelInDB(**{"name": "olinguito",
                              "n_rooms": 25,
                              "total_operation_cost": 140875000,
                              "l_days": 120,
                              "h_days": 100, "l_price": 0,
                              "m_price": 0,
                              "h_price": 0}),
    "Hotel1": HotelInDB(**{"name": "Hotel1",
                           "n_rooms": 20,
                           "total_operation_cost": 120450000,
                           "l_days": 100,
                           "h_days": 80, "l_price": 0,
                           "m_price": 0,
                           "h_price": 0}),
    "Hotel2": HotelInDB(**{"name": "Hotel2",
                           "n_rooms": 30,
                           "total_operation_cost": 189435000,
                           "l_days": 150,
                           "h_days": 90, "l_price": 0,
                           "m_price": 0,
                           "h_price": 0}),
}


def get_hotel_info(hotel_name: str):
    if hotel_name in database_hotels.keys():
        return database_hotels[hotel_name]
    else:
        return None


def create_hotel(hotel_in: HotelInDB):
    if hotel_in.name in database_hotels:
        return False
    else:
        database_hotels[hotel_in.name] = hotel_in
        return True


def update_hotel(hotel_in_db: HotelInDB):
    database_hotels[hotel_in_db.name] = hotel_in_db
    return hotel_in_db

# Devuelve los valores de lista de hoteles


def get_all_hotels():
    return database_hotels.values()
