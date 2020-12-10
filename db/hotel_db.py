from typing import Dict
from pydantic import BaseModel


class HotelInDB(BaseModel):
    name: str
    n_rooms: int
    operation_cost: float 
    l_days: int 
    h_days: int


 '''    username: str
    password: str
    balance: int '''

database_hotels=Dict[str,HotelInDB]
database_hotels={
    "Hotel1": HotelInDB(**{"name":"Hotel1",
                            "n_rooms": 20,
                            "operation_cost": 15000,
                            "l_days":100,
                            "h_days":80}),
    "Hotel2": HotelInDB(**{"name":"Hotel2",
                            "n_rooms": 30,
                            "operation_cost": 20000,
                            "l_days":150,
                            "h_days":90}),
}


def get_hotel(name: str):
    if name in database_hotels.keys():
        return database_hotels[name]
    else:
        return None


def update_hotel(hotel_in_db: HotelInDB):
    database_hotels[hotel_in_db.name] = user_in_db
    return hotel_in_db
    
