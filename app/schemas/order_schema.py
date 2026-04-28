from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class OrderItemIn(BaseModel):

    product_id: int
    quantity: int
    price_per_item: float


class OrderCreateIn(BaseModel):

    total_price: Optional[float] = None
    items: List[OrderItemIn]


class OrderItemOut(BaseModel):

    id: int
    product_id: int
    product_title: str
    quantity: int
    price_per_item: float
    total_item_price: float

    class Config:
        from_attributes = True


class OrderOut(BaseModel):

    id: int
    user_id: int
    total_price: float
    created_at: datetime
    order_items: List[OrderItemOut]

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):

    msg: str
    order_id: int