import os
from flask import Flask, render_template, request, jsonify
from pusher import Pusher

app = Flask(__name__, template_folder='../templates')

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
    pusher_client.trigger(f"room-{data['room']}", 'new-signal', data)
    return jsonify({"status": "success"})

@app.route('/send-chat', methods=['POST'])
def send_chat():
    data = request.json
    pusher_client.trigger(f"room-{data['room']}", 'new-chat', data)
    return jsonify({"status": "success"})
