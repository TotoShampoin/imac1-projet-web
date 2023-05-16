from flask import render_template
from __main__ import app

@app.route("/menu", methods=["GET"])
def menu():
    return render_template("menu.html")

