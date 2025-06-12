
from textblob import TextBlob
from datetime import datetime
from collections import defaultdict

class SentimentService:
    def __init__(self):
        # date_str -> entry
        self.entries = {}

    def analyze_text(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity

    def save_entry(self, date_str, text):
        polarity, subjectivity = self.analyze_text(text)
        entry = {
            'date': date_str,
            'text': text,
            'polarity': polarity,
            'subjectivity': subjectivity
        }
        self.entries[date_str] = entry
        return entry

    def get_entry(self, date_str):
        return self.entries.get(date_str)

    def get_weekly_trends(self, start_date, end_date):
        # parse dates
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
        # group by ISO week
        weeks = defaultdict(list)
        for date_str, entry in self.entries.items():
            d = datetime.fromisoformat(date_str)
            if start <= d <= end:
                week_key = f"{d.isocalendar()[0]}-W{d.isocalendar()[1]}"
                weeks[week_key].append(entry['polarity'])
        # compute averages
        trends = []
        for week, polarities in sorted(weeks.items()):
            avg = sum(polarities)/len(polarities) if polarities else 0
            trends.append({'week': week, 'average_polarity': avg})
        return trends

# singleton
sentiment_service = SentimentService()
