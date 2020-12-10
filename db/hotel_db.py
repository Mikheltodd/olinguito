from typing import Dict
from pydantic import BaseModel


class HotelInDB(BaseModel):
    username: str
    password: str
    balance: int


database_users = Dict[str, HotelInDB]
database_users = {
    "camilo24": HotelInDB(**{"username": "camilo24",
                             "password": "root",
                             "balance": 12000}),
    "andres18": HotelInDB(**{"username": "andres18",
                             "password": "hola",
                             "balance": 34000}),
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None


def update_user(user_in_db: HotelInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
