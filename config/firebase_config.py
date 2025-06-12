import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with actual path
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()