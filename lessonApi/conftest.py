import pytest


@pytest.fixture(scope="session")
def dog_base_url():
    return "https://dog.ceo"