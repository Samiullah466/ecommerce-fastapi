from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.core import security as auth


def get_profile(current_user: models.User):

    return current_user


def update_profile(
        db: Session,
        current_user: models.User,
        payload: schemas.UserProfileUpdate
):

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(current_user, key, value)

    db.commit()
    db.refresh(current_user)

    return current_user


def change_password(
        db: Session,
        current_user: models.User,
        payload: schemas.ChangePasswordIn
):

    if not auth.verify_password(payload.old_password, current_user.password):
        raise HTTPException(status_code=400, detail="Old password incorrect")

    current_user.password = auth.hash_password(payload.new_password)

    db.commit()

    return {"msg": "Password updated successfully"}