# from typing import List
# from fastapi import APIRouter, Depends, HTTPException, Request, Query
# from sqlalchemy.orm import Session
# from fastapi.responses import JSONResponse
# from app import models, auth, schemas
# from app.database import get_db
# from datetime import datetime, timedelta, timezone
# import hashlib, secrets
# from app.auth import create_reset_token
# import asyncio
# from app.email_utils import send_reset_email
# from jose import JWTError, jwt


# SECRET_KEY = "mysecretkey"
# ALGORITHM = "HS256"


# app = APIRouter()

# # ----- Helper: JWT Token verification -----
# def get_current_user(request: Request, db: Session = Depends(get_db)):
#     user_payload = getattr(request.state, "user", None)
#     if not user_payload:
#         raise HTTPException(status_code=401, detail="Not authenticated")
#     email = user_payload.get("sub")
#     user = db.query(models.User).filter(models.User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=401, detail="User not found")
#     return user

# @app.get("/")
# def home():
#     return {"msg": "Welcome to Ecommerce API"}


# # ----- Auth routes -----
# # Signup 
# @app.post("/signup")
# def signup(data: schemas.SignupIn, db: Session = Depends(get_db)):
#     if db.query(models.User).filter(models.User.email == data.email).first():
#         raise HTTPException(status_code=400, detail="Email already registered")

#     hashed = auth.hash_password(data.password)
    
#     user = models.User(
#         name=data.name,
#         email=data.email,
#         phone=data.phone,
#         gender=data.gender,
#         password=hashed
#     )
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return { "User created successfully"}
# #               _______________________________________
# # Login
# @app.post("/login", response_model=schemas.TokenOut)
# def login(data: schemas.LogIn, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == data.email.strip().lower()).first()
#     if not user or not auth.verify_password(data.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     token = auth.create_access_token(subject=user.email, extra={"role": "user", "user_id": user.id})
#     return {"access_Token": token, "token_type": "Bearer"}

# #               _______________________________________

# # ----- Product routes -----
# # Add Products
# @app.post("/products", response_model=schemas.ProductOut)
# def add_product(payload: schemas.ProductIn, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
#     # print in terminal for checking
#     # print("Post Products:", add_product)
    
#     product = models.Product(
#         title=payload.title,
#         description=payload.description,
#         price=payload.price,
#         quantity=payload.quantity,
#         user_id = current_user.id
#     )
#     # Print Product data in terminal for checking
#     print("Post Product data: ", product)
    
#     db.add(product)
#     db.commit()
#     db.refresh(product)
#     return product
# #               _______________________________________

# # View All Products 
# @app.get("/products", response_model=list[schemas.ProductOut])
# def list_products(
#     db: Session = Depends(get_db),
#     sort_by: str = Query(default="id", description="Field to sort by (price, title, id)"),
#     order: str = Query(default="asc", description="Sorting order: asc or desc")
# ):
#      # Print Details in terminal
#     #print("Get Products:",list_products)
    
#     print(f" Sorting by: {sort_by} ({order})")
    
#     valid_fields = ["id", "title", "price", "quantity"] # allowed sort field
    
#     if sort_by not in valid_fields:
#         raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
    
#     # Dynamic sort logic
#     sort_column = getattr(models.Product, sort_by)
#     if order == "desc":
#         sort_column = sort_column.desc()
        
#     products = db.query(models.Product).order_by(sort_column).all()
    
   
#     return products
# #               _______________________________________

# # Delete Products by id
# @app.delete("/products/{product_id}")
# def delete_product(product_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
#     # Not found Product
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
    
#     # Ownership check
#     if product.user_id != current_user.id:
#         raise HTTPException(status_code=403, detail="You can only delete your own products")
    
#     db.delete(product)
#     db.commit()
#     return {f"msg": f"Product{product_id} deleted successfully"}
# #               _______________________________________

# # ----- Cart routes -----
# # Add Products in Cart
# @app.post("/cart", response_model=dict)
# def add_to_cart(item: schemas.CartAddIn, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")

