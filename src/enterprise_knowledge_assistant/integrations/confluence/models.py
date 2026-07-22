from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConfluencePage:
    page_id: str
    title: str
    body_html: str
    source_url: str
    space_key: str
    version: int
