from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.database import Base, get_db
from core.auth import get_current_user
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"id": 1, "username": "testuser"}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user
client = TestClient(app)

def test_create_task():
    Base.metadata.create_all(bind=engine)

    response = client.post(
        "/v1/tasks/",
        json={
            "name": "TaskOne",
            "priority": "high",
            "description": "integration test",
            "deadline": "2026-03-24T12:00:00",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "TaskOne"
    assert data["priority"] == "high"
    assert data["description"] == "integration test"
    assert data["deadline"] == "2026-03-24T12:00:00"