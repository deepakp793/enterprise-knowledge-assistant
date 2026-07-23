from enterprise_knowledge_assistant.ingestion.document_factory import (
    convert_confluence_page_to_document,
)
from enterprise_knowledge_assistant.integrations.confluence.models import (
    ConfluencePage,
)


def test_converts_confluence_page_to_langchain_document() -> None:
    page = ConfluencePage(
        page_id="12345",
        title="Deployment Guide",
        body_html=("<h1>Deployment</h1><p>Use the production pipeline.</p>"),
        source_url=("https://example.atlassian.net/wiki/spaces/ENG/pages/12345"),
        space_key="ENG",
        version=7,
    )

    document = convert_confluence_page_to_document(page)

    assert document.page_content == (
        "Deployment Guide\n\nDeployment\nUse the production pipeline."
    )
    assert document.metadata == {
        "source": ("https://example.atlassian.net/wiki/spaces/ENG/pages/12345"),
        "source_type": "confluence",
        "page_id": "12345",
        "title": "Deployment Guide",
        "space_key": "ENG",
        "version": 7,
    }
