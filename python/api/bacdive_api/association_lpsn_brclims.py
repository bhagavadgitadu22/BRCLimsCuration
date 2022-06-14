import csv
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

f = open('../../output/lpsn_gss_2022-05-03.csv', 'r', newline='', encoding='utf8')
records_dsm = csv.reader(f, delimiter=',', quotechar='"')
ids_dsm = [[record[0], record[1], [elmt.strip() for elmt in record[8].split(';')]] for record in records_dsm]
f.close()

cursor = get_cursor("new_brc6")
cursor.execute(open("../analyse/communs_dsm_cip.sql", "r").read())
records_cip = cursor.fetchall()

result = []
i= 0
for record in records_cip:
    id_cip = record[0]
    refs_equis_cip = record[4].split(';')
    
    for ref_cip in refs_equis_cip:
        for elmt in ids_dsm:
            if ref_cip in elmt[2] and elmt[0] in record[1]:
                line = [id_cip, record[2], record[3], record[1], elmt[0], elmt[1], ref_cip, record[4], elmt[2]]
                result.append(line)

    i += 1
    if i%50 == 0:
        print(str(i)+" versus "+str(len(result)))

print(len(result))
f = open('../../output/cip_new_taxos2.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(result)
f.close()
