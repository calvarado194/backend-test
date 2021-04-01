from sqlalchemy.orm import Session, query
from sqlalchemy.sql.functions import mode

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_businesses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Business).offset(skip).limit(limit).all()


def get_business(db: Session, business_id: int):
    return db.query(models.Business).filter(models.Business.id == business_id).first()


def create_business(db: Session, business: schemas.BusinessCreate):
    db_business = models.Business(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)

    return db_business


def update_business(db: Session, business_id: int, business_data: dict):
    db_business = (
        db.query(models.Business).filter(models.Business.id == business_id).first()
    )

    for k, v in business_data.items():
        db_business.__setattr__(k, v)

    db.commit()
    db.refresh(db_business)
    return db_business


def delete_business(db: Session, business_id: int):
    deleted_rows = (
        db.query(models.Business).filter(models.Business.id == business_id).delete()
    )
    db.commit()
    return {"success": deleted_rows > 0}
