from datetime import datetime, timedelta
from config.firebase_config import db

def add_reminder(user_id, reminder_type, time_str):
    reminder_data = {
        'user_id': user_id,
        'type': reminder_type,
        'time': time_str,
        'created_at': datetime.utcnow()
    }
    db.collection('reminders').add(reminder_data)
    return reminder_data

def get_reminders(user_id):
    reminders = db.collection('reminders').where('user_id', '==', user_id).stream()
    return [r.to_dict() for r in reminders]

def check_due_reminders(user_id):
    now = datetime.utcnow().strftime('%H:%M')
    reminders = get_reminders(user_id)
    due = [r for r in reminders if r['time'] == now]
    return due