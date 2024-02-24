from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from datetime import date


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=120)
    last_name: str = Field(min_length=3, max_length=120)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=100)
    birthday: date
    description: str = Field(max_length=250)


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    description: str

    class Config:
        from_attributes = True
