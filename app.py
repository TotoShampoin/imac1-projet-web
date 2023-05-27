#!/usr/bin/python3

from flask import Flask,render_template,send_from_directory,abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = "secret"

## Il faudra trouver un moyen d'isoler cette partie là, pour un code plus propre...

# Importer les fonctions dans modules/utils.py
from modules.utils import *
import modules.database

import routes.commande
import routes.manager
import routes.panier

# Cette fonction permet de chercher le bon fichier à partir de l'url
# Exemple avec l'url:  site.com/info/jeu
@app.route('/', defaults={'url_path': ''})
@app.route("/<path:url_path>")
def default(url_path: str):
    # template html
    #   ./templates/info/jeu/index.html
    #   ./templates/info/jeu.html
    print(url_path)
    if exists_and_is_dir(f"templates/{url_path}") and exists_and_is_file(f"templates/{url_path}/index.html"):
        return render_template(f"{url_path}/index.html")
    if exists_and_is_file(f"templates/{url_path}.html"):
        return render_template(f"{url_path}.html")
    if exists_and_is_file(f"templates/{url_path}"):
        return render_template(f"{url_path}")
    
    # fichier static
    #   ./static/info/jeu
    if exists_and_is_file(f"static/{url_path}"):
        return send_from_directory("static", url_path)

    # le fichier n'existe pas: erreur 404
    abort(404)

# En cas d'erreur 404 ou 500, utiliser les fichiers
#   ./templates/error/404.html
#   ./templates/error/500.html
@app.errorhandler(404)
def error404(error):
    return render_template("error/404.html", error = error), 404
@app.errorhandler(500)
def error500(error):
    return render_template("error/500.html", error = error), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
