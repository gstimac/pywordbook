from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_wordbook():
    return "Hello wordbook!"

@app.route('/goc')
def hello_goc():
    return "Hello Goc!"