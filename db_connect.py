from psycopg2 import connect
import json

def connection(config_file):


    cfg_string = open(config_file).read()
    cfg_json = json.loads(cfg_string)
    return connect(user=cfg_json["username"],
                   password=cfg_json["passwd"],
                   host=cfg_json["hostname"],
                   database=cfg_json["db_name"])

############ INICJALIZACJA

config_path = "db.json"

try:

    cnx = connection(config_path)
    print("Polaczono z baza ")
except Exception as e:


    print("Niepowodzenie:", e)
    exit()

cursor = cnx.cursor()

############ DEFINICJE FUNKCJI

def db_execute(cursor, sql):


    try:
        cursor.execute(sql)
    except Exception as e:
        print("Niepowodzenie:", e)