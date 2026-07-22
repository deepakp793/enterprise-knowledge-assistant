import json

from enterprise_knowledge_assistant.integrations.confluence.mapper import (
    map_confluence_page,
)


def test_maps_confluence_payload_to_page() -> None:
    payload = """
{
  "id": "12345",
  "title": "Deployment Guide",
  "body": {
    "storage": {
      "value": "<p>Deploy using the production pipeline.</p>"
    }
  },
  "version": {
    "number": 7
  }
}
"""
    payload_json = json.loads(payload)

    base_url = "https://learningaideep.atlassian.net/wiki"
    space_key = "4"

    confluence_page = map_confluence_page(
        payload=payload_json,
        base_url=base_url,
        space_key=space_key,
    )

    assert confluence_page.page_id == "12345"
    assert confluence_page.body_html == "<p>Deploy using the production pipeline.</p>"
    assert (
        confluence_page.source_url
        == "https://learningaideep.atlassian.net/wiki/spaces/4/pages/12345"
    )
    assert confluence_page.space_key == "4"
    assert confluence_page.version == 7
    assert confluence_page.title == "Deployment Guide"
