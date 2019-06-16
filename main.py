from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!doctype html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/cypher" method="post">
                <label for="rotate-by">Rotate By: 
                    <input type="text" id="rotate-by" name="rot" value="0">
                </label>
                <textarea name="text"></textarea>
                <button type="submit">Submit Query</button>
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form 

@app.route("/", methods=['POST'])
def encrypt():
    rot= int(request.form['rot'])
    text= request.form['text']
    encrypted = rotate_string(text, rot)

    return <h1>'encrypted'</h1>

app.run()
