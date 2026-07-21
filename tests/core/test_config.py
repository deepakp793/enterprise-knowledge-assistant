import pytest
from pydantic import ValidationError

from enterprise_knowledge_assistant.core.config import Settings


def test_settings_accepts_valid_values() -> None:

    settings = Settings(
        confluence_base_url="https://example.atlassian.net/wiki",
        confluence_email="developer@example.com",
        confluence_api_token="test-token",
        _env_file=None,
    )

    assert str(settings.confluence_base_url) == "https://example.atlassian.net/wiki"
    assert settings.confluence_email == "developer@example.com"
    assert settings.confluence_api_token.get_secret_value() == "test-token"
    assert "test-token" not in repr(settings)


def test_settings_rejects_missing_required_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    environment_variables = (
        "CONFLUENCE_BASE_URL",
        "CONFLUENCE_EMAIL",
        "CONFLUENCE_API_TOKEN",
    )

    for variable_name in environment_variables:
        monkeypatch.delenv(variable_name, raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_settings_rejects_invalid_confluence_url() -> None:

    with pytest.raises(ValidationError):
        Settings(
            confluence_base_url="httpsexample.atlassian.net/wiki",
            confluence_email="developer@example.com",
            confluence_api_token="test-token",
            _env_file=None,
        )
