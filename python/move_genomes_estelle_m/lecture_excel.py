import csv
import re
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

f = open('C:/Users/mboutrou/Documents/numeros_sequences.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')

cursor = get_cursor("restart_db_pure")
cursor.execute(open("../analyse/last_version_souches_lots.sql", "r").read())

str_sql = "SELECT sch_identifiant, lot_numero, REPLACE(REPLACE(CONCAT(REGEXP_REPLACE(sch_identifiant, '[_ -.T]+', '', 'g'), REGEXP_REPLACE(split_part(lot_numero, '_', 1), '[_ -.T]+', '', 'g')), 'CIP', ''), 'CRBIP', '') FROM last_version_souches_lots"
cursor.execute(str_sql)
ids_lots_colles = cursor.fetchall()

ids = {}
yes = 0
no = 1
for record in records:
    result = record[0].replace('_', '').replace('-', '').replace(' ', '').replace('.', '').replace('T', '').replace('CIP', '').replace('CRBIP', '')

    bool = False
    for colle in ids_lots_colles:
        if colle[2] == result:
            bool = True
    if bool:
        yes += 1
    else:
        no += 1
        print(record[0])
        print(result)

f.close()

print(yes)
print(no)
