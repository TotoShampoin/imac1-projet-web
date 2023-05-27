from flask import render_template, session, redirect
from __main__ import app
from modules.database import cursor, db

def startPanier():
    cursor.execute("""
        INSERT INTO Commande (etat) VALUES ("commande")
    """)
    db.commit()
    return cursor.lastrowid

def fetchPanier(session):
    if 'comid' not in session:
        session['comid'] = startPanier()
    return session['comid']

def getCommandAlimentContent(comid):
    cursor.execute(f"""
        SELECT
            Aliment.aliid, Aliment.libelle, Aliment.prix, Aliment.category, CommandeAliment.quantite
        FROM Aliment
        JOIN CommandeAliment ON CommandeAliment.aliid = Aliment.aliid
        WHERE CommandeAliment.comid = {comid}
    """)
    commande = [{
        "id": int(al[0]),
        "libelle": str(al[1]),
        "prix": float(al[2]),
        "category" : str(al[3]),
        "quantite": int(al[4])
    } for al in cursor.fetchall()]
    return commande

@app.route("/panier", methods=["GET"])
def panier():
    comid = fetchPanier(session)
    commande = getCommandAlimentContent(comid)
    sousTotal = sum([com['prix']*com['quantite'] for com in commande])
    prix_total = sousTotal + 2
    sousTotal = round(sousTotal,2)
    prix_total = round(prix_total,2)

    return render_template("panier.html",
        commande = commande,
        prix_total = prix_total,
        sousTotal = sousTotal
    )