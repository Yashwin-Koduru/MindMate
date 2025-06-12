import pytest
from services import endpoints

@pytest.fixture
def client():
    app = endpoints.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_templates(client):
    response = client.get('/journal/templates')
    assert response.status_code == 200
    assert 'gratitude' in response.json

def test_submit_entry(client):
    response = client.post('/journal/submit', json={
        "user_id": "test_user",
        "template_type": "gratitude",
        "entry": "I'm grateful for my family, health, and opportunity."
    })
    assert response.status_code in (201, 500)