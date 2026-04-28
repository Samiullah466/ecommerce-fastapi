from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas


def create_product(db: Session, payload: schemas.ProductIn, user_id: int):

    product = models.Product(
        title=payload.title,
        description=payload.description,
        price=payload.price,
        quantity=payload.quantity,
        user_id=user_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_all_products(db: Session, sort_by: str = "id", order: str = "asc"):

    valid_fields = ["id", "title", "price", "quantity"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    sort_column = getattr(models.Product, sort_by)

    if order == "desc":
        sort_column = sort_column.desc()

    products = db.query(models.Product).order_by(sort_column).all()

    return products


def delete_product(db: Session, product_id: int, user_id: int):

    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(product)
    db.commit()

    return {"msg": "Product deleted successfully"}


def update_product(
        db: Session,
        product_id: int,
        payload: schemas.ProductUpdate,
        user_id: int
):

    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product