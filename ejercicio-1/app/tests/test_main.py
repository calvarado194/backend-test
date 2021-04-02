from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import pytest

from ..main import app, get_db
from ..db.database import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


@pytest.fixture
def auth_token():
    response = client.post(
        "/token",
        data={"username": "ema@oneninefour.cl", "password": "L6Lbc82QN67XZBJE"},
    )
    token = response.json()["access_token"]

    return token


@pytest.fixture
def test_business(auth_token):
    test_business = {
        "name": "ACME Inc.",
        "rut": "78964585-K",
        "address": "Fake Street 123",
        "contact_email": "hello@acme.io",
    }

    response = client.post(
        "/empresas/",
        headers={"Authorization": "Bearer {}".format(auth_token)},
        json=test_business,
    )

    return response.json()


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_business(auth_token):
    fake = Faker("es_MX")

    fake_business = {
        "name": fake.company(),
        "rut": "76008913-3",
        "address": fake.street_address(),
        "contact_email": fake.email(),
    }

    response = client.post(
        "/empresas/",
        headers={"Authorization": "Bearer {}".format(auth_token)},
        json=fake_business,
    )
    assert response.status_code == 200
    response = response.json()
    for k, v in fake_business.items():
        assert k in response
        assert response[k] == v

    assert "id" in response


def test_get_businesses(auth_token, test_business):
    response = client.get(
        "/empresas", headers={"Authorization": "Bearer {}".format(auth_token)},
    )

    assert response.status_code == 200
    response = response.json()
    assert len(response) > 0

    for business in response:
        if business["rut"] == test_business["rut"]:
            assert True
            assert business["name"] == test_business["name"]


def test_get_one_business(auth_token, test_business):
    response = client.get(
        "/empresas/{}".format(test_business["id"]),
        headers={"Authorization": "Bearer {}".format(auth_token)},
    )

    assert response.status_code == 200
    response = response.json()

    assert "id" in response

    assert response["id"] == test_business["id"]
    assert response["name"] == test_business["name"]
    assert response["rut"] == test_business["rut"]
    assert response["address"] == test_business["address"]
    assert response["contact_email"] == test_business["contact_email"]


def test_update_business(auth_token, test_business):
    business_update = {
        "address": "New Faker Street 194",
        "contact_email": "contact@acme.io",
    }

    response = client.put(
        "/empresas/{}".format(test_business["id"]),
        headers={"Authorization": "Bearer {}".format(auth_token)},
        json=business_update,
    )

    assert response.status_code == 200
    response = response.json()

    assert response["id"] == test_business["id"]
    assert response["name"] == test_business["name"]
    assert response["address"] != test_business["address"]
    assert response["address"] == business_update["address"]
    assert response["contact_email"] != test_business["contact_email"]
    assert response["contact_email"] == business_update["contact_email"]


def test_delete_business(auth_token, test_business):
    response = client.delete(
        "/empresas/{}".format(test_business["id"]),
        headers={"Authorization": "Bearer {}".format(auth_token)},
    )

    assert response.status_code == 200
    response = response.json()

    assert response["success"]

    response = client.get(
        "/empresas/{}".format(test_business["id"]),
        headers={"Authorization": "Bearer {}".format(auth_token)},
    )

    assert response.status_code == 404
