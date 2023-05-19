import mysql.connector, configparser

# Données dans database/auth.cfg
cfg = configparser.ConfigParser()
cfg.read("database/auth.cfg")
DB_HOST = cfg["DATABASE"]["DB_HOST"]
DB_PORT = cfg["DATABASE"]["DB_PORT"]
DB_NAME = cfg["DATABASE"]["DB_NAME"]
DB_USER = cfg["DATABASE"]["DB_USER"]
DB_PASS = cfg["DATABASE"]["DB_PASS"]

try:
    db = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
except:
    print("Connexion impossible à la base de données.\nLes identifiants dans database/auth.cfg sont certainement invalides pour votre machine.\nAssurez-vous aussi que la base de donnée indiquée existe\n\n\t- Thomas\n")
    exit()

cursor = db.cursor()

# Charger database/tables.sql
def exec_sql(path):
    with open(path) as file:
        sql = file.read().strip().split(";")
        for s in sql:
            cursor.execute(s)
        db.commit()


print("Suppression des tables existantes")
exec_sql("database/supprimer.sql")

print("Création des nouvelles tables")
exec_sql("database/tables.sql")

print("Ajout des fausses données")
exec_sql("database/donnees.sql")

