from app import app

@app.route('/')
def index():
    return 'Hello Medi!'

@app.route('/<name>/<colour>')
def greet(name, colour):
    return f'Hello {name} your fav colour is {colour}!'
    