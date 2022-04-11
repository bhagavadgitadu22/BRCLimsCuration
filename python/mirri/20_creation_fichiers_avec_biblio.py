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

cursor = get_cursor("new_brc")
cursor.execute(open("../envoi_souches/mirri_biblio_par_id.sql", "r").read())
cursor.execute(open("../envoi_souches/mirri.sql", "r").read())
records = cursor.fetchall()

f_biblis = open('../../output/bilan_biblis.csv', 'r', encoding="utf-8", newline='')
biblis = csv.reader(f_biblis, delimiter=';')

biblis_par_id = {}
correspondances_biblis = []
numero  = 0
for elmt in biblis:
    ids_elmt = elmt[0]
    type_elmt = elmt[1]
    val_elmt = elmt[2]

    if not(type_elmt == "doi" or type_elmt == "pmid"):
        numero += 1
        list = [numero, val_elmt, '', '', elmt[3], elmt[4], elmt[5], '', elmt[6], elmt[7]]
        correspondances_biblis.append(list)

    for id_elmt in ids_elmt.split(','):
        int_id = int(id_elmt)
        if int_id not in biblis_par_id:
            biblis_par_id[int_id] = []

        if type_elmt == "doi" or type_elmt == "pmid":
            biblis_par_id[int_id].append(val_elmt)
        else:
            biblis_par_id[int_id].append(numero)
    
rows_strains = []
for record in records:
    xxx_id = record[0]
    row = [r for r in record[1:]]
    refs = ""
    if xxx_id in biblis_par_id:
        for ref in biblis_par_id[xxx_id]:
            if refs != '':
                refs += ';'
            refs += str(ref)
    row[35] = refs

    rows_strains.append(row)

f_strains = open('../../output/sheet_strains.csv', 'w', encoding="utf-8", newline='')
writer_strains = csv.writer(f_strains, delimiter=';')
writer_strains.writerows(rows_strains)
f_strains.close()

f_literature = open('../../output/sheet_literature.csv', 'w', encoding="utf-8", newline='')
writer_literature = csv.writer(f_literature, delimiter=';')
writer_literature.writerows(correspondances_biblis)
f_literature.close()

f_biblis.close()