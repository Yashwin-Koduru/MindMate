from flask import Blueprint, request, jsonify
from config.firebase_config import db

journal_bp = Blueprint('journal_bp', __name__)

@journal_bp.route('/journal/user/<user_id>', methods=['GET'])
def get_user_journals(user_id):
    try:
        entries = db.collection('journal_entries').where('user_id', '==', user_id).stream()
        result = [{**entry.to_dict(), 'id': entry.id} for entry in entries]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@journal_bp.route('/journal/<entry_id>', methods=['DELETE'])
def delete_journal_entry(entry_id):
    try:
        db.collection('journal_entries').document(entry_id).delete()
        return jsonify({"status": "success", "message": "Entry deleted"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@journal_bp.route('/journal/<entry_id>', methods=['PUT'])
def update_journal_entry(entry_id):
    data = request.json
    try:
        db.collection('journal_entries').document(entry_id).update(data)
        return jsonify({"status": "success", "message": "Entry updated"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500