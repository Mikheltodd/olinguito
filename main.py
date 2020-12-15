# Mauricio & Allison: definir las funciones de la api y sus url
from fastapi.middleware.cors import CORSMiddleware

from db.hotel_db import HotelInDB
from db.hotel_db import get_hotel_info, update_hotel, get_all_hotels

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
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "https://localhost", "http://localhost:8080", "https://olinguito-app.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.get("/hotel/details/{hotel_name}")
async def get_hotel(hotel_name: str):
    hotel_in_db = get_hotel_info(hotel_name)
    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")

    hotel_out = HotelOut(**hotel_in_db.dict())

    return hotel_out


@api.put("/hotel/calculation/")
async def make_calculation(calculation_in: CalculationIn):
    # Consulta del hotel y valores de U e I from CalculationIn
    hotel = get_hotel_info(calculation_in.hotel_name)
    u = calculation_in.expected_profit
    i = calculation_in.incidental_value

    # Validación entradas
    if hotel == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")
    if calculation_in.expected_profit < 0 or calculation_in.incidental_value < 0:
        raise HTTPException(
            status_code=400, detail="Porcentaje de utilidad y/o Porcentaje de imprevistos no pueden ser negativos")

    # Cálculo de los precios
    calculation_results_db = CalculationInDB(**calculation_in.dict())

    calculation_results_db = calculate_prices(calculation_results_db, hotel)
    calculation_out = CalculationOut(**calculation_results_db.dict())
    return calculation_out


@api.get("/hotel/list")
async def list_hotels():
    hotels_in_db = get_all_hotels()
    hotels_out = []
    for hotel in hotels_in_db:
        hotel_out = HotelOut(**hotel.dict())
        hotels_out.append(hotel_out)

    return hotels_out
