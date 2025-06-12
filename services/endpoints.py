from flask import Flask, request, jsonify
from src.service.feature_helper import add_reminder, get_reminders, check_due_reminders

app = Flask(__name__)

@app.route('/reminders', methods=['POST'])
def create_reminder():
    data = request.json
    try:
        result = add_reminder(data['user_id'], data['type'], data['time'])
        return jsonify({'status': 'success', 'reminder': result}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/reminders/<user_id>', methods=['GET'])
def fetch_reminders(user_id):
    try:
        result = get_reminders(user_id)
        return jsonify({'user_id': user_id, 'reminders': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/reminders/due/<user_id>', methods=['GET'])
def check_reminder_due(user_id):
    try:
        result = check_due_reminders(user_id)
        return jsonify({'user_id': user_id, 'due_reminders': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)