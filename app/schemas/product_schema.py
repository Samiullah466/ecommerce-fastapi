from pydantic import BaseModel, Field
from typing import Optional


class ProductIn(BaseModel):

    title: str = Field(..., min_length=1, max_length=100)

    description: str = Field(..., min_length=1)

    price: float = Field(..., gt=0)

    quantity: Optional[int] = Field(0, ge=0)


class ProductUpdate(BaseModel):

    title: Optional[str] = Field(None, min_length=1, max_length=100)

    description: Optional[str] = Field(None, min_length=1)

    price: Optional[float] = Field(None, gt=0)

    quantity: Optional[int] = Field(None, ge=0)


class ProductOut(BaseModel):

    id: int
    title: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True