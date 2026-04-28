from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app import schemas, models
from app.services import cart_service
from app.dependencies import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


# Add to cart
@router.post("/")
def add_to_cart(
    item: schemas.CartAddIn,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return cart_service.add_to_cart(db, current_user.id, item)


# View cart
@router.get("/", response_model=list[schemas.CartItemOut])
def view_cart(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return cart_service.get_cart(db, current_user.id)


# Delete cart item
@router.delete("/{item_id}")
def delete_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return cart_service.remove_from_cart(
        db,
        current_user.id,
        item_id
    )


# Increment / Decrement quantity
@router.patch("/{item_id}/quantity")
def update_cart_quantity(
    item_id: int,
    action: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return cart_service.update_cart_quantity(
        db,
        current_user.id,
        item_id,
        action
    )