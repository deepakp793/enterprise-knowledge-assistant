from langchain_core.documents import Document

from enterprise_knowledge_assistant.ingestion.text_splitter import split_documents


def test_splits_document_and_preserves_metadata() -> None:
    document = Document(
        page_content=(
            "Deployment requires an approved change request and a tested "
            "release artifact. After approval, the production pipeline "
            "deploys the release. Engineers then verify application health "
            "and monitor production logs."
        ),
        metadata={
            "source": "https://example.atlassian.net/wiki/pages/12345",
            "page_id": "12345",
            "source_type": "confluence",
        },
    )

    chunks = split_documents(
        [document],
        chunk_size=60,
        chunk_overlap=10,
    )

    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 60 for chunk in chunks)

    for chunk in chunks:
        assert chunk.metadata["source"] == document.metadata["source"]
        assert chunk.metadata["page_id"] == "12345"
        assert chunk.metadata["source_type"] == "confluence"
        assert "start_index" in chunk.metadata

    start_indexes = [chunk.metadata["start_index"] for chunk in chunks]

    assert start_indexes[0] == 0
    assert start_indexes == sorted(start_indexes)
