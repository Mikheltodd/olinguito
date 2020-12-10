from pydantic import BaseModel


class HotelIn(BaseModel):
    username: str
    password: str


class HotelOut(BaseModel):
    username: str
    balance: int
