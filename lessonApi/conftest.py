import pytest


@pytest.fixture(scope="session")
def dog_base_url():
    return "https://dog.ceo"


@pytest.fixture(scope="session")
def brew_base_url():
    return "https://api.openbrewerydb.org"
