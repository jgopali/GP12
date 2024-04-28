from fastapi.testclient import TestClient
from ..controllers import promotions as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotion(db_session):
    #Sample Data
    promotion_data = {
        "name": "4/20 Deal",
        "discountAmount": "5.00",
        "daysRemaining": "5"
    }

    promotion_object = model.Promotions(**promotion_data)

    #Call create function
    created_info = controller.create(db_session, promotion_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "4/20 Deal"
    assert created_info.discountAmount == "5.00"
    assert created_info.daysRemaining == "5"


