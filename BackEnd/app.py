from flask import Flask
import eigenbestand


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/uitdedb")
def uitdedb():
    return eigenbestand.ganaardedb()