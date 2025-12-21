import os
from flask import Flask, render_template, request, jsonify
from pusher import Pusher

app = Flask(__name__, template_folder='../templates')

# Initialize Pusher
# These are pulled from Vercel Environment Variables
pusher_client = pusher.Pusher(
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
    # Trigger the event to the specific room channel
    pusher_client.trigger(f'room-{room_id}', 'new-signal', data)

    return jsonify({"status": "success"})



