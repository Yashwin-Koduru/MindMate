from datetime import date

class MoodService:
    """Service for handling daily mood tracking entries."""
    def __init__(self):
        # In-memory storage; replace with DB as needed
        self._entries = {}  # key: ISO date string

    def save_entry(self, entry_date: str, mood_value: int, note: str = '') -> dict:
        entry = {'date': entry_date, 'mood': mood_value, 'note': note}
        self._entries[entry_date] = entry
        return entry

    def get_entry(self, entry_date: str) -> dict:
        return self._entries.get(entry_date)

# Singleton instance
mood_service = MoodService()
