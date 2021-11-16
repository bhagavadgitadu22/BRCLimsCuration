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
    f = open('../../output/cip_modifies.csv', 'r', newline='')
    rows = csv.reader(f, delimiter=';')

    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    differences = {"temperature": [], "historique": []}

    i = 0
    for row in rows:
        id_cip = row[0]

        cursor.execute("SELECT * FROM t_souche WHERE xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute("SELECT * FROM t_souche WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        # 40_historique_bacillus
        if record[68] != record_curated[68]:
            differences["historique"].append([id_cip, record[68], record_curated[68]])

        # 90_temperature
        if record[44] != record_curated[44]:
            differences["temperature"].append([id_cip, record[44], record_curated[44]])

        if i%1000 == 0:
            print(str(i)+" souches traitees")
        i+=1

    f2 = open('../../output/cip_ce_qui_a_ete_modifie.csv', 'w', newline='')
    writer2 = csv.writer(f2, delimiter=';')
    writer2.writerows(differences["temperature"])
    f.close()

    f.close()

main()
