# WELLNESS SUGGESTIONS
from datetime import datetime, timedelta
from config.firebase_config import db

def analyze_mood_and_habits(user_id):
    now = datetime.utcnow()
    last_week = now - timedelta(days=7)

    # Fetch recent moods
    moods = db.collection('mood_logs').where('user_id', '==', user_id).where('timestamp', '>=', last_week).stream()
    mood_scores = []
    for mood in moods:
        data = mood.to_dict()
        mood_scores.append(int(data.get('mood', 5)))

    # Fetch recent habits
    habits = db.collection('habit_logs').where('user_id', '==', user_id).where('timestamp', '>=', last_week).stream()
    habit_count = sum(1 for _ in habits)

    # Simple logic for suggestions
    suggestions = []

    if not mood_scores:
        suggestions.append("Try journaling your thoughts to track your mental state.")
    elif sum(mood_scores) / len(mood_scores) < 5:
        suggestions.append("Consider a short walk or breathing exercise to uplift your mood.")

    if habit_count < 5:
        suggestions.append("Try adding a daily habit like hydration or 10-minute meditation.")

    if not suggestions:
        suggestions.append("You're doing great! Keep up your wellness routine.")

    return suggestions

# Journal Templates
journal_templates = {
    "gratitude": "What are three things you're grateful for today?",
    "stress_relief": "What’s been stressing you out lately, and how might you handle it better?",
    "goal_setting": "What’s one short-term goal you want to achieve this week?"
}

def get_templates():
    return journal_templates

def format_entry(user_id, template_type, entry_text):
    return {
        "user_id": user_id,
        "template_type": template_type,
        "prompt": journal_templates.get(template_type, ""),
        "entry": entry_text
    }
