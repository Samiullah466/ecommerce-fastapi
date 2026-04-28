from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserProfileOut(BaseModel):

    id: int
    name: str
    email: EmailStr
    phone: str
    gender: str

    date_of_birth: Optional[datetime]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

    default_shipping_address: Optional[str]
    billing_address: Optional[str]

    class Config:
        from_attributes = True


class UserProfileUpdate(BaseModel):

    name: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None

    date_of_birth: Optional[datetime] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None

    default_shipping_address: Optional[str] = None
    billing_address: Optional[str] = None