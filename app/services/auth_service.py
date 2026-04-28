from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.core import security
# from app.utils import hash_password
import secrets
from datetime import datetime, timedelta, timezone



def signup_user(db: Session, data: schemas.SignupIn):

    existing = db.query(models.User).filter(
        models.User.email == data.email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = security.hash_password(data.password)

    user = models.User(
        name=data.name,
        email=data.email,
        phone=data.phone,
        gender=data.gender,
        password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"msg": "User created successfully"}


def login_user(db: Session, data: schemas.LogIn):

    user = db.query(models.User).filter(
        models.User.email == data.email.lower().strip()
    ).first()

    if not user or not security.verify_password(data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
    )

    token = security.create_access_token(
        data={
            "sub": user.email,
            "user_id":  user.id,
            "role": "user"
            }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
    
# Forgot password
def forgot_password(db: Session, data):

    user = db.query(models.User).filter(
        models.User.email == data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Email not found"
        )

    # Generate reset token
    token = secrets.token_urlsafe(32)

    user.reset_token_hash = token
    user.reset_token_expiry = datetime.now(timezone.utc) + timedelta(hours=1)
    
    db.commit()

    return {
        "msg": "Password reset token generated",
        "reset_token": token
    }


# Reset password
def reset_password(db: Session, data):

    user = db.query(models.User).filter(
        models.User.reset_token_hash == data.token
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired token"
        )
    
    if user.reset_token_expiry < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="Token has expired"
        )

    user.password = security.hash_password(data.new_password)
    
    user.reset_token_hash = None
    user.reset_token_expiry = None

    db.commit()

    return {"msg": "Password reset successful"}