#     existing = db.query(models.CartItem).filter(
#         models.CartItem.user_id == current_user.id,
#         models.CartItem.product_id == item.product_id
#     ).first()

#     if existing:
#         existing.quantity += item.quantity
#     else:
#         db.add(models.CartItem(user_id=current_user.id, product_id=item.product_id, quantity=item.quantity))

#     db.commit()
#     return {"msg": "Added to cart"}

# #               _______________________________________

# # View products in Cart
# @app.get("/cart", response_model=list[schemas.CartItemOut])
# def get_cart(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     items = db.query(models.CartItem).filter(models.CartItem.user_id == current_user.id).all()
#     return items 

# #               _______________________________________

# # Delete products in Cart
# @app.delete("/cart/{item_id}")
# def remove_from_cart(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     item = db.query(models.CartItem).filter(
#         models.CartItem.id == item_id,
#         models.CartItem.user_id == current_user.id
#     ).first()
    
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found in your cart")
    
#     db.delete(item)
#     db.commit()
#     return {"msg": f"Item {item_id} removed from cart"}

# #               _______________________________________

# # Increment / Decrement cart quantity
# @app.patch("/cart/{item_id}/quantity", response_model=dict)
# def update_cart_item_quantity(
#     item_id: int,
#     action: str,  # "increment" or "decrement"
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user)
# ):
    
#     #print(" current_user.id =", current_user.id)
#     #print(" item_id =", item_id)
    
#     cart_item = db.query(models.CartItem).filter(
#         models.CartItem.id == item_id,
#         models.CartItem.user_id == current_user.id
#     ).first()
    
#     #print(" cart_item =", cart_item)

#     if not cart_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     if action == "increment":
#         cart_item.quantity += 1
#     elif action == "decrement":
#         cart_item.quantity -= 1
#     else:
#         raise HTTPException(status_code=400, detail="Invalid action")

#     # Remove item if quantity becomes zero
#     if cart_item.quantity <= 0:
#         db.delete(cart_item)
#         db.commit()
#         return {"msg": "Item removed from cart"}

#     db.commit()
#     db.refresh(cart_item)
#     return {"msg": f"Quantity updated to {cart_item.quantity}"}

# #               _______________________________________

# # Update Products
# @app.put("/products/{product_id}", response_model=schemas.ProductOut)
# def update_products(
#     product_id: int, 
#     payload: schemas.ProductUpdate, 
#     db: Session = Depends(get_db), 
#     current_user: models.User = Depends(get_current_user)
# ):
#     #  Find product by ID
#     product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
#     # Validation checks
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found!")
    
#     # Check ownership
#     if product.user_id != current_user.id:
#         raise HTTPException(status_code=403, detail="You can only update your own products")
    
#     #  Update allowed fields
#     for key, value in payload.model_dump(exclude_unset=True).items():
#         setattr(product, key, value)
        
        
#     db.commit()
#     db.refresh(product)
    
#     print(f"Product updated by {current_user.email}: {product.title}")
#     return product

# #               _______________________________________

# # Orders route
# @app.post("/orders", response_model=schemas.OrderResponse)
# def create_order(order_data: schemas.OrderCreateIn,
#                  db: Session = Depends(get_db),
#                  current_user: models.User = Depends(get_current_user)
#     ):
    
#     # Auto-calculate total price
#     Total_sum_price = sum(item.quantity * item.price_per_item for item in order_data.items)
    
#     # Create main order
#     new_order = models.Order(
#         user_id=current_user.id, 
#         total_price=Total_sum_price    
#     )
#     db.add(new_order)
#     db.commit()
#     db.refresh(new_order)
    
#     # Add all order items + update product stock
#     for item in order_data.items:
#         product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        
#         if not product:
#             raise HTTPException(status_code=404, detail=f"Product ID {item.product_id} not found")
        
#         # Check if enough stock available
#         if product.quantity < item.quantity:
#             raise HTTPException(status_code=400, detail=f"Not enough stock for product '{product.title}'")
        
