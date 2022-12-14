from flask import Flask
import eigenbestand
from flask_cors import CORS, cross_origin




app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/uitdedb")
@cross_origin()
def uitdedb():
    return eigenbestand.ganaardedb()