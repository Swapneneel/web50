from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!"  #This is the variable which will generate dyanmic content on index.html
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
     headline = "Goodbye!"
     return render_template("index.html", headline=headline)
