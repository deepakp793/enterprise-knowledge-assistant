import httpx2

from enterprise_knowledge_assistant.integrations.confluence.client import (
    ConfluenceClient,
)


def test_get_page_returns_mapped_confluence_page() -> None:
    def handle_request(request: httpx2.Request) -> httpx2.Response:
        assert request.method == "GET"
        assert request.url.path == "/wiki/api/v2/pages/12345"
        assert request.url.params["body-format"] == "storage"

        return httpx2.Response(
            status_code=200,
            json={
                "id": "12345",
                "title": "Deployment Guide",
                "body": {
                    "storage": {"value": "<p>Deploy using the production pipeline.</p>"}
                },
                "version": {"number": 7},
            },
        )

    transport = httpx2.MockTransport(handle_request)

    client = ConfluenceClient(
        base_url="https://example.atlassian.net/wiki",
        email="developer@example.com",
        api_token="test-token",
        space_key="ENG",
        transport=transport,
    )

    try:
        page = client.get_page("12345")
    finally:
        client.close()

    assert page.page_id == "12345"
    assert page.title == "Deployment Guide"
    assert page.source_url == (
        "https://example.atlassian.net/wiki/spaces/ENG/pages/12345"
    )
