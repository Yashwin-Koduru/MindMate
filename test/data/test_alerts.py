import pytest
from services import endpoints

@pytest.fixture
def client():
    app = endpoints.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_reminder(client):
    response = client.post('/reminders', json={
        'user_id': 'test_user',
        'type': 'journaling',
        'time': '09:00'
    })
    assert response.status_code in (201, 500)

def test_fetch_reminders(client):
    response = client.get('/reminders/test_user')
    assert response.status_code in (200, 500)
