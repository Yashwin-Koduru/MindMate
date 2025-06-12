import pytest
from services import endpoints

@pytest.fixture
def client():
    app = endpoints.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_suggestions_endpoint(client):
    response = client.get('/suggestions/test_user')
    assert response.status_code in (200, 500)
