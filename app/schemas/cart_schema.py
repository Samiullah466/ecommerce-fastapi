from pydantic import BaseModel
from app.schemas.product_schema import ProductOut


class CartAddIn(BaseModel):

    product_id: int
    quantity: int


class CartItemOut(BaseModel):

    id: int
    product: ProductOut
    quantity: int

    class Config:
        from_attributes = True