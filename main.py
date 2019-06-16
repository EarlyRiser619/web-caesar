from flask import flask

app = Flask(__name__)
app.config['DEBUG'] = True

forms = """
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
                <label for="rotate-by">
                    <input type="text" id="rotate-by" name="rot">
                </label>
                <input type="textarea" name="text">

        </body>
    </html>
    """

@ app_route("/")
def index():
    return form 

app.run()
