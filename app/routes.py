# app/routes.py
from flask import Blueprint, render_template, request, redirect
from datetime import datetime

main = Blueprint('main', __name__)
messages = []

@main.route('/')
def index():
    return render_template('index.html', messages=messages)

@main.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    messages.append({'username': username, 'message': message, 'timestamp': timestamp})
    return redirect('/')
