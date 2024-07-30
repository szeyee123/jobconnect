from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    PENDING = "pending"
    CANCELLED = "cancelled"
    PROCESSING = "processing"
    SUCCESS = "success"
    REJECTED = "rejected"

class Application(BaseModel):
    candidate_id: str
    job_id: str
    status: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "candidate_id": "1",
                    "job_id": "1",
                    "status": "pending",
                }
            }


class Job(BaseModel):
    company_id: str
    name: str
    description: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "company_id": "123",
                    "name": "jobname",
                    "description": "jobdescription",
                }
            }
