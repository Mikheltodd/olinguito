# Miguel: Calculation Model
from datetime import datetime
from pydantic import BaseModel
from db.hotel_db import HotelInDB
from db.hotel_db import update_hotel


class CalculationInDB(BaseModel):
    id_calculation: int = 0
    hotel_name: str
    date: datetime = datetime.now()
    expected_profit: float
    incidental_value: float
    h_price: float = 0
    m_price: float = 0
    l_price: float = 0


database_calculations = []
generator = {"id": 0}


def calculate_prices(calculation_in_db: CalculationInDB, hotel_in_db: HotelInDB):

    # Calculation Values
    generator["id"] = generator["id"] + 1
    calculation_in_db.id_calculation = generator["id"]
    u = calculation_in_db.expected_profit/100
    i = calculation_in_db.incidental_value/100
    l_days = hotel_in_db.l_days
    h_days = hotel_in_db.h_days
    m_days = 365 - l_days - h_days
    operation_cost = (hotel_in_db.total_operation_cost/hotel_in_db.n_rooms)/365
    l_price = operation_cost*(1+i)
    m_price = operation_cost*(1+u)
    h_price = ((365-m_days)*m_price - l_days*l_price)/h_days

    # Values for Calculation Results & Hotel

    calculation_in_db.l_price = l_price
    calculation_in_db.m_price = m_price
    calculation_in_db.h_price = h_price
    hotel_in_db.l_price = l_price
    hotel_in_db.m_price = m_price
    hotel_in_db.h_price = h_price

    update_hotel(hotel_in_db)

    # Save Calculation Results in DB
    database_calculations.append(calculation_in_db)
    return calculation_in_db


def get_calculations_list(hotel_name: str):
    calculations = []
    for cal in database_calculations:
        if cal.hotel_name == hotel_name:
            calculations.append(cal)
    return calculations


def get_calculation_hotels():
    return database_calculations
