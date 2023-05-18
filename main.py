# Imported flask class from flask
from flask import Flask
# define app as Flask
app = Flask(__name__)


@app.route("/")
# defined a method
def hello_world():
    return "Hello, World!"


app.run(debug=True)
