import os
from flask import Flask, render_template, request, jsonify
from pusher import Pusher  # We import the Class directly

app = Flask(__name__, template_folder='../templates')

# Initialize Pusher using the class directly
pusher_client = Pusher(
  app_id='2093703',
  key='c7f2cd8e7835a9dc4425',
  secret='22d37c4c1b5c1318c3f2',
  cluster='ap2',
  ssl=True
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-signal', methods=['POST'])
def send_signal():
    data = request.json
    room_id = data.get('room')
    
    # Safety check: if Pusher isn't initialized or room is missing
    if not room_id or not pusher_client:
        return jsonify({"status": "error", "message": "Missing room or config"}), 400

    # Trigger the event to the specific room channel
    pusher_client.trigger(f'room-{room_id}', 'new-signal', data)

    return jsonify({"status": "success"})
