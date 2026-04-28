from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app import schemas, models
from app.services import order_service
from app.dependencies import get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


# Create order
@router.post("/", response_model=schemas.OrderResponse)
def create_order(
    order_data: schemas.OrderCreateIn,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return order_service.create_order(
        db,
        current_user.id,
        order_data
    )


# Get user orders
@router.get("/my-orders", response_model=list[schemas.OrderOut])
def my_orders(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return order_service.get_user_orders(
        db,
        current_user.id
    )