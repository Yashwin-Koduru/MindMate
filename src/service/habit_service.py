
from datetime import datetime, timedelta

class HabitService:
    def __init__(self):
        # store entries as date_str -> {habit: bool}
        self.entries = {}

    def save_status(self, date_str, habit, done):
        day = self.entries.setdefault(date_str, {})
        day[habit] = done
        return {'date': date_str, 'habit': habit, 'done': done}

    def get_status(self, date_str):
        return self.entries.get(date_str, {})

    def get_weekly_progress(self, week_start):
        # week_start: 'YYYY-MM-DD'
        start = datetime.fromisoformat(week_start)
        progress = {}
        for i in range(7):
            d = (start + timedelta(days=i)).date().isoformat()
            progress[d] = self.entries.get(d, {})
        return progress

# singleton
habit_service = HabitService()
