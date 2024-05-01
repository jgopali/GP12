from fastapi.testclient import TestClient
from ..controllers import payment_info as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_payment_info(db_session):
    #Sample Data
    payment_info_data = {
        "card_number": "212567666",
        "expiration_date": "122222"
    }

    payment_info_object = model.PaymentInfo(**payment_info_data)

    #Call create function
    created_info = controller.create(db_session, payment_info_object)

    #Test Cases
    assert created_info is not None
    assert created_info.card_number == "212567666"
    assert created_info.expiration_date == "122222"

