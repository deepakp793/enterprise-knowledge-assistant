from fastapi import status
from fastapi.testclient import TestClient

from enterprise_knowledge_assistant.main import create_app


def test_health_check_ok() -> None:
    application = create_app()

    with TestClient(application) as client:
        response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