#         # Decrement product stock
#         product.quantity -= item.quantity
        
#         # Create order item entry
#         order_item = models.OrderItem(
#             order_id=new_order.id,
#             product_id=item.product_id,
#             quantity=item.quantity,
#             price_per_item=item.price_per_item,
#             total_item_price=item.quantity * item.price_per_item
#         )
        
#         db.add(order_item)
    
#     # After all updates, commit changes together
#     db.commit()
#     db.refresh(new_order)

#     # clear user's cart after successful order
#     db.query(models.CartItem).filter(models.CartItem.user_id == current_user.id).delete()
#     db.commit()
        
#     return {"msg": "Order placed successfully", "order_id": new_order.id}

# # _________________________________

# # Return all orders placed by the currently logged-in user.

# @app.get("/my-orders", response_model=List[schemas.OrderOut])
# def get_my_orders(
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user)
# ):
#     orders = (
#         db.query(models.Order)
#         .filter(models.Order.user_id == current_user.id)
#         .all()
#     )

#     if not orders:
#         raise HTTPException(status_code=404, detail="No orders found")

#     result = []
#     for order in orders:
#         order_items_data = []
#         for item in order.order_items:
#             # Ensure related product exists
#             product_title = item.product.title if item.product else "Unknown"

#             order_items_data.append({
#                 "id": item.id,
#                 "product_id": item.product_id if item.product_id else 0,   # fallback for None
#                 "product_title": product_title,
#                 "quantity": item.quantity,
#                 "price_per_item": item.price_per_item,
#                 "total_item_price": item.total_item_price,
#             })

#         result.append({
#             "id": order.id,
#             "user_id": order.user_id,
#             "total_price": order.total_price,
#             "created_at": order.created_at,
#             "order_items": order_items_data,
#         })

#     return result 

# # ------------------- FORGOT PASSWORD -------------------

# @app.post("/forgot-password")
# async def forgot_password(data: schemas.ForgotPasswordIn, db: Session = Depends(get_db)):
#     # check if user email exist in database
#     user = db.query(models.User).filter(models.User.email == data.email.strip().lower()).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="Email not registered")

#     #  Create short-lived reset token (15 min)
#     expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     reset_token = jwt.encode(
#         {"sub": user.email, "exp": expire},
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )

#     # Create reset link
#     reset_link = f"http://localhost:5173/reset-password?token={reset_token}"

#     # Send reset email
#     await send_reset_email(user.email, reset_link)

#     return {"msg": "Password reset link sent to your email!"}


# # ------------------- RESET PASSWORD -------------------

# @app.post("/reset-password")
# def reset_password(data: schemas.ResetPasswordIn, db: Session = Depends(get_db)):
#     try:
#         # Decode token aur email
#         payload = jwt.decode(data.token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
#         email = payload.get("sub")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")

#     # User lookup
#     user = db.query(models.User).filter(models.User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Password update
#     user.password = auth.hash_password(data.new_password)
#     db.commit()

#     return {"msg": "Password reset successfully! Please login again"}

# #               _______________________________________

# # Get Profile
# @app.get("/profile", response_model=schemas.UserProfileOut)
# def get_profile(current_user: models.User = Depends(get_current_user)):
#     return current_user


# # Update Profile
# @app.put("/profile", response_model=schemas.UserProfileOut)
# def update_profile(
#     payload: schemas.UserProfileUpdate,
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user)
# ):
#     for key, value in payload.model_dump(exclude_unset=True).items():
#         setattr(current_user, key, value)

#     db.commit()
#     db.refresh(current_user)
#     return current_user

# # Change Password
# @app.put("/profile/change-password")
# def change_password(
#     payload: schemas.ChangePasswordIn,
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user)
# ):
#     if not auth.verify_password(payload.old_password, current_user.password):
#         raise HTTPException(status_code=400, detail="Old password incorrect")
#     current_user.password = auth.hash_password(payload.new_password)
#     db.commit()
#     return {"msg": "Password updated successfully"}


