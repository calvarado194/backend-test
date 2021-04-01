from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel

from db import schemas, crud
from db.database import SessionLocal


app = FastAPI(
    title="Ejercicio 2", description="API REST para CRUD de empresas.", version="1.0"
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "2dcb553c89361352c87ebdfe4fe2952d96e4db703f524956d40436537b7e3630"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

tags_metadata = [
    {"name": "login", "description": "Control de acceso",},
    {
        "name": "crud",
        "description": "Endpoints para creación, lectura, actualización y eliminación.",
    },
    {
        "name": "healthcheck",
        "description": "Endpoint sencillo para chequeo de inicialización.",
    },
]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=Token, tags=["login"])
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/hello", tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}


@app.get("/empresas/", tags=["crud"], response_model=List[schemas.Business])
async def get_businesses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user),
):
    businesses = crud.get_businesses(db, skip, limit)
    return businesses


@app.get("/empresas/{business_id}", tags=["crud"], response_model=schemas.Business)
async def get_business(
    business_id: int,
    response: Response,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user),
):
    business = crud.get_business(db, business_id)
    if business is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return business


@app.post("/empresas/", tags=["crud"], response_model=schemas.Business)
async def create_business(
    business: schemas.BusinessCreate,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user),
):
    db_business = crud.create_business(db, business)
    return db_business


@app.put("/empresas/{business_id}", tags=["crud"], response_model=schemas.Business)
async def update_business(
    business_id: int,
    business: dict,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user),
):
    db_business = crud.update_business(db, business_id, business)
    return db_business


@app.delete(
    "/empresas/{business_id}", tags=["crud"], response_model=schemas.BusinessDelete
)
async def delete_business(
    business_id: int,
    response: Response,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user),
):
    db_response = crud.delete_business(db, business_id)
    if not db_response["success"]:
        response.status_code = status.HTTP_404_NOT_FOUND
    return db_response
