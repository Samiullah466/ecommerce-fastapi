from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import schemas
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


# Signup
@router.post("/signup")
def signup(data: schemas.SignupIn, db: Session = Depends(get_db)):
    return auth_service.signup_user(db, data)


# Login
@router.post("/login", response_model=schemas.TokenOut)
def login(data: schemas.LogIn, db: Session = Depends(get_db)):
    return auth_service.login_user(db, data)

# Forgot Password
@router.post("/forgot-password")
def forgot_password(
    data: schemas.ForgotPasswordIn,
    db: Session = Depends(get_db)
):
    return auth_service.forgot_password(db, data)


# Reset Password
@router.post("/reset-password")
def reset_password(
    data: schemas.ResetPasswordIn,
    db: Session = Depends(get_db)
):
    return auth_service.reset_password(db, data)