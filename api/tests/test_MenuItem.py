from fastapi.testclient import TestClient
from ..controllers import menu_items as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menuItem(db_session):
    #Sample Data
    menuItem_data = {
        "name": "Spaghetti",
        "price": "12"
    }

    menuItem_object = model.MenuItem(**menuItem_data)

    #Call create function
    created_info = controller.create(db_session, menuItem_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "Spaghetti"
    assert created_info.price == "12"

