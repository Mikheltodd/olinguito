# Estefany: definir parámetros de entrada y salida de los cálculos en calculation_models.py
from pydantic import BaseModel
from datetime import datetime


class CalculationIn(BaseModel):
    hotel_name: str
    expected_profit: float
    incidental_value: float


class CalculationOut(BaseModel):
    id_calculation: int
    hotel_name: str
    date: datetime = datetime.now()
    h_price: float
    m_price: float
    l_price: float
