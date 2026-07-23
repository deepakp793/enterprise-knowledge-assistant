from bs4 import BeautifulSoup
from langchain_core.documents import Document

from enterprise_knowledge_assistant.integrations.confluence.models import ConfluencePage


def convert_confluence_page_to_document(confluence_page: ConfluencePage) -> Document:
    soup = BeautifulSoup(confluence_page.body_html, "html.parser")
    body_text = soup.get_text(separator="\n", strip=True)

    page_content = f"{confluence_page.title}\n\n{body_text}"

    document = Document(
        page_content=page_content,
        metadata={
            "source": confluence_page.source_url,
            "source_type": "confluence",
            "page_id": confluence_page.page_id,
            "title": confluence_page.title,
            "space_key": confluence_page.space_key,
            "version": confluence_page.version,
        },
    )

    return document
