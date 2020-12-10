# Miguel: Calculation Model
from datetime import datetime
from pydantic import BaseModel


class CalculationInDB(BaseModel):
    id_calculation: int = 0
    hotel_name: str
    date: datetime = datetime.now()
    expected_profit: float
    incidental_value: float
    h_price: float
    m_price: float
    l_price: float


database_calculations = []
generator = {"id": 0}


def calculate_prices(calculation_in_db: CalculationInDB, hotel_in_db: HotelInDB, u: float, i: float):

    # Calculation Values
    u = u/100
    i = i/100
    l_days = hotel_in_db.l_days
    h_days = hotel_in_db.h_days
    m_days = 365 - l_days - h_days
    l_price = hotel_in_db.operation_cost*(1+i)
    m_price = hotel_in_db.operation_cost*(1+u)
    h_price = ((365-m_days)*m_price - l_days*l_price)/h_days

    # Values for Calculation Results
    generator["id"] = generator["id"] + 1
    hotel_name = hotel_in_db.hotel_name
    calculation_in_db.id_calculation = generator["id"]
    calculation_in_db.hotel_name = hotel_name
    calculation_in_db.expected_profit = u
    calculation_in_db.incidental_value = i
    calculation_in_db.l_price = l_price
    calculation_in_db.m_price = m_price
    calculation_in_db.h_price = h_price

    # Save Calculation Results in DB
    database_calculations.append(calculation_in_db)
    return calculation_in_db
