from jose import jwt
from app.core.config import settings


def decode_token(token: str):

    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

    return payload