from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# class OwnerSchema(BaseModel):
#     fullname: str
#     email: EmailStr
#
#
# class OwnerResponse(OwnerSchema):
#     id: int = 1
#
#     class Config:
#         from_attributes = True


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=120)
    last_name: str = Field(min_length=3, max_length=120)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=100)
    # birthday:
    description: str = Field(min_length=3, max_length=250)


# class ContaceUpdateSchema(ContactSchema):
#     completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    # birthday:
    description: str

    class Config:
        from_attributes = True
