# Projet Web IMAC

## Pré-requis

- Python3, avec les modules suivants:
    - flask
    - flask_cors
    - mysql.connector
- Un serveur MySQL
    - Copiez-collez le ficher [database/auth-example.cfg](./database/auth-example.cfg) en [database/auth.cfg](./database/auth.cfg)
    - Modifiez le fichier [database/auth.cfg](./database/auth.cfg) pour y mettre les identifiants de votre serveur MySQL.
    - Si vous avez Docker, vous pouvez utiliser le petit docker-compose dans le même dossier. C'est un simple conteneur MySQL avec phpMyAdmin.

## Lancer le site

```bash
python3 app.py
```
