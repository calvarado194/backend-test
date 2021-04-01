from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int

    class Config:
        orm_mode = True


class BusinessBase(BaseModel):
    name: str
    address: str
    rut: str
    contact_email: Optional[str] = None


class BusinessCreate(BusinessBase):
    pass


class BusinessUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    rut: Optional[str]
    contact_email: Optional[str]


class Business(BusinessBase):
    id: int

    class Config:
        orm_mode = True


class BusinessDelete(BaseModel):
    success: bool
