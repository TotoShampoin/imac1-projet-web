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

def changeCommandState(comid):
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


@app.route("/manager", methods=["GET"])
def manager():
    commandes = getCommandes()
    return render_template("manager.html",
        commandes = commandes,
    )

@app.route("/manager/command/change/<int:comid>", methods=["GET"])
def manager_command_change(comid: int):
    changeCommandState(comid)
    return redirect("/manager")
