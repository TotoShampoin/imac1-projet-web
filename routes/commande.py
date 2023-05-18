from flask import render_template
from __main__ import app
from modules.database import cursor, db

def getAliments():
    cursor.execute("""
        SELECT
            Aliment.aliid, Aliment.libelle, Aliment.prix, Aliment.category
        FROM Aliment;
    """)
    fetched = cursor.fetchall()
    fetched2 = [{
        "id": int(al[0]),
        "libelle": str(al[1]),
        "prix": float(al[2]),
        "category": str(al[3])
    } for al in fetched]
    aliments = {
        "burger": list(filter(lambda a: a["category"] == "burger", fetched2)),
        "boisson": list(filter(lambda a: a["category"] == "boisson", fetched2)),
        "accompagnement": list(filter(lambda a: a["category"] == "accompagnement", fetched2)),
        "dessert": list(filter(lambda a: a["category"] == "dessert", fetched2)),
    }
    return aliments

@app.route("/menu", methods=["GET"])
def menu():
    aliments = getAliments()
    return render_template("menu.html",
        aliments = aliments,
    )

