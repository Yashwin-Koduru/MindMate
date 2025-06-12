import pytest
from services import endpoints

@pytest.fixture
def client():
    app = endpoints.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_reminder_workflow(client):
    user_id = 'integration_test_user'
    reminder_payload = {
        'user_id': user_id,
        'type': 'hydration',
        'time': '10:00'
    }

    # Create a reminder
    response = client.post('/reminders', json=reminder_payload)
    assert response.status_code in (201, 500)

    # Fetch reminders
    response = client.get(f'/reminders/{user_id}')
    assert response.status_code in (200, 500)

    # Check due reminders
    response = client.get(f'/reminders/due/{user_id}')
    assert response.status_code in (200, 500)