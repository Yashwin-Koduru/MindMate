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
