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