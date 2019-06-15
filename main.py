from flask import flask

app = Flask(__name__)
app.config['DEBUG'] = True

@ app_route("/")
def index():
    return "Hello World"

app.run()
