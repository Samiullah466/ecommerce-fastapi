# from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
# from sqlalchemy.orm import relationship
# from app.database import Base


# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False, index=True)
#     phone = Column(String, nullable=False)
#     gender = Column(String, nullable=False)
#     password = Column(String, nullable=False)
    
#     # new fields for password reset
#     reset_token_hash = Column(String, nullable=True)
#     reset_token_expiry = Column(DateTime, nullable=True)
    
#     # new fields for personal info
#     date_of_birth = Column(DateTime, nullable=True)
#     # new fields for address info
#     street = Column(String,nullable=True)
#     city = Column(String, nullable=True)
#     state = Column(String, nullable=True)
#     zip_code = Column(String, nullable=True)
#     default_shipping_address = Column(String, nullable=True)
#     billing_address = Column(String, nullable=True)
    
#      # one-to-many: user -> cart items
#     cart_items = relationship("CartItem", back_populates="user")
#     # one-to-many: user -> products 
#     products = relationship("Product", back_populates="user")
#     # one-to-many: user -> orders
#     orders = relationship("Order", back_populates="user")
    

    
# class Product(Base):
#     __tablename__ = "products"
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Float, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
    
#     # Backref from cart items
#     # one-to-many: product -> cart_items
#     cart_items = relationship("CartItem", back_populates="product",cascade="all, delete-orphan")
    
#     # link back to user 
#     # many-to-one: product -> user
#     user = relationship("User", back_populates="products")
    
    

# class CartItem(Base):
#     __tablename__ = "cart_items"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE" ), nullable=False)
#     quantity = Column(Integer, nullable=False, default=1)
    
#     # many-to-one: cart_item -> user
#     user = relationship("User", back_populates="cart_items")
    
#     # many-to-one: cart_item -> product
#     product = relationship("Product", back_populates="cart_items")
    
# class Order(Base):
#     __tablename__ = "orders"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     total_price = Column(Float, nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
    
#     # Relationships
#     # many-to-one: order -> user
#     user = relationship("User", back_populates="orders") 
    
#      # one-to-many: order -> order_items
#     order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan") 
    
# class OrderItem(Base):
#     __tablename__ = "order_items"
    
#     id = Column(Integer, primary_key=True, index=True)
#     order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"), nullable=True)
#     quantity = Column(Integer, nullable=False)
#     price_per_item = Column(Float, nullable=False)
#     total_item_price = Column(Float, nullable=False)
    
#     # Relationship
#     # many-to-one: order_item -> order
#     order = relationship("Order", back_populates="order_items")
    
#     # many-to-one: order_item -> product
#     product = relationship("Product")