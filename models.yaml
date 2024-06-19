from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
