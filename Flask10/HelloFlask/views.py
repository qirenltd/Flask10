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


