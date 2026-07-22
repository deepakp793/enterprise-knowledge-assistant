import httpx2

from enterprise_knowledge_assistant.integrations.confluence.mapper import (
    map_confluence_page,
)
from enterprise_knowledge_assistant.integrations.confluence.models import ConfluencePage


class ConfluenceClient:
    def __init__(
        self,
        *,
        base_url: str,
        email: str,
        api_token: str,
        space_key: str,
        timeout_seconds: float = 10.0,
        transport: httpx2.BaseTransport | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._email = email
        self._api_token = api_token
        self._space_key = space_key
        self._timeout_seconds = timeout_seconds

        self._http_client = httpx2.Client(
            base_url=f"{self._base_url}/",
            auth=(self._email, self._api_token),
            headers={"Accept": "application/json"},
            timeout=self._timeout_seconds,
            transport=transport,
        )

    def get_page(self, page_id: str) -> ConfluencePage:
        response = self._http_client.get(
            f"api/v2/pages/{page_id}",
            params={"body-format": "storage"},
        )

        response.raise_for_status()
        payload = response.json()

        return map_confluence_page(
            payload=payload,
            base_url=self._base_url,
            space_key=self._space_key,
        )

    def close(self) -> None:
        self._http_client.close()
