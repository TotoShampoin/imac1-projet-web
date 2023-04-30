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
db = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cursor = db.cursor()

# Charger database/tables.sql
with open("database/tables.sql") as file:
    sql = file.read()
    cursor.execute(sql, multi=True)
    db.commit()

