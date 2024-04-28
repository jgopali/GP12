from fastapi.testclient import TestClient
from ..controllers import order_details as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_orderDetail(db_session):
    #Sample Data
    orderDetail_data = {
        "quantity": "4",
        "price": "12"
    }

    orderDetail_object = model.OrderDetail(**orderDetail_data)

    #Call create function
    created_info = controller.create(db_session, orderDetail_object)

    #Test Cases
    assert created_info is not None
    assert created_info.quantity == "4"
    assert created_info.price == "12"

