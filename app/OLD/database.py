# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/ecommerce_db"

# engine = create_engine(DATABASE_URL, future=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True )


# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()