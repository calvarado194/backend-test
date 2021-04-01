from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    address = Column(String)
    rut = Column(String, index=True)
    contact_email = Column(String, default="")
