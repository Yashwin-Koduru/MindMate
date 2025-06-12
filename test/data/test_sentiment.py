
import pytest
from src.service.sentiment_service import SentimentService

@pytest.fixture
def service():
    return SentimentService()

def test_analyze_and_save(service):
    date = '2025-06-10'
    text = 'I am very happy today!'
    entry = service.save_entry(date, text)
    assert entry['date'] == date
    assert 'polarity' in entry and -1.0 <= entry['polarity'] <= 1.0
    # retrieve
    fetched = service.get_entry(date)
    assert fetched == entry

def test_weekly_trends(service):
    # add two entries
    service.save_entry('2025-06-01', 'Good day')
    service.save_entry('2025-06-03', 'Bad day')
    trends = service.get_weekly_trends('2025-06-01', '2025-06-07')
    # Should have one week entry
    assert isinstance(trends, list)
    assert len(trends) == 1
    assert 'week' in trends[0] and 'average_polarity' in trends[0]

def test_endpoints(client):
    # POST
    resp = client.post('/sentiment', json={'date': '2025-06-11', 'text': 'Feeling okay'})
    assert resp.status_code == 201
    data = resp.get_json()
    assert 'polarity' in data
    # GET
    resp2 = client.get('/sentiment?date=2025-06-11')
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    assert data2['text'] == 'Feeling okay'
    # Trends
    resp3 = client.get('/sentiment-trends?start=2025-06-01&end=2025-06-30')
    assert resp3.status_code == 200
    trends = resp3.get_json()
    assert isinstance(trends, list)
