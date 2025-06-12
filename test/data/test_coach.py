import pytest
from unittest.mock import patch
from src.service.ai_coach_service import coach_service

def test_coach_service_get_response():
    dummy_history = [{'role': 'user', 'content': 'Hello'}]
    with patch('openai.ChatCompletion.create') as mock_create:
        mock_create.return_value = type('o', (), {'choices': [type('c', (), {'message': {'content': 'Hi there'}})]})
        reply = coach_service.get_response(dummy_history)
        assert reply == 'Hi there'

def test_coach_endpoint(client):
    from flask import json
    # Mock service
    with patch('src.service.ai_coach_service.coach_service.get_response') as mock_get:
        mock_get.return_value = 'Test reply'
        resp = client.post('/coach', json={'history': [{'role':'user','content':'Hi'}]})
        assert resp.status_code == 200
        data = resp.get_json()
        assert data['reply'] == 'Test reply'

    # Missing history
    resp2 = client.post('/coach', json={})
    assert resp2.status_code == 400
