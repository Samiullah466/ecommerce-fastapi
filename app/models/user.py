# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from app.db.base import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String)  
#     gender = Column(String)
#     password = Column(String)

#     products = relationship("Product", back_populates="user")
#     cart_items = relationship("CartItem", back_populates="user")
#     orders = relationship("Order", back_populates="user")

from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True,index=True)
    phone = Column(String)
    gender = Column(String)
    password = Column(String)

    reset_token_hash = Column(String,nullable=True)
    reset_token_expiry = Column(DateTime,nullable=True)

    date_of_birth = Column(DateTime,nullable=True)
    street = Column(String,nullable=True)
    city = Column(String,nullable=True)
    state = Column(String,nullable=True)
    zip_code = Column(String,nullable=True)

    default_shipping_address = Column(String,nullable=True)
    billing_address = Column(String,nullable=True)


    # Relationships
    
    cart_items = relationship("CartItem",back_populates="user", cascade="all, delete-orphan")
    products = relationship("Product",back_populates="user")
    orders = relationship("Order",back_populates="user", cascade="all, delete-orphan")
