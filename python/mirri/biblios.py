import pandas as pd
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

cursor = get_cursor("new_brc")
cursor.execute(open("../envoi_souches/mirri_biblio.sql", "r").read())
records = cursor.fetchall()

biblis = []
for record in records:
    bibli = record[0]
    if 'doi' in bibli:
        elmt = bibli.split('doi:')[1]
    elif 'pmid' in bibli:
        elmt = bibli.split('pmid:')[1]
    else:
        print(bibli)
