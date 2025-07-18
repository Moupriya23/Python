from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid)
    message = data['message']
    print(f"Message received from {username}: {message}")
    send({'user': username, 'message': message}, broadcast=True)

@socketio.on('set_username')
def set_username(username):
    users[request.sid] = username

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
