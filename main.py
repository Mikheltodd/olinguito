# Mauricio & Allison: definir las funciones de la api y sus url
from fastapi.middleware.cors import CORSMiddleware
from db.hotel_db import HotelInDB
from db.hotel_db import get_hotel_info, update_hotel
from db.calculation_db import CalculationInDB
from db.calculation_db import calculate_prices
from models.hotel_models import HotelIn, HotelOut
from models.calculation_models import CalculationIn, CalculationOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()


# @api.post("/hotel/update/")
# async def update_hotel(user_in: HotelIn):

#     return hotel_info


# @api.get("/hotel/details/{hotel_name}")
# async def get_hotel_info(hotel_name: str):

#     return hotel_info


@api.put("/hotel/calculation/")
async def make_calculation(calculation_in: CalculationIn):
    # Consulta del hotel y valores de U e I from CalculationIn
    hotel = get_hotel_info(calculation_in.hotel_name)
    u = calculation_in.expected_profit
    i = calculation_in.incidental_value

    # Validación entradas
    if hotel == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")
    if calculation_in.expected_profit < 0 | | calculation_in.incidental_value < 0:
        raise HTTPException(
            status_code=400, detail="Porcentaje de utilidad y/o Porcentaje de imprevistos no pueden ser negativos")

    # Cálculo de los precios
    calculation_results_db = calculate_prices(
        calculation_in, hotel, u, i)
    calculation_results = CalculationOut(**calculation_results_db.dict())
    return calculation_results
