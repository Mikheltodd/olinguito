from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str

database_users = Dict[str, UserInDB]
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24","password":"root"}),
    "andres18": UserInDB(**{"username":"andres18", "password":"hola"}),
    "eslunap19": UserInDB(**{"username":"eslunap19","password":"123456"})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db:UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db