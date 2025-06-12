from flask import Flask, request, jsonify
from firebase_admin import auth
from config.firebase_config import db

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data['email']
    password = data['password']
    display_name = data.get('display_name', '')

    try:
        user = auth.create_user(
            email=email,
            password=password,
            display_name=display_name
        )
        db.collection('users').document(user.uid).set({
            'email': email,
            'display_name': display_name
        })
        return jsonify({'status': 'success', 'uid': user.uid}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/verify-token', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    try:
        decoded = auth.verify_id_token(token)
        return jsonify({'status': 'verified', 'uid': decoded['uid']})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

if __name__ == '__main__':
    app.run(debug=True)