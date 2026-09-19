from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Backend is running successfully!"
    }


def test_message():
    response = client.get("/api/message")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Hello from FastAPI Backend!"
    }