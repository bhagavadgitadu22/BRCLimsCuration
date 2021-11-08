import psycopg2
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def main():
    f = open('../../output/hors_cip_modifies.csv', 'r', newline='')
    rows = csv.reader(f, delimiter=';')

    cursor = get_cursor("brc_db")
    cursor_curated = get_cursor("new_brc")

    for row in rows:
        id_cip = row[0]
        differences = {}

        cursor.execute("SELECT * FROM t_souche WHERE xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute("SELECT * FROM t_souche WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        # 40_historique_bacillus
        

        # 90_temperature
        if record[44] != record_curated[44]:
            differences["temperature"] = [record[44], record_curated[44]]

    f.close()

main()
