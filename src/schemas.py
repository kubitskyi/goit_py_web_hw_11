from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class ContactSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: Optional[date]
    additional_info: Optional[str]

    class Config:
        from_attributes = True


class ContactBirthday(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthday: date