from flask import render_template, session, redirect
from __main__ import app
from modules.database import cursor, db

def getCommandes():
    cursor.execute("""
        SELECT
            Commande.comid, Commande.etat, Commande.adresse, Commande.contact
        FROM Commande
    """)
    fetched = cursor.fetchall()
    fetched2 = [{
        "id": int(co[0]),
        "etat": str(co[1]),
        "adresse": str(co[2]),
        "contact": str(co[3])
    } for co in fetched]
    commandes = {
        "preparation": list(filter(lambda a: a["etat"] == 'preparation', fetched2)),
        "livraison": list(filter(lambda a: a["etat"] == 'livraison', fetched2)),
        "fini": list(filter(lambda a: a["etat"] == 'fini', fetched2)),
    }
    return commandes

def getIngredients():
    cursor.execute("""
        SELECT
            Ingredient.ingid, Ingredient.libelle, Ingredient.stock
        FROM Ingredient
    """)
    fetched = cursor.fetchall()
    ingredients = [{
        "id": int(ing[0]),
        "libelle": str(ing[1]),
        "stock": int(ing[2]),
    } for ing in fetched]
    return ingredients

def moveDownCommandState(comid):
    cursor.execute(f"""
        SELECT
            Commande.etat
        FROM Commande
        WHERE Commande.comid = {comid}
    """)
    fetched = cursor.fetchall()
    etat = fetched[0][0]
    if etat == 'preparation':
        cursor.execute(f"""
            UPDATE Commande
            SET etat = 'livraison'
            WHERE comid = {comid}
        """)
    elif etat == 'livraison':
        cursor.execute(f"""
            UPDATE Commande
            SET etat = 'fini'
            WHERE comid = {comid}
        """)
    db.commit()

def moveUpCommandState(comid):
    cursor.execute(f"""
        SELECT
            Commande.etat
        FROM Commande
        WHERE Commande.comid = {comid}
    """)
    fetched = cursor.fetchall()
    etat = fetched[0][0]
    if etat == 'fini':
        cursor.execute(f"""
            UPDATE Commande
            SET etat = 'livraison'
            WHERE comid = {comid}
        """)
    elif etat == 'livraison':
        cursor.execute(f"""
            UPDATE Commande
            SET etat = 'preparation'
            WHERE comid = {comid}
        """)
    db.commit()

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

def addToStock(ingid):
    cursor.execute(f"""
        UPDATE Ingredient
        SET stock = stock + 1
        WHERE ingid = {ingid}
    """)
    db.commit()

def removeFromStock(ingid):
    cursor.execute(f"""
        UPDATE Ingredient
        SET stock = stock - 1
        WHERE ingid = {ingid}
    """)
    db.commit()

@app.route("/manager", methods=["GET"])
def manager():
    commandes = getCommandes()
    ingredients = getIngredients()
    commande_aliments = []
    for etat in commandes:
        commande_aliments += [{
            "id": commande['id'],
            "contenu": getCommandContent(commande['id']),
        } for commande in commandes[etat]]
    return render_template("manager.html",
        commandes = commandes,
        ingredients = ingredients,
        commande_aliments = commande_aliments,
    )

@app.route("/manager/command/move_down/<int:comid>", methods=["GET"])
def manager_command_move_down(comid: int):
    moveDownCommandState(comid)
    return redirect("/manager")

@app.route("/manager/command/move_up/<int:comid>", methods=["GET"])
def manager_command_move_up(comid: int):
    moveUpCommandState(comid)
    return redirect("/manager")

@app.route("/manager/stock/add/<int:ingid>", methods=["GET"])
def manager_stock_add(ingid: int):
    addToStock(ingid)
    return redirect("/manager")

@app.route("/manager/stock/remove/<int:ingid>", methods=["GET"])
def manager_stock_remove(ingid: int):
    removeFromStock(ingid)
    return redirect("/manager")