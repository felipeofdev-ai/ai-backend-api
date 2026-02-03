from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ai_endpoint_success():
    payload = {
        "prompt": "Explain what FastAPI is"
    }

    response = client.post("/ai/generate", json=payload)

    assert response.status_code == 200
    assert "response" in response.json()


def test_ai_endpoint_empty_prompt():
    payload = {
        "prompt": ""
    }

    response = client.post("/ai/generate", json=payload)

    assert response.status_code == 422
