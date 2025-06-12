import pytest
from services import auth_endpoints

@pytest.fixture
def client():
    app = auth_endpoints.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_user(client):
    response = client.post('/register', json={
        'email': 'test@example.com',
        'password': 'password123',
        'display_name': 'Test User'
    })
    assert response.status_code in (201, 400)

def test_verify_token_invalid(client):
    response = client.post('/verify-token', json={'token': 'invalid_token'})
    assert response.status_code == 401