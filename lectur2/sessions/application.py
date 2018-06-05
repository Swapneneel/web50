from flask import Flask, render_template, request, session
from flask_session import Session  #flask_session doesn't come with flask need to install seperately
                                     #with pip. Type "pip install flask_session"

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if seesion.get("notes") is None:
        session["notes"] = []  #This change is to diiferntiate the each user's notes
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes = notes)
