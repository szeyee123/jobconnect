from enum import Enum
from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    description: str
    email: str
    work_experience: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "name": "candidatename",
                    "description": "candidatedescription",
                    "email": "email",
                    "work_experience": "workexperience",
                }
            }

class CandidateLogin(BaseModel):
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