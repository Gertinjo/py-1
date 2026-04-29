from pydantic import BaseModel , conint , constr
from typing import Optional

# class User (BaseModel):
#     id: int
#     name: str
#     age: float
#     email: str
#
# user = User (id= 1 , name="Gerti" , age=12.5 , email="gerti@gmail.com")
#
# print(user)


class User (BaseModel):
    id: int
    name: str
    age: float = 0.0
    email: str = "test@gmail.com"

user1 = User (id= 1 , name="Gerti" )

print(user1)