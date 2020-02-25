from flask import Flask
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    return "企人"

@app.route('/liao')
def liao():
    return "企人聊" 

@app.route('/sou')
def sou():
    return "企人搜"

@app.route('/buy')
def buy():
    return "企人买"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

