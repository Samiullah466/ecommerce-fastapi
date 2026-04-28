from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))
    
     # Relationships

    user = relationship("User", back_populates="products")
    
    cart_items = relationship("CartItem", back_populates="product", cascade="all, delete-orphan")