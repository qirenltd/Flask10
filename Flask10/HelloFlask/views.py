from flask import Flask
from HelloFlask import app
from datetime import datetime
from flask import render_template


@app.route('/')
@app.route('/qiren')
def qiren():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    html_content = "<html><head><title>企人</title></head><body>"
    html_content += "<strong>企人中心</strong> on " + formatted_now
    html_content += "</body></html>"

    return html_content

@app.route('/liao')
def liao():
    return "<html><head><title>企人聊</title></head>企人聊" 

@app.route('/sou')
def sou():
    #render_template 加载模板
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return "企人搜"+render_template(
        "index.html",
        content = "<strong>Hello, Flask!</strong> on " + formatted_now)

@app.route('/buy')
def buy():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    b="企人买"
    a="买"
    return render_template("index.html",content=formatted_now,title=a,message=b)