# from datetime import datetime
# from pydantic import BaseModel, EmailStr
# from typing import Optional, List


# class SignupIn(BaseModel):
#     name : str
#     email : EmailStr
#     phone : str
#     gender : str
#     password : str
    

# class LogIn(BaseModel):
#     email : EmailStr
#     password : str
    

# class TokenOut(BaseModel):
#     access_Token: str
#     token_type: str = "Bearer"
    

# class ProductIn(BaseModel):
#     title : str
#     description: str
#     price: float
#     quantity: Optional[int]
    

# class ProductOut(BaseModel):
#     id: int
#     title: str
#     description: str
#     price: float
#     quantity: int
#     class Config:
#         from_attributes = True
        
        
# class CartAddIn(BaseModel):
#     product_id: int
#     quantity: int

# class CartItemOut(BaseModel):
#     id: int
#     product: ProductOut
#     quantity: int
#     class Config:
#         from_attributes = True
        
# class ProductUpdate(BaseModel):
#     title: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     quantity: Optional[int] = None
    
# class OrderItemIn(BaseModel):
#     product_id: int
#     quantity: int
#     price_per_item: float
    
    
# class OrderCreateIn(BaseModel):
#     total_price: Optional[float] = None
#     items: List[OrderItemIn]
    
    
# class OrderItemOut(BaseModel):
#     id: int
#     product_id: int
#     product_title: str   # Add
#     quantity: int
#     price_per_item: float
#     total_item_price: float
    
#     class Config:
#         from_attributes = True
        
        
# class OrderOut(BaseModel):
#     id: int
#     user_id: int
#     total_price: float
#     created_at: datetime
#     order_items: List[OrderItemOut]
#     class Config:
#         from_attributes = True
        
# class OrderResponse(BaseModel):
#     msg: str
#     order_id: int
    
    
# # Forgot Password
# class ForgotPasswordIn(BaseModel):
#     email: EmailStr
    
# class ResetPasswordIn(BaseModel):
#     token: str
#     new_password: str
    
# # USER PROFILE SCHEMAS

# # For Viewing Profile:
# class UserProfileOut(BaseModel):
#     id: int
#     name: str
#     email: EmailStr
#     phone: str
#     gender: str
#     date_of_birth: Optional[datetime]
#     street: Optional[str]
#     city: Optional[str]
#     state: Optional[str]
#     zip_code: Optional[str]
#     default_shipping_address: Optional[str]
#     billing_address: Optional[str]

#     class Config:
#         from_attributes = True

# # For Updating Profile:
# class UserProfileUpdate(BaseModel):
#     name: Optional[str] = None
#     phone: Optional[str] = None
#     gender: Optional[str] = None
#     date_of_birth: Optional[datetime] = None
#     street: Optional[str] = None
#     city: Optional[str] = None
#     state: Optional[str] = None
#     zip_code: Optional[str] = None
#     default_shipping_address: Optional[str] = None
#     billing_address: Optional[str] = None


# # PASSWORD CHANGE SCHEMA
# class ChangePasswordIn(BaseModel):
#     old_password: str
#     new_password: str
