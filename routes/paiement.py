from flask import render_template, session, redirect
from __main__ import app
from modules.database import cursor, db

def startCommand():
    cursor.execute("""
        INSERT INTO Commande (etat) VALUES ("commande")
    """)
    db.commit()
    return cursor.lastrowid

def fetchCommand(session):
    if 'comid' not in session:
        session['comid'] = startCommand()
    return session['comid']

def getCommandContent(comid):
    cursor.execute(f"""
        UPDATE Commande
        SET Commande.etat = "preparation"
        WHERE Commande.comid = {comid}
    """)
    db.commit()

@app.route("/valide", methods=["GET"])
def command_add():
    comid = fetchCommand(session)
    getCommandContent(comid)
    return render_template("valide.html")
