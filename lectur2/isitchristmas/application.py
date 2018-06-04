import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()  #it is the way of getting the
    ischristmas = now.month == 12 and now.day == 25
    #new_yaer = True
    return render_template("index.html", new_year = ischristmas)
