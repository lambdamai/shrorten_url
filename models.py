from sqlalchemy import Boolean, Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)


class ShortendUrl(Base):
    __tablename__ = "shorturl"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=True)
    short_link = Column(String, nullable=True, index=True, unique=True)
