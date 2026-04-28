from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app import schemas, models
from app.services import profile_service as user_service
from app.dependencies import get_current_user

router = APIRouter(prefix="/profile", tags=["User"])


# Get profile
@router.get("/", response_model=schemas.UserProfileOut)
def get_profile(
    current_user: models.User = Depends(get_current_user)
):
    return user_service.get_profile(current_user)


# Update profile
@router.put("/", response_model=schemas.UserProfileOut)
def update_profile(
    payload: schemas.UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_service.update_profile(
        db,
        current_user,
        payload
    )


# Change password
@router.put("/change-password")
def change_password(
    payload: schemas.ChangePasswordIn,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_service.change_password(
        db,
        current_user,
        payload
    )