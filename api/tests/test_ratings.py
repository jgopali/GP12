from fastapi.testclient import TestClient
from ..controllers import ratings_review as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_rating(db_session):
    #Sample Data
    rating_data = {
        "rating": "5",
        "review": "This is a test"
    }

    rating_object = model.Ratings(**rating_data)

    #Call create function
    created_info = controller.create(db_session, rating_object)

    #Test Cases
    assert created_info is not None
    assert created_info.rating == "5"
    assert created_info.review == "This is a test"

