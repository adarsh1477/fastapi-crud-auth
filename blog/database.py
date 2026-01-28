from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog/blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args = {"check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush = False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()