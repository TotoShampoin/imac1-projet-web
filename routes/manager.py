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


@app.route("/manager", methods=["GET"])
def manager():
    commandes = getCommandes()
    ingredients = getIngredients()
    return render_template("manager.html",
        commandes = commandes,
        ingredients = ingredients,
    )

@app.route("/manager/command/move_down/<int:comid>", methods=["GET"])
def manager_command_move_down(comid: int):
    moveDownCommandState(comid)
    return redirect("/manager")

@app.route("/manager/command/move_up/<int:comid>", methods=["GET"])
def manager_command_move_up(comid: int):
    moveUpCommandState(comid)
    return redirect("/manager")
