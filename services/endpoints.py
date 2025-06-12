from flask import Flask, request, jsonify
from src.service.feature_helper import analyze_mood_and_habits
from config.firebase_config import db

app = Flask(__name__)

@app.route('/suggestions/<user_id>', methods=['GET'])
def get_suggestions(user_id):
    try:
        suggestions = analyze_mood_and_habits(user_id)
        return jsonify({'user_id': user_id, 'suggestions': suggestions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)