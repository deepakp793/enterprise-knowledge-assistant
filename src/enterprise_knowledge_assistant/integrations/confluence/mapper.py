from collections.abc import Mapping
from typing import Any

from enterprise_knowledge_assistant.integrations.confluence.models import ConfluencePage


def map_confluence_page(
    payload: Mapping[str, Any],
    base_url: str,
    space_key: str,
) -> ConfluencePage:
    confluence_page = ConfluencePage(
        page_id=payload["id"],
        title=payload["title"],
        body_html=payload["body"]["storage"]["value"],
        source_url=f"{base_url.rstrip('/')}/spaces/{space_key}/pages/{payload['id']}",
        space_key=space_key,
        version=payload["version"]["number"],
    )

    return confluence_page
