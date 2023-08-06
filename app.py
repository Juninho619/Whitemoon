from flask import Flask, flash, request, render_template
from flask_session import Session


# Configure application
app = Flask(__name__)


@app.route("/")
def index():

    if request.method == "GET":
        text = request.form.get("text")
        keyword = request.form.get("keyword")

    return render_template("index.html")

def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        return render_template("contact.html")

def about():
    if request.method == "GET":
        return render_template("about.html")
    else:
        return render_template("about.html")


