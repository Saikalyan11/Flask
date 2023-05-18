# Imported flask class from flask
from flask import Flask, render_template
# define app as Flask
app = Flask(__name__)


@app.route("/")
# defined a method
def hello_world():
    return render_template('index.html')


app.run(debug=True)
