from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.main import app, get_db
from src.database import Base


SQL_ALCHEMY_DB_URL = "sqlite:///:memory:"

engine = create_engine(
    SQL_ALCHEMY_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


TestingSessionLocal = sessionmaker(
    autoflush=False, autocommit=False, bind=engine)


Base.metadata.create_all(bind=engine)


def get_mock_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_mock_db


client = TestClient(app)


# Testing if server is working
def test_get_server():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server is running"


def test_get_all_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    item = {"title": "hello", "description": "world"}
    response = client.post("/items", json=item)
    item.update({"id": 1})
    assert response.status_code == 201
    assert response.json() == item


def test_get_item_by_id():
    item = {"title": "hello", "description": "world", "id": 1}
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == item


def test_update_item():
    item = {"title": "hello", "description": "updated"}
    response = client.put("/items/1", json=item)
    item.update({"id": 1})
    assert response.status_code == 200
    assert response.json() == item


def test_delete_item():
    item = {"title": "hello", "description": "updated", "id": 1}
    response = client.put("/items/1", json=item)
    assert response.status_code == 200
    assert response.json() == item
