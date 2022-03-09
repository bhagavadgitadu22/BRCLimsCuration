import csv
import re
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

f = open('C:/Users/mboutrou/Documents/numeros_sequences.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')

cursor = get_cursor("restart_db_pure")
cursor.execute(open("../analyse/last_version_souches_lots.sql", "r").read())

ids = {}
for record in records:
    result = [elmt.replace("pas de souche", '').strip() for elmt in re.split('[-_]{1}', record[0], 1)]

    pattern = re.compile("^[0-9-_]+$")
    if len(result) == 2 and pattern.match(result[1]):
        id_cip = result[0].replace('CIP', '')
        if id_cip not in ids:
            ids[id_cip] = []

        lot_cip = result[1]
        if lot_cip not in ids[id_cip]:
            ids[id_cip].append(lot_cip)

    elif len(result) != 1:
        print(result)

    str_sql = "SELECT lot_numero FROM last_version_souches_lots WHERE sch_identifiant LIKE '%"+id_cip+"%'"
    cursor.execute(str_sql)
    records = cursor.fetchall()
    

    # id_cip = record[0].split('_')[0].replace('CIP', '')
    # if id_cip not in ids:
    #     ids[id_cip] = []
    # if '_' in record[0]:
    #     lot_cip = record[0].split('_')[1].strip()
    #     ids[id_cip].append(lot_cip)
    # elif '-' in record[0]:
    #     print(record[0])

f.close()
