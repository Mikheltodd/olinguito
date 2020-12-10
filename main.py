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


@api.post("/user/auth/")
async def auth_user(user_in: HotelIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}


@api.get("/user/balance/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out


@api.put("/user/transaction/")
async def make_transaction(transaction_in: CalculationIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400, detail="Sin fondos suficientes")
    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)
    transaction_in_db = TransactionInDB(
        **transaction_in.dict(), actual_balance=user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)
    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out
