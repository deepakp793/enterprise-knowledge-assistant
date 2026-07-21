from importlib import import_module


def test_package_is_importable() -> None:
    package = import_module("enterprise_knowledge_assistant")

    assert package.__name__ == "enterprise_knowledge_assistant"
