from fastapi.testclient import TestClient
from ..controllers import cust_info as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_cust_info(db_session):
    #Sample Data
    customer_info_data = {
        "name": "John Doe",
        "phone": "0123456789",
        "email": "johndoe@mail.com",
        "address": "123 Cherrybowl Lane"
    }

    cust_info_object = model.CustomerInfo(**customer_info_data)

    #Call create function
    created_info = controller.create(db_session, cust_info_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "John Doe"
    assert created_info.email == "johndoe@mail.com"
    assert created_info.phone == "0123456789"
    assert created_info.address == "123 Cherrybowl Lane"


