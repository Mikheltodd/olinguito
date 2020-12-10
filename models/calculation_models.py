from pydantic import BaseModel
from datetime import datetime


class CalculationIn(BaseModel):
    username: str
    value: int


class CalculationOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int
