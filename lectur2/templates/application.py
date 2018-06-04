from flask import Flask, render_template

app = Flask(__name__)
#flask will llok into the folder name "templates" inside to the main directory
@app.route("/")
def index():
    return render_template("index.html")
