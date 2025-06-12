# Daily Mood Tracking endpoints
from flask import request, jsonify
from src.service.mood_service import mood_service

@app.route('/mood', methods=['POST'])
def add_mood():
    data = request.get_json()
    entry_date = data.get('date')
    mood = data.get('mood')
    note = data.get('note', '')
    if not entry_date or mood is None:
        return jsonify({'error': 'date and mood required'}), 400
    entry = mood_service.save_entry(entry_date, int(mood), note)
    return jsonify(entry), 201

@app.route('/mood', methods=['GET'])
def fetch_mood():
    entry_date = request.args.get('date')
    if not entry_date:
        return jsonify({'error': 'date query param required'}), 400
    entry = mood_service.get_entry(entry_date)
    if not entry:
        return jsonify({'error': 'entry not found'}), 404
    return jsonify(entry), 200


# AI-Driven Sentiment Analysis endpoints
from src.service.sentiment_service import sentiment_service

@app.route('/sentiment', methods=['POST'])
def add_sentiment():
    data = request.get_json()
    date = data.get('date')
    text = data.get('text')
    if not date or not text:
        return jsonify({'error': 'date and text required'}), 400
    entry = sentiment_service.save_entry(date, text)
    return jsonify(entry), 201

@app.route('/sentiment', methods=['GET'])
def get_sentiment():
    date = request.args.get('date')
    if not date:
        return jsonify({'error': 'date query param required'}), 400
    entry = sentiment_service.get_entry(date)
    if not entry:
        return jsonify({'error': 'entry not found'}), 404
    return jsonify(entry), 200

@app.route('/sentiment-trends', methods=['GET'])
def sentiment_trends():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({'error': 'start and end query params required'}), 400
    trends = sentiment_service.get_weekly_trends(start, end)
    return jsonify(trends), 200


# AI-Powered Mental Health Coach endpoint
from flask import request, jsonify
from src.service.ai_coach_service import coach_service

@app.route('/coach', methods=['POST'])
def coach():
    data = request.get_json()
    history = data.get('history', [])
    if not isinstance(history, list) or not history:
        return jsonify({'error': 'message history required'}), 400
    try:
        reply = coach_service.get_response(history)
        return jsonify({'reply': reply}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
