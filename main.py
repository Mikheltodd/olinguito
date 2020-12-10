# Mauricio & Allison: definir las funciones de la api y sus url
from fastapi.middleware.cors import CORSMiddleware
from db.hotel_db import HotelInDB
from db.hotel_db import update_user, get_user
from db.calculation_db import CalculationInDB
from db.calculation_db import save_transaction
from models.hotel_models import HotelIn, HotelOut
from models.calculation_models import CalculationIn, CalculationOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()


@api.post("/hotel/update/")
async def update_hotel(user_in: HotelIn):

    return hotel_info


@api.get("/hotel/details/{hotel_name}")
async def get_hotel_info(hotel_name: str):

    return hotel_info


@api.put("/calculation/")
async def calculate_prices(calculation_in_db: CalculationInDB, hotel_data: HotelInDB, u: float, i: float):
    calculation_results = calculation_results(
        calculation_in_db, hotel_data, u, i)
    return calculation_results
