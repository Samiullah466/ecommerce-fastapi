from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app import schemas, models
from app.services import product_service
from app.dependencies import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])


# Add product
@router.post("/", response_model=schemas.ProductOut)
def add_product(
    payload: schemas.ProductIn,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return product_service.create_product(db, payload, current_user.id)


# View products
@router.get("/", response_model=list[schemas.ProductOut])
def list_products(
    db: Session = Depends(get_db),
    sort_by: str = Query(default="id"),
    order: str = Query(default="asc")
):
    return product_service.get_all_products(db, sort_by, order)


# Delete product
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return product_service.delete_product(db, product_id, current_user.id)


# Update product
@router.put("/{product_id}", response_model=schemas.ProductOut)
def update_product(
    product_id: int,
    payload: schemas.ProductUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return product_service.update_product(
        db,
        product_id,
        payload,
        current_user.id
    )