# from passlib.context import CryptContext
# from jose import jwt
# from fastapi import HTTPException,status
# from datetime import datetime, timedelta, timezone
# from typing import Optional
# import secrets, hashlib


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# #print("Password_Hash",pwd_context)


# SECRET_KEY = "mysecretkey"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE = 3600 # Token Expire time


# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)
# # print("Hashed password:", hash_password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# def create_access_token(subject: str, expires_delta: Optional[timedelta]= None, extra: dict = None):
#     to_encode = {"sub":str(subject)}
#     if extra:
#         to_encode.update(extra)
#     expire = datetime.now(timezone.utc) + (expires_delta or timedelta(seconds=ACCESS_TOKEN_EXPIRE))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def decode_access_token(token: str):
    
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid or expired")
    
# # Generate token     
# def create_reset_token():
#      """Generate a unique reset token, hash it, and set expiry."""
#      raw_token = secrets.token_urlsafe(32)
#      token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
#      expiry = datetime.now() + timedelta(minutes=10)  # 10 min valid
#      return raw_token, token_hash, expiry