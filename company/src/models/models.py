from enum import Enum
from pydantic import BaseModel


class Company(BaseModel):
    name: str
    description: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "name": "companyname",
                    "description": "companydescription",
                    "email": "email",
                }
            }


class CompanyLogin(BaseModel):
    email: str
    password: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "email": "email",
                    "password": "anything",
                }
            }
        
class User(BaseModel):
    userId: str
    role: str

    class Config:
        orm_mode = True