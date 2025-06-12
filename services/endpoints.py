

# Daily Mood Tracking endpoints
from flask import request, jsonify
def add_mood():
    data = request.get_json()
    date = data.get('date')
    mood = data.get('mood')
    note = data.get('note', '')
    if not date or mood is None:
        return jsonify({'error': 'date and mood required'}), 400
    return jsonify(entry), 201

def fetch_mood():
    date = request.args.get('date')
    if not date:
        return jsonify({'error': 'date query param required'}), 400
    entry = get_mood_entry(date)
    if not entry:
        return jsonify({'error': 'entry not found'}), 404
    return jsonify(entry), 200


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
