from ..cartao import app as meuapp
import pytest

@pytest.fixture
def app():
    return meuapp

