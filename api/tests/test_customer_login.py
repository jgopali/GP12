from fastapi.testclient import TestClient
from ..controllers import cust_login as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_cust_login(db_session):
    #Sample Data
    customer_login_data = {
        "username": "JohnDoe",
        "password_hash": "<PASSWORD>"
    }

    cust_login_object = model.CustomerLogin(**customer_login_data)

    #Call create function
    created_info = controller.create(db_session, cust_login_object)

    #Test Cases
    assert created_info is not None
    assert created_info.username == "JohnDoe"
    assert created_info.password_hash == "<PASSWORD>"

