# Journal Templates Endpoints
from flask import Flask, request, jsonify
from config.firebase_config import db
from src.service.feature_helper import get_templates, format_entry

app = Flask(__name__)

@app.route('/journal/templates', methods=['GET'])
def fetch_templates():
    return jsonify(get_templates()), 200

@app.route('/journal/submit', methods=['POST'])
def submit_entry():
    data = request.json
    user_id = data['user_id']
    template_type = data['template_type']
    entry_text = data['entry']

    entry_data = format_entry(user_id, template_type, entry_text)

    try:
        db.collection('journal_entries').add(entry_data)
        return jsonify({"status": "success", "message": "Entry saved"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
from services.journal_api import journal_bp
app.register_blueprint(journal_bp)

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


# Daily Habit Tracker endpoints
from flask import request, jsonify
from src.service.habit_service import habit_service

@app.route('/habit', methods=['POST'])
def add_habit():
    data = request.get_json()
    date = data.get('date')
    habit = data.get('habit')
    done = data.get('done', False)
    if not date or not habit:
        return jsonify({'error':'date and habit required'}), 400
    entry = habit_service.save_status(date, habit, done)
    return jsonify(entry), 201

@app.route('/habit', methods=['GET'])
def fetch_habit():
    date = request.args.get('date')
    if not date:
        return jsonify({'error':'date query param required'}), 400
    status = habit_service.get_status(date)
    return jsonify({'date':date, 'status':status}), 200

@app.route('/habit/progress', methods=['GET'])
def fetch_progress():
    week_start = request.args.get('week_start')
    if not week_start:
        return jsonify({'error':'week_start query param required'}), 400
    progress = habit_service.get_weekly_progress(week_start)
    return jsonify({'week_start': week_start, 'progress': progress}), 200
  