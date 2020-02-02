from datetime import datetime
from flask import Flask, request
import time

app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello! Я кончаю на клавиатуру!", "time": time.time()},
    {"username": "Maria", "text": "Hello, Jack! Can you lick my pussy?", "time": time.time()},
]
users = {
    'Jack': '12345',
    'Maria': '12345'
}
@app.route("/")
def hello_view():
    return "<h1>Welcome to LiteIM</h1>"

@app.route("/status")
def status_view():
        return {
            'time':datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'Users': len(users),
            'messages': len(messages)
        }

@app.route("/messages")
def messages_view():
    """
    Получение сообщений после отметки after
    imput: after - отметка времени
    output: JSON {
            messages: [
            {"username": str, "text": str, "time": float},
            ...
                ]
            }
    """
    after = float(request.args['after'])
    new_messages = [message for message in messages if message['time'] > after]
    return {'messages': new_messages}

@app.route("/send", methods = ['POST'])
def send_view():
    """
    отправка сообщений
    imput: JSON {
            "username": str,
            "password": str,
            "text": str,
            }
    output:  JSON {"ok": bool}
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    if username not in users or users[username] != password:
        return {'ok': False}
    text = data["text"]

    messages.append({"username": username, "text": text, "time": time.time()})

    return {'ok': True}

@app.route("/auth", methods = ['POST'])
def auth_view():
    """
    Авторизовать пользователя или сообщить что пароль неверный.
    imput: JSON {
            "username": str,
            "password": str,
            }
    output:  JSON {"ok": bool}
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    if username not in users:
        users[username] = password
        return {'ok': True}
    elif users[username] == password:
        return {'ok': True}
    else:
        return {'ok': False}

app.run()

