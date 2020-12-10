# Estefany: definir parámetros de entrada y salida de los hoteles en hotel_models.py
from pydantic import BaseModel


class HotelIn(BaseModel):
<<<<<<< HEAD


class HotelOut(BaseModel):
=======
    name: str
    n_rooms: int 
    operation_cost: float 
    l_days: int 
    h_days: int 



class HotelOut(BaseModel):
    name: str
    n_rooms: int 
    operation_cost: float 
    l_days: int 
    h_days: int 
    
>>>>>>> 4da846dd214ecf2b2cce9a6ecde9054062a069ca
