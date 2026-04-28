from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas


# Add product to cart
def add_to_cart(db: Session, user_id: int, item: schemas.CartAddIn):

    product = db.query(models.Product).filter(
        models.Product.id == item.product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing = db.query(models.CartItem).filter(
        models.CartItem.user_id == user_id,
        models.CartItem.product_id == item.product_id
    ).first()

    if existing:
        existing.quantity += item.quantity
    else:
        new_item = models.CartItem(
            user_id=user_id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(new_item)

    db.commit()

    return {"msg": "Added to cart"}


# View cart
def get_cart(db: Session, user_id: int):

    items = db.query(models.CartItem).filter(
        models.CartItem.user_id == user_id
    ).all()

    return items


# Delete item from cart
def remove_from_cart(db: Session, user_id: int, item_id: int):

    item = db.query(models.CartItem).filter(
        models.CartItem.id == item_id,
        models.CartItem.user_id == user_id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"msg": f"Item {item_id} removed from cart"}


# Update quantity
def update_cart_quantity(
        db: Session,
        user_id: int,
        item_id: int,
        action: str
):

    cart_item = db.query(models.CartItem).filter(
        models.CartItem.id == item_id,
        models.CartItem.user_id == user_id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")

    if action == "increment":
        cart_item.quantity += 1

    elif action == "decrement":
        cart_item.quantity -= 1

    else:
        raise HTTPException(status_code=400, detail="Invalid action")

    if cart_item.quantity <= 0:
        db.delete(cart_item)
        db.commit()
        return {"msg": "Item removed from cart"}

    db.commit()
    db.refresh(cart_item)

    return {"msg": f"Quantity updated to {cart_item.quantity}"}