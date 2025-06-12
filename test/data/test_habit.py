
def test_habit_service():
    from src.service.habit_service import HabitService
    svc = HabitService()
    date = '2025-06-12'
    res = svc.save_status(date, 'meditation', True)
    assert res['done'] is True
    status = svc.get_status(date)
    assert status['meditation'] is True
    # test weekly
    week = svc.get_weekly_progress('2025-06-10')
    assert isinstance(week, dict)
    assert '2025-06-12' in week

def test_endpoints_habit(client):
    # Test POST
    resp = client.post('/habit', json={'date':'2025-06-12','habit':'hydration','done':False})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['habit']=='hydration'
    # Test GET status
    resp2 = client.get('/habit?date=2025-06-12')
    assert resp2.status_code == 200
    d2 = resp2.get_json()
    assert 'hydration' in d2['status']
    # Test GET progress
    resp3 = client.get('/habit/progress?week_start=2025-06-10')
    assert resp3.status_code == 200
    p = resp3.get_json()
    assert p['week_start']=='2025-06-10'
