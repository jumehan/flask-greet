from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    '''Returns a welcome message'''

    html = "<html><p>welcome</p></html>"
    return html

@app.get("/welcome/home")
def welcome_home():
    '''Returns a welcome home message'''

    html = "<html><p>welcome home</p></html>"
    return html

@app.get("/welcome/back")
def welcome_back():
    '''Returns a welcome back message'''

    html = "<html><p>welcome back</p></html>"
    return html
