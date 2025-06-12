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