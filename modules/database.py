import mysql.connector, configparser, os

# Données dans database/auth.cfg
cfg = configparser.ConfigParser()
cfg.read("database/auth.cfg")
DB_HOST = cfg["DATABASE"]["DB_HOST"]
DB_PORT = cfg["DATABASE"]["DB_PORT"]
DB_NAME = cfg["DATABASE"]["DB_NAME"]
DB_USER = cfg["DATABASE"]["DB_USER"]
DB_PASS = cfg["DATABASE"]["DB_PASS"]

# Base de donnée
try:
    db = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
except:
    print("Erreur lors de la connexion à la base de données.\nLes identifiants dans database/auth.cfg sont certainement invalides pour votre machine.")
    exit()

cursor = db.cursor()

# Charger database/tables.sql
with open("database/tables.sql") as file:
    sql = file.read().strip().split(";")
    for s in sql:
        cursor.execute(s)
    db.commit()

