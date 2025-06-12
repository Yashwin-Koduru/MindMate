def test_save_and_mood_service():
    # Assuming mood_service.save_entry and mood_service.get_entry imported
    from src.service.mood_service import mood_service
    date = '2025-06-12'
    mood_val = 7
    note = 'Feeling good'
    saved = mood_service.save_entry(date, mood_val, note)
    assert saved['date'] == date
    assert saved['mood'] == mood_val
    assert saved['note'] == note

    fetched = mood_service.get_entry(date)
    assert fetched == saved

def test_endpoints_mood(client):
    # client fixture from pytest-flask
    # Test POST
    resp = client.post('/mood', json={'date': '2025-06-12', 'mood': 5, 'note': 'Test'})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['mood'] == 5
    # Test GET
    resp2 = client.get('/mood?date=2025-06-12')
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    assert data2['note'] == 'Test'
