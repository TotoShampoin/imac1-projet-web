from flask import render_template, session, redirect
from __main__ import app
from modules.database import cursor, db

def startCommand():
    cursor.execute("""
        INSERT INTO Commande (etat) VALUES ("commande")
    """)
    db.commit()
    return cursor.lastrowid

def cancelCommand(comid):
    cursor.execute(f"""
        DELETE FROM CommandeAliment WHERE CommandeAliment.comid = {comid}
    """)
    cursor.execute(f"""
        DELETE FROM Commande WHERE Commande.comid = {comid}
    """)
    db.commit()

def fetchCommand(session):
    if 'comid' not in session:
        session['comid'] = startCommand()
    return session['comid']

def getCommandContent(comid):
    cursor.execute(f"""
        SELECT
            Aliment.aliid, Aliment.libelle, Aliment.prix, CommandeAliment.quantite
        FROM Aliment
        JOIN CommandeAliment ON CommandeAliment.aliid = Aliment.aliid
        WHERE CommandeAliment.comid = {comid}
    """)
    commande = [{
        "id": int(al[0]),
        "libelle": str(al[1]),
        "prix": float(al[2]),
        "quantite": int(al[3]),
    } for al in cursor.fetchall()]
    return commande

def getIngredients(aliid):
    cursor.execute(f"""
        SELECT Ingredient.ingid, libelle, stock FROM `Ingredient`
        JOIN AlimentIngredient ON Ingredient.ingid = AlimentIngredient.ingid
        WHERE AlimentIngredient.aliid = {aliid}
    """)
    fetched = cursor.fetchall()
    ingredients = [{
        "id": int(ing[0]),
        "libelle": str(ing[1]),
        "stock": int(ing[2])
    } for ing in fetched]
    return ingredients

def getAliments():
    cursor.execute("""
        SELECT
            Aliment.aliid, Aliment.libelle, Aliment.prix, Aliment.category
        FROM Aliment
    """)
    fetched = cursor.fetchall()
    fetched2 = []
    for al in fetched:
        ingredients = getIngredients(al[0])
        fetched2.append({
            "id": int(al[0]),
            "libelle": str(al[1]),
            "prix": float(al[2]),
            "category": str(al[3]),
            "ingredients": ", ".join([ing["libelle"] for ing in ingredients]),
            "disponible": False if 0 in [int(ing["stock"]) for ing in ingredients] else True
        })
    aliments = {
        "burger": list(filter(lambda a: a["category"] == "burger", fetched2)),
        "boisson": list(filter(lambda a: a["category"] == "boisson", fetched2)),
        "accompagnement": list(filter(lambda a: a["category"] == "accompagnement", fetched2)),
        "dessert": list(filter(lambda a: a["category"] == "dessert", fetched2)),
    }
    return aliments

def addToBasket(comid, aliid):
    cursor.execute(f"""
        INSERT INTO `CommandeAliment`(comid, aliid, quantite)
        VALUES({comid}, {aliid}, 1)
        ON DUPLICATE KEY UPDATE
            quantite = quantite + 1
    """)
    db.commit()

def removeFromBasket(comid, aliid):
    cursor.execute(f"""
        UPDATE CommandeAliment
        SET quantite = quantite - 1
        WHERE comid = {comid} AND aliid = {aliid}
    """)
    cursor.execute(f"""
        SELECT quantite FROM CommandeAliment
        WHERE comid = {comid} AND aliid = {aliid}
    """)
    qtt = cursor.fetchone()[0]
    if qtt <= 0:
        cursor.execute(f"""
            DELETE FROM CommandeAliment
            WHERE comid = {comid} AND aliid = {aliid}
        """)
    db.commit()


@app.route("/menu", methods=["GET"])
def menu():
    comid = fetchCommand(session)
    commande = getCommandContent(comid)
    aliments = getAliments()
    return render_template("menu.html",
        aliments = aliments,
        commande = commande,
    )

@app.route("/menu/add/<int:aliid>", methods=["GET"])
def menu_add(aliid: int):
    comid = fetchCommand(session)
    addToBasket(comid, aliid)
    return redirect("/menu")

@app.route("/menu/remove/<int:aliid>", methods=["GET"])
def menu_remove(aliid: int):
    comid = fetchCommand(session)
    removeFromBasket(comid, aliid)
    return redirect("/menu")

@app.route("/menu/cancel", methods=["GET"])
def menu_cancel():
    comid = fetchCommand(session)
    cancelCommand(comid)
    session.clear()
    return redirect("/")



