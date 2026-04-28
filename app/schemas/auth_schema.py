from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Literal
import re


class SignupIn(BaseModel):

    name: str

    email: EmailStr

    phone: str = Field(
        ...,
        pattern=r"^(\+92|0)3[0-9]{2}[0-9]{7}$"
    )

    gender: Literal["male", "female", "other"]

    password: str = Field(..., min_length=8)

    # ---------- Normalize Gender ----------
    @field_validator("gender", mode="before")
    @classmethod
    def normalize_gender(cls, v):
        if isinstance(v, str):
            v = v.lower()
        return v

    # ---------- Password Strength ----------
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase letter")

        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain number")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain special character")

        return v


class LogIn(BaseModel):

    email: EmailStr
    password: str


class TokenOut(BaseModel):

    access_token: str
    token_type: str = "Bearer"


class ForgotPasswordIn(BaseModel):

    email: EmailStr


class ResetPasswordIn(BaseModel):

    token: str
    new_password: str = Field(..., min_length=8)

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, v):

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase letter")

        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain number")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain special character")

        return v


class ChangePasswordIn(BaseModel):

    old_password: str
    new_password: str = Field(..., min_length=8)

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, v):

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase letter")

        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain number")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain special character")

        return v