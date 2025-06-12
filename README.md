# MindMate - AI Mental Wellness App

## Features
- Firebase Authentication (Login & Registration)
- Secure Data Storage (Firestore)
- React Native Frontend

## Setup Instructions

### Backend
1. Install dependencies:
```bash
pip install flask firebase-admin
```
2. Place your Firebase `serviceAccountKey.json` in the `config/` folder.
3. Run the Flask app:
```bash
export FLASK_APP=services/auth_endpoints.py
flask run
```

### Frontend
1. Ensure React Native and Firebase are configured.
2. Use `LoginScreen.js` in your React Native app.

### Testing
```bash
pytest test/
```

## AI-Driven Sentiment Analysis

New endpoints for sentiment analysis of journal entries:
- **POST** `/sentiment` `{ date: 'YYYY-MM-DD', text: 'entry text' }` ➔ analyzes and stores polarity & subjectivity.
- **GET** `/sentiment?date=YYYY-MM-DD` ➔ retrieves analysis for a given date.
- **GET** `/sentiment-trends?start=YYYY-MM-DD&end=YYYY-MM-DD` ➔ returns weekly average polarity between dates.

Requires `textblob` dependency (`pip install textblob`).


## AI-Powered Mental Health Coach

- **Endpoint**: POST `/coach`  
  - Request JSON: `{ history: Array<{role: String, content: String}> }`  
  - Response JSON: `{ reply: String }`  
- **Frontend Component**: `frontend/components/ChatCoach.jsx`  
- **Service**: `frontend/services/coachService.js`  


## Daily Habit Tracker

Track habits (`meditation`, `hydration`, `physical`) with:
- POST `/habit` JSON `{date, habit, done}`
- GET `/habit?date=YYYY-MM-DD`
- GET `/habit/progress?week_start=YYYY-MM-DD`

Frontend component: `HabitTracker.jsx`, service: `habitService.js`.
