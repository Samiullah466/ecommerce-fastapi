from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app import models, schemas


def create_order(db: Session, user_id: int, order_data: schemas.OrderCreateIn):

    total_price = sum(
        item.quantity * item.price_per_item
        for item in order_data.items
    )

    new_order = models.Order(
        user_id=user_id,
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order_data.items:

        product = db.query(models.Product).filter(
            models.Product.id == item.product_id
        ).first()

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )

        if product.quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for {product.title}"
            )

        product.quantity -= item.quantity

        order_item = models.OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_per_item=item.price_per_item,
            total_item_price=item.quantity * item.price_per_item
        )

        db.add(order_item)

    db.commit()

    db.query(models.CartItem).filter(
        models.CartItem.user_id == user_id
    ).delete()

    db.commit()

    return {"msg": "Order placed successfully", "order_id": new_order.id}


def get_user_orders(db: Session, user_id: int):

    orders = db.query(models.Order)\
        .options(
            joinedload(models.Order.order_items)
            .joinedload(models.OrderItem.product)
        )\
        .filter(models.Order.user_id == user_id)\
        .all()

    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")

    result = []

    for order in orders:

        items = []

        for item in order.order_items:
            items.append({
                "id": item.id,
                "product_id": item.product_id,
                "product_title": item.product.title if item.product else None,
                "quantity": item.quantity,
                "price_per_item": item.price_per_item,
                "total_item_price": item.total_item_price
            })

        result.append({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "created_at": order.created_at,
            "order_items": items
        })

    return